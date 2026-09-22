# 素材来源与使用范围

仓库包含两类示例：五组使用 AI 生成虚构人物的头像，以及一组用户明确授权用于项目示例展示的真实旅行照片与插画（由 README 迁至项目主页）。授权限于本次旅行案例，没有扩展到其他私人照片、证件照或早期对话的原始风格图。

- `skills/editorial-avatar/references/style-anchor.png`：Codex 内置图像工具从纯文字生成的半写实手绘参考。最终指令见相邻 `style-anchor.prompt.txt`。曾生成一张纹理更重的候选，因偏向油画质感未选为参考；当前参考是第二次生成，没有使用任何输入图片。
- `examples/developer/source.png`：Codex 内置图像工具纯文字生成的虚构男性照片。
- `examples/developer/avatar.png`：以上照片提供人物身份，公共风格图提供绘画语言，按 GitHub / Hugging Face 用途生成。
- `examples/developer/preview-screenshot.png`：2026-09-22 从 `examples/developer/preview.html` 截取的浏览器预览，展示上述虚构人物头像在深浅背景下的四档圆形裁切；截图为缩略展示，不用于量测 CSS 像素。
- `examples/speaker/source.png` 与 `avatar.png`：Codex 图像工具生成的虚构女性源照片与大会演讲者头像。它们是独立的 Codex 测试素材，不是 ChatGPT 网页试验的下载文件。
- `examples/remove-glasses/avatar.png`：基于公开的 developer/avatar.png 去除眼镜，2026-09-22 一次编辑生成。
- `examples/researcher/avatar.png`：同一虚构男性源照片与公共风格参考，按深色研究团队主页用途重新设计，2026-09-22 一次生成。
- `examples/speaker-smile/avatar.png`：基于公开的 speaker/avatar.png 调整微笑与头部姿态，2026-09-22 一次编辑生成。首版后来因头身姿态不协调被用户否定，保留作为问题案例。
- `examples/speaker-smile/avatar-v2.png`：收到反馈后，从原 speaker/avatar.png 与 speaker/source.png 重新调整头颈肩，追加一次修正生成；未使用私人照片，尚待用户确认。

文件哈希、生成入口、参考图顺序和实际指令记录在 [manifest.json](examples/manifest.json)。工具没有公开的模型标识与 seed 记为 `null`。图像不会因记录相同 prompt 而保证逐像素重现。

## 真实旅行案例

- `examples/travel/source.png`：用户提供的旅行照片之公开副本。图像工具未能读取原 JPEG，使用 PNG 转换版生成。发布时移除了 EXIF、文本等元数据，保留颜色信息及原 PNG 的 IDAT 图像数据；原文件没有被改写。
- `examples/travel/illustration.png`：2026-09-22 生成的旅行氛围插画，用户认可并明确要求加入 GitHub README 示例。街景和构图经过重绘，不能作为现场记录。
- 实际画风输入为早期对话中提供的参考图，不是仓库的公共 style-anchor.png。该参考未获再分发授权，因此只记录哈希与输入位置，不发布图像或私人路径。不能声称仅凭仓库内素材可完整复现本次输入。
- 上述真实照片及其人物插画仅获本仓库示例展示授权，**不属于 MIT 许可或下述虚构素材的开放再分发范围**。其他用途需另获权利人许可。

对本项目有权许可的 AI 生成素材，允许使用、修改和再分发，可随项目代码共同使用。该许可不表示生成素材具有独占权利，也不覆盖使用者另行上传的肖像、商标或其他第三方素材。贡献真实人物示例时，需要同时具备照片使用权和人物公开展示许可；不要把只允许私下编辑的照片提交到仓库。
