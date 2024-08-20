# GENERATING CODE

```shell
pyside6-uic -g python mainwindow.ui -o mainwindow.py
```

```shell
pyside6-rcc -g python resources.qrc -o resources_rc.py
```

# GENERATE BINARY
```shell
pyinstaller --onefile gitstats.py --name gitstats
```
