#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	for m in range(6):
		move_right()
		for n in range(26):
			fill_cell()
			move_right()
		fill_cell()
		move_down()
		for i in range(27):
			fill_cell()
			move_left()

		move_down()
	move_right()






if __name__ == '__main__':
    run_tasks()
