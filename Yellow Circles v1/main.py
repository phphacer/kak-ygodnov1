import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor


class YellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)

        self.painter = QPainter()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.toggleButton.clicked.connect(self.resume_or_pause)

    def resume_or_pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.toggleButton.setText("Запустить процесс рисования")
        else:
            self.timer.start(1000)
            self.toggleButton.setText("Остановить процесс присования")

    def paintEvent(self, event):
        self.painter.begin(self)
        self.drawNewCircle()
        self.painter.end()

    def drawNewCircle(self):
        x, y = random.randint(0, self.width()), random.randint(0, self.height())
        r = random.randint(15, 150)
        self.painter.setBrush(QColor("yellow"))
        self.painter.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication([])
    window = YellowCircle()
    window.show()
    app.exec()
