[![](https://img.shields.io/pypi/v/serverpath.svg?style=flat-square)](https://pypi.org/project/serverpath)
[![](https://img.shields.io/pypi/pyversions/serverpath.svg?style=flat-square&logo=python)](https://pypi.org/project/serverpath)
[![](https://img.shields.io/pypi/l/serverpath.svg?style=flat-square)](https://pypi.org/project/serverpath)
[![](https://img.shields.io/pypi/wheel/serverpath.svg?style=flat-square)](https://pypi.org/project/serverpath)
[![](https://img.shields.io/github/last-commit/deluccial/serverpath.svg?style=flat-square)](https://github.com/deluccial/serverpath/commits)
[![](https://img.shields.io/github/languages/code-size/deluccial/serverpath.svg?style=flat-square)](https://github.com/deluccial/serverpath)

Platform-independent server-share path discovery.

To install:

`pip install serverpath`

Examples:
```
from serverpath import get_path

# from Windows machine without mapped network drive
get_path("server", "share")
>>> \\server\share

# from Windows machine with mapped network drive X
get_path("server", "share")
>>> X:\\

# from Windows machine where server is local machine and drive D is shared over network 
get_path("my-computer", "share")
>>> D:\\

# from Unix machine with Samba mount in /mnt without share
get_path("server")
>>> /mnt/server

# from Unix machine with Samba mount in /mnt with share
get_path("server", "share")
>>> /mnt/server/share

# from Unix machine with mount in custom path
get_path("server", "share", unix_path_prefix="/mymount")
>>> /mymount/server/share
```
