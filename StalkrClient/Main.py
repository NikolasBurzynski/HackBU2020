from PyQt5.QtWidgets import *
import LoginDialog

app = QApplication([])

login = LoginDialog.LoginDialog()

login.show()

app.exec_()
