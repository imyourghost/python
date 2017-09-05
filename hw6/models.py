# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):  # storage = Storge()
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
        return '{} ToDo: {}'.format(
            '+' if self.done else '-',
            self.heading
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToReadItem(BaseItem):
    def __init__(self, heading, due_date, url):
        super(ToReadItem, self).__init__(heading)
        self.due_date = due_date
        self.url = url


    def __str__(self):
        return '{} ToRead: {} before {} from {}'.format(
            '+' if self.done else '-',
            self.heading,
            self.due_date,
            self.url,
        )

#    @classmethod
#    def construct(cls):
#        input_function = get_input_function()
#        heading = input_function('Input heading: ')
#        return ToReadItem(heading)


    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        due_date = input_function('Input Due_date: ')
        url = input_function('Input url: ')
       
        return ToReadItem(heading, due_date, url)

class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return '{} ToBuy: {} for {}'.format(
            '+' if self.done else '-',
            self.heading,
            self.price,
        )


    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)