from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import WindowManager

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


        self.grid.addWidget(self.title_label, 0, 0)
