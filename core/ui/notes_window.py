from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, 
                             QPushButton, QStackedWidget, QHBoxLayout, 
                             QLineEdit, QButtonGroup, QRadioButton,
                             QTextEdit, QSpacerItem, QSizePolicy, QScrollArea)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)

from core.manager import Manager
from core.ui.dialogs import TimeLabel
# QWidget -> QStackedWidget -> QWidgets
# class_layout -> 

class NotesPage(QWidget): # QWidget -> QStackedWidget -> QWidgets
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.InitUi()
    
    def InitUi(self):
        self.InitMainPage()
        self.InitAddPage()
        self.InitPage()
    def InitPage(self):
        self.ContainerPage()
        self.NoteButtons()
        self.Layouting()
    def InitMainPage(self):
        self.MainPage()
        self.NoteLists()
        self.NotePages()
        self.MainPageLayout()
    def InitAddPage(self):
        self.AddPage()
        self.AddPageLayout()

    def ContainerPage(self):
        self.central_widget = QStackedWidget(self)
        self.central_widget.addWidget(self.main_page)
        self.central_widget.addWidget(self.add_page)
        self.central_widget.setCurrentWidget(self.main_page)
    def NoteButtons(self):
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addStretch()

        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.remove_button = QPushButton("Remove")

        self.add_button.setFixedSize(100, 30)
        self.edit_button.setFixedSize(100, 30)
        self.remove_button.setFixedSize(100, 30)
        
        self.setStyleSheet("QPushButton{"
                           "background-color: white;"
                           "}")

        self.add_button.clicked.connect(lambda _, page=self.add_page: self.SwitchPage(page))
        # self.remove_button.clicked.connect()
        # self.edit_button.clicked.connect()

        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.edit_button)
        self.buttons_layout.addWidget(self.remove_button)
    def Layouting(self):
        self.central_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout(self)
        layout.addWidget(self.central_widget)
        
        layout.addLayout(self.buttons_layout)
        self.setLayout(layout)


    def MainPage(self):
        self.main_page = QWidget(self)
    def NoteLists(self):
        # Scroll area & inner widget
        self.scroll_area = QScrollArea(self.main_page)
        self.scroll_area.setWidgetResizable(True)

        self.widget_list = QWidget(self.scroll_area)
        self.widget_list_layout = QVBoxLayout(self.widget_list)
        
        
        self.notes = self.manager.return_notes
        self.note_buttons = []

        if isinstance(self.notes, dict):
            for note in self.notes:
                note_button = QPushButton(
                    f"{self.notes[note]['Title']}\n{note}\n{self.notes[note]['Subject']}", self.widget_list)
                note_button.clicked.connect(lambda _, button=note_button: self.switch_content(button))
                note_button.setCheckable(True)
                self.widget_list_layout.addWidget(note_button)  # ✅ not self.notes_button
                self.note_buttons.append(note_button)
        else:
            self.notes_label = QLabel(self.notes)
            self.notes_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.notes_label.setStyleSheet("background-color: white; font-weight: bold;")
            self.notes_label.setFont(QFont("Arial", 10))
            self.widget_list_layout.addWidget(self.notes_label)

        self.widget_list.setLayout(self.widget_list_layout)
        self.scroll_area.setWidget(self.widget_list)
        
        
    def refreshNotes(self):
        self.notes = self.manager.return_notes

        if isinstance(self.notes, dict):
            for note in self.notes:
                print(note)
                note_button = QPushButton(f"{self.notes[note]['Title']}\n{note}\n{self.notes[note]['Subject']}", self.widget_list)
                note_button.clicked.connect(lambda _, button=note_button: self.SwitchContent(button))
                note_button.setCheckable(True)
                self.widget_list_layout.addWidget(note_button)
                self.note_buttons.append(note_button)
        else:
            self.notes_label = QLabel(self.notes, self.widget_list)
            self.notes_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.notes_label.setStyleSheet("background-color: white;"
                                     "font-weight: bold;")
            self.notes_label.setFont(QFont("Arial, 10"))
              
    def NotePages(self):
        self.notes_showing = QWidget(self.main_page)

        self.title_label = QLabel("Title : ", self)
        self.subject_label = QLabel("Subject : ", self)
        self.desc_label = QLabel("Description : ", self)
        self.notes_text = QLabel("Notes : ", self)

        self.setStyleSheet("QLabel{"
                           "background-color: white;"
                           "}") 
    def MainPageLayout(self):
        
        self.main_page_layout = QHBoxLayout(self.main_page)
        self.main_page_layout.addWidget(self.scroll_area)
        self.main_page_layout.addWidget(self.notes_showing)
        self.main_page_layout.setStretch(0, 1)
        self.main_page_layout.setStretch(1, 1)
        #-----------------------------------------------
        self.notes_showing_layout = QVBoxLayout(self)
        self.notes_showing_layout.addWidget(self.title_label)
        self.notes_showing_layout.addWidget(self.subject_label)
        self.notes_showing_layout.addWidget(self.desc_label)
        self.notes_showing_layout.addWidget(self.notes_text)
        self.notes_showing.setLayout(self.notes_showing_layout)

        self.notes_showing.setStyleSheet("background-color: white;")
        #------------------------------------------------
        self.scroll_area.setWidget(self.widget_list)
    def SwitchContent(self, button):
        notesID = button.text().split("\n")
        note = self.manager.see_note(notesID[1], notesID[2])
        if isinstance(note, dict):
            self.title_label.setText(f"Title : {note['Title']}")
            self.subject_label.setText(f"Subject : {note['Subject']}")
            self.desc_label.setText(f"Description : {note['Desc']}")
            self.notes_text.setText(f"Notes : {note['Notes']}")

    def AddPage(self):
        self.add_page = QWidget(self)
        self.add_page.setStyleSheet("background-color: white;")
        self.add_page_layout = QVBoxLayout(self.add_page)

        self.title_line_edit = QLineEdit(self)
        self.title_line_edit.setPlaceholderText("Enter the title")

        self.button_group = QButtonGroup(self)
        self.maths_checkbox = QRadioButton("Maths", self)
        self.button_group.addButton(self.maths_checkbox)
        self.science_checkbox = QRadioButton("Science", self)
        self.button_group.addButton(self.science_checkbox)
        self.languages_button = []
        for language in self.manager.return_languages:
            language_box = QRadioButton(language ,self)
            self.languages_button.append(language_box)
            self.button_group.addButton(language_box)

        self.other_widget = QWidget(self)
        self.other_widget_layout = QHBoxLayout(self.other_widget)
        self.other_widget_radio = QRadioButton("Other", self)
        self.other_widget_lineEdit = QLineEdit(self)
        self.other_widget_lineEdit.setPlaceholderText("Enter the subject")
        self.other_widget_layout.addWidget(self.other_widget_radio)
        self.other_widget_layout.addWidget(self.other_widget_lineEdit)
        self.button_group.addButton(self.other_widget_radio)

        self.desc_text_edit = QTextEdit(self)
        self.desc_text_edit.setPlaceholderText("Enter the brief description")

        self.note_text_edit = QTextEdit(self)
        self.note_text_edit.setPlaceholderText("Enter the notes")

        self.exit_button = QPushButton("<-", self)
        self.submit_button = QPushButton("Submit",self)
        self.exit_button.clicked.connect(lambda _, page=self.main_page: self.SwitchPage(page))
        self.exit_button.clicked.connect(self.refreshNotes)
        self.submit_button.clicked.connect(self.createNewNote)
        self.submit_button.clicked.connect(lambda _, page=self.add_page_layout: self.resetInputs(page))
        self.result_label = QLabel(self)
    def AddPageLayout(self):
        self.add_page_layout.addWidget(self.exit_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.add_page_layout.addWidget(self.title_line_edit)
        self.add_page_layout.addWidget(self.maths_checkbox)
        self.add_page_layout.addWidget(self.science_checkbox)
        for language in self.languages_button:
            self.add_page_layout.addWidget(language)
        self.add_page_layout.addWidget(self.other_widget, alignment=Qt.AlignmentFlag.AlignLeft)
        self.add_page_layout.addWidget(self.desc_text_edit)
        self.add_page_layout.addWidget(self.note_text_edit)
        self.add_page_layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.add_page_layout.addWidget(self.result_label)
    def isFormValid(self):
        title_value = self.title_line_edit.text()
        desc_value = self.desc_text_edit.toPlainText()
        note_value = self.note_text_edit.toPlainText()

        checked_button = self.button_group.checkedButton()
        
        
        if not checked_button:
            return False
        
        if checked_button.text() == "Other":
            other_value = self.other_widget_lineEdit.text()
            return all([title_value, desc_value, note_value, other_value])

        return all([title_value, desc_value, note_value])
    def createNewNote(self):
        if self.isFormValid():
            if self.button_group.checkedButton().text() == "Other":
                self.manager.add_note(self.title_line_edit.text(), self.desc_text_edit.toPlainText(), self.other_widget_lineEdit.text(), self.note_text_edit.toPlainText())
            else:
                self.manager.add_note(self.title_line_edit.text(), self.desc_text_edit.toPlainText(), self.button_group.checkedButton().text(), self.note_text_edit.toPlainText())
            self.result_label.setText("Succsesfully created notes !")
        else:
            self.result_label.setText("Please make sure to fill everything !")
    def resetInputs(self, layout):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QRadioButton):
                widget.setChecked(False)
            elif widget == self.other_widget:
                self.other_widget_lineEdit.clear()
                self.other_widget_radio.setChecked(False)

    def RemovePage(self):
        self.remove_widget = QWidget(self)
    
    def SwitchPage(self, page):
        self.central_widget.setCurrentWidget(page)
