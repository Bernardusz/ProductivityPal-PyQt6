from utils.file_helper import get_current_date

class PomodoroFeature:
    def __init__(self):
        self.logs = {}
        self.logs["25/5"] = {}
        self.logs["50/10"] = {}

    def Pomodoro25(self, id, subject, note):
        self.logs["25/5"][id] = PomodoroLog("25/5", subject, id)
        duration = 25*60
        session = self.pomodoro_session(note, duration)
        return {"type" : "25/5",
                "generator" : session,
                "title" : id} 
        
    def Pomodoro50(self, id, subject, note):
        self.logs["50/10"][id] = PomodoroLog("50/10", subject, id)
        duration = 50*60
        session = self.pomodoro_session(note, duration)
        return {"type" : "50/10",
                "generator" : session,
                "title" : id} 

    def pomodoro_session(self, note, duration):  # duration in seconds for testing
        yield f"Starting Pomodoro: {note}"
        yield "Half the time has passed!"
        yield "3/4 of the time has passed!"
        yield f"Time's up! Good job, soldier! Rest for {duration/(5*60)} !"

class PomodoroLog:
    def __init__(self, type, subject, id):
        self.id = id
        self.subjec = subject
        self.date = get_current_date()
        self.type = type
