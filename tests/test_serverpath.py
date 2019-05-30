import pytest
import platform
from pathlib import Path
from serverpath import get_path

if platform.system() == 'Windows':

    def test_windows():
        with pytest.warns(UserWarning):
            assert get_path(server_name="computer-name", share_name="share") == Path(r"\\computer-name\share")

else:

    def test_unix():
        with pytest.warns(UserWarning):
            assert get_path(server_name="computer-name", share_name="share") == Path("/mnt/computer-name/share")

