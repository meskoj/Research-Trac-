# Research Track 1: first assignment
This is the script for the first assignment of the course Research Track 1 at UniGE.

The goal is to let the robot brings all the tokens in the same position.
## How to run the program
In order to run the script, clone the folder and with the terminal go inside the folder robot-sim.
Once there is possible to write the following command to run the script.

```bash
$ python run.py asssignment.py
```
## Pseudocode
```python
#Set global variables
a_th = 2.0 #threshold to control linear distance
d_th = 0.4 #threshold to control orientation
grabbed = False #used to know if a token is grabbed by the robot

R = Robot() #instance an object of class robot

function drive(speed, seconds): this function set a linear velocity to the robot with certain speed and for x seconds

function turn(speed, seconds): this function is used to set an angular velocity to the robot

function select_nearest_token(token_id): this function let the robot choose the nearest token in is sight not already taken before

function go_to_token(selected_token): this function is used to search the token selected by the previous function and to bring the robot to it.

function count_token(): this function count the number of tokens in the are

Define the main function:

Create a list of token_id and put the code of the first token in it.
Create a counter to store the information of the number of tokens already taken

number_of_token = count_token()

While counter is less than number_of_token:

	Selected_token = select_nearest_token(token_id)
	
	If selected_token not found:
		Turn(speed, seconds)
		
	Else:
	
		Go_to_token(selected_token)
		Token_id.append(selected_token) #add to the list the token id taken 
		go_to_token(token_id[0]) #go to the first saved token
		counter incrementation
```

## Some improvements
1) Adding the coordinates of the center can enhance the robot's efficiency in gathering all the tokens to that specific point.
2) In preparation for real-world applications, the robot should prioritize gentleness when grabbing and releasing tokens. This can be done by monitoring object distances and decelerating to avoid collisions.
