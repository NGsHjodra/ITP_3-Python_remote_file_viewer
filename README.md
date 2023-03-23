# ITP_3-Python_remote_file_viewer
Simple remote file viewer with asyncio. \
The client connects to the server and allows users to enter commands and see the results of their execution.

## Main functions

### cd  – for changing the current directory. By default, the current directory is the start directory of the server. Example command: 
```
> cd C:\test
OK
```
### list – list all files in the current directory. Example:
```
> list
server.py
test.txt
readme.doc
```
### get [filename]. Reads the file and sends it’s content to the client. Example:
``` 
> get text.txt
Here we have some not so long text…
```
