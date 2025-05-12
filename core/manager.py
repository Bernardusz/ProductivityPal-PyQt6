from features.notes_feature import NotesFeature, Notes, MathNotes, ScienceNotes, LanguagesNotes
from features.pomodoro_feature import PomodoroFeature, PomodoroLog
from features.todo_feature import ToDoFeature, ToDo

class Manager:
    def __init__(self):
        self.note_feature = NotesFeature()
        self.pomodoro_feature = PomodoroFeature()
        self.todo_feature =  ToDoFeature()

    #Notes methods
    def add_note(self, title, desc, subject, note):
        done = self.note_feature.add_note(title, desc, subject, note)
        if done:
            return f"Successfully added note !"
        else:
            return f"Unsuccessful to add note !"

    def edit_note(self, id, subject, edit, change):
        done = self.note_feature.edit_notes(id, subject, edit, change)
        if done:
            return f"Successfully edited note !"
        else:
            return f"Unsuccessful to edit note !"
    def remove_note(self, id, subject):
        done = self.note_feature.remove_notes(id, subject)
        if done:
            return f"Successfully removed note !"
        else:
            return f"Unsuccessful to remove note !"
    def see_note(self, id, subject):
        exist = self.note_feature.see_exist(id, subject)
        if exist:
            return exist.notes
        else:
            return f"Unable to show note !"
        
    def add_formula(self, id, formula_name, formula):
        done = self.note_feature.add_formula(id, formula_name, formula)
        if done:
            return f"Successfully added formula !"
        else:
            return f"Unable to add formula !"

    def add_vocab(self, id, word, meaning):
        done = self.note_feature.add_vocab(id, word, meaning)
        if done:
            return f"Successfully added vocab !"
        else:
            return f"Unable to add vocab !"
    
    def see_vocab_formula(self, id):
        done = self.note_feature.see_vocab_formula(id)
        if done:
            return done
        else:
            return f"Unable to get vocab/formula !"

    def export_txt(self, file, id):
        done = self.note_feature.export_txt(file, id)
        if done:
            return f"Successfully exported !"
        else:
            return f"Unable to export"

    #Tasks methods
    def add_task(self, title, desc, priority, deadline, notes):
        self.todo_feature.add_todo(title, desc, priority, deadline, notes)

    @property
    def see_task(self):
        task = self.todo_feature.see_task
        if task:
            return task
        else:
            return f"Unable to get the task !" 
        
    def see_task_by(self, by, type):
        task = self.todo_feature.see_task_by(by, type)
        if task:
            return task
        else:
            return f"Unable to get the task !"
    def mark_done(self, title):
        done = self.todo_feature.mark_done(title)
        if done:
            return f"Marked done !"
        else:
            return f"Unable to mark done !"

    #json methods
    def save_json(self, file):
        pass

    def load_json(self, file):
        pass

    #pomodoro methods

    def pomodoro(self, id, subject, method):
        note = self.see_note(id, subject)
        if method == "25/5":
            return self.pomodoro_feature.Pomodoro25(id, subject, note)
        elif method == "50/10":
            return self.pomodoro_feature.Pomodoro50(id, subject, note)


    
