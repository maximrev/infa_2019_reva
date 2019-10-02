#!/usr/bin/python3

from pyrob.api import *


@task(delay= 0.01)
def task_8_11():
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        else:
            if wall_is_above():
                move_down()
                fill_cell()
                move_up()
            else:
                if wall_is_beneath():
                    move_up()
                    fill_cell()
                    move_down()
                else:
                    move_down()
                    fill_cell()
                    move_up()
                    move_up()
                    fill_cell()
                    move_down()
        move_right()
    if wall_is_above() and wall_is_beneath():
        fill_cell()
    else:
        if wall_is_above():
            move_down()
            fill_cell()
            move_up()
        else:
            if wall_is_beneath():
                move_up()
                fill_cell()
                move_down()
            else:
                move_down()
                fill_cell()
                move_up()
                move_up()
                fill_cell()
                move_down()    


if __name__ == '__main__':
    run_tasks()
