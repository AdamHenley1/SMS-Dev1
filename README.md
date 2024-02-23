# MERLIN HACKATHON 2024 | Team NotTheCIA

## HAC Society Overview
### Overview
HAC Society is a world building game, set in a procedurally generated retro map. You have a civilisation of people; these people will do their own things, but you can set community goals (such as upgrading the town hall), which you will pay them to do for you.

You get the money to pay for this from the taxes that the people will pay to you. They get taxed some money when they trade with each other, or [ maybe another thing ].

There are more details on specific parts of this shown below.


## The World
The world is a grid of points along an x and y axis. Each block can start as one of three block: dirt (shown by a space), a tree (shown by a little tree), or water (shown by a little bar).

When the game is started, the a new world can be generated on the fly, or one can be loaded from a file.

## The People

## The Economy


### People Plan
ToDo:
- Design class for people
- Get people interacting with environment
- Money system so people can trades goods for money
- Tax system any trade 20% rounded up gets taxed to you so you can buy more trees and things

Development:
- Created a dictionary containing the different job options and how many woker in each. This was used in the getJob function to get a number for the probability of what the job assigned should be based on the workers there already are. Less wokers means higher probability of that specific job being assigned.
- Created a getName function which selects a random first and last name from their respective files.
- There is a class for World as well as the dirt, trees and water. 


### World Plan
ToDo:
- Get storage working
- Get world generation working
- weather


## Misc
### Developers
- [Adam](https://github.com/AdamHenley1)
- [Andrea](https://github.com/andreac47)
- [Cam](https://github.com/FishFuck3r)
