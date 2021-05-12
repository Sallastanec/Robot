#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while wall_is_above() and wall_is_beneath():
    	move_right()
    	if wall_is_above() and wall_is_beneath() and wall_is_on_the_right():
    		while not wall_is_on_the_left():
    			move_left()
    		if wall_is_on_the_left() and wall_is_beneath() and wall_is_above():
    			while not wall_is_on_the_right() and wall_is_above() and wall_is_beneath():
    				move_right()
    			break
    		else:
    			while not wall_is_above():
    				move_up()

    	elif wall_is_on_the_right():
    		while not wall_is_above():
    			move_up()
    		while not wall_is_on_the_left():
    			move_left()





if __name__ == '__main__':
    run_tasks()
