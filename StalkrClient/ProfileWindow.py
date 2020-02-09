from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import StalkRAPIAccess as stalkR
import WindowManager


class ProfileWindow:
    def __init__(self, wm, uid, pwd):
        self.wm = wm
        self.uid = uid
        self.pwd = pwd
        self.info = stalkR.get_complete_info(uid, pwd)

        self.window = QWidget()
        self.window.setWindowTitle("StalkR Profile")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

        self.title_label = QLabel("StalkME: " + self.info[1] + " " + self.info[0])
        title_font = QFont('SansSerif', 16)
        title_font.setBold(True)
        self.title_label.setFont(title_font)

        self.rel_stat = QComboBox()
        self.rel_stat.addItems(["Single", "Taken", "Not Looking"])
        self.rel_stat.setCurrentIndex(stalkR.status_text_to_index(self.info[2]))

        self.grid.addWidget(self.title_label, 0, 0)

        self.grid.addWidget(QLabel("My Status"), 1, 0)
        self.grid.addWidget(self.rel_stat, 1, 1)

    def show(self):
        self.window.show()
