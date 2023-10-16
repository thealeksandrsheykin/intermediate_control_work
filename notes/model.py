# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import json
from view import View
from note import Note


class Model(object):

    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.id > max_id:
                max_id = item.id
        id = max_id + 1
        note.id = id
        self.notes.append(note)
        self.write_json(self.notes)

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.id == search_id:
                return note
        else:
            View.display_note_id_not_exist(search_id)

    def read_notes(self):
        return self.read_json()

    def update_note(self, search_id, note):
        self.notes = self.read_notes()
        for item in self.notes:
            if item.note_id == search_id:
                item.date = note.date
                item.name = note.name
                item.data = note.data

        self.write_json(self.notes)

    def delete_note(self, search_id):
        self.notes = self.read_notes()

        for index, note in enumerate(self.notes):
            if note.id == search_id:
                del self.notes[index]

        self.write_json(self.notes)

    def delete_all_notes(self):
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json(self.notes)

    def write_json(self, notes):
        json_strings_list = list()
        for note in notes:
            json_strings_list.append({'id': note.id, 'date': note.date, 'name': note.name, 'data': note.data})

        notes_json = json.dumps(json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.filename, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        notes_list = list()
        try:
            with open(self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['name'], item['data']))

            return notes_list
        except ValueError:
            return self.notes
