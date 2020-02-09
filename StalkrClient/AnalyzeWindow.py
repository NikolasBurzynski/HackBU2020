from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import WindowManager
import cv2
import StalkRAPIAccess as stalkR

class AnalyzeWindow:
    def __init__(self, wm):
        self.wm = wm
        self.window = QWidget()
        self.window.setWindowTitle("StalkR Analyze")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

        self.title_label = QLabel("StalkR Analyze")
        title_font = QFont('SansSerif', 16)
        title_font.setBold(True)
        self.title_label.setFont(title_font)

        self.submit_to_analyze = QPushButton("Select Image")
        self.submit_to_analyze.clicked.connect(self.send_analysis_image)

        self.grid.addWidget(self.title_label, 0, 0)

    def send_analysis_image(self):
        name = QFileDialog.getOpenFileName()[0]
        if name[-3:len(name)] == "jpg":
            data = stalkR.submit_picture(self.uid, self.pwd, True, cv2.imread(name))

