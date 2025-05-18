from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt
import sys
from core.ui.main_window import MyWindow
app = QApplication(sys.argv)

Window = MyWindow()
Window.show()

if __name__ == "__main__":
    app.exec()
