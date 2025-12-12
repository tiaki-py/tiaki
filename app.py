from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.on_button_click)
        button.clicked.connect(self.on_button_toggle)

        self.setMinimumSize(QSize(100,100))
        self.setMaximumSize(QSize(3840,1980))

        self.setCentralWidget(button)
    
    def on_button_click(self):
        print("Quelle jour es tu?")
    
    def on_button_toggle(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()