from PyQt5.QtWidgets import *
import WindowManager

wm = WindowManager.WindowManager()

app = QApplication([])

wm.make_login()

app.exec_()
