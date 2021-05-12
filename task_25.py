#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

	move_down()
	for i in range(4):
		move_down(2)
		move_right()
		fill_cell()
		move_up()
		fill_cell()
		move_right()
		fill_cell()
		move_left(2)
		fill_cell()
		move_up()
		move_right()
		fill_cell()
		move_left()
		move_right(4)
		move_down(2)
		move_right()
		fill_cell()
		move_up()
		fill_cell()
		move_right()
		fill_cell()
		move_left(2)
		fill_cell()
		move_up()
		move_right()
		fill_cell()
		move_left()


if __name__ == '__main__':
    run_tasks()
