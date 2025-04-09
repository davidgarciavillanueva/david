from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, ClassVar


@dataclass
class Note:
HIGH: ClassVar[str] = 'HIGH'
MEDIUM: ClassVar[str] = 'MEDIUM'
LOW: ClassVar[str] = 'LOW'

code: int
title: str
text: str
importance: str = MEDIUM
creation_date: datetime = field(default_factory=datetime.now)
tags: list[str] = field(default_factory=list)

def add_tag(self, tag: str):
if tag not in self.tags:
self.tags.append(tag)

def _str_(self) -> str:
return f"Date: {self.creation_date}\n{self.title}: {self.text}"


@dataclass
class Notebook:
notes: Dict[int, Note] = field(default_factory=dict)

def add_note(self, title: str, text: str, importance: str) -> int:
new_code = len(self.notes) + 1
new_note = Note(code=new_code, title=title, text=text, importance=importance)
self.notes[new_code] = new_note
return new_code

def delete_note(self, code: int):
if code in self.notes:
del self.notes[code]

def important_notes(self) -> list[Note]:
return [note for note in self.notes.values() if note.importance in {Note.HIGH, Note.MEDIUM}]

def notes_by_tag(self, tag: str) -> list[Note]:
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
