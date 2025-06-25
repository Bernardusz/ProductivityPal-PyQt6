from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, 
                             QPushButton, QStackedWidget, QHBoxLayout, 
                             QLineEdit, QButtonGroup, QRadioButton,
                             QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)

class TimeLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.timeBar()
    
    def timeBar(self):
        #time bar
        self.setStyleSheet("background-color: #ffffff;"
                                     "font-weight: bold;")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumHeight(30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000) 

        self.update_clock()
    
    def update_clock(self):
        current_time_date = QDateTime.currentDateTime()
        self.setText(f"Time to study 📚                                          {current_time_date.toString('dd/MM/yy - HH:mm:ss')}                                          For a Brighter Future  ! 🌟")

