#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	m=0
	while m<5:
		for i in range (10):
			move_down()
			fill_cell()
			move_down()
			move_right()
			fill_cell()
			move_up()
			fill_cell()
			move_right()
			fill_cell()
			move_up()
			move_left()
			fill_cell()
			move_left()
			i+=1
			move_right(2)
			if wall_is_on_the_right():
				move_left(38)
			else:
				move_right(2)
		m+=1
		move_down(2)
		if wall_is_beneath():
			move_up(2)
		else:
			move_down(2)





if __name__ == '__main__':
    run_tasks()
