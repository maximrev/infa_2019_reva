#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_4_3():
    move_right(27)
    for i in range(27):
        for y in range(12):
            fill_cell()
            move_down()
        move_up(12)
        move_left()
    move_down(12)
    move_right()


if __name__ == '__main__':
    run_tasks()
