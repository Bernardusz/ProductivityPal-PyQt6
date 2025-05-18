from utils.file_helper import generate_id, file_exists
class NotesFeature:
    def __init__(self):
        self.notes = {}
        self.languages = ["Indonesian", "English", "Hungarian", "Mandarin"]
    
    def add_note(self, title, desc, subject, notes):
        id = generate_id(title, self.notes)
        if subject == "Math":
            self.notes[id] = MathNotes(title, desc, "Math", notes)
            return id
        elif subject == "Science":
            self.notes[id] = ScienceNotes(title, desc, "Science", notes)
            return id
        elif subject in self.languages:
            self.notes[id] = LanguagesNotes(title, desc, subject, notes)
            return id
        else:
            self.notes[id] = Notes(title, desc, subject, notes)
            return id
        
    def see_exist(self, id, subject): 
        if id in self.notes:
            if self.notes[id].subject == subject:
                return self.notes[id]
            else:
                return False
        else:
            return False
    
    def edit_notes(self, id, subject, edit, change):
        obj = self.see_exist(id, subject)
        if obj:
            if edit == "Title":
                obj.title = change
                new_id = generate_id(change, self.notes)
                self.notes[new_id] = self.notes.pop(id)
                return True
            elif edit == "Desc":
                obj.desc = change
                return True
            elif edit == "Notes":
                obj.notes = change
                return True
            else:
                return False
        else:
            return False
        
    def remove_notes(self, id, subject):
        obj = self.see_exist(id, subject)
        if obj:
            self.notes.pop(id)
            return True
        else:
            return False
        
    def add_formula(self, id, formula_name, formula):
        obj = self.see_exist(id, "Math")
        obj1 = self.see_exist(id, "Science")
        if obj:
            obj.add_formula(formula_name, formula)
            return True
        elif obj1:
            obj1.add_formula(formula_name, formula)
            return True
        else:
            return False
    
    def add_vocab(self, id, word, meaning):
        for language in self.languages:
            obj = self.see_exist(id, language)
            if obj:
                break
            else:
                pass
        if obj:
            obj.add_vocab(word, meaning)
            return True
        else:
            return False
    
    def see_vocab_formula(self, id):
        if id in self.notes:
            if self.notes[id].subject in ["Math", "Science"]:
                return self.notes[id].formula
            elif self.notes[id].subject in self.languages:
                return self.notes[id].vocab
            else:
                return False
        else:
            return False
    
    def export_txt(self, file, id):
        file_path = file_exists(file)
        if id in self.notes:
            title = self.notes[id].title
            desc = self.notes[id].desc
            subject = self.notes[id].subject
            note = self.notes[id].note 
            if file_path:
                with open(file_path, "w") as f:
                    f.write(f"{title}\n")
                    f.write("---\n")
                    f.write(f"{subject}\n")
                    f.write(f"{desc}\n")
                    f.write("---")
                    f.write(f"{note}")
                return True
            else:
                return False
        else:
            return False
        


class Notes:
    def __init__(self, title, desc, subject, notes):
        self.title = title
        self.desc = desc
        self.subject = subject
        self.notes = notes

class MathNotes(Notes):
    def __init__(self, title, desc, subject, notes):
        super().__init__(title, desc, subject, notes)
        self.formula = {}
    
    def add_formula(self, name, formula):
        self.formula[name] = formula
    
class ScienceNotes(Notes):
    def __init__(self, title, desc, subject, notes):
        super().__init__(title, desc, subject, notes)
        self.formula = {}
    
    def add_formula(self, name, formula):
        self.formula[name] = formula

class LanguagesNotes(Notes):
    def __init__(self, title, desc, subject, notes):
        super().__init__(title, desc, subject, notes)
        self.vocab = {}

    def add_vocab(self, word, meaning):
        self.vocab[word] = meaning
