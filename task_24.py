#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down(3)
    move_right(2)
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_left()
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left()
    
if __name__ == '__main__':
    run_tasks()
