# Author: Jerek Shoemaker
# myWSU id: F498Q788
# Date: March 19 2016
# CS771 Artificial Intelligence
# Programming Assignment #1

import copy;

class State():

    # Constructor for State Class
    def __init__(self, puzzle = [], goal = [], depth = -1, size = 0, parent = None):
        self.puzzle = puzzle;
        self.goal = goal;
        self.size = size;
        self.empty = self.getEmpty();
        self.gn = depth;
        self.hn = -1;
        self.fn = -1;
        self.parent = parent;

    # String representation for State Class
    def __str__(self):
        s = "";
        # Print Rows
        for i in range(self.size):
            # Print Columns
            for j in range(self.size):
                s += str(self.puzzle[(3 * i) + j]);
                if j < self.size - 1:
                    s += " ";
            s += '\n';
        return s;

    def __repr__(self):
        s = "\n";
        # Print Rows
        for i in range(self.size):
            # Print Columns
            for j in range(self.size):
                s += str(self.puzzle[(3 * i) + j]);
                if j < self.size - 1:
                    s += " ";
        return s;

    # Used to check equality of 2 States
    def __eq__(self, other):
        return self.getPuzzle() == other.getPuzzle();

    # Get the position of the empty tile
    def getEmpty(self):
        return self.puzzle.index(0);

    # Get the States depth value
    def getDepth(self):
        return self.gn;

    # Get the States goal array
    def getGoal(self):
        return self.goal;

    # Get the States puzzle array
    def getPuzzle(self):
        return self.puzzle;

    # Get the States value
    def getValue(self):
        return self.value;

    # Get the manhattan distance
    def getMD(self):
        return self.hn;

    # Set the depth
    def setDepth(self, d):
        self.gn = d;

    # Set h(n)
    def setMD(self, m):
        self.hn = m;

    # Set f(n)
    def setValue(self, v):
        self.fn = v;

    # Set the parent node
    def setParent(self, p):
        self.parent = p;

    # Make a move
    def move(self, dir, depth):
        newState = copy.deepcopy(self);
        e = newState.getEmpty();

        # Up
        if dir == 'u':
            newState.swap(e - self.size, e);

        # Down
        elif dir == 'd':
            newState.swap(e + self.size, e);

        # Left
        elif dir == 'l':
            newState.swap(e - 1, e);

        # Right
        elif dir == 'r':
            newState.swap(e + 1, e);

        # Invalid Direction
        else:
            print("Invalid Direction for Move");

        # Update the States values
        newState.refresh(depth);
        #print(newState);
        return newState;

    # Swap two different tiles
    def swap(self, to, at):
        temp = self.puzzle[at];
        self.puzzle[at] = self.puzzle[to];
        self.puzzle[to] = temp;
        return;

    # Copy the State Object
    def copy(self):
        return copy.deepcopy(self);

    # Print two States inline
    def printStates(self):
        # Print out labels for the start and goal states
        print("Start State\tGoal State");

        # Print each row
        for i in range(3):
            print("  ", end = "");
            # Print columns
            for j in range(3):
                print(str(self.getPuzzle()[(3 * i) + j]), end = " ");
            print('\t  ', end = "");
            for m in range(3):
                print(str(self.getGoal()[(3 * i) + m]), end = " ");
            print('');
        print('\n');
        return 0;

    # Calculate the Manhattan Distance
    def calcMD(self):
        sum = 0;
        num = self.size * self.size;

        for i in range(num):
            if self.getPuzzle()[i] != 0:
                g = self.getGoal().index(self.puzzle[i]);
                sum += (abs(g - i) // 3) + (abs(g - i) % 3);
        return sum;

    # Calculate and set the States value
    def calcValue(self):
        self.value = self.getDepth() + self.getMD();

    # Update the values (f(n), g(n), h(n))
    def refresh(self, d):
        self.setDepth(d);
        self.setMD(self.calcMD());
        self.setValue(self.calcValue());

    # Check to see if the puzzle has been solved
    def solved(self):
        return self.getPuzzle() == self.getGoal();
