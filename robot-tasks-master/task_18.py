#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_28():
    while wall_is_above() and not wall_is_on_the_right():
        move_right()
    if not wall_is_above():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    else:
        while wall_is_above():
            move_left()
       
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()
