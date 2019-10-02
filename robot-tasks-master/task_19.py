#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_29():
    while not wall_is_on_the_left():
        move_left()
    if not wall_is_beneath():
        while not wall_is_above():
            move_up()
    else:
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_above():
            move_up()
        if not wall_is_beneath():
            while not wall_is_on_the_left():
                move_left()
        


if __name__ == '__main__':
    run_tasks()
