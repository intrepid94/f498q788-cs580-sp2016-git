# Author: Jerek Shoemaker
# myWSU id: F498Q788
# Date: March 19 2016
# CS771 Artificial Intelligence
# Programming Assignment #1

import os;
import time;
import sys;
from state import State;
from queue import PriorityQueue;
import time
sys.path.append('..');

def main():
    # Defaults for testing
    # init = [1, 2, 3, 4, 5, 6, 0, 7, 8];
    # final = [1, 2, 3, 4, 5, 6, 7, 8, 0];
    SIZE = 3;

    # Get inital and goal states
    init = createPuzzle("start");
    final = createPuzzle("goal");
    startState = State(init, final, 0, SIZE);
    startState.refresh(0);

    # Print the initial States
    startState.printStates();

    # Solve the puzzle
    if not startState.solved():
        solve(startState);

def createPuzzle(type):
    # Initalize variables
    col = 0;
    row = 2;
    val = 0;
    puzzle = [0] * 9;

    # Create Board
    for i in range(9):
        # Clear the screen
        os.system('clear');
        # Get tile value
        val = eval(input("Enter value for the tile located at (" + str(row) + ", " + str(col) + ") coordinate position for " + type + " configuration : "));
        time.sleep(0.3);
        # Place value in puzzle
        puzzle[(3 * (2 - row)) + col] = val;
        if col < 3:
            col += 1;
        if col == 3:
            col = 0;
            row -= 1;
    os.system('clear');
    return puzzle;


def solve(state):
    solved = False;
    queue = PriorityQueue();
    visited = [];

    visited.append(state);

    # Main loop
    while solved == False:
        empty = state.getEmpty();
        gn = state.getDepth() + 1;

        # Move left
        if 1 <= empty and empty % 3 != 0:
            left = state.move('l', gn);
            left.setParent(state);
            if not any(i == left for i in visited):
                queue.put((left.getValue(), time.time(), left));
                if(left.solved() == True):
                    solved = True;
                    state = left;

        # Move right
        if empty < 8 and empty % 3 != 2 and solved == False:
            right = state.move('r', gn );
            right.setParent(state);
            if not any(i == right for i in visited):
                queue.put((right.getValue(), time.time(), right));
                if(right.solved() == True):
                    solved = True;
                    state = right;

        # Move up
        if 3 <= empty and solved == False:
            up = state.move('u', gn);
            up.setParent(state);
            if not any(i == up for i in visited):
                queue.put((up.getValue(), time.time(), up));
                if(up.solved() == True):
                    solved = True;
                    state = up;

        # Move down
        if empty <= 5 and solved == False:
            down = state.move('d', gn);
            down.setParent(state);
            if not any(i == down for i in visited):
                queue.put((down.getValue(), time.time(), down));
                if(down.solved() == True):
                    solved = True;
                    state = down;

        # Move to next state
        if solved == False:
            state = queue.get()[2];
            visited.append(state);

    # Print steps to solution
    printPath(state);

# Print steps to solution
def printPath(state):
    step = 0;
    path = [];
    path.append(state);

    # Add all States to array
    while state.parent:
        path.append(state.parent);
        state = state.parent;

    # Print States from inital to goal
    for i in reversed(path):
        print("Step " + str(step) + ":");
        print(i);
        step += 1;


# Main Thread
if __name__ == '__main__':
    main();
