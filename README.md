# Team AI - Final Project

Sources:

- https://github.com/NiklasEi/dots-and-boxes-python - used for our base game but modified heavily to work with our algorithm  
    (files: Pics folder, dotsAndBoxes.py)

###File Explanations
- dotsAndBoxes.py - Has the main game and UI
- Minimax.py - Where our algorithm lives
- OtherAlgorithms.py - Where the Random, Greedy, and Defensive algorithms are
- Sandbox.py - Just used for testing
- dotsAndBoxesTesting.py - Used for multiple run testing without UI for faster results

### How to run the main game

To start a game do:
```
python3 dotsAndBoxes.py
```
You can add a number as an argument to change the size of the game.
```
python3 dotsAndBoxes.py 20
```
The command above would start a 20x20 game. The default size is 10x10.
######NOTE: dotsAndBoxes.py code has to be changed manually if you want to try the other algorithms (line 84). Also there is 
######no manual playing ability anymore since we had to remove it

## Test Environment
For the test environment, in the main method you can run the game by calling
```
# This would run 100 games which would be against the Greedy Algorithm and have a max depth of 3
for i in range(100):
    run_game(5, 3, 3)

# run_game(Gameboard Size, Opponent Algorithm, Max Depth)
# Opponent alogirthms: 1 = Random, 2 = Greedy, 3 = Defensive
```

To run the test environment which give no UI, then do:
```
python3 dotsAndBoxesTesting.py
```
If you keep the output csv file in the code, then that will show all the games ran during the test. Just a warning, it
will overwrite what is in that file after each run.
