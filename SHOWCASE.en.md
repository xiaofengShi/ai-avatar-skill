# One photo, a portrait for its purpose.

Editorial Avatar / Case gallery

The same photo can serve different purposes. These cases show how the intended use changes composition, wardrobe, and color, and how a targeted edit changes a result.

## Case comparisons

**Six cases, organized by purpose.** The travel illustration uses a real photo whose owner approved public display of this case and liked the result. The other five cases cover two AI-generated fictional people. Codex's built-in image tool produced every final image. Source and result are shown at equal size; open either image to inspect it at full resolution.

| Purpose and request | Source photo / edit base | Generated result | Design, observations, and record |
| --- | --- | --- | --- |
| **Travel illustration**<br>Casual photo → environmental portrait<br>Keep the side profile, glasses, and travel feel | [<img src="examples/travel/source.png" alt="Real travel source photo" width="220">](examples/travel/source.png) | [<img src="examples/travel/illustration.png" alt="Travel illustration approved by the photo owner" width="220">](examples/travel/illustration.png) | **Approved by the user for display.** The person is brought closer; signs, greenery, and soft daylight establish the setting. The street scene was reconstructed, not reproduced faithfully.<br>[Request](examples/travel/request.txt) · [Actual prompt](examples/travel/generation.prompt.txt) |
| **GitHub / Hugging Face**<br>Natural and approachable<br>Keep glasses | [<img src="examples/developer/source.png" alt="Fictional man's source photo" width="220">](examples/developer/source.png) | [<img src="examples/developer/avatar.png" alt="Semi-realistic community avatar" width="220">](examples/developer/avatar.png) | Navy casual clothing and a pale blue-grey background preserve the grey short hair and age cues. Skin texture is still rather fine.<br>[Request](examples/developer/request.txt) · [Actual prompt](examples/developer/generation.prompt.txt) · [Circular crop](examples/developer/preview.html) |
| **Conference speaker**<br>Keep age, skin tone,<br>and short curls | [<img src="examples/speaker/source.png" alt="Fictional woman's source photo" width="220">](examples/speaker/source.png) | [<img src="examples/speaker/avatar.png" alt="Speaker portrait with a plum jacket" width="220">](examples/speaker/avatar.png) | A plum jacket and grey-violet background create a calm, warm portrait. Facial features were redrawn slightly.<br>[Request](examples/speaker/request.txt) · [Actual prompt](examples/speaker/generation.prompt.txt) · [Circular crop](examples/speaker/preview.html) |
| **Remove glasses only**<br>Keep composition, expression,<br>clothing, background, and style | [<img src="examples/developer/avatar.png" alt="Edit base wearing glasses" width="220">](examples/developer/avatar.png) | [<img src="examples/remove-glasses/avatar.png" alt="Community avatar without glasses" width="220">](examples/remove-glasses/avatar.png) | Frame, nose pads, and temples are gone; the overall design remains close to the base. The eye area was reconstructed, not recovered from behind the glasses.<br>[Request](examples/remove-glasses/request.txt) · [Actual prompt](examples/remove-glasses/generation.prompt.txt) · [Circular crop](examples/remove-glasses/preview.html) |
| **Research team homepage**<br>Same person, new context<br>Keep glasses and age cues | [<img src="examples/developer/source.png" alt="Fictional source photo for a team avatar" width="220">](examples/developer/source.png) | [<img src="examples/researcher/avatar.png" alt="Deep-green research team avatar" width="220">](examples/researcher/avatar.png) | Deep-green clothing, a blue-green background, and soft side light. At 40 px the shoulders have weak contrast, though the face remains recognizable; this does not show it is better than the community version.<br>[Request](examples/researcher/request.txt) · [Actual prompt](examples/researcher/generation.prompt.txt) · [Circular crop](examples/researcher/preview.html) |
| **Smile and pose correction**<br>Coordinate head, neck, shoulders<br>Keep the smile, outfit, and palette | [<img src="examples/speaker/avatar.png" alt="Speaker portrait before expression edit" width="220">](examples/speaker/avatar.png) | [<img src="examples/speaker-smile/avatar-v2.png" alt="Revised head, neck, and shoulders; awaiting user review" width="220">](examples/speaker-smile/avatar-v2.png) | The user said the first version's head and body pointed in conflicting directions. One revision reduced the tilt and adjusted the shoulder line and neckline. **The revision has not been approved by the user.**<br>[Problematic first result](examples/speaker-smile/avatar.png) · [Feedback](examples/speaker-smile/feedback.txt) · [Correction prompt](examples/speaker-smile/correction.prompt.txt) · [Circular crop](examples/speaker-smile/preview-v2.html) |

Examples made from 2026-09-21 to 2026-09-22. Each of the five fictional-character cases had one initial generation. The smile case then received one correction after user feedback. The first travel call failed to read a JPEG and produced no image; after conversion to PNG, the same brief produced one result. The travel case also used a style image from an earlier conversation. Permission to redistribute that image was not granted, so it is not in this repository and is not a bundled public style reference.

These are cases where the assistant followed the skill workflow to write a creative brief and execute an edit or generation. There has been no independent human review or controlled repeat test. One user's approval of one image does not establish stable results. See the [validation record](validation.en.html) for inputs, observations, and limits, and the [asset notes](https://github.com/xiaofengShi/ai-avatar-skill/blob/main/ASSETS.md) for provenance.

## Small sizes matter

These circular crops render directly from the high-resolution fictional-character result, rather than enlarging a low-resolution screenshot.

<div class="crop-demo" aria-label="Circular avatar crops on light and dark backgrounds">
  <div class="crop-panel light"><strong>Light interface</strong><div class="crop-sizes">
    <figure><img src="examples/developer/avatar.png" width="40" height="40" alt="40-pixel circular crop"><figcaption>40 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="64" height="64" alt="64-pixel circular crop"><figcaption>64 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="128" height="128" alt="128-pixel circular crop"><figcaption>128 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="256" height="256" alt="256-pixel circular crop"><figcaption>256 px</figcaption></figure>
  </div></div>
  <div class="crop-panel dark"><strong>Dark interface</strong><div class="crop-sizes">
    <figure><img src="examples/developer/avatar.png" width="40" height="40" alt="40-pixel circular crop"><figcaption>40 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="64" height="64" alt="64-pixel circular crop"><figcaption>64 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="128" height="128" alt="128-pixel circular crop"><figcaption>128 px</figcaption></figure>
    <figure><img src="examples/developer/avatar.png" width="256" height="256" alt="256-pixel circular crop"><figcaption>256 px</figcaption></figure>
  </div></div>
</div>

For true CSS dimensions, [open the full preview](examples/developer/preview.html) at 100% browser zoom.

## Get started

[Activate the Codex skill](https://github.com/xiaofengShi/ai-avatar-skill#codex) · [Use the ChatGPT prompt](https://github.com/xiaofengShi/ai-avatar-skill#chatgpt)

Give the assistant your photo and its purpose. Installation, capabilities, requirements, and contribution guidance are in the [usage guide](https://github.com/xiaofengShi/ai-avatar-skill/blob/main/README.md).
