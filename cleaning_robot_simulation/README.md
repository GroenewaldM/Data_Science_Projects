# Cleaning Robot

## Summary

This program:
* Simulates two different types of robots cleaning the tiles of a square room.
* Simulates multiple robots, of two different types, cleaning the tiles of a square room.
* Plots a graph to compare the time it takes for an increasing number of each type of robot to clean the same room.
* Plots a graph to compare the time it takes for each type of robot to clean rooms of different shapes.


## Getting Started

* Download the distribution code from https://github.com/GroenewaldM/Data_Science_Projects/tree/main/cleaning_robot_simulation.
* Run cleaning_robot.py
* Once a simulation is complete, exit the simulation to view the next one.

## Understanding

The two types of robots that are simulated are StandardRobot and RandomWalkRobot. StandardRobot navigates by moving in a straight line intil a boundary of the room has been reached upon which it changes direction randomly and tries to move again.RandomWalkRobot randomly changes direction with every move step.

testRobotMovement simulates the movement of a single robot in a 5x5 room while runSimulation allows you to select a number of robots as well as the size of a room.
To use runSimulation uncomment the appropriatly commented sections sections of code.

## Example Output

py -m cleaning_robot

*Robot simulation pop-up*

*Robot simulation pop-up*

Plotting 1 robots...

Plotting 2 robots...

Plotting 3 robots...

Plotting 4 robots...

Plotting 5 robots...

Plotting 6 robots...

Plotting 7 robots...

Plotting 8 robots...

Plotting 9 robots...

Plotting 10 robots...

Plotting cleaning time for a room of width: 10 by height: 30

Plotting cleaning time for a room of width: 20 by height: 15

Plotting cleaning time for a room of width: 25 by height: 12

Plotting cleaning time for a room of width: 50 by height: 6

*Figure pop-up*

*Figure pop-up*

## Authors

* Project by MITx 6.00.2x: Introduction to Computational Thinking and Data Science
* Project completed by Monique Groenewald
