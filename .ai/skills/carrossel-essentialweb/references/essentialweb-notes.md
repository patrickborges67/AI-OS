# EssentialWeb Carousel Notes

- Sempre usar `assets/Logo EssentialWeb.png` como logo da marca nos carrosséis da EssentialWeb.
- Na capa, substituir iniciais genéricas como `E` pela logo dentro do badge do handle.
- Para HTML editável, copiar a logo para a pasta do carrossel como `assets/logo-essentialweb.png`.
- Para HTML inline, embutir a logo em base64 junto com a imagem da capa.
- Encoding: manter todos os HTMLs e MDs em UTF-8 sem BOM. Ao gerar ou regravar arquivos no Windows, não usar `Set-Content` sem controle explícito; preferir escrita UTF-8 sem BOM e validar que não restaram sequências mojibake típicas de texto UTF-8 lido como Windows-1252.
