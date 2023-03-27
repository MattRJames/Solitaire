"""
Matheson James, mjam534
Creative component of the solitaire assingment

Code recreates a more traditional solitaire using the base code from the code
runner work as a foundation, game is best played in the terminal.

"""

import random
import os


    
class Card:

    def __init__(self, number, suit):
        self.__number = number
        self.__suit = suit
        
        if suit == "clubs" or suit == "spades":
            self.__colour = "black"

        else:
            self.__colour = "red"

        if self.__number == 1:
            self.__display_number = "A"

        elif self.__number > 1 and self.__number < 10:
            self.__display_number = self.__number

        elif self.__number == 10:
            self.__display_number ="x"
        elif self.__number == 11:
            self.__display_number ="J"

        elif self.__number == 12:
            self.__display_number ="Q"

        elif self.__number == 13:
            self.__display_number ="K"

       



    def get_number(self):
        return self.__number

    def get_suit(self):
        return self.__suit

    def get_colour(self):
        return self.__colour

    def __str__(self):
        if self.__suit == "clubs":
            symbol = "♣"
        if self.__suit == "spades":
            symbol = "♠"
        if self.__suit == "hearts":
            symbol = "♥"
        if self.__suit == "diamonds":
            symbol = "♦"
        
        return "[{}{}]".format(self.__display_number,symbol)

            
class CardPile:
    def __init__(self):
        self.__items = []

    def add_top(self, item):
        item = [item]
        self.__items = item + self.__items

    def add_bottom(self,item):
        self.__items =self.__items + [item]

    def remove_top(self):
        output = self.__items[:1]
        self.__items = self.__items[1:]
        return output[0]

    def remove_bottom(self):
        return self.__items.pop(len(self.__items) -1 )

    def size(self):
        return len(self.__items)

    def peek_top(self):
        return self.__items[0]

    def peek_bottom(self):
        return self.__items[len(self.__items) - 1]

    def shuffle(self):
        self.__items = random.sample(self.__items,52)

    def get_items(self):
        return self.__items

    def print_all(self, index):
        string = ""
        if index == 0:
            for index in range(len(self.__items)):
                if index == 0:
                    string = str(self.__items[0])
                    
                
                else:
                    string += " *"

        else:
            
            for number in self.__items:
                string += str(number) + " "
                
        print(string)
    
            


    


