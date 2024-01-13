# Research Track 1: first assignment
This is the script for the first assignment of the course Research Track 1 at the University of Genoa. Made by Marco Meschini S6273938

## Environment and goal
The environment used in this project is a 2D playground in which is present a moving robot that can interact with some tokens scattered throughout the area.
Some functions, such as the one to control the motor or to see the surround tokens, have been provided with the simulator and are part of the class `Robot().` While, the ones used in the `assignment.py` have been built to accomplish this specific task.
For more information about the environment and the class is possible to see this [repository](https://github.com/CarmineD8/python_simulator/tree/assignment23).

In this case, the playground is organized in this way:
* At the start the robot is on the top-left corner.
* There are 6 golden tokens positioned around the so called _arena_.

The final goal is to control the robot and gather all the tokens to the same position.
## How to run the program
The simulator requires a Python 2.7 installation, the [pygame](https://www.pygame.org) library, [PyPyBox2D](https://pypi.org/project/pypybox2d/2.1-r331/), and [PyYAML](https://pypi.org/project/PyYAML/).
In order to run the script, clone the folder and go inside the folder robot-sim.
Once there is possible to write the following command to run the script.

```bash
$ python2 run.py asssignment.py
```
## Code structure and functionality
The first step is to define the global variables that are used by the robot. They are:
* ```d_th```  is the distance threshold at which the robot can successfully grab a token. Adjust this threshold to control how close the robot needs to be for token grabbing.
* ```a_th```  is the orientation threshold, it is used by the robot to know wheter it is well aligned with respect to the token.
* ```grabbed``` is a boolean variable that is used to know if the robot is carrying an object. Initially, it is set to False (the robot is free) and when it grabs a token the variable becomes True.
### Motion functions
Two functions are used to control the robot's movements inside the playground; they are ```drive()``` and ```turn()```. In particular, the first one controls the robot's linear motion by setting the motor's velocity, 
allowing the robot to move forward or backward at a specified speed for a defined duration. While, the second one controls the robot's rotational motion by adjusting the motor's velocity. It enables the robot to turn around its own axis.
### Vision function
Another important function to make the robot robust is the ```count_token()```. This is a vision function to let the robot perform a 360° turn and count the number of tokens in the playground. By using this function, the robot can adapt to scenarios where the number of tokens differs from the expected 6, making it versatile and capable of solving unknown problems.
### Function to find and gather tokens
Finally, there are two functions to select a token and take it. The first one is ```select_nearest_token()```; This function enables the robot to identify and select the nearest available token within its field of view. It returns the unique identifier of the selected token. The second one is ```go_to_token()```; with this function, the robot navigates to the token that was previously selected using `select_nearest_token()`. Once at the token's location, the robot will grab the token. These two functions work together to facilitate the robot's token collection strategy.

## Pseudocode
```python
#Set global variables
a_th = 2.0 #threshold to control the orientation
d_th = 0.4 #threshold to control the linear threshold
grabbed = False #used to know if the robot has grabbed a token

R = Robot() #instance an object of class robot

function drive(speed, seconds): this function set a linear velocity to the robot with certain speed
and for x seconds

function turn(speed, seconds): this function is used to set an angular velocity to the robot

function select_nearest_token(token_id): this function let the robot choose the nearest token in
is sight not already taken before

function go_to_token(selected_token): this function is used to search the token selected by the
previous function and to bring the robot to it.

function count_token(): this function count the number of tokens in the playground

Define the main function:

Create a list of token_id and put the code of the first token in it.
Create a counter to store the information of the number of tokens already taken

number_of_token = count_token()

While counter is less than number_of_token:

	selected_token = select_nearest_token(token_id)
	
	If selected_token not found:
		turn(speed, seconds)
		
	Else:
	
		go_to_token(selected_token)
		token_id.append(selected_token) #add to the list the token id taken 
		go_to_token(token_id[0]) #go to the first saved token
		counter incrementation
```

## Some improvements
1) The first adjustment can be done by selecting a bigger values for both the linear and the rotational speeds, to make the robot be faster in accomplish its task. The problem is that by increasing the speeds become difficult to control the robot finding the correct orientation and avoiding possible obstacles.
2) Adding the coordinates of the center can enhance the robot's efficiency in gathering all the tokens to that specific point. Or more in general, it could be useful to implement a function, that knowing the position of each token, computes some geometric calculations finding the point that minimize the travel lenght.
3) A big simplification is that the robot searches only for the nearest token in its sight. To greatly increase the robot performance an idea can be to scan the environment at the start and find the position of all the tokens. Then, it could computes the optimised path to gather the tokens in the fastest way.
4) In preparation for real-world applications, the robot should prioritize gentleness when grabbing and releasing tokens. This can be done by monitoring object distances and decelerating to avoid collisions.
