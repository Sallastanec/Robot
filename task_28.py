#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
	n=0
	while n<6:
		if fill_cell():
			n=n+1
			move_right()




if __name__ == '__main__':
    run_tasks()
