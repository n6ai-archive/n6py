"""GitApp unit test"""

from pathlib import Path
from n6py.app import GitApp

URL = "https://github.com/<USER>/<REPO>"
APP_SCRIPT = "app.py"
INPUT_DIR = "/content/input"
OUTPUT_DIR = "/content/output"


def test_git_app():
    """
    Should return variables.
    """
    app = GitApp(URL, APP_SCRIPT, INPUT_DIR, OUTPUT_DIR)

    assert app.url == URL
    assert app.app_script == APP_SCRIPT
    assert app.input_dir == INPUT_DIR
    assert app.output_dir == OUTPUT_DIR

    assert app.name == "<REPO>"
    assert app.dir == str(Path("/usr/local/<REPO>"))
    assert app.app_script_path == str(Path("/usr/local/<REPO>/app.py"))


def test_git_app_msg():
    """
    Should return messages.
    """
    app = GitApp(URL, APP_SCRIPT, INPUT_DIR, OUTPUT_DIR)

    assert app.msg(0) == "Success ✨"
    assert app.msg(1) == "Something went wrong ❌ Code: 1"

    assert app.msg(0, success_msg="Success") == "Success"
    assert app.msg(1, error_msg="Error") == "Error Code: 1"

    assert app.msg(2, [0, 2]) == "Success ✨"
