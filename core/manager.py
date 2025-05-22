from core.features.notes_feature import NotesFeature
from core.features.pomodoro_feature import PomodoroFeature
from core.features.todo_feature import ToDoFeature
from core.utils.file_helper import save_json, load_data, get_current_date, get_current_time
class Manager:
    def __init__(self):
        self.note_feature = NotesFeature()
        self.pomodoro_feature = PomodoroFeature()
        self.todo_feature =  ToDoFeature()

    #Notes methods
    def add_note(self, title, desc, subject, note):
        done = self.note_feature.add_note(title, desc, subject, note)
        if done:
            return f"Successfully added note ! Id : {done}"
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
        
    @property
    def return_notes(self):
        notes = self.note_feature.return_notes
        if notes:
            return notes
        else:
            return f"No notes available at the moment"
    #Tasks methods
    def add_task(self, title, desc, priority, deadline):
        self.todo_feature.add_todo(title, desc, priority, deadline)

    @property
    def see_task(self):
        task = self.todo_feature.see_task
        if task:
            return task
        else:
            return f"No tasks found !" 
        
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
        Json = {}

        Tasks = self.todo_feature.todo
        Json["Task"] = {}
        
        for task in Tasks:
            titletask = self.todo_feature.todo[task].title
            desctask = self.todo_feature.todo[task].desc
            prioritytask = self.todo_feature.todo[task].priority
            deadlinetask = self.todo_feature.todo[task].deadline
            finishedtask = self.todo_feature.todo[task].finished
            Json["Task"][task] = {"Title" : titletask,
                                  "Description" : desctask,
                                  "Priority" : prioritytask,
                                  "Deadline" : deadlinetask,
                                  "Finished" : finishedtask}
        

        Notes = self.note_feature.notes
        for note in Notes:
            titlenote = self.note_feature.notes[note].title
            descnote = self.note_feature.notes[note].desc
            subjectnote = self.note_feature.notes[note].subject
            notes = self.note_feature.notes[note].notes
            if subjectnote in ["Math", "Science"]:
                formulanote = self.note_feature.notes[note].formula
                Json["Notes"][note] = {"Title" : titlenote,
                                       "Description" : descnote,
                                       "Subject" : subjectnote,
                                       "Note" : notes,
                                       "Formulas" : formulanote}
            elif subjectnote in self.note_feature.languages:
                vocabnote = self.note_feature.notes[note].vocab
                Json["Notes"][note] = {"Title" : titlenote,
                                       "Description" : descnote,
                                       "Subject" : subjectnote,
                                       "Note" : notes,
                                       "Vocab" : vocabnote}
            else:
                Json["Notes"][note] = {"Title" : titlenote,
                                       "Description" : descnote,
                                       "Subject" : subjectnote,
                                       "Note" : notes}
            


        Logs25 = self.pomodoro_feature.logs["25/5"]
        for id in Logs25:
            notepomodoro25 = Logs25[id].id
            subjectpomodoro25 = Logs25[id].subject
            datepomodoro25 = Logs25[id].date
            typepomodoro25 = Logs25[id].type
            Json["Pomodoro Log"]["25/5"][id] = {"Id Note" : notepomodoro25,
                                                "Subject Note" : subjectpomodoro25,
                                                "Date" : datepomodoro25,
                                                "Type" : typepomodoro25}
        Logs50 = self.pomodoro_feature.logs["50/10"]
        for id in Logs50:
            notepomodoro50 = Logs25[id].id
            subjectpomodoro50 = Logs25[id].subject
            datepomodoro50 = Logs25[id].date
            typepomodoro50 = Logs25[id].type
            Json["Pomodoro Log"]["50/10"][id] = {"Id Note" : notepomodoro50,
                                                "Subject Note" : subjectpomodoro50,
                                                "Date" : datepomodoro50,
                                                "Type" : typepomodoro50}
        

        save_json(file, Json)

    def load_json(self, file):
        Json = load_data(file)
        if Json:
            
            for task in Json["Task"]:
                titletask = Json["Task"][task]["Title"]
                desctask = Json["Task"][task]["Description"]
                prioritytask = Json["Task"][task]["Priority"]
                deadlinetask = Json["Task"][task]["Deadline"]
                finishedtask = Json["Task"][task]["Finished"]
                if finishedtask == True:
                    self.add_task(titletask, desctask, prioritytask, deadlinetask)
                    self.mark_done(titletask)
                elif finishedtask == False:
                    self.add_task(titletask, desctask, prioritytask, deadlinetask)
            

            Notes = self.note_feature.notes
            for note in Notes:
                titlenote = Json["Notes"][note]["Title"]
                descnote = Json["Notes"][note]["Description"]
                subjectnote = Json["Notes"][note]["Subject"]
                notes = Json["Notes"][note]["Notes"]
                if subjectnote in ["Math", "Science"]:
                    formulas = Json["Notes"][note]["Formulas"]
                    placeholder, id = self.add_note(titlenote, descnote, subjectnote, notes).split(": ")
                    for formula in formulas:
                        self.add_formula(id, formula, formulas[formula])
                elif subjectnote in self.note_feature.languages:
                    vocabs = Json["Notes"][note]["Vocabs"]
                    placeholder, id = self.add_note(titlenote, descnote, subjectnote, notes).split(": ")
                    for vocab in vocabs:
                        self.add_vocab(id, vocab, vocabs[vocab])
                else:
                    self.add_note(titlenote, descnote, subjectnote, notes)
                


            Logs25 = Json["Pomodoro Log"]["25/5"]
            for id in Logs25:
                notepomodoro25 = Logs25[id]["Id Note"]
                subjectpomodoro25 = Logs25[id]["Subject Note"]
                datepomodoro25 = Logs25[id]["Date"]
                typepomodoro25 = Logs25[id]["Type"]
                self.pomodoro_feature.add_log(notepomodoro25, subjectpomodoro25, typepomodoro25, datepomodoro25)
                
            Logs50 = Json["Pomodoro Log"]["50/10"]
            for id in Logs50:
                notepomodoro50 = Logs50[id]["Id Note"]
                subjectpomodoro50 = Logs50[id]["Subject Note"]
                datepomodoro50 = Logs50[id]["Date"]
                typepomodoro50 = Logs50[id]["Type"]
                self.pomodoro_feature.add_log(notepomodoro50, subjectpomodoro50, typepomodoro50, datepomodoro50)
            
        

    #pomodoro methods

    def pomodoro(self, id, subject, method):
        note = self.see_note(id, subject)
        if method == "25/5":
            return self.pomodoro_feature.Pomodoro25(id, subject, note)
        elif method == "50/10":
            return self.pomodoro_feature.Pomodoro50(id, subject, note)
    
    @property
    def get_date(self):
        return get_current_date()
    
    def get_time(self):
        return get_current_time()
    
