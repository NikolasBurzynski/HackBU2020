from PyQt5.QtWidgets import *
import StalkRAPIAccess as stalkR
import WindowManager


class ProfileWindow:
    def __init__(self, wm, uid, pwd):
        self.wm = wm
        self.uid = uid
        self.pwd = pwd

        self.window = QWidget()
        self.window.setWindowTitle("StalkR Profile")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

    def show(self):
        self.window.show()