class Solitaire:
    def __init__(self, cards):
        self.__piles = []
        self.__goal_piles = []
        self.__num_cards = len(cards)
        self.__num_piles = ((self.__num_cards // 8) + 3) - 1
        self.__max_num_moves = self.__num_cards * 4
        for i in range(self.__num_piles):
            self.__piles.append(CardPile())
        for i in range(self.__num_cards):
            (self.__piles[0]).add_bottom(cards[i])
        
        
        

    def get_pile(self, i):
        return self.__piles[i]

    

    def display(self):
        diplay_lists =[]
        column0 = (self.__piles[0])
        max_length = 4
        string = "Draw   1   2   3   4   5   6   7"
        print("-" * len(string))
        print(string)
        for pile in self.__piles[1:]:
            if pile.size() > max_length:
                max_length = pile.size()

        for index in range(max_length):
            string = ""
            for count in range(self.__num_piles):
                if count == 0 and index > 0 and (index < 4 and index < self.__piles[count].size()):
                    string = string + "  *   "
                elif count == 0 and index > 0 and (index >=4 or index > self.__piles[count].size()):
                    string = string + "      "
                else:
                    try:
                        
                        string = string + ((self.__piles[count].get_items())[index]).__str__()
                        if count == 0:
                            string = string + "  "
                    except IndexError:
                        if count == 0:
                            string = string + "      "
                        else:
                            string = string + "    "
            print(string)

        
            
    def move(self,p1,p2):

        

        
        pile1 = self.__piles[p1]
        pile2 = self.__piles[p2]

              
        
        if p1 == 0 and p2 == 0:
            pile = self.__piles[p1]
            if pile.size() == 0:
                return
            top_card = pile.peek_top()
            pile.add_bottom(top_card)
            pile.remove_top()


        elif p1 == 0 and p2 > 0:
            

            if pile1.size() == 0:
                
                return

            card_value1 = pile1.peek_top()
            
            if pile2.size() != 0:
                card_value2 = pile2.peek_bottom()
            else:
                card_value2 = 0

            if pile2.size() == 0 or card_value1.get_number() == card_value2.get_number() - 1:
                if pile2.size() == 0 or card_value1.get_colour() != card_value2.get_colour():
                
                    pile2.add_bottom(card_value1)
                    pile1.remove_top()


        
                


        elif p1 > 0 and p2 > 0:
            
            
            if pile1.size() == 0 or pile2.size() == 0:
                return

            card_value1 = pile1.peek_top()
            
            card_value2 = pile2.peek_bottom()
            

            if card_value1.get_number() == card_value2.get_number() - 1:
                if  card_value1.get_colour() != card_value2.get_colour():
                    
                
                    
                    for count in range(pile1.size()):
                        
                        value = card_value1 = pile1.peek_top()
                        pile2.add_bottom(value)
                    
                        pile1.remove_top()

    
    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.__max_num_moves and not self.is_complete():
            os.system('cls')
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            try:
                row1 = int(input("Move from row no.:"),10)
                print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
                row2 = int(input("Move to row no.:"),10)
                if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                    self.move(row1, row2)
                move_number += 1
            except:
                print("Remember to only enter valid values!")
        if self.is_complete():
            self.display()
            print("You Win in", move_number - 1, "steps!\n")
            value = input("Press enter to go home, champ")
        else:
            print("You Lose!")
            value = input("Press enter to return the menu")
            
    


    def is_complete(self):

        if (self.__piles[0]).size() == 0:
            pile1_empty = True

        else:
            pile1_empty = False
            
        count = 0
        for pile in self.__piles:
            if pile.size() > 0:
                count += 1

        if count == 4:
            single_pile = True
        else:
            single_pile = False

        if pile1_empty == True and single_pile == True:
            return True

        else:
            return False
            
    


def initialize():
    deck = []

    for number in range(1,14):
        card = Card(number,"diamonds")
        deck.append(card)

    for number in range(1,14):
        card = Card(number,"hearts")
        deck.append(card)

    for number in range(1,14):
        card = Card(number,"spades")
        deck.append(card)

    for number in range(1,14):
        card = Card(number,"clubs")
        deck.append(card)
        

    random.shuffle(deck)
    game = Solitaire(deck)
    game.play()
    
    


def main():
    user_input = None
    
    while user_input != 3:
        os.system("cls")
        print('1. Play')
        print('2. Instructions')
        print('3. Exit')
        user_input = input("please enter the number of the option you wish to select: ")

        while user_input != "1" and user_input != "2" and user_input != "3":
            user_input = input("please type a valid value: ")
            

        if user_input == '1':
                
                initialize()

        elif user_input == '2':
                
            print("Game Rules:")
            print("-General Rules: The aim of the game is to move the cards around to create four piles of cards each containing 13 cards, if you fail to do so in the allotted number of turns you will lose")
            print("The deck is a standard set of playing cards with no jokers however the 10 card has been swapped for an x.\n")
            print("The move counter will not change if you enter invalid values, however if the positions are valid and the move isn't allowed a move will be added to the counter")
            print("The draw pile is located at position 0, furthermore if the position 0 is both the destination and origin of a move a new card will be drawn from the deck.")
            print("-Card Movement: Cards are moved by typing the pile you want to move the card from and the pile you want the card to be placed in. You will be prompted to enter the positions seperatly.")
            print("a cards can only be moved to positions where the card it is being placed onto is of the opposite colour(spades/clubs are black, diamonds/hearts are red)")
            print("additionally the card at the top of the pile being moved must be one less than the bottom of the pile it is being moved onto.")
            print("note: the card order is ascending order is A,2,3,4,5,6,7,8,9,x,J,Q,K\n\n")

        elif user_input == '3':
            return

            
        
    
main()
                            
    

        
        


















    
