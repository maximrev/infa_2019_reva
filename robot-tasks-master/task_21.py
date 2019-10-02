#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    for i in range(13):
        for y in range(i+1):
            fill_cell()
            move_right()
        for y in range(i+1):
            move_left()
        move_down()


if __name__ == '__main__':
    run_tasks()
