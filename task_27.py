#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	i=0
	move_right()
	fill_cell()
	while not wall_is_on_the_right():
		move_right()
		fill_cell()
		i+=1






if __name__ == '__main__':
    run_tasks()
