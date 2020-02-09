from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import StalkRAPIAccess as stalkR
import sr_imutils
import cv2
import WindowManager


class ProfileWindow:
    def __init__(self, wm, uid, pwd):
        self.wm = wm
        self.uid = uid
        self.pwd = pwd
        self.info = stalkR.get_complete_info(uid, pwd)

        self.window = QWidget()
        self.window.setWindowTitle("StalkR Profile")
        self.window.setGeometry(10, 10, 300, 50)
        qr = self.window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.grid = QGridLayout()
        self.window.setLayout(self.grid)

        self.title_label = QLabel("StalkME: " + self.info[1] + " " + self.info[0])
        title_font = QFont('SansSerif', 16)
        title_font.setBold(True)
        self.title_label.setFont(title_font)

        self.rel_stat = QComboBox()
        self.rel_stat.addItems(["Single", "Taken", "Not Looking"])
        self.rel_stat.setCurrentIndex(stalkR.status_text_to_index(self.info[2]))
        self.rel_stat.currentIndexChanged.connect(self.rel_stat_changed)

        self.img_index = 1
        self.next_img = QPushButton("Next Image")
        self.next_img.clicked.connect(self.get_next_image)
        self.prev_img = QPushButton("Previous Image")
        self.prev_img.clicked.connect(self.get_prev_image)
        self.up_img = QPushButton("Upload")
        self.up_img.clicked.connect(self.upload_new)

        self.analyze = QPushButton("Analyze New Image")
        self.analyze.clicked.connect(self.open_analyze)

        self.image = QLabel()
        self.pixmap = None
        ir = stalkR.get_image(self.uid, self.pwd, self.uid, self.img_index)
        if ir[0]:
            self.set_image(ir[1])

        self.grid.addWidget(self.title_label, 0, 0)
        self.grid.addWidget(QLabel("(" + self.uid + ")"), 1, 0)

        self.grid.addWidget(QLabel("My Status"), 2, 0)
        self.grid.addWidget(self.rel_stat, 2, 1)
        self.grid.addWidget(self.analyze, 3, 0, 1, 2)

        self.grid.addWidget(self.prev_img, 0, 2)
        self.grid.addWidget(self.next_img, 0, 3)
        self.grid.addWidget(self.up_img, 0, 4)
        self.grid.addWidget(self.image, 1, 2, 2, 3)

    def set_image(self, img):
        resized = sr_imutils.scale_and_pad(img)
        cv2.imwrite("current.jpg", resized)
        self.image = QLabel()
        self.pixmap = QPixmap("current.jpg")
        self.image.setPixmap(self.pixmap)
        self.grid.addWidget(self.image, 1, 2, 2, 3)

    def show(self):
        self.window.show()

    def get_next_image(self):
        response = stalkR.get_image(self.uid, self.pwd, self.uid, self.img_index + 1)
        if response[0]:
            self.img_index += 1
            self.set_image(response[1])

    def get_prev_image(self):
        response = stalkR.get_image(self.uid, self.pwd, self.uid, self.img_index - 1)
        if response[0]:
            self.img_index -= 1
            self.set_image(response[1])

    def rel_stat_changed(self):
        stalkR.set_status(self.uid, self.pwd, self.rel_stat.currentText())

    def upload_new(self):
        name = QFileDialog.getOpenFileName()[0]
        if name[-3:len(name)] == "jpg":
            index = int(stalkR.submit_picture(self.uid, self.pwd, True, cv2.imread(name)))
            self.set_image(stalkR.get_image(self.uid, self.pwd, self.uid, index)[1])
            self.img_index = index

    def open_analyze(self):
        self.wm.make_analyze()