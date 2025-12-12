from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")


        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(3840,1980))

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()