import json
import os
from datetime import datetime



def file_exists(path):
    return os.path.isfile(path)

def create_file_if_not_exists(path, data):
    if not file_exists(path):
        save_json(path, data)
        
def delete_file(path):
    if file_exists(path):
        os.remove(path)

def save_json(file_path, data): #It's usually create a new one anyway
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)

def get_current_date():
    return datetime.now().strftime("%d:%m:%y")

def is_deadline_close(deadline_str):
    deadline = datetime.strptime(deadline_str, "%d:%m:%y")
    today = datetime.now()
    days_left = (deadline - today).days

    return days_left <= 5  # Returns True if 5 days or less, else False

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def generate_id(word): #Will be developed alongside features, need to know how will the object be created
    pass




    
