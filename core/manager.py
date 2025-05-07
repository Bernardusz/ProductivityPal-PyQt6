from features.notes_feature import NotesFeature, Notes, MathNotes, ScienceNotes, LanguagesNotes
from features.pomodoro_feature import PomodoroFeature, Pomodoro
from features.todo_feature import ToDoFeature, ToDo

class Manager:
    def __init__(self):
        self.note_feature = NotesFeature
        self.pomodoro_feature = PomodoroFeature()
        self.todo_feature =  ToDoFeature()

    #Notes methods
    def add_note(self, title, desc, subject, note):
        pass

    def edit_note(self, title, subject):
        pass

    def remove_note(self, title, subject):
        pass

    def see_note(self, title, subject):
        pass

    def add_formula(self, title, subject, formula_name, formula):
        pass

    def add_vocab(self, title, subject, word, meaning):
        pass
    
    def see_vocab_formula(self, title, subject):
        pass

    def export_txt(self, file, title, subject):
        pass

    #Tasks methods
    def add_task(self, title, desc, priority, deadline, notes):
        self.todo_feature.add_todo(title, desc, priority, deadline, notes)

    @property
    def see_task(self):
        task = self.todo_feature.see_task
        if task:
            return task
        else:
            return False    
        
    def see_task_by(self, by, type):
        self.see_task_by(by, type)

    def mark_done(self, title):
        pass

    #json methods
    def save_json(self, file):
        pass

    def load_json(self, file):
        pass

    #pomodoro methods

    def pomodoro(self, title, subject, method):
        pass

    
