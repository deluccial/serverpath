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
get_path("my-computer")
>>> /mnt/server

# from Unix machine with Samba mount in /mnt with share
get_path("my-computer", "share")
>>> /mnt/server/share

# from Unix machine with mount in custom path
get_path("my-computer", "share", unix_path_prefix="/mymount")
>>> /mymount/server/share
```