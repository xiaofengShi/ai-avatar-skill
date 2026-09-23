<h1 align="center"><img src="assets/logo-v2.png" width="40" height="40" alt="">&nbsp; <img src="assets/wordmark.svg" width="220" height="40" alt="Editorial Avatar"> <a href="https://xiaofengshi.github.io/ai-avatar-skill/"><img src="assets/homepage-link.svg" width="108" height="40" alt="Homepage ↗"></a></h1>

Give one photo and its purpose — let AI act as designer and photographer for your portrait.

[<img src="assets/icons/code.svg" width="16" height="16" alt=""> Codex skill](#codex) · [<img src="assets/icons/chat.svg" width="16" height="16" alt=""> ChatGPT prompt](#chatgpt) · [Validation log](VALIDATION.md) · [Issues](https://github.com/xiaofengShi/ai-avatar-skill/issues) · [中文文档](#zh)

## What it does

| Capability | How it works |
| --- | --- |
| Purpose-driven design | Provide a photo and where it will be used. If the purpose is unclear, the assistant asks first, then designs pose, composition, styling, lighting, and palette. The source photo's head angle is a reference, not a required output angle. |
| Style & local edits | Semi-realistic illustration by default; request other art styles, keep glasses, or adjust expressions — and keep iterating on a version you approve. |
| Avatar crop check | Preview circular crops at 40, 64, 128, and 256 px, on both light and dark backgrounds. |
| Two entry points | Codex runs the skill; ChatGPT uses a two-stage prompt (plan, then generate). |

**Requirement:** your environment must have image generation capability. This project provides the workflow and tools — not a model or generation quota. Examples, before/after comparisons, and crop screenshots live on the [project homepage](https://xiaofengshi.github.io/ai-avatar-skill/); this README covers installation and usage.

<a id="chatgpt"></a>

## ChatGPT: copy and start

1. Open the [ChatGPT prompt](prompts/chatgpt.md) and copy the plan-stage code block.
2. Paste it into a ChatGPT conversation with image generation, attach a photo and its purpose — for example: "For GitHub and Hugging Face, keep my glasses, design everything else yourself."
3. To stay close to the example art style, also attach the [style reference](skills/editorial-avatar/references/style-anchor.png) and note clearly that it only defines the art style. Attaching just the person's photo works too, but describing the style in words may produce larger variation.
4. After reviewing the plan, send the second "generate per plan" block to get the image. Then iterate on a result you approve — for example: "Keep this composition and outfit, only remove the glasses."

The ChatGPT entry splits plan and generate into two messages so image requests do not skip purpose clarification. Without a stated purpose, the assistant is expected to ask first, then design. The Codex entry runs design and generation continuously once the purpose is clear. ChatGPT cannot read photos from local file paths — attach them in the conversation. Image generation, upload, and editing are provided by your account and current interface; this project does not provide generation quota. See the [official image usage guide](https://help.openai.com/en/articles/11084440).

<a id="codex"></a>

## Codex: activate the skill

Once installed, pick `editorial-avatar` in the Codex input box, attach a photo, and state the purpose — or send directly:

```text
$editorial-avatar This photo is for my GitHub and Hugging Face avatar. Keep my glasses; design everything else yourself.
```

After activation, Codex reads the skill and completes purpose clarification, portrait design, image generation, and avatar preview. Daily use needs only a photo and your requirements — no manual Python runs or file copying.

**First use, not yet installed:** call the installer skill in Codex first:

```text
$skill-installer Install the skill at https://github.com/xiaofengShi/ai-avatar-skill/tree/main/skills/editorial-avatar
```

After installation, pick or type `$editorial-avatar` in the next conversation; already-installed users can activate directly. Installing and invoking are two steps — the repository link itself does not register the skill automatically.

This skill requires image generation capability in the current Codex environment. Without it, the assistant explains the limitation and provides a creative brief. See the [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) for invocation details.

## Check small sizes and circular crops

The Codex skill calls the bundled preview tool. You can also ask in conversation: "Check this avatar at small sizes and circular crops, and show me a preview."

[See crop examples on the showcase page](https://xiaofengshi.github.io/ai-avatar-skill/showcase.html#preview) · [Open a real preview](https://xiaofengshi.github.io/ai-avatar-skill/examples/developer/preview.html)

Open the generated HTML in a browser at 100% zoom. It includes circular crops at 40, 64, 128, and 256 CSS px, light and dark backgrounds, and the full original image; images are embedded for offline sharing. It does not modify the original, upload files, or judge whether the result looks good. The preview embeds the original image data — sharing the preview shares the image. Existing output is refused by default; add `--force` to replace it.

Online preview links in this README are served via GitHub Pages; HTML file pages inside the GitHub repo show source only. For offline viewing, download the repository and open the HTML in a browser.

Example previews in this repo use `--linked` to reference originals by relative path, avoiding duplicate copies of large image data in Git. In this mode, keep the HTML and images in their relative positions when offline; without the flag, a standalone embedded version is generated.

## Maintenance & contributing

Core design logic lives only in [workflow.md](skills/editorial-avatar/references/workflow.md). The ChatGPT prompt is generated from it, and Codex reads it directly — do not hand-edit generated files.

The commands below let maintainers verify the toolkit; regular users go through the skill entry points above. The Python tools depend only on the standard library; maintenance checks require Python 3.9+. To debug the avatar preview on its own:

```bash
python3 skills/editorial-avatar/scripts/preview_avatar.py avatar.png --output preview.html
```

```bash
python3 scripts/build_prompt.py
python3 scripts/build_prompt.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

This README covers features and usage; [SHOWCASE.md](SHOWCASE.md) maintains the case gallery and generates `showcase.html`; the landing pages `index.html` (English) and `zh.html` (中文) are hand-authored; [VALIDATION.md](VALIDATION.md) generates `validation.html`. The web template and styles live in `scripts/showcase.html`. HTML is generated with Node 20+ and the dev dependency `marked`; regular use does not require installing them. GitHub Pages publishes the generated HTML from the `main` branch root, with `.nojekyll` preserving original static file paths. After updating docs, regenerate the HTML and commit it together:

```bash
npm ci
npm run build:docs
npm run check:docs
```

When contributing examples, submit the purpose, the division of labor among inputs, the actual prompts, unselected trial results, and known issues; only submit material you have the right to publish. Distinguish tool-generated output, assistant review, and user approval — do not delete failed images and claim stability. Claims of quality improvement should include short-prompt comparisons under the same input, same model, and same retry budget.

So far the project has a small number of fictional-character tests, one real travel-photo case, and basic interaction tests. There is no evidence yet of better image quality than short prompts, or of stable output — see the [validation log](VALIDATION.md) for the full boundaries.

## License & assets

Code, prompts, and docs are under the [MIT License](LICENSE). The AI-generated fictional assets bundled with this repo may be used and redistributed with the project; see [asset notes](ASSETS.md) for sources and scope. The travel case is licensed only for display as an example in this repository — neither MIT nor the fictional-asset redistribution terms apply to it. The license also does not cover photos uploaded by users.

---

<a id="zh"></a>

# 中文文档

给一张照片，说明用途，让 AI 作为设计师与摄影师完成肖像设计。

## 能做什么

| 能力 | 使用方式 |
| --- | --- |
| 按用途设计 | 提供照片与使用场景；用途不明确时先澄清，再设计构图、造型、光线与配色。 |
| 风格与局部修改 | 默认半写实手绘，可指定其他画风、保留眼镜或调整表情，并在认可版本上继续修改。 |
| 头像裁切检查 | 查看 40、64、128、256 px 圆形裁切，以及深浅背景下的效果。 |
| 两种使用入口 | Codex 通过 skill 执行；ChatGPT 通过方案、生成两阶段 prompt 使用。 |

**使用要求：**当前环境需具备图像生成能力。本项目提供工作流与工具，不提供模型或生成额度。示例、前后对照和裁切截图集中在[项目主页](https://xiaofengshi.github.io/ai-avatar-skill/)；这里保留安装与使用说明。

## ChatGPT：复制即可开始

1. 打开 [ChatGPT prompt](prompts/chatgpt.md)，复制“方案阶段”代码块。
2. 在支持图像生成的 ChatGPT 对话中粘贴，附上照片与用途，例如：“用于 GitHub 和 Hugging Face，保留眼镜，其他由你设计。”
3. 想靠近示例画风，可同时附上 [风格参考图](skills/editorial-avatar/references/style-anchor.png)，明确标注它只提供画风。只附人物照片也可以，但文字定义风格可能产生更大变化。
4. 看过方案后发送第二条“按方案生成”代码块，取得图像。在认可的结果上继续要求修改，例如：“保留这版的构图和服装，只去掉眼镜。”

ChatGPT 入口分成方案、生成两条消息，避免图像请求跳过用途澄清。未说明用途时，预期先问用途；明确后由助手设计。Codex 入口在用途明确后连续执行设计与生成。ChatGPT 无法凭本地文件路径读取照片，需要实际附图。图像生成、上传与编辑能力由你的账户及当前界面提供；本项目不提供生成额度。[官方图像使用说明](https://help.openai.com/en/articles/11084440)。

## Codex：直接激活 skill

已安装后，在 Codex 输入框中选择 `editorial-avatar`，附上照片并说明用途；也可以直接发送：

```text
$editorial-avatar 这张图用于 GitHub 和 Hugging Face 的头像，保留眼镜，其余由你设计。
```

激活后由 Codex 读取 skill，完成用途澄清、肖像设计、图像生成与头像预览。日常使用只需照片和需求，无需手动运行 Python 或复制文件。

**首次使用、尚未安装时**，先在 Codex 中调用安装 skill：

```text
$skill-installer 请安装 https://github.com/xiaofengShi/ai-avatar-skill/tree/main/skills/editorial-avatar 中的 skill。
```

安装完成后，在下一轮对话选择或输入 `$editorial-avatar` 使用。已经安装的用户直接激活即可。安装和调用是两个步骤，仓库链接本身不会自动注册 skill。

此 skill 需要当前 Codex 环境已提供图像生成能力。缺少该能力时，助手会说明限制并提供创作简报。调用方式见 [Codex skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 检查小尺寸与圆形裁切

Codex skill 会调用附带的预览工具。你也可以在对话中要求：“检查这版头像的小尺寸和圆形裁切，并给我预览。”

[查看案例页中的裁切展示](https://xiaofengshi.github.io/ai-avatar-skill/showcase.html#preview) · [打开实际预览](https://xiaofengshi.github.io/ai-avatar-skill/examples/developer/preview.html)

用浏览器打开生成的 HTML，以 100% 缩放查看。包含 40、64、128、256 CSS 像素的圆形裁切、深浅底色与完整原图；图片内嵌，可离线分享。它不修改原图、不上传文件，也不会自动判断好不好看。生成的预览包含原始图片数据，分享预览等于分享图片。已有输出默认拒绝覆盖；需要替换时添加 `--force`。

README 中的在线预览链接通过 GitHub Pages 展示；GitHub 仓库中的 HTML 文件页只显示源码。离线查看时下载仓库，用浏览器打开对应 HTML。

仓库内的示例预览使用 `--linked` 相对引用原图，避免在 Git 中重复保存大块图片数据。该模式离线使用时需保留 HTML 与图片的相对位置；默认不加此选项时仍生成独立的内嵌版。

## 维护与贡献

核心设计逻辑只维护在 [workflow.md](skills/editorial-avatar/references/workflow.md)。ChatGPT prompt 从它生成，Codex 直接读取它；不要手工修改生成文件。

以下命令供维护者验证工具包，普通用户通过上述 skill 入口使用。Python 工具只依赖标准库，维护检查要求 Python 3.9+。单独调试头像预览时可运行：

```bash
python3 skills/editorial-avatar/scripts/preview_avatar.py avatar.png --output preview.html
```

```bash
python3 scripts/build_prompt.py
python3 scripts/build_prompt.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

README 维护功能与使用说明；[SHOWCASE.md](SHOWCASE.md) 维护案例展示，生成案例页 `showcase.html`；落地页 `index.html`（英文）与 `zh.html`（中文）为手工维护；[VALIDATION.md](VALIDATION.md) 生成 `validation.html`。网页模板与样式位于 `scripts/showcase.html`。HTML 通过 Node 20+ 与开发依赖 `marked` 生成，普通使用不需要安装这些依赖。GitHub Pages 从 `main` 分支根目录发布已生成的 HTML，`.nojekyll` 保留静态文件的原始路径；更新文档后应重新生成 HTML 并一并提交：

```bash
npm ci
npm run build:docs
npm run check:docs
```

贡献示例时提交用途、输入分工、实际指令、未挑选的试验结果及具体问题；只提交你有权公开的素材。区分工具已生成、助手审片和用户认可，不把失败图删掉后宣称稳定。涉及质量提升的主张应增加同输入、同模型条件与相同重试预算的简短 prompt 对照。

当前完成了少量虚构人物测试、一组真实旅行照片案例与基本交互测试，尚无证据证明画质优于简短 prompt 或能够稳定出片，完整边界见 [验证记录](VALIDATION.md)。

## 许可与素材

代码、prompt 与文档采用 [MIT License](LICENSE)。本仓库附带的 AI 生成虚构素材可随项目使用与再分发，来源及适用范围见 [素材说明](ASSETS.md)。旅行案例仅获本仓库示例展示授权，不适用 MIT 或虚构素材的再分发许可。许可也不覆盖用户另行上传的照片。
