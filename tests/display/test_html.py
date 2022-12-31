"""html unit test"""

from n6py.display import HTML, html

# pylint: disable=line-too-long
data = [
    {
        "content": "<h1>Hello World!</h1>",
        "load": None,
        "result": '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0,shrink-to-fit=no"><style>html, body {background: transparent; overflow: hidden; padding: 0; margin: 0;}</style></head><body><h1>Hello World!</h1></body></html>',
    },
    {
        "content": "<h1>Hello World!</h1>",
        "load": "tailwind",
        "result": '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0,shrink-to-fit=no"><script src="https://cdn.tailwindcss.com"></script><style>html, body {background: transparent; overflow: hidden; padding: 0; margin: 0;}</style></head><body><h1>Hello World!</h1></body></html>',
    },
    {
        "content": "<h1>Hello World!</h1>",
        "load": ["alpine", "tailwind", "bootstrap"],
        "result": '<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0,shrink-to-fit=no"><link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://unpkg.com/alpinejs@latest/dist/cdn.min.js"></script><script src="https://cdn.tailwindcss.com"></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js"></script><style>html, body {background: transparent; overflow: hidden; padding: 0; margin: 0;}</style></head><body><h1>Hello World!</h1></body></html>',
    },
]
# pylint: enable=line-too-long


def test_html_class():
    """
    Template should match the defined result.
    """
    content = data[0]["content"]
    doc = HTML(content)

    assert doc.template == data[0]["result"]


def test_html():
    """
    Should return the defined result for each entry in list.
    """
    for entry in data:
        load = entry["load"]
        content = entry["content"]
        result = html(content, load, raw=True)

        assert result == entry["result"]
