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
from core.ui.dialogs import TimeLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.initiation()

    def initiation(self):
        self.setup_window()
        self.init_pages()
        self.page_management()
        self.layouting()

    def setup_window(self):
        self.setWindowTitle("ProductivityPal")
        self.setGeometry(700, 300, 960, 540)
        self.setStyleSheet("background-color: black;")

    def init_pages(self):
        self.central_widget = QWidget()
        self.stacked_widget = QStackedWidget()
        self.time_label = TimeLabel()
        self.home_page = HomePage() 
        self.note_page = NotesPage()
        
        self.setCentralWidget(self.central_widget)

    def layouting(self):
        self.time_label.setFixedHeight(20)
        self.central_widget_layout = QVBoxLayout()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.note_page)
        self.stacked_widget.setCurrentWidget(self.home_page)

        self.central_widget_layout.addWidget(self.stacked_widget)
        self.central_widget_layout.addWidget(self.time_label)
        self.central_widget.setLayout(self.central_widget_layout)
    def page_management(self):
        self.home_page.switchPageSignal.connect(self.switchPage)
    
    def switchPage(self, page_name):
        if page_name == "Notes":
            self.stacked_widget.setCurrentWidget(self.note_page)

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
