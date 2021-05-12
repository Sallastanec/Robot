#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
	i=13
	move_down(13)
	while i>0:
		move_right()
		for	n in range (i):
			fill_cell()
			move_up()
		move_down(i)
		i-=1
	move_left(12)
	move_down(1)


if __name__ == '__main__':
    run_tasks()
