from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, QPushButton,
                             QStackedWidget)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)
import sys
from core.manager import Manager
from core.ui.home_window import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.initiation()

    def initiation(self):
        self.page_management()
        self.init_pages()
        self.setup_window()
    def setup_window(self):
        self.setWindowTitle("ProductivityPal")
        self.setGeometry(700, 300, 960, 540)
        self.setStyleSheet("background-color: black;")

    def page_management(self):
        self.central_widget = QStackedWidget()
        

    def init_pages(self):
        self.home_page = HomePage()

        self.central_widget.addWidget(self.home_page)
        self.central_widget.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.central_widget)
        
        
def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
