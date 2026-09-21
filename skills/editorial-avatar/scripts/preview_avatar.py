#!/usr/bin/env python3
"""Create an offline, non-destructive avatar preview (Python standard library only)."""
import argparse
import base64
from html import escape
from pathlib import Path
import os
from urllib.parse import quote


def image_uri(path):
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        mime = "image/png"
    elif data.startswith(b"\xff\xd8\xff"):
        mime = "image/jpeg"
    elif data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        mime = "image/webp"
    elif data[:6] in (b"GIF87a", b"GIF89a"):
        mime = "image/gif"
    else:
        raise ValueError("Unsupported image signature; use PNG, JPEG, WebP or GIF")
    return f"data:{mime};base64," + base64.b64encode(data).decode("ascii")


def render(path, linked_output=None):
    uri = image_uri(path)
    if linked_output is not None:
        uri = quote(Path(os.path.relpath(path.resolve(), linked_output.resolve().parent)).as_posix())
    storage = "图片以相对路径引用，离线分享时需保留图片与 HTML 的相对位置" if linked_output else "所有图像已内嵌，无上传和网络请求"
    name = escape(path.name)
    panels = []
    for theme, label in (("light", "浅色界面"), ("dark", "深色界面")):
        samples = "".join(
            f'<figure><img src="{uri}" width="{size}" height="{size}" '
            f'alt="{size} 像素居中圆形裁切" class="avatar">'
            f'<figcaption>{size} px</figcaption></figure>'
            for size in (40, 64, 128, 256)
        )
        panels.append(f'<section class="{theme}"><h2>{label}</h2><div class="samples">{samples}</div></section>')
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data: 'self'; style-src 'unsafe-inline'; base-uri 'none'">
<title>头像裁切检查 · {name}</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#eceeeb;color:#202823;font:16px/1.6 system-ui,sans-serif}}
main{{max-width:1080px;margin:auto;padding:clamp(12px,3vw,32px)}}h1{{font-size:clamp(23px,4vw,34px);line-height:1.2}}
h1,p,figcaption{{overflow-wrap:anywhere}}section{{padding:16px;margin:20px 0;border-radius:12px;border:1px solid #cbd1ca}}
h2{{font-size:18px;margin:0 0 20px}}.light{{background:#fff}}.dark{{background:#151b20;color:#f0f3f4;border-color:#343e45}}
.samples{{display:flex;flex-wrap:wrap;align-items:end;gap:24px}}figure{{margin:0;text-align:center;max-width:100%}}
.avatar{{display:block;object-fit:cover;object-position:center;border-radius:50%;max-width:100%}}
figcaption{{margin-top:8px;font-size:14px}}.original{{display:block;width:min(100%,512px);height:auto}}
@media print{{body{{background:white}}section{{break-inside:avoid}}.dark{{print-color-adjust:exact;-webkit-print-color-adjust:exact}}}}
</style></head><body><main><h1>头像裁切检查</h1><p>{name} · 原图未修改。{storage}。</p>
<p>以浏览器 100% 缩放查看。尺寸为 CSS 像素，窄于 312 px 的页面可能压缩最大样本。圆裁切采用居中 cover；真实平台可能允许不同取景。</p>
{''.join(panels)}<section class="light"><h2>完整原图</h2><img class="original" src="{uri}" alt="未裁切的完整头像"></section>
<p>检查：小尺寸能否认出人物；发型、眼镜是否被误裁；表情和头颈肩是否自然；深浅底色下是否清晰。预览生成不代表审美检查通过。</p>
</main></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--linked", action="store_true", help="link the local image relative to output instead of embedding it")
    args = parser.parse_args()
    if args.image.resolve() == args.output.resolve():
        parser.error("Output must not replace the source image")
    try:
        document = render(args.image, args.output if args.linked else None)
        with args.output.open("w" if args.force else "x", encoding="utf-8") as file:
            file.write(document)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Preview failed: {error}\n")
    print(args.output)


if __name__ == "__main__":
    main()
