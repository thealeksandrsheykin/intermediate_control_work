# -*- coding: utf-8 -*-
# !/usr/bin/env python3


class Note:
    def __init__(self, id, date, name, data):
        self._id = id
        self._name = name
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
        return self._name


    @name.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self._data

    @data.setter
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



