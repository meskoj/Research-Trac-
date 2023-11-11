from __future__ import print_function
import time
from sr.robot import *

a_th = 2.0
#float: Threshold for the control of the orientation

d_th = 0.4
#float: Threshold for the control of the linear distance

grabbed = False
#Boolean: To know if the robot has grabbed a token

R = Robot()
#Instance of the class Robot


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
    dist = 100
    
    for token in R.see():   
        if token.dist < dist and token.info.code not in token_id:
            dist = token.dist
	    selected_token = token.info.code
	    
    if dist == 100:
	return -1
    else:
   	return selected_token



	
def go_to_token(selected_token):
	"""
	Function used to find the token selected by select_nearest_token and let the robot
	go to it
	
	Arg: selected_token(int): code of the selected token
	"""
	global grabbed
	found = False
	while 1:
	
		for token in R.see():
			if token.info.code == selected_token:
				dist = token.dist
				rot_y = token.rot_y
				found = True
				
	 	if found == True and dist < 2*d_th and grabbed is True: #if the robot is near the token selected to group all the tokens, 
	 								#it release the token in the hand
			grabbed = False
			R.release()
			drive(-50, 0.5)
			break
			
		elif found == True and dist > d_th: #if the robot is far from the token, the robot goes towards it
			if -a_th <= rot_y <= a_th: #if the robot is well aligned with the token, it goes forward
				print("Ah, that'll do.")
				drive(50, 0.5)
			elif rot_y < -a_th: #if the robot is not well aligned with the token, it moves on the left or on the right
				print("Left a bit...")
			   	turn(-2, 0.5)
			elif rot_y > a_th:
				print("Right a bit...")
				turn(+2, 0.5)
				
		elif found == True and dist < d_th and grabbed is False: #if the robot is near the token to grab, the robot grabs it
			grabbed = True
			R.grab()
			break
			
		else: #if the token has not been found, the robot turns
			turn(20,0.5)


def count_token():
	"""
	Function used to count the number of tokens in the arena
	"""
	
	token_list = []
	for i in range(10): #the robot revolves around itself to find all the tokens
		for token in R.see():
			if token.info.code not in token_list:
				token_list.append(token.info.code)
		turn(25,0.5)
	return len(token_list)  			    			    	

def main():

	token_number = count_token()
	token_id = [] #Create the list to store the token id
	
	while len(R.see()) == 0 : #Until the token is not found, turn
		turn(25,0.5) 
		
	first_token = R.see()[0].info.code #Saving the code of the first token where all the others will be brought		
	token_id.append(first_token)
	
	i = 1
	while i < token_number:
		selected_token = select_nearest_token(token_id)
		
		if selected_token == -1:
			turn(20,0.5)
		else:
			go_to_token(selected_token) #Go to grab one token
			token_id.append(selected_token)
			go_to_token(token_id[0]) #Bring the token grabbed to the first token
			i = i + 1

			
main()
