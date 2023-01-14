#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    if(idx >= 0 and len(copied_list) > idx):
        copied_list[idx] = element
    return copied_list
