#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
   	if wall_is_above() and wall_is_on_the_left():
   		move_down(9)
   		move_right(9)
   	elif wall_is_above() and wall_is_on_the_right():
   		move_down(9)
   		move_left(9)
   	elif wall_is_beneath() and wall_is_on_the_right():
   		move_up(9)
   		move_left(9)
   	elif wall_is_beneath() and wall_is_on_the_left():
   		move_up(9)
   		move_right(9)
    	


if __name__ == '__main__':
    run_tasks()
