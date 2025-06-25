from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, QPushButton,
                             QStackedWidget)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)
import sys
from core.manager import Manager
from core.ui.home_window import HomePage
from core.ui.notes_window import NotesPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.initiation()

    def initiation(self):
        self.setup_window()
        self.init_pages()
        self.page_management()


    def setup_window(self):
        self.setWindowTitle("ProductivityPal")
        self.setGeometry(700, 300, 960, 540)
        self.setStyleSheet("background-color: black;")

    def init_pages(self):
        self.central_widget = QStackedWidget()
        self.home_page = HomePage() 
        self.note_page = NotesPage()
        
        self.central_widget.addWidget(self.home_page)
        self.central_widget.addWidget(self.note_page)
        self.central_widget.setCurrentWidget(self.home_page)
        self.setCentralWidget(self.central_widget)

    def page_management(self):
        self.home_page.switchPageSignal.connect(self.switchPage)
    
    def switchPage(self, page_name):
        if page_name == "Notes":
            self.central_widget.setCurrentWidget(self.note_page)

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
