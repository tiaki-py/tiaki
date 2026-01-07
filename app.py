import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.label = QLabel("Click this window")
        self.label.setMouseTracking(True)
        self.setCentralWidget(self.label)
    
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("LEFTmousepressevent")
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText("MIDDLEmousepressevent")

        elif e.button() == Qt.RightButton:
            self.label.setText("RIGHTmousepressevent")


    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("LEFTmousereleaseevent")
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText("MIDDLEmousereleaseevent")

        elif e.button() == Qt.RightButton:
            self.label.setText("RIGHTmousereleaseevent")


    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("LEFTmouseDoubleclickeEvent")
        
        elif e.button() == Qt.MiddleButton:
            self.label.setText("MIDDLEmouseDoubleclickeEvent")

        elif e.button() == Qt.RightButton:
            self.label.setText("RIGHTmouseDoubleclickEvent")


app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()