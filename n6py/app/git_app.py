"""app module"""

from typing import Union, Iterable
import os
import subprocess
from pathlib import Path
from urllib.parse import urlparse


class GitApp:
    """
    A class that provides a unified API for wrapping and enhancing
    git repositories with commands for easy usage on Linux systems.
    """

    def __init__(
        self,
        url: Union[None, str],
        app_script: Union[None, str, Path],
        input_dir: Union[None, str, Path] = None,
        output_dir: Union[None, str, Path] = None,
    ):
        """
        Parameters
        ----------
        url: HTTPS GitHub repo URL.
        app_script: The entry python script, relative to the repo root, that starts the app.
        input_dir: Optional path to the input directory that the app will operate on.
        output_dir: Optional path to the output directory where the results will be stored.

        Examples
        --------
        >>> class MyApp(GitApp):
        ...   def __init__(self):
        ...     self.url = 'https://github.com/<USER>/<REPO>'
        ...     self.app_script = 'app.py'
        >>> app = MyApp()
        >>> app.install()
        'App installed 📦'
        """
        self.url = url
        self.app_script = app_script
        self.input_dir = input_dir
        self.output_dir = output_dir

    @property
    def name(self):
        """The app name derived from the URL."""
        return os.path.basename(urlparse(self.url).path).split(".")[0]

    @property
    def dir(self):
        """App installation directory."""
        return str(Path("/usr/local", self.name))

    @property
    def app_script_path(self):
        """Absolute path to the app start script."""
        return str(Path(self.dir, self.app_script))

    def msg(
        self,
        code: int,
        success_codes: Union[int, Iterable] = 0,
        success_msg: str = "Success ✨",
        error_msg: str = "Something went wrong ❌",
    ):
        """
        Creates an success or error message.

        Parameters
        ----------
        code: The bash returncode.
        success_codes: Returncodes that should be considered successful.
        success_msg: A string that will be returned on success.
        error_msg: A string that will be returned on error.

        Examples
        --------
        >>> app = GitApp('https://github.com/<USER>/<REPO>', 'app.py')
        >>> app.msg(code=0)
        'Success ✨'
        """
        if (isinstance(success_codes, int) and code == success_codes) or (
            isinstance(success_codes, Iterable) and code in success_codes
        ):
            return success_msg

        return f"{error_msg} Code: {code}"

    def install(self):
        """
        Installs the app.

        Returns
        -------
        A message about success or failure of the process.
        """
        cmd = f"""
            git clone {self.url} {self.dir}; \
            cd {self.dir}; \
            pip install -r requirements.txt
        """

        result = subprocess.run(cmd, shell=True, check=True)
        return self.msg(result.returncode, success_msg="App installed 📦")

    def uninstall(self):
        """
        Uninstalls the app.

        Returns
        -------
        A message about success or failure of the process.
        """
        cmd = f"rm -rf {self.dir}"
        result = subprocess.run(cmd, shell=True, check=True)
        return self.msg(result.returncode, success_msg="App uninstalled ♻️")

    def run(self, flags: str = ""):
        """
        Runs the app.

        Parameters
        ----------
        flags: optional flags that should be passed to the app script.

        Returns
        -------
        A message about success or failure of the process.
        """
        cmd = f"python {self.app_script_path} {flags}"
        result = subprocess.run(cmd, shell=True, check=True)
        return self.msg(result.returncode)
