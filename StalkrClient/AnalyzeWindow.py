from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import WindowManager
import sr_imutils
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

        self.image = QLabel()
        self.pixmap = None

        self.grid.addWidget(self.title_label, 0, 0)
        self.grid.addWidget(self.submit_to_analyze, 0, 1)


    def set_image(self, img):
        resized = sr_imutils.scale_and_pad(img)
        cv2.imwrite("current.jpg", resized)
        self.image = QLabel()
        self.pixmap = QPixmap("current.jpg")
        self.image.setPixmap(self.pixmap)
        self.grid.addWidget(self.image, 1, 0, 1, 2)


    def send_analysis_image(self):
        name = QFileDialog.getOpenFileName()[0]
        if name[-3:len(name)] == "jpg":
            img = cv2.imread(name)
            self.set_image(img)
            data = stalkR.submit_picture(self.uid, self.pwd, True, img)

