from PyQt5.QtWidgets import *
import LoginDialog
import CreateDialog
import ProfileWindow


class WindowManager:
    def __init__(self):
        self.login = None
        self.create_account = None
        self.my_profile = None
        self.analyze = None

    def make_login(self):
        self.login = LoginDialog.LoginDialog(self)
        self.login.show()

    def make_create_account(self):
        self.create_account = CreateDialog.CreateDialog(self)
        self.create_account.show()

    def make_my_profile(self, uid, pwd):
        self.my_profile = ProfileWindow.ProfileWindow(self, uid, pwd)
        self.my_profile.show()