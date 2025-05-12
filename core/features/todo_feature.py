from utils.file_helper import generate_id, is_deadline_close
class ToDoFeature:
    def __init__(self):
        self.todo = {}
    
    def add_todo(self, title, desc, priority, deadline):
        id = generate_id(title, self.todo)
        self.todo[id] = ToDo(title, desc, priority, deadline)
        return True
    
    @property
    def see_task(self):
        if self.todo:
            placeholder = {}
            for key in self.todo:
                placeholder[key] = {"Title" : placeholder[key].title,
                                    "Description" : placeholder[key].desc,
                                    "Priority" : placeholder[key].priority,
                                    "Deadline" : placeholder[key].deadline,
                                    "Finished" : placeholder[key].finished}
            return placeholder
        else:
            return False
    def see_task_by(self, by, type):
        if by == "Priority":
            if type == "Low":
                data = {}
                for key in self.todo:
                    if self.todo[key].priority == "Low":
                        data[key] = self.todo[key]
                
            elif type == "Medium":
                data = {}
                for key in self.todo:
                    if self.todo[key].priority == "Medium":
                        data[key] = self.todo[key] 

            elif type == "High":
                data = {}
                for key in self.todo :
                    if self.todo[key].priority == "High":
                        data[key] = self.todo[key]
            return data
            
        elif by == "Unfinished":
            data = {}
            for key in self.todo:
                if self.todo[key].finished == False:
                    data[key] = self.todo[key]
            return data

        elif by == "Finished":
            data = {}
            for key in self.todo:
                if self.todo[key].finished == True:
                    data[key] = self.todo[key]
            return data
        
        elif by == "Deadline":
            for key in self.todo:
                if is_deadline_close(self.todo[key].deadline):
                    data[key] = self.todo[key]
            return data
        
        else:
            return False
        
    
    def mark_done(self, title):
        data = {}
        listofkey = [key for key in self.todo if title in key]
        for task in listofkey:
            self.todo[task].finished = True
        return True
        

class ToDo:
    def __init__(self, title, desc, priority, deadline):
        self.title = title
        self.desc = desc
        self.priority = priority
        self.deadline = deadline
        self.finished = False
