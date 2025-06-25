from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, 
                             QPushButton, QStackedWidget, QHBoxLayout, 
                             QLineEdit, QButtonGroup, QRadioButton,
                             QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)

from core.manager import Manager

# QWidget -> QStackedWidget -> QWidgets
# class_layout -> 

class NotesPage(QWidget): # QWidget -> QStackedWidget -> QWidgets
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.init_ui()
    
    def init_ui(self):
        self.notes_list()
        self.notes_page()
        self.layouting()
    
    def notes_list(self):
        self.widget_list = QWidget(self)
        self.widget_list.setStyleSheet("background-color: white;")
        self.widget_list_layout = QVBoxLayout(self)
        self.notes = self.manager.return_notes
        self.note_buttons = []
        
        if isinstance(self.notes, dict):
            for note in self.notes:
                note_button = QPushButton(note, self)
                note_button.clicked.connect()
                note_button.setCheckable(True)
                self.widget_list_layout.addWidget(self.notes_button)
                self.note_buttons.append(note_button)
        else:
            self.notes_label = QLabel(self.notes, self)
            self.notes_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.notes_label.setStyleSheet("background-color: white;"
                                     "font-weight: bold;")
            self.notes_label.setFont(QFont("Arial, 10"))
            self.widget_list_layout.addWidget(self.notes_label)
        self.widget_list.setLayout(self.widget_list_layout)
    
    def notes_page(self):
        self.notes_showing = QWidget(self)
        self.notes_showing.setStyleSheet("background-color: white;")
        self.notes_showing_layout = QGridLayout(self)

        self.title_label = QLabel("Title : ", self)
        self.notes_showing_layout.addWidget(self.title_label)

        self.subject_label = QLabel("Subject : ", self)
        self.notes_showing_layout.addWidget(self.subject_label)

        self.desc_label = QLabel("Description : ", self)
        self.notes_showing_layout.addWidget(self.desc_label)

        self.notes_text = QLabel("Notes : ", self)
        self.notes_showing_layout.addWidget(self.notes_text)

        self.setStyleSheet("QLabel{"
                           "background-color: white;"
                           "}")
        self.notes_showing.setLayout(self.notes_showing_layout)


        
    def layouting(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.widget_list)
        layout.addWidget(self.notes_showing)

        self.setLayout(layout)
