import json

class Note:
    def __init__(self, id, title, text, created_at):
        self.id = id
        self.title = title
        self.text = text
        self.created_at = created_at

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "created_at": self.created_at
        })

class Notebook:
    def __init__(self):
        self.notes = []

    def create_note(self, title, text, created_at):
        note = Note(len(self.notes) + 1, title, text, created_at)
        self.notes.append(note)
        with open("notes.json", "w") as f:
            f.write(note.to_json())
