# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from datetime import datetime


class Note:
    def __init__(self):
        self._data = None
        self._name = None
        self._id = None
        self._date = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @id.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self.data

    @id.setter
    def data(self, value):
        self._data = value

    @property
    def date(self):
        return self.date

    @property
    def date(self):
        return self._date.strftime('%Y, %B %d, %A | %H:%M')

    @date.setter
    def date(self, value):
        self._date = datetime.strftime(value, '%Y, %B %d, %A | %H:%M')


