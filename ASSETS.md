# 素材来源与使用范围

仓库中的人物均为本项目测试时生成的虚构人物。没有包含维护者的证件照、私人头像、第三方原始风格图或历史私人试验。

- `skills/editorial-avatar/references/style-anchor.png`：Codex 内置图像工具从纯文字生成的半写实手绘参考。最终指令见相邻 `style-anchor.prompt.txt`。曾生成一张纹理更重的候选，因偏向油画质感未选为参考；当前参考是第二次生成，没有使用任何输入图片。
- `examples/developer/source.png`：Codex 内置图像工具纯文字生成的虚构男性照片。
- `examples/developer/avatar.png`：以上照片提供人物身份，公共风格图提供绘画语言，按 GitHub / Hugging Face 用途生成。
- `examples/speaker/source.png` 与 `avatar.png`：Codex 图像工具生成的虚构女性源照片与大会演讲者头像。它们是独立的 Codex 测试素材，不是 ChatGPT 网页试验的下载文件。
- `examples/remove-glasses/avatar.png`：基于公开的 developer/avatar.png 去除眼镜，2026-09-22 一次编辑生成。
- `examples/researcher/avatar.png`：同一虚构男性源照片与公共风格参考，按深色研究团队主页用途重新设计，2026-09-22 一次生成。
- `examples/speaker-smile/avatar.png`：基于公开的 speaker/avatar.png 调整微笑与头部姿态，2026-09-22 一次编辑生成。三个新增案例均未使用私人照片，没有隐藏的重试或候选筛选。

文件哈希、生成入口、参考图顺序和实际指令记录在 [manifest.json](examples/manifest.json)。工具没有公开的模型标识与 seed 记为 `null`。图像不会因记录相同 prompt 而保证逐像素重现。

对本项目有权许可的 AI 生成素材，允许使用、修改和再分发，可随项目代码共同使用。该许可不表示生成素材具有独占权利，也不覆盖使用者另行上传的肖像、商标或其他第三方素材。贡献真实人物示例时，需要同时具备照片使用权和人物公开展示许可；不要把只允许私下编辑的照片提交到仓库。
