#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    new_key = key
    new_value = value
    update = {**a_dictionary, new_key: new_value}
    print(update)
