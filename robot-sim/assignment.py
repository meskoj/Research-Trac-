from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

grabbed = False
#Boolean to know if the robot is grabbing a token

R = Robot()
""" instance of the class Robot"""


def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
   	
   	
   	
def select_nearest_token(token_id):
    """
    Function to find the nearest token not already taken before
    
    Arg: token_id (list): list of tokens already brought in position
    """
    dist=100
    
    for token in R.see():   

        if token.dist < dist and token.info.code not in token_id:
            dist=token.dist
	    selected_token = token.info.code
    if dist==100:
	return -1
    else:
   	return selected_token



	
def go_to_token(selected_token):

	"""
	Function used to find the token selected by select_nearest_token and to bring
	the robot to it.
	
	Arg: selected_token(int): code of the selected token
	"""
	global grabbed
	found = False
	while 1:
	
		for token in R.see():
			if token.info.code == selected_token:
				dist=token.dist
				rot_y=token.rot_y
				found = True
				
	 	if found == True and dist < 2*d_th and grabbed is True:
			grabbed = False
			R.release()
			drive(-50, 0.5)
			break
			
		elif found == True and dist > d_th:
			if -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
				print("Ah, that'll do.")
				drive(50, 0.5)
			elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
				print("Left a bit...")
			   	turn(-3, 0.5)
			elif rot_y > a_th:
				print("Right a bit...")
				turn(+3, 0.5)
				
		elif found == True and dist < d_th and grabbed is False:
			grabbed = True
			R.grab()
			break
			
		else:
			turn(20,0.5)


def count_token():
	"""
	Function used to count the number of tokens in the arena
	"""
	
	token_list = []
	for i in range(10):
		for token in R.see():
			print(token.info.code)
			if token.info.code not in token_list:
				token_list.append(token.info.code)
		turn(25,0.5)
	return len(token_list)  			    			    	

def main():

	counter = count_token()
	token_id = [-1] #Create the list to store the token id
	token_id[0] = R.see()[0].info.code #Saving the code of the first token where all the other will be brought
	i = 1
	
	while i < counter:
		selected_token = select_nearest_token(token_id)
		
		if selected_token == -1:
			turn(20,0.5)
		else:
			go_to_token(selected_token) #Go to grab one token
			token_id.append(selected_token)
			go_to_token(token_id[0]) #Bring the token grabbed to the first token
			i = i + 1

			
main()
