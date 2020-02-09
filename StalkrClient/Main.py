from PyQt5.QtWidgets import *
import WindowManager
import StalkRAPIAccess as StalkR

wm = WindowManager.WindowManager()

app = QApplication([])

wm.make_login()

app.exec_()

