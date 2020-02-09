from PyQt5.QtWidgets import *
import StalkRAPIAccess as stalkR
import WindowManager


class CreateDialog:
    def __init__(self, wm):

        self.wm = wm

        self.window = QWidget()
        self.window.setWindowTitle("Become the StalkR")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

        self.msg = QLabel("")
        self.msg_define = False

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()

        self.pwd_entry = QLineEdit()
        self.pwd_entry.setEchoMode(QLineEdit.Password)
        self.pwd_confirm = QLineEdit()
        self.pwd_confirm.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton("Create Account")
        self.submit.clicked.connect(self.submit_pressed)

        self.back = QPushButton("Cancel")
        self.back.clicked.connect(self.back_pressed)

        self.agree = QCheckBox("I'm over 18 and agree to have my data collected")

        self.grid.addWidget(QLabel("First Name"), 0, 0)
        self.grid.addWidget(self.first_name, 0, 1)

        self.grid.addWidget(QLabel("Last Name"), 1, 0)
        self.grid.addWidget(self.last_name, 1, 1)

        self.grid.addWidget(QLabel("Password"), 2, 0)
        self.grid.addWidget(self.pwd_entry, 2, 1)

        self.grid.addWidget(QLabel("Confirm"), 3, 0)
        self.grid.addWidget(self.pwd_confirm, 3, 1)

        self.grid.addWidget(self.agree, 4, 0, 1, 2)

        self.grid.addWidget(self.submit, 5, 1)
        self.grid.addWidget(self.back, 5, 0)

    def show(self):
        self.window.show()

    def set_msg(self, text):
        self.msg.setText(text)
        if not self.msg_define:
            self.msg_define = True
            self.grid.addWidget(self.msg, 6, 0, 1, 2)

    def submit_pressed(self):
        self.set_msg("Working...")
        if self.agree.isChecked():
            if len(self.first_name.text()) != 0:
                if len(self.last_name.text()) != 0:
                    if len(self.pwd_entry.text()) != 0:
                        if self.pwd_entry.text() == self.pwd_confirm.text():
                            create_status = stalkR.create_account(self.pwd_entry.text(), self.first_name.text(), self.last_name.text())
                            if create_status[0]:
                                self.wm.make_my_profile(create_status[1], self.pwd_entry.text())
                                self.window.close()
                            else:
                                self.set_msg("Account rejected")
                        else:
                            self.set_msg("Passwords do not match")
                    else:
                        self.set_msg("Password is required")
                else:
                    self.set_msg("Last name is required")
            else:
                self.set_msg("First name is required")
        else:
            self.set_msg("You MUST meet our conditions to register")

    def back_pressed(self):
        self.wm.make_login()
        self.window.close()
