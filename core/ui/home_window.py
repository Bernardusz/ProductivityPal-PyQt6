from PyQt6.QtWidgets import (QLabel, QWidget, QVBoxLayout, 
                             QGridLayout, QPushButton,)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDateTime, QTimer, pyqtSignal
import sys
from core.manager import Manager
from core.ui.dialogs import TimeLabel
class HomePage(QWidget):
    switchPageSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.initUI()

    def initUI(self):
        self.functions_button()
        self.task_bar()
        self.notes_bar()
        self.layouting()
   
    def functions_button(self):
        #Some button
        self.notesButton = QPushButton("Notes 📝", self)
        self.notesButton.setStyleSheet("background-color: white;")
        self.notesButton.setMinimumSize(300, 100)
        self.notesButton.clicked.connect(lambda: self.switchPageSignal.emit("Notes"))
        self.taskButton = QPushButton("To Do 📃", self)
        self.taskButton.setStyleSheet("background-color: white;")
        self.taskButton.setMinimumSize(300, 100)
        # self.taskButton.clicked.connect()
        self.pomodoroButton = QPushButton("Pomodoro ⌚", self)
        self.pomodoroButton.setStyleSheet("background-color: white;")
        self.pomodoroButton.setMinimumSize(300, 100)
        # self.pomodoroButton.clicked.connect()

    def task_bar(self):
        #Upcoming task
        self.taskWidget = QWidget(self)
        self.taskWidget.setStyleSheet("background-color: white;")
        Tasks = self.manager.see_task
        taskLayout = QVBoxLayout()
        if isinstance(Tasks, dict):
            for title in Tasks:
                self.taskButton = QPushButton(title, self)
                # self.button.clicked.connect(self.manager.see_task)
                taskLayout.addWidget(self.taskButton)
        else:
            taskLabel = QLabel(Tasks, self)
            taskLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            taskLabel.setStyleSheet("background-color: white;"
                                    "font-weight: bold;")
            taskLabel.setFont(QFont("Arial", 20))
            taskLayout.addWidget(taskLabel)
        self.taskWidget.setLayout(taskLayout)

    def notes_bar(self):
        self.notesWidget = QWidget(self)
        self.notesWidget.setStyleSheet("background-color: white;")
        notes = self.manager.return_notes
        notesLayout = QVBoxLayout()
        if isinstance(notes, dict):
            for title in notes:
                self.noteButton = QPushButton(title, self)
                # self.noteButton.clicked.connect()
                notesLayout.addWidget(self.taskButton)
        else:
            notesLabel = QLabel(notes, self)
            notesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            notesLabel.setStyleSheet("background-color: white;"
                                     "font-weight: bold;")
            notesLabel.setFont(QFont("Arial, 10"))
            notesLayout.addWidget(notesLabel)
        self.notesWidget.setLayout(notesLayout)


    def layouting(self):
        layout = QGridLayout()

        layout.addWidget(self.notesButton, 4, 0)
        layout.addWidget(self.taskButton, 4, 1)
        layout.addWidget(self.pomodoroButton, 4, 2)
        layout.addWidget(self.taskWidget, 1, 0, 2, 2)
        layout.addWidget(self.notesWidget, 1, 2, 1, 1)
        self.setLayout(layout)
