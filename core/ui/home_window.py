from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, QPushButton,
                             QStackedWidget)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)
import sys
from core.manager import Manager



class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.initUI()

    def initUI(self):
        self.functions_button()
        self.task_bar()
        self.time_bar()
        self.notes_bar()
        self.layouting()
   
    def functions_button(self):
        #Some button
        self.notesButton = QPushButton("Notes 📝", self)
        self.notesButton.setStyleSheet("background-color: white;")
        self.notesButton.setMinimumSize(300, 100)
        # self.notesButton.clicked.connect()
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

    def time_bar(self):
        #time bar
        self.timeLabel = QLabel(self)
        self.timeLabel.setStyleSheet("background-color: #ffffff;"
                                     "font-weight: bold;")
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setMaximumHeight(30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000) 

        self.update_clock()

    def layouting(self):
        layout = QGridLayout()

        layout.addWidget(self.notesButton, 4, 0)
        layout.addWidget(self.taskButton, 4, 1)
        layout.addWidget(self.pomodoroButton, 4, 2)
        layout.addWidget(self.taskWidget, 1, 0, 2, 2)
        layout.addWidget(self.timeLabel, 5, 0, 1, 3)
        layout.addWidget(self.notesWidget, 1, 2, 1, 1)
        self.setLayout(layout)

    def update_clock(self):
        current_time_date = QDateTime.currentDateTime()
        self.timeLabel.setText(f"Time to study 📚                                          {current_time_date.toString('dd/MM/yy - HH:mm:ss')}                                          For a Brighter Future  ! 🌟")
