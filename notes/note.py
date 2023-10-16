# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from datetime import datetime
from counter import counter


class Note:
    def __init__(self, id, name, data, date):
        self.id = id
        self.name = name
        self.data = data
        self.date = date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        print(self._name)
        return self._name

    @id.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self._data

    @id.setter
    def data(self, value):
        self._data = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return f'\nЗаметка: {self._id}\nДата:{self._date}\nИмя: {self._name}\nСодержание: {self._data}\n'


