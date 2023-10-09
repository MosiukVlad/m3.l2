from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLabel,
                             QListWidget, QLineEdit, QTextEdit, 
                             QInputDialog, QHBoxLayout, QVBoxLayout)

import json

app = QApplication([])

notes_win = QWidget ()
notes_win.setWindowTitle("Smart notes")
notes_win.resize(900,600)


list_notes = QListWidget()
list_notes_label = QLabel ("Notes list")

button_note_create = QPushButton("Create")
button_note_del = QPushButton("Delete")
button_note_save = QPushButton("Save")


field_tag = QLineEdit("")
field_tag.setPlaceholderText("Enter tag...")
field_text = QTextEdit("")

button_tag_add = QPushButton("Add")
button_tag_del = QPushButton("Delete")
button_tag_search = QPushButton("Search")

list_tags = QListWidget()
list_tags_label = QLabel("Tags list")


col1 = QVBoxLayout()
col2 = QVBoxLayout()
row1= QHBoxLayout()
row2= QHBoxLayout()
row3= QHBoxLayout()
row4= QHBoxLayout()

notes_win.show()
app.exec_()