"""html unit test"""

from n6py.display import html

# pylint: disable=line-too-long
data = [
    {
        "content": "<h1>Hello World!</h1>",
        "load": None,
        "result": '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head><body><h1>Hello World!</h1></body></html>',
    },
    {
        "content": "<h1>Hello World!</h1>",
        "load": ["alpine", "tailwind", "bootstrap"],
        "result": '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><link href="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/css/bootstrap.min.css" rel="stylesheet"><script src="https://unpkg.com/alpinejs@latest/dist/cdn.min.js" defer></script><script src="https://cdn.tailwindcss.com" defer></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@latest/dist/js/bootstrap.bundle.min.js" defer></script></head><body><h1>Hello World!</h1></body></html>',
    },
]
# pylint: enable=line-too-long


def test_html():
    """
    Should return the defined result for each entry in list.
    """
    for entry in data:
        load = entry["load"]
        content = entry["content"]
        result = html(content, load, raw=True)
        print(result)
        assert result == entry["result"]
