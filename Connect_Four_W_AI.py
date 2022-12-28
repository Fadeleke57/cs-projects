# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:16:18 2022

@author: fadel
"""

class Board():
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, init_height, init_width):
        '''constructs a new Board object'''
        self.height=init_height
        self.width=init_width
        self.slots = [[' '] * self.width for row in range(self.height)]
         
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-'*(2*self.width+1)
        s += '\n'
        for col in range(self.width):
            s += ' ' + str(col%10) 
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        count = 0
        for row in range(self.height):
            if self.slots[row][col]== 'X' or self.slots[row][col]== 'O':
                count +=1
        
        row = -1
        while self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
            if count == self.height:
                break
            row -= 1
        self.slots[row][col] = checker
            
    ### add your reset method here ###
    def reset(self):
        '''reset the Board object'''
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column 
        col on the calling Board object. Otherwise, it should return False.'''
        
        if 0 <= col < self.width:
            if self.slots[0][col]==' ':
                return True
        return False

    def is_full(self):
        ''' returns True if the called Board object is completely full of checkers,
        and returns False otherwise.'''
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True
    
    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object.
        If the column is empty, then the method should do nothing.'''
        count = 0
        for row in range(self.height):
            if self.slots[row][col]== 'X' or self.slots[row][col]== 'O':
                count +=1
                
        row = 0
        while self.slots[row][col] == ' ':
            if count == 0:
                break
            row += 1
        self.slots[row][col]= ' '
        
    def is_win_for(self, checker):
        '''accepts a parameter checker that is either 'X' or 'O', and returns True 
        if there are four consecutive slots containing checker on the board. Otherwise, 
        it should return False.'''
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) or self.is_vertical_win(checker) or \
           self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker):
                return True
        else:
            return False
        
    def is_horizontal_win(self, checker):
            """ Checks for a horizontal win for the specified checker."""
            for row in range(self.height):
                for col in range(self.width - 3):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row][col + 1] == checker and \
                       self.slots[row][col + 2] == checker and \
                       self.slots[row][col + 3] == checker:
                        return True

            # if we make it here, there were no horizontal wins
            return False
        
    def is_vertical_win(self, checker):
            """ Checks for a vertical win for the specified checker."""
            for row in range(self.height - 3):
                for col in range(self.width):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row+1][col] == checker and \
                       self.slots[row+2][col] == checker and \
                       self.slots[row+3][col] == checker:
                        return True

            # if we make it here, there were no vertical wins
            return False
        
    def is_down_diagonal_win(self, checker):
            """ Checks for a down_diagonal win for the specified checker."""
            for row in range(self.height-3):
                for col in range(self.width-3):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row +1][col +1] == checker and \
                       self.slots[row +2][col +2] == checker and \
                       self.slots[row +3][col +3] == checker:
                        return True

            # if we make it here, there were no down_diagonal wins
            return False
        
    def is_up_diagonal_win(self, checker):
            """ Checks for a up_diagonal win for the specified checker."""
            for row in range(self.height-3, self.height):
                for col in range(self.width-3):
                    # Check if the next four columns in this row
                    # contain the specified checker.
                    if self.slots[row][col] == checker and \
                       self.slots[row -1][col +1] == checker and \
                       self.slots[row -2][col +2] == checker and \
                       self.slots[row -3][col +3] == checker:
                       return True

            # if we make it here, there were no up_diagonal wins
            return False
        
class Player:
    '''represent a player of the Connect Four game'''
    def __init__(self, checker):
        '''constructs a new Player object'''
        assert(checker == 'X' or checker == 'O')
        self.checker= checker
        self.num_moves= 0
        
    def __repr__(self):
        '''returns a string representing a Player object. The string returned 
        should indicate which checker the Player object is using'''
        s = 'Player' + ' ' + self.checker
        return s
        
    def opponent_checker(self):
        '''returns a one-character string representing the checker of the Player
        object’s opponent.'''
        if self.checker == 'X':
            return 'O'
        else: 
            return 'X'
        
    def next_move(self, b):
        '''accepts a Board object b as a parameter and returns the column where the
        player wants to make the next move.'''
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))    
            if b.can_add_to(col)== False:
                print('Try again!')
                print()
                
            else:
                return col

import random  

class AIPlayer(Player):
    '''can be used for an intelligent computer player that chooses the best option 
    from the available columns.'''
    def __init__(self, checker, tiebreak, lookahead):
        '''constructs a new AIPlayer object'''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak= tiebreak
        self.lookahead= lookahead
        
    def __repr__(self):
        '''returns a string representing an AIPlayer object'''
        s = 'AIPlayer' + ' ' + self.checker + ' ' + '(' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        '''takes a list scores containing a score for each column of the board,
        and that returns the index of the column with the maximum score.'''
        list_max_scores=[]
        rand_list=[]
        count=0
        for i in scores:
            if not i == max(scores):
                count+=1
            elif i == max(scores):
                count+=1
                list_max_scores+=[[i, count-1]]
                rand_list+=[count-1]
        
        if self.tiebreak == 'LEFT':
            return list_max_scores[0][1]
        elif self.tiebreak == 'RIGHT':
            return list_max_scores[-1][1]
        else:
            return random.choice(rand_list)
        
    def scores_for(self, b):
        '''takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b.'''
    
        scores= [50]* b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = max(opp_scores)
                #remove checker
                b.remove_checker(col)
                
        return scores
    
    def next_move(self, b):
        '''overrides (i.e., replaces) the next_move method that is inherited from 
        Player. Rather than asking the user for the next move, this version of 
        next_move should return the called AIPlayer‘s judgment of its best possible 
        move.'''
        self.num_moves += 1
        col = self.max_score_column(self.scores_for(b))
        while True:
            return col
        
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
     '''takes two parameters: a Player object p for the player whose move is 
     being processed, and a Board object b for the board on which the game is 
     being played.'''
     s = str(p) 
     print(s +"'s", 'turn')
     
     player_next_move= p.next_move(b)
     b.add_checker(str(p.checker), player_next_move)
     print('\n')
     print(b)
   
     if b.is_win_for(str(p.checker)) == True:
         print(s, 'wins in', p.num_moves, 'moves.')
         print('Congratulations!')
         return True     
     elif b.is_win_for('X') == False and b.is_win_for('O') == False and b.is_full() == False:
         return False
     else:
         print('It'+"'"+'s', 'a tie!')
         return True
     
class RandomPlayer(Player):
    '''can be used for an unintelligent computer player that chooses at random 
    from the available columns.'''
    def next_move(self, b):
        '''choose at random from the columns in the board b that are not yet 
        full, and return the index of that randomly selected column'''
        
        self.num_moves += 1
        
        available_ind=[]
        for c in range(b.width):
            if b.can_add_to(c):
                available_ind+=[c]
        
        col=random.choice(available_ind)
        return col
