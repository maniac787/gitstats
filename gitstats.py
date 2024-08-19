#!/usr/bin/env python3
import argparse
import logging
import sys
import time
from typing import List

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from core import gitlog, gitblame, gitls
from core.model.blame import Blame
from core.model.numstat import Numstat
from printer.printer import Printer
from qt.interfaces.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.mostrar_mensaje)
        self.actionSalir.triggered.connect(self.close)

    def mostrar_mensaje(self):
        text = self.lineEdit.text()
        git_report(text)
        QMessageBox.information(self, 'Mensaje', "Reporte generado")


def git_report(git_repo_path):
    start_time = time.process_time()
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="gitstats - a statistical analysis tool for git repositories")
    parser.add_argument("--format", choices=("markdown", "confluencewiki"), required=True,
                        help="print the results in markdown or in confluence wiki format")
    parser.add_argument("--load", action="store_true", help="try loading previous data")
    parser.add_argument("--version", action="version", version="%(prog)s 0.2")
    args = parser.parse_args()
    repo_path = git_repo_path  # 'D:\\Projects\\BAC\\AZURE\\bancadigital-lib-integration-data-power'

    if args.format == "confluencewiki":
        printer = Printer("confluencewiki", repo_path)

    elif args.format == "markdown":
        printer = Printer("markdown", repo_path)

    else:
        parser.exit(1, args.format + "is not supported")
        raise Exception(args.format + "is not supported")

    gitlog.git_log_numstat_merges(args.load, repo_path)
    numstat: List[Numstat] = gitlog.git_log_numstat_no_merges(args.load, repo_path)
    files = gitls.git_ls_files(repo_path)
    blame: List[Blame] = gitblame.git_blame(repo_path, files, args.load)

    printer.print(numstat, blame)
    logging.info("--- %s seconds ---" % (time.process_time() - start_time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
