"""display_html unit test"""

from n6py.display import display_html

# pylint: disable=line-too-long
data = [
    {
        "content": "<h1>Hello World!</h1>",
        "preset": None,
        "result": '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head><body><h1>Hello World!</h1></body></html>',
    },
    {
        "content": "<h1>Hello World!</h1>",
        "preset": "alpine-tailwind",
        "result": '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><script src="https://unpkg.com/alpinejs@latest/dist/cdn.min.js" defer crossorigin></script><script src="https://cdn.tailwindcss.com" defer crossorigin></script></head><body><h1>Hello World!</h1></body></html>',
    },
    {
        "content": "<h1>Hello World!</h1>",
        "preset": "bootstrap",
        "result": '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js" defer crossorigin></script></head><body><h1>Hello World!</h1></body></html>',
    },
]
# pylint: enable=line-too-long


def test_display_html():
    """
    Should return the defined result for each entry in list.
    """
    for entry in data:
        preset = entry["preset"]
        content = entry["content"]
        result = display_html(content, preset, raw=True)

        assert result == entry["result"]
