#!/usr/bin/python3


def element_at(my_list, idx):
    if(idx >= 0 and len(my_list) > idx):
        return my_list[idx]
    return 'None'
