# Research Track 1: first assignment
This is the script for the first assignment of the course Research Track 1 at UniGE.

The goal is to let the robot bring all the tokens in the same position.

In order to run the script, go inside the folder and write:

```bash
$ python run.py exercise1.py
```

```python
#Set global variables
 a_th = 2.0 #threshold to control linear distance
 d_th = 0.4 #threshold to control orientation
grabbed = False #used to know if a token is grabbed by the robot

R = Robot() #instance an object of class robot

function drive(speed, seconds) #This function set a linear velocity to the robot with certain speed and for x seconds

function turn(speed, seconds) This function is used to set an angular velocity to the robot

function select_nearest_token(token_id) #Let the robot choose the nearest token in is sight not already taken before

function go_to_token(selected_token) #This function is used to search the token selected by the previous function and to bring the robot to it.

Define the main function:

Create a list of token_id and put the code of the first token in it.
Create a counter to store the information of the number of tokens already taken

While counter is less than 6:

	Selected_token = select_nearest_token(token_id)
	
	If selected_token not found:
		Turn(speed, seconds)
		
	Else:
	
		Go_to_token(selected_token)
		Token_id.append(selected_token) #add to the list the token id taken 
		go_to_token(token_id[0]) #go to the first saved token
		counter incrementation
```
