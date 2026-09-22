# Editorial Avatar

给一张照片，说明要用在哪里，让 AI 作为设计师与摄影师完成肖像设计。

适用于 ChatGPT 用户和具备图像生成能力的 Codex 用户。默认半写实手绘，支持其他画风与后续修改；用途不清楚时先问，明确后由助手完成造型、光线、色彩与构图。

这套创作流程与工具包帮助你减少重复交代、保存设计原则，并提供可复查示例和真实尺寸预览。

## 先看示例

以下人物及原始照片均为 AI 生成的虚构素材。示例展示实际输入和输出，不能作为真实人物身份保真的证据。生成条件与评审边界见 [验证记录](VALIDATION.md)。

目前有 **5 组图像示例**：开源社区头像、大会演讲者头像、去眼镜局部编辑、研究团队深色头像、微笑与姿态调整。后面三组复用前面的虚构人物，便于观察用途和编辑要求变化后的结果；不代表五个独立人物测试。

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

### 去掉眼镜，保留整体设计

测试请求：“继续修改这张 GitHub / Hugging Face 头像：只去掉眼镜，保留这一版的构图、神态、发型、衣服、背景和画风。”

| 编辑基底 | 去眼镜结果 |
| --- | --- |
| ![带眼镜的编辑基底](examples/developer/avatar.png) | ![去掉眼镜后的社区头像](examples/remove-glasses/avatar.png) |

观察：镜框、鼻托和镜腿已去除，服装、背景与整体构图接近原版；眼周有补绘，不能当成遮挡细节的真实还原，也不保证其他位置像素不变。一次生成，无重试。[实际生成指令](examples/remove-glasses/generation.prompt.txt) · [圆裁切预览](examples/remove-glasses/preview.html)。

### 同一人物，用于研究团队主页

测试请求：“为研究团队官网做一张头像。保留眼镜和年龄感，半写实手绘；主页采用深色视觉，请你设计服装、光线和背景。”

| 原始虚构照片 | 深色研究团队头像 |
| --- | --- |
| ![用于研究团队头像的原始虚构照片](examples/developer/source.png) | ![深绿色便装与蓝绿色背景的研究团队头像](examples/researcher/avatar.png) |

设计：深绿便装与蓝绿色背景，柔和侧光突出面部，保留眼镜、灰白头发和胡茬。40 px 下肩部与背景对比偏弱，脸部仍可辨；不能据此认为深色版优于社区版。一次生成，无重试。[实际生成指令](examples/researcher/generation.prompt.txt) · [圆裁切预览](examples/researcher/preview.html)。

### 微笑与轻微歪头

测试请求：“在这张大会演讲者头像的基础上，稍微歪头，增加一个自然的露齿微笑，像和熟人交流。保留人物年龄感、服装、背景、画风和画幅。”

| 编辑基底 | 表情与姿态调整 |
| --- | --- |
| ![修改前的大会演讲者头像](examples/speaker/avatar.png) | ![轻微歪头并露齿微笑的演讲者头像](examples/speaker-smile/avatar.png) |

观察：轻微歪头与少量露齿可见，梅紫外套、灰紫背景和短卷发延续；面部纹理与头肩位置也有重绘。40 px 下可以看到笑意，不能细辨牙齿和眼部细节。一次生成，无重试。[实际生成指令](examples/speaker-smile/generation.prompt.txt) · [圆裁切预览](examples/speaker-smile/preview.html)。

新增测试于 2026-09-22 完成。请求由维护助手构造，并按仓库 workflow 编写实际生成简报；这些是流程指导下的生成与编辑样例，不是独立新会话的 skill 自动触发测试。全部为 Codex 内置图像工具输出，已作助手视觉检查，尚未获独立真人评价。

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
$skill-installer 请安装 https://github.com/xiaofengShi/editorial-avatar/tree/main/skills/editorial-avatar 中的 skill。
```

安装完成后，在下一轮对话选择或输入 `$editorial-avatar` 使用。已经安装的用户直接激活即可。安装和调用是两个步骤，仓库链接本身不会自动注册 skill。

此 skill 需要当前 Codex 环境已提供图像生成能力。缺少该能力时，助手会说明限制并提供创作简报。调用方式见 [Codex skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 检查小尺寸与圆形裁切

Codex skill 会调用附带的预览工具。你也可以在对话中要求：“检查这版头像的小尺寸和圆形裁切，并给我预览。”

用浏览器打开生成的 HTML，以 100% 缩放查看。包含 40、64、128、256 CSS 像素的圆形裁切、深浅底色与完整原图；图片内嵌，可离线分享。它不修改原图、不上传文件，也不会自动判断好不好看。生成的预览包含原始图片数据，分享预览等于分享图片。已有输出默认拒绝覆盖；需要替换时添加 `--force`。

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
