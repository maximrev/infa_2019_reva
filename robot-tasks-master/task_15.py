#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while not wall_is_beneath():
            move_down()
            move_right()
    else:
        if wall_is_above() and wall_is_on_the_right():
            while not wall_is_beneath():
                move_down()
                move_left()
        else:
            if wall_is_beneath() and wall_is_on_the_right():
                while not wall_is_above():
                    move_up()
                    move_left()
            else:
                while not wall_is_above():
                    move_up()
                    move_right()
        


if __name__ == '__main__':
    run_tasks()
