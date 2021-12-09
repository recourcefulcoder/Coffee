import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QIcon


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.can_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("icon.jfif"))
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM main_table").fetchall()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            elem = data[i]
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem[j])))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
