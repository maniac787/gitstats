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

# MD 2 PDF

## Ubuntu

```shell
sudo apt-get install wkhtmltopdf
```

## MAC

```shell
brew install wkhtmltopdf
```

## Windows:

Descarga e instala wkhtmltopdf desde [wkhtmltopdf](www.wkhtmltopdf.org)