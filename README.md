# Editorial Avatar

给一张照片，说明要用在哪里，让 AI 作为设计师与摄影师完成肖像设计。

适用于 ChatGPT 用户和具备图像生成能力的 Codex 用户。默认半写实手绘，支持其他画风与后续修改；用途不清楚时先问，明确后由助手完成造型、光线、色彩与构图。

这套创作流程与工具包帮助你减少重复交代、保存设计原则，并提供可复查示例和真实尺寸预览。

## 先看示例

以下人物及原始照片均为 AI 生成的虚构素材。示例展示实际输入和输出，不能作为真实人物身份保真的证据。生成条件与评审边界见 [验证记录](VALIDATION.md)。

### 开源社区头像

委托：用于 GitHub 和 Hugging Face，保留眼镜，自然、容易接近。

| 原始虚构照片 | Codex 图像工具成片 |
| --- | --- |
| ![虚构男性原始照片](examples/developer/source.png) | ![保留圆框眼镜的半写实社区头像](examples/developer/avatar.png) |

设计：保留圆框眼镜、灰白短发与年龄感；墨蓝便装配浅蓝灰背景，安静自然的神态。[实际生成指令](examples/developer/generation.prompt.txt) · [圆裁切与小尺寸预览](examples/developer/preview.html)。

### 大会演讲者头像

委托：技术大会官网的演讲者介绍头像，保留年龄感、自然肤色与短卷发。

| 原始虚构照片 | Codex 图像工具成片 |
| --- | --- |
| ![虚构女性原始照片](examples/speaker/source.png) | ![梅紫外套与浅灰紫背景的演讲者头像](examples/speaker/avatar.png) |

设计：梅紫便装外套配浅灰紫背景，保留短卷发与灰白发丝，神态平静亲和。[实际生成指令](examples/speaker/generation.prompt.txt) · [圆裁切与小尺寸预览](examples/speaker/preview.html)。两组均由 Codex 图像工具生成。

## ChatGPT：复制即可开始

1. 打开 [ChatGPT prompt](prompts/chatgpt.md)，复制“方案阶段”代码块。
2. 在支持图像生成的 ChatGPT 对话中粘贴，附上照片与用途，例如：“用于 GitHub 和 Hugging Face，保留眼镜，其他由你设计。”
3. 想靠近示例画风，可同时附上 [风格参考图](skills/editorial-avatar/references/style-anchor.png)，明确标注它只提供画风。只附人物照片也可以，但文字定义风格可能产生更大变化。
4. 看过方案后发送第二条“按方案生成”代码块，取得图像。在认可的结果上继续要求修改，例如：“保留这版的构图和服装，只去掉眼镜。”

ChatGPT 入口分成方案、生成两条消息，避免图像请求跳过用途澄清。未说明用途时，预期先问用途；明确后由助手设计。Codex 入口在用途明确后连续执行设计与生成。ChatGPT 无法凭本地文件路径读取照片，需要实际附图。图像生成、上传与编辑能力由你的账户及当前界面提供；本项目不提供生成额度。[官方图像使用说明](https://help.openai.com/en/articles/11084440)。

## Codex：安装完整 skill 文件夹

下载本仓库后，在仓库根目录执行以下命令。命令使用 Python 3，目标已存在时拒绝覆盖：

```bash
python3 -c 'from pathlib import Path; import shutil; d=Path.home()/".agents/skills/editorial-avatar"; d.parent.mkdir(parents=True, exist_ok=True); shutil.copytree("skills/editorial-avatar", d)'
```

安装位置依照 [Codex 本地 skills 文档](https://learn.chatgpt.com/docs/build-skills)。如果你的环境已在其他目录安装同名 skill，应先决定更新哪份，避免同时安装两个版本。安装后在可选 skills 中确认 `editorial-avatar`；未出现时重新启动 Codex。

附上照片并发送：

```text
$editorial-avatar 这张图用于 GitHub 和 Hugging Face 的头像，保留眼镜，其余由你设计。
```

此 skill 不会为 Codex 增加图像生成能力：需要当前环境已提供 `image_gen`。缺少该工具时只能得到创作简报，不能称为已完成图像生成。预览脚本只需 Python 3 标准库，无需 Node 或 API key；维护检查脚本要求 Python 3.9+。

## 检查小尺寸与圆形裁切

```bash
python3 skills/editorial-avatar/scripts/preview_avatar.py avatar.png --output preview.html
```

用浏览器打开生成的 HTML，以 100% 缩放查看。包含 40、64、128、256 CSS 像素的圆形裁切、深浅底色与完整原图；图片内嵌，可离线分享。它不修改原图、不上传文件，也不会自动判断好不好看。生成的预览包含原始图片数据，分享预览等于分享图片。已有输出默认拒绝覆盖；需要替换时添加 `--force`。

仓库内的示例预览使用 `--linked` 相对引用原图，避免在 Git 中重复保存大块图片数据。该模式离线使用时需保留 HTML 与图片的相对位置；默认不加此选项时仍生成独立的内嵌版。

## 维护与贡献

核心设计逻辑只维护在 [workflow.md](skills/editorial-avatar/references/workflow.md)。ChatGPT prompt 从它生成，Codex 直接读取它；不要手工修改生成文件。

```bash
python3 scripts/build_prompt.py
python3 scripts/build_prompt.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

README 与验证记录是 Markdown 事实源。HTML 阅读版通过 Node 20+ 与开发依赖 `marked` 生成，普通使用不需要安装这些依赖：

```bash
npm ci
npm run build:docs
npm run check:docs
```

贡献示例时提交用途、输入分工、实际指令、未挑选的试验结果及具体问题；只提交你有权公开的素材。区分工具已生成、助手审片和用户认可，不把失败图删掉后宣称稳定。涉及质量提升的主张应增加同输入、同模型条件与相同重试预算的简短 prompt 对照。

当前只完成少量虚构人物与基本交互测试，尚无证据证明画质优于简短 prompt 或能够稳定出片，完整边界见 [验证记录](VALIDATION.md)。

## 许可与素材

代码、prompt 与文档采用 [MIT License](LICENSE)。本仓库附带的 AI 生成虚构素材可随项目使用与再分发，来源及适用范围见 [素材说明](ASSETS.md)。许可不覆盖用户另行上传的照片，也不为生成内容承诺独占性或第三方权利状况。
