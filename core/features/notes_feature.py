from utils.file_helper import generate_id
class NotesFeature:
    def __init__(self):
        self.notes = {}
    
    def add_note(self, title, desc, subject, notes):
        id = generate_id(title, )
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
