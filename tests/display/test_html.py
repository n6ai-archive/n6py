"""html unit test"""

from pathlib import Path
from tempfile import TemporaryDirectory

from n6py.display import HTML, html

# pylint: disable=line-too-long
def template(content: str = ""):
    """Builds template for testing comparison"""
    return f'<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0,shrink-to-fit=no">{content}<style>html, body {{background: transparent !important; overflow: hidden; padding: 0; margin: 0;}}</style></head><body><h1>Hello World!</h1></body></html>'


data = [
    {
        "content": "<h1>Hello World!</h1>",
        "load": None,
        "result": template(),
    },
    {
        "content": "<h1>Hello World!</h1>",
        "load": "tailwind",
        "result": template('<script src="https://cdn.tailwindcss.com"></script>'),
    },
    {
        "content": "<h1>Hello World!</h1>",
        "load": ["bootstrap", "tailwind"],
        "result": template(
            '<link href="https://unpkg.com/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://unpkg.com/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script><script src="https://cdn.tailwindcss.com"></script>'
        ),
    },
]
# pylint: enable=line-too-long


def test_html_class_display():
    """
    Template should match the defined result.
    """
    content = data[0]["content"]
    doc = HTML(content)

    assert doc.template == data[0]["result"]


def test_html_class_save():
    """
    Should save a file to disk and the contents
    of that file should match the defined result.
    """
    content = data[0]["content"]
    doc = HTML(content)

    with TemporaryDirectory() as tmpdir:
        file = Path(tmpdir).joinpath("file.html")
        doc.save(file)

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            assert content == data[0]["result"]


def test_html():
    """
    Should return the defined result for each entry in list.
    """
    for entry in data:
        load = entry["load"]
        content = entry["content"]
        result = html(content, load, raw=True)

        assert result == entry["result"]
