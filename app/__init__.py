from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'
    
    code: int
    title: str
    text: str
    importance: str = MEDIUM
    creation_date: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

def add_tag(self, tag: str) -> None:
    if tag not in self.tags:
        self.tags.append(tag)

def _str_(self) -> str:
    return f"Date: {self.creation_date}\n{self.title}: {self.text}"

@dataclass
class Notebook:
    notes: Dict[int, Note] = field(default_factory=dict)

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        note = Note(code, title, text, importance)
        self.notes[code] = note
        return code

    def delete_note(self, code: int) -> None:
        if code in self.notes:
            del self.notes[code]

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes.values() if note.importance in [Note.HIGH, Note.MEDIUM]]

    def notes_by_tag(self, tag: str) -> List[Note]:
        return [note for note in self.notes.values() if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        tag_count = {}

        for note in self.notes.values():
         for tag in note.tags:
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1

        if not tag_count:
            return ""

    max_count = max(tag_count.values())
    most_common_tags = [tag for tag, count in tag_count.items() if count == max_count]

    return min(most_common_tags)
