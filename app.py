from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_button_click)

        self.setCentralWidget(self.button)

    def on_button_click(self):
        self.button.setText("Already clicked.")
        self.button.setEnabled(False)
        self.setWindowTitle("My Single-use App")


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()