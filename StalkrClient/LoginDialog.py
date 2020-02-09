from PyQt5.QtWidgets import *
import StalkRAPIAccess as stalkR
import WindowManager


class LoginDialog:
    def __init__(self, wm):

        self.wm = wm

        self.window = QWidget()
        self.window.setWindowTitle("StalkR Login")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

        self.msg = QLabel("")
        self.msg_define = False

        self.uid_edit = QLineEdit()

        self.pwd_edit = QLineEdit()
        self.pwd_edit.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton("Login")
        self.submit.clicked.connect(self.login_pressed)

        self.create = QPushButton("Create")
        self.create.clicked.connect(self.create_pressed)

        self.grid.addWidget(QLabel("User ID"), 0, 0)
        self.grid.addWidget(self.uid_edit, 0, 1)

        self.grid.addWidget(QLabel("Password"), 1, 0)
        self.grid.addWidget(self.pwd_edit, 1, 1)

        self.grid.addWidget(self.submit, 2, 1)
        self.grid.addWidget(self.create, 2, 0)

    def show(self):
        self.window.show()

    def set_msg(self, text):
        self.msg.setText(text)
        if not self.msg_define:
            self.msg_define = True
            self.grid.addWidget(self.msg, 3, 0, 1, 2)

    def login_pressed(self):
        self.set_msg("Working...")

        if not stalkR.authenticate(self.uid_edit.text(), self.pwd_edit.text()):
            self.set_msg("Incorrect UID or password")
        else:
            self.set_msg("Opening...")
            self.window.close()

    def create_pressed(self):
        self.wm.make_create_account()
        self.window.close()
