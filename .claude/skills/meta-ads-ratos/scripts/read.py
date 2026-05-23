#!/usr/bin/env python3
"""
Meta Ads Ratos — Read operations (22 subcommands)
CLI for reading Meta Ads data via facebook-business SDK.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_api,
    resolve_account,
    print_json,
    handle_fb_error,
    add_account_arg,
    add_fields_arg,
    add_pagination_args,
    add_status_filter_arg,
    parse_fields,
    parse_status_filter,
)
from lib.pagination import fetch_url


# ---------------------------------------------------------------------------
# Lazy SDK imports
# ---------------------------------------------------------------------------

def _sdk():
    """Lazy import SDK classes. Returns dict for attribute access."""
    from facebook_business.adobjects.adaccount import AdAccount
    from facebook_business.adobjects.campaign import Campaign
    from facebook_business.adobjects.adset import AdSet
    from facebook_business.adobjects.ad import Ad
    from facebook_business.adobjects.adcreative import AdCreative
    from facebook_business.adobjects.user import User
    from facebook_business.adobjects.adspixel import AdsPixel
    return {
        "AdAccount": AdAccount, "Campaign": Campaign, "AdSet": AdSet,
        "Ad": Ad, "AdCreative": AdCreative, "User": User,
        "AdsPixel": AdsPixel,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_params(args, include_status=True):
    """Build common params dict from argparse namespace."""
    params = {"limit": 100}
    if hasattr(args, "limit") and args.limit:
        params["limit"] = min(args.limit, 100)
    if hasattr(args, "after") and args.after:
        params["after"] = args.after
    if hasattr(args, "before") and args.before:
        params["before"] = args.before
    if include_status and hasattr(args, "status") and args.status:
        statuses = parse_status_filter(args.status)
        if statuses:
            params["effective_status"] = statuses
    return params


def _collect(cursor, limit=None):
    """Collect ALL results from an SDK cursor, auto-paginating."""
    results = [cursor[i] for i in range(len(cursor))]
    while cursor.load_next_page():
        results.extend([cursor[i] for i in range(len(cursor))])
    if limit:
        return results[:limit]
    return results


_BUDGET_FIELDS = (
    "daily_budget", "lifetime_budget", "budget_remaining",
    "spend_cap", "amount_spent", "balance",
)


def _format_budgets(results):
    """Converte campos de orcamento de centavos para reais (/ 100)."""
    for row in results:
        if not hasattr(row, 'get'):
            continue
        for field in _BUDGET_FIELDS:
            val = row.get(field)
            if val is not None:
                try:
                    row[field] = f"{int(val) / 100:.2f}"
                except (ValueError, TypeError):
                    pass
    return results


# ---------------------------------------------------------------------------
# 1. accounts
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_accounts(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or ["account_id", "name", "account_status", "currency"]
    params = {"limit": 100}
    accounts = S["User"]("me").get_ad_accounts(fields=fields, params=params)
    print_json(_collect(accounts, args.limit))


# ---------------------------------------------------------------------------
# 2. account-details
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_account_details(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "name", "business_name", "account_status", "balance",
        "amount_spent", "currency", "created_time",
    ]
    account = S["AdAccount"](args.id).api_get(fields=fields)
    print_json(account)


# ---------------------------------------------------------------------------
# 3. campaign
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_campaign(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "objective", "daily_budget",
        "lifetime_budget", "created_time", "updated_time",
    ]
    campaign = S["Campaign"](args.id).api_get(fields=fields)
    print_json(_format_budgets([campaign])[0])


# ---------------------------------------------------------------------------
# 4. campaigns
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_campaigns(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "objective", "daily_budget", "lifetime_budget",
    ]
    params = _build_params(args)
    campaigns = S["AdAccount"](account_id).get_campaigns(fields=fields, params=params)
    print_json(_format_budgets(_collect(campaigns, args.limit)))


# ---------------------------------------------------------------------------
# 5. adset
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_adset(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "campaign_id", "daily_budget",
        "lifetime_budget", "targeting", "optimization_goal",
    ]
    adset = S["AdSet"](args.id).api_get(fields=fields)
    print_json(_format_budgets([adset])[0])


# ---------------------------------------------------------------------------
# 6. adsets-by-ids
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_adsets_by_ids(args):
    init_api()
    S = _sdk()
    ids = [i.strip() for i in args.ids.split(",")]
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "campaign_id", "daily_budget",
        "lifetime_budget", "targeting",
    ]
    results = []
    for adset_id in ids:
        adset = S["AdSet"](adset_id).api_get(fields=fields)
        results.append(adset)
    print_json(_format_budgets(results))


# ---------------------------------------------------------------------------
# 7. adsets
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_adsets(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "campaign_id", "daily_budget",
        "lifetime_budget", "optimization_goal",
    ]
    params = _build_params(args)
    adsets = S["AdAccount"](account_id).get_ad_sets(fields=fields, params=params)
    print_json(_format_budgets(_collect(adsets, args.limit)))


# ---------------------------------------------------------------------------
# 8. adsets-by-campaign
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_adsets_by_campaign(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "daily_budget", "lifetime_budget",
        "targeting", "optimization_goal",
    ]
    params = _build_params(args)
    adsets = S["Campaign"](args.campaign).get_ad_sets(fields=fields, params=params)
    print_json(_format_budgets(_collect(adsets, args.limit)))


# ---------------------------------------------------------------------------
# 9. ad
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_ad(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "adset_id", "campaign_id",
        "creative", "created_time", "updated_time",
    ]
    ad = S["Ad"](args.id).api_get(fields=fields)
    print_json(ad)


# ---------------------------------------------------------------------------
# 10. ads
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_ads(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "adset_id", "campaign_id", "creative",
    ]
    params = _build_params(args)
    ads = S["AdAccount"](account_id).get_ads(fields=fields, params=params)
    print_json(_collect(ads, args.limit))


# ---------------------------------------------------------------------------
# 11. ads-by-campaign
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_ads_by_campaign(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "adset_id", "creative",
    ]
    params = _build_params(args)
    ads = S["Campaign"](args.campaign).get_ads(fields=fields, params=params)
    print_json(_collect(ads, args.limit))


# ---------------------------------------------------------------------------
# 12. ads-by-adset
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_ads_by_adset(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "status", "campaign_id", "creative",
    ]
    params = _build_params(args)
    ads = S["AdSet"](args.adset).get_ads(fields=fields, params=params)
    print_json(_collect(ads, args.limit))


# ---------------------------------------------------------------------------
# 13. creative
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_creative(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "url_tags", "link_url", "object_story_spec",
        "body", "title", "call_to_action_type",
    ]
    creative = S["AdCreative"](args.id).api_get(fields=fields)
    print_json(creative)


# ---------------------------------------------------------------------------
# 14. creatives-by-ad
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_creatives_by_ad(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "url_tags", "link_url", "object_story_spec",
        "body", "title", "call_to_action_type",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    creatives = S["Ad"](args.ad).get_ad_creatives(fields=fields, params=params)
    print_json(_collect(creatives, args.limit))


# ---------------------------------------------------------------------------
# 15. preview
# ---------------------------------------------------------------------------

PREVIEW_FORMATS = [
    "DESKTOP_FEED_STANDARD",
    "RIGHT_COLUMN_STANDARD",
    "MOBILE_FEED_STANDARD",
    "MOBILE_FEED_BASIC",
    "INSTAGRAM_STANDARD",
    "INSTAGRAM_STORY",
    "INSTAGRAM_REELS",
    "MARKETPLACE_MOBILE",
    "AUDIENCE_NETWORK_OUTSTREAM_VIDEO",
    "INSTANT_ARTICLE_STANDARD",
    "MESSENGER_MOBILE_INBOX_MEDIA",
]


@handle_fb_error
def cmd_preview(args):
    """Gera preview HTML de um criativo em um ou mais formatos.

    Formatos disponiveis: DESKTOP_FEED_STANDARD, RIGHT_COLUMN_STANDARD,
    MOBILE_FEED_STANDARD, MOBILE_FEED_BASIC, INSTAGRAM_STANDARD,
    INSTAGRAM_STORY, INSTAGRAM_REELS, MARKETPLACE_MOBILE,
    AUDIENCE_NETWORK_OUTSTREAM_VIDEO, INSTANT_ARTICLE_STANDARD,
    MESSENGER_MOBILE_INBOX_MEDIA

    Use --format all para gerar preview em todos os formatos.
    """
    init_api()
    S = _sdk()
    if args.format.lower() == "all":
        all_previews = []
        for fmt in PREVIEW_FORMATS:
            try:
                previews = S["AdCreative"](args.creative).get_previews(
                    params={"ad_format": fmt}
                )
                for p in _collect(previews):
                    p["_format"] = fmt
                    all_previews.append(p)
            except Exception:
                pass
        print_json(all_previews)
    else:
        params = {"ad_format": args.format}
        previews = S["AdCreative"](args.creative).get_previews(params=params)
        print_json(_collect(previews))


# ---------------------------------------------------------------------------
# 16. images
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_images(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "hash", "url", "url_128", "width", "height", "created_time",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    images = S["AdAccount"](account_id).get_ad_images(fields=fields, params=params)
    print_json(_collect(images, args.limit))


# ---------------------------------------------------------------------------
# 17. videos
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_videos(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "title", "description", "length", "source",
        "picture", "created_time", "updated_time",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    videos = S["AdAccount"](account_id).get_ad_videos(fields=fields, params=params)
    print_json(_collect(videos, args.limit))


# ---------------------------------------------------------------------------
# 18. activities
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_activities(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "event_type", "event_time", "actor_name", "object_name",
        "extra_data", "translated_event_type",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    activities = S["AdAccount"](account_id).get_activities(fields=fields, params=params)
    print_json(_collect(activities, args.limit))


# ---------------------------------------------------------------------------
# 19. activities-by-adset
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_activities_by_adset(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "event_type", "event_time", "actor_name", "object_name",
        "extra_data", "translated_event_type",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    activities = S["AdSet"](args.adset).get_activities(fields=fields, params=params)
    print_json(_collect(activities, args.limit))


# ---------------------------------------------------------------------------
# 20. custom-audiences
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_custom_audiences(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "subtype", "description", "approximate_count",
        "data_source", "delivery_status", "time_created", "time_updated",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    audiences = S["AdAccount"](account_id).get_custom_audiences(fields=fields, params=params)
    print_json(_collect(audiences, args.limit))


# ---------------------------------------------------------------------------
# 21. lookalike-audiences
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_lookalike_audiences(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "subtype", "description", "approximate_count",
        "lookalike_spec", "delivery_status", "time_created", "time_updated",
    ]
    params = {"filtering": [{"field": "subtype", "operator": "EQUAL", "value": "LOOKALIKE"}]}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    audiences = S["AdAccount"](account_id).get_custom_audiences(fields=fields, params=params)
    print_json(_collect(audiences, args.limit))


# ---------------------------------------------------------------------------
# 22. pixels
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_pixels(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "code", "last_fired_time", "is_unavailable",
        "owner_ad_account", "owner_business",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    pixels = S["AdAccount"](account_id).get_ads_pixels(fields=fields, params=params)
    print_json(_collect(pixels, args.limit))


# ---------------------------------------------------------------------------
# 23. pixel
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_pixel(args):
    init_api()
    S = _sdk()
    fields = parse_fields(args.fields) or [
        "id", "name", "code", "last_fired_time", "is_unavailable",
        "owner_ad_account", "owner_business",
    ]
    pixel = S["AdsPixel"](args.id).api_get(fields=fields)
    print_json(pixel)


# ---------------------------------------------------------------------------
# 24. pixel-stats
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_pixel_stats(args):
    init_api()
    S = _sdk()
    params = {}
    if args.start_time:
        params["start_time"] = args.start_time
    if args.end_time:
        params["end_time"] = args.end_time
    if args.aggregation:
        params["aggregation"] = args.aggregation
    stats = S["AdsPixel"](args.id).get_stats(params=params)
    print_json(_collect(stats, args.limit))


# ---------------------------------------------------------------------------
# 25. custom-conversions
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_custom_conversions(args):
    init_api()
    S = _sdk()
    account_id = resolve_account(args.account)
    fields = parse_fields(args.fields) or [
        "id", "name", "account_id", "custom_event_type", "rule",
        "pixel", "data_sources", "creation_time", "first_fired_time",
        "last_fired_time", "is_archived", "default_conversion_value",
    ]
    params = {}
    if args.limit:
        params["limit"] = args.limit
    if args.after:
        params["after"] = args.after
    conversions = S["AdAccount"](account_id).get_custom_conversions(
        fields=fields,
        params=params,
    )
    print_json(_collect(conversions, args.limit))


# ---------------------------------------------------------------------------
# 26. paginate
# ---------------------------------------------------------------------------

@handle_fb_error
def cmd_paginate(args):
    result = fetch_url(args.url)
    print_json(result)


# ---------------------------------------------------------------------------
# CLI parser
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Meta Ads Ratos — Read operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # 1. accounts
    p = sub.add_parser("accounts", help="List ad accounts for authenticated user")
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=None, help="Max results (default: all)")
    p.set_defaults(func=cmd_accounts)

    # 2. account-details
    p = sub.add_parser("account-details", help="Get details of one ad account")
    p.add_argument("--id", required=True, help="Account ID (ex: act_123)")
    add_fields_arg(p)
    p.set_defaults(func=cmd_account_details)

    # 3. campaign
    p = sub.add_parser("campaign", help="Get one campaign by ID")
    p.add_argument("--id", required=True, help="Campaign ID")
    add_fields_arg(p)
    p.set_defaults(func=cmd_campaign)

    # 4. campaigns
    p = sub.add_parser("campaigns", help="List campaigns of an account")
    add_account_arg(p)
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_campaigns)

    # 5. adset
    p = sub.add_parser("adset", help="Get one ad set by ID")
    p.add_argument("--id", required=True, help="Ad set ID")
    add_fields_arg(p)
    p.set_defaults(func=cmd_adset)

    # 6. adsets-by-ids
    p = sub.add_parser("adsets-by-ids", help="Get multiple ad sets by IDs")
    p.add_argument("--ids", required=True, help="Comma-separated ad set IDs")
    add_fields_arg(p)
    p.set_defaults(func=cmd_adsets_by_ids)

    # 7. adsets
    p = sub.add_parser("adsets", help="List ad sets of an account")
    add_account_arg(p)
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_adsets)

    # 8. adsets-by-campaign
    p = sub.add_parser("adsets-by-campaign", help="List ad sets of a campaign")
    p.add_argument("--campaign", required=True, help="Campaign ID")
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_adsets_by_campaign)

    # 9. ad
    p = sub.add_parser("ad", help="Get one ad by ID")
    p.add_argument("--id", required=True, help="Ad ID")
    add_fields_arg(p)
    p.set_defaults(func=cmd_ad)

    # 10. ads
    p = sub.add_parser("ads", help="List ads of an account")
    add_account_arg(p)
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_ads)

    # 11. ads-by-campaign
    p = sub.add_parser("ads-by-campaign", help="List ads of a campaign")
    p.add_argument("--campaign", required=True, help="Campaign ID")
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_ads_by_campaign)

    # 12. ads-by-adset
    p = sub.add_parser("ads-by-adset", help="List ads of an ad set")
    p.add_argument("--adset", required=True, help="Ad set ID")
    add_fields_arg(p)
    add_status_filter_arg(p)
    add_pagination_args(p)
    p.set_defaults(func=cmd_ads_by_adset)

    # 13. creative
    p = sub.add_parser("creative", help="Get one creative by ID")
    p.add_argument("--id", required=True, help="Creative ID")
    add_fields_arg(p)
    p.set_defaults(func=cmd_creative)

    # 14. creatives-by-ad
    p = sub.add_parser("creatives-by-ad", help="Get creatives of an ad")
    p.add_argument("--ad", required=True, help="Ad ID")
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.set_defaults(func=cmd_creatives_by_ad)

    # 15. preview
    p = sub.add_parser("preview", help="Get ad preview HTML")
    p.add_argument("--creative", required=True, help="Creative ID")
    p.add_argument("--format", default="DESKTOP_FEED_STANDARD",
                   help="Formato: DESKTOP_FEED_STANDARD, MOBILE_FEED_STANDARD, "
                        "INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTAGRAM_REELS, "
                        "ou 'all' para todos (default: DESKTOP_FEED_STANDARD)")
    p.set_defaults(func=cmd_preview)

    # 16. images
    p = sub.add_parser("images", help="List ad images")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_images)

    # 17. videos
    p = sub.add_parser("videos", help="List ad videos")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_videos)

    # 18. activities
    p = sub.add_parser("activities", help="Activity log of an account")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_activities)

    # 19. activities-by-adset
    p = sub.add_parser("activities-by-adset", help="Activity log of an ad set")
    p.add_argument("--adset", required=True, help="Ad set ID")
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_activities_by_adset)

    # 20. custom-audiences
    p = sub.add_parser("custom-audiences", help="List custom audiences")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_custom_audiences)

    # 21. lookalike-audiences
    p = sub.add_parser("lookalike-audiences", help="List lookalike audiences")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_lookalike_audiences)

    # 22. pixels
    p = sub.add_parser("pixels", help="List pixels/datasets of an account")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_pixels)

    # 23. pixel
    p = sub.add_parser("pixel", help="Get one pixel/dataset by ID")
    p.add_argument("--id", required=True, help="Pixel/Dataset ID")
    add_fields_arg(p)
    p.set_defaults(func=cmd_pixel)

    # 24. pixel-stats
    p = sub.add_parser("pixel-stats", help="Get pixel event stats")
    p.add_argument("--id", required=True, help="Pixel/Dataset ID")
    p.add_argument("--start-time", help="Start time accepted by Meta API")
    p.add_argument("--end-time", help="End time accepted by Meta API")
    p.add_argument("--aggregation", help="Aggregation accepted by Meta API")
    p.add_argument("--limit", type=int, default=None, help="Max results (default: all)")
    p.set_defaults(func=cmd_pixel_stats)

    # 25. custom-conversions
    p = sub.add_parser("custom-conversions", help="List custom conversions of an account")
    add_account_arg(p)
    add_fields_arg(p)
    p.add_argument("--limit", type=int, default=25, help="Max results (default: 25)")
    p.add_argument("--after", help="Pagination cursor")
    p.set_defaults(func=cmd_custom_conversions)

    # 26. paginate
    p = sub.add_parser("paginate", help="Fetch a raw pagination URL")
    p.add_argument("--url", required=True, help="Full pagination URL")
    p.set_defaults(func=cmd_paginate)

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
