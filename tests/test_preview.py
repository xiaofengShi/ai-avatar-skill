import base64
import importlib.util
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/editorial-avatar/scripts/preview_avatar.py"
spec = importlib.util.spec_from_file_location("preview", SCRIPT)
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)
PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII=")


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img":
            self.images.append(attrs)
        if tag == "script":
            self.scripts += 1


class PreviewTests(unittest.TestCase):
    def test_embeds_original_bytes_and_escapes_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / '<script>alert(1)<script>.png'
            source.write_bytes(PNG)
            page = preview.render(source)
            tags = Tags()
            tags.feed(page)
            self.assertEqual(tags.scripts, 0)
            self.assertEqual(len(tags.images), 9)
            for img in tags.images:
                self.assertEqual(base64.b64decode(img["src"].split(",")[1]), PNG)
            self.assertEqual(sorted(int(i["width"]) for i in tags.images if "width" in i), [40,40,64,64,128,128,256,256])
            self.assertEqual(source.read_bytes(), PNG)

    def test_output_protection_and_invalid_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / '人物.png'
            output = Path(directory) / 'preview.html'
            source.write_bytes(PNG)
            command = [sys.executable, str(SCRIPT), str(source), "--output", str(output)]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            old = output.read_bytes()
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            self.assertEqual(output.read_bytes(), old)

            self.assertEqual(subprocess.run(command + ["--force"], capture_output=True).returncode, 0)
            overwrite_source = [sys.executable, str(SCRIPT), str(source), "--output", str(source), "--force"]
            self.assertNotEqual(subprocess.run(overwrite_source, capture_output=True).returncode, 0)
            self.assertEqual(source.read_bytes(), PNG)
            source.write_text('<svg onload="alert(1)"/>')
            self.assertNotEqual(subprocess.run(command + ["--force"], capture_output=True).returncode, 0)
            self.assertEqual(output.read_bytes(), old)

    def test_linked_preview_uses_portable_escaped_path(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            source = folder / '人物 #1.png'
            source.write_bytes(PNG)
            output = folder / 'pages' / 'preview.html'
            tags = Tags()
            tags.feed(preview.render(source, output))
            for image in tags.images:
                self.assertEqual((output.parent / unquote(image['src'])).resolve(), source.resolve())
                self.assertNotIn('#', image['src'])


if __name__ == "__main__":
    unittest.main()
