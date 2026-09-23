# Validation record

First checks: 2026-09-21; additional cases: 2026-09-22; pose rule updated: 2026-09-23. This English record covers the published examples, entry points, preview tool, and evidence limits. The [Chinese log](validation.html) retains the detailed test chronology.

## What the evidence supports

- The Chinese ChatGPT prompt is generated from the canonical Chinese workflow, which the Codex skill reads. The English ChatGPT prompt is generated from a maintained English translation. A generated prompt is a packaging check, not a behavioral test.
- Codex's built-in image tool produced five public avatar cases involving two AI-generated fictional people: two source-photo portraits, one new-use portrait of the same person, and two edits of prior avatars. The assistant prepared the briefs using the skill workflow; these were not blind tests of automatic skill activation.
- One additional case uses a real travel photo. Its owner liked the result and approved its display here. This is one user-approved image, not six independent user reviews.
- Preview-tool checks cover preservation of source image bytes, embedded display, HTML escaping of filenames, overwrite refusal for both input and output, and rejection of SVG image input. The skill package passed structural checks. Neither result proves aesthetic quality.

## Review of published cases

The [case gallery](showcase.en.html#examples) pairs each source or edit base with its result, actual request, and generation prompt. It also preserves the problematic first smile result and its correction.

**Travel illustration.** The person photo supplied identity and context. A separate style reference from an earlier conversation supplied painting language, so this case does not have the same reference conditions as the fictional examples. Redistribution permission for that reference was not granted; the repository records its hash and input position but does not include the image. The first image call failed with `invalid_image_file` for the JPEG. Conversion to PNG followed by the same brief produced one result, without quality retries or candidate selection. The assistant observed that the side profile, glasses, short hair, and backpack remained, while the street setting was reconstructed. The image should not be treated as a faithful map or directions. The user said the result was good and approved public display. This does not establish identity fidelity across people or stable generations. The travel image was reviewed as a vertical environmental portrait, not as a circular avatar.

**Community avatar.** A fictional man's photo and a public style reference informed the GitHub / Hugging Face avatar. One generation preserved visible cues including glasses, grey hair, facial hair, and broad facial shape; skin texture remained finer than in the reference style. Only the assistant reviewed it. It has no independent user approval.

**Conference speaker.** A separately generated fictional woman's photo and the same public style reference informed a speaker portrait. One generation retained visible age, skin-tone, and curl cues while changing the outfit and background. Some facial features were redrawn. It has no user approval or measured identity-fidelity result.

**Three additional cases.** Removing glasses from the community avatar left the broad design similar, but the previously hidden eye area was newly painted, not recovered. A research-team variation kept glasses and age cues; at 40 px its shoulder contrast was weak. A smile-and-tilt edit initially produced an awkward head/body alignment. The user flagged that error. One correction reduced the tilt and adjusted shoulders and neckline; the assistant inspected its full image and circular crops, but the user has not approved this revised version. The earlier assistant assessment of the first version's pose was wrong: small-size crop checks did not catch the whole-body problem.

Five fictional-character cases had one initial image call each; the smile case then had one correction. Actual requests, prompts, input roles, hashes, and outputs are in the published case directories. These examples show process coverage, not a success rate.

## Purpose versus the source camera angle

On 2026-09-23 the real travel source photo was also tried locally for a conference-speaker use. The first brief kept too much of the side profile, making both eyes and the face less visible for that purpose. A revised local result turned the face closer to the camera; the assistant inspected 160 px and 240 px speaker-card views and found both eyes visible without an obvious head/neck/shoulder problem. The revised image has not been approved for public display and is **not** counted among the six public cases. Because the source exposes only one side of the face, the unseen side must be inferred by the model; its fidelity is unverified. The shared workflow now treats source angle as a reference to weigh against purpose, not a fixed constraint.

## ChatGPT interaction checks

The 2026-09-21 Chrome test used a fictional woman generated in ChatGPT itself; no private photo was uploaded. An early single-message Chinese workflow plus a vague avatar request generated an image without asking where the avatar would be used. After a conference purpose was supplied, another image was generated, but it remained more photographic than the requested illustration. This was **not** a successful purpose-clarification test.

The workflow was then split into planning and generation messages. In the same conversation, the revised Chinese plan referred to the original photo and specified attire, backdrop, expression, and painting direction; a second message triggered image generation. In a separate new conversation, an unspecified-purpose avatar request received a question about intended use and no image. These checks support basic two-stage interaction for that tested Chinese wording, but not consistent style matching. The webpage did not expose a verifiable internal image prompt, model version, seed, or downloadable file; the ChatGPT output is not included here. The new-conversation clarification check had neither a stated purpose nor an attached photo. The later workflow update for adjusting source head angle has not been retested in ChatGPT.

The [English ChatGPT prompt](https://github.com/xiaofengShi/ai-avatar-skill/blob/main/prompts/chatgpt.en.md) was translated and generated on 2026-09-23. The Chinese observations above do **not** establish that the English wording clarifies purpose, completes both stages, or handles edits correctly. On 2026-09-23 a short excerpt of its English planning rules plus a vague avatar request was submitted in a logged-out ChatGPT browser page. The sent message was visible, but the browser interaction timed out before a reply could be verified. This was not a full-prompt or two-stage trial; English behavior remains unverified.

## Circular crops and site checks

The assistant inspected Codex results in a browser at actual 40, 64, 128, and 256 CSS pixels on light and dark backgrounds. Hair and face were not accidentally cut by the circular mask; fine facial hair and curls are hard to distinguish at 40 px. This is an assistant visual check, not an independent human assessment. The [full preview](examples/developer/preview.html) uses relative references for repository examples; the ordinary tool mode embeds image bytes in a shareable offline HTML file. Sharing that HTML shares the image.

The prior homepage was checked at 1280 px desktop and 390 px mobile widths: six cases displayed in two and one columns respectively, 12 images loaded locally, and the page had no horizontal overflow. Keyboard expansion of the trial notes worked. The 390 px check used a browser viewport, not a physical phone. Print layout and opening the preview through `file://` were not visually verified. Site changes after that check require a new review.

## Boundaries and a reproducible test plan

No controlled comparison against a short prompt, repeated generation across real people, independent human quality review, or quantitative identity evaluation has been performed. We therefore do not claim the project produces better images than two ordinary prompts, or that it consistently preserves identity or style. Cases involving different people, entry points, or style-reference conditions cannot establish a model or product ranking.

For a behavioral check, use the public [fictional source photo](examples/developer/source.png) in an image-capable fresh conversation and record the exact message, entry point, date, output, and retries. Try a vague “make me an avatar” request (the assistant should ask its purpose), then a concrete GitHub/Hugging Face request (design without a parameter questionnaire), followed by a local edit (preserve the approved base). A side-profile-to-speaker request should weigh the purpose against the source angle and disclose that unseen facial details are inferred. A controlled quality comparison would require the same inputs, model conditions, and retry budget, with human review of equally sized outputs.

## Maintainer checks

```bash
python3 scripts/build_prompt.py --check
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
npm run check:docs
```

The [Chinese validation log](validation.html) contains the fuller case-by-case observations and [ChatGPT observation record](https://github.com/xiaofengShi/ai-avatar-skill/blob/main/tests/chatgpt-observations.json). Check results for this release should be added there and summarized here; do not infer live-site status from a successful local build.
