"""
Matheson james
mjam534

This is the base form of the solitarie assignment with the additional code from the
template.

"""


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

    def print_all(self, index):
        string = ""
        if index == 0:
            
            for position in range(len(self.__items)):
                if position == 0:
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
        self.__num_cards = len(cards)
        self.__num_piles = (self.__num_cards // 8) + 3
        self.__max_num_moves = self.__num_cards * 2
        for i in range(self.__num_piles):
            self.__piles.append(CardPile())
        for i in range(self.__num_cards):
            self.__piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.__piles[i]

    def display(self):
        for index in range(self.__num_piles):
            pile = self.get_pile(index)
            string = "{}:".format(index)
            print(string, end = " ")
            pile.print_all(index)

    def move(self,p1,p2):
        

        pile1 = self.__piles[p1]
        pile2 = self.__piles[p2]
        
        if p1 == p2:
            
            if pile1.size() == 0:
                return
            top_card = pile1.peek_top()
            pile1.add_bottom(top_card)
            pile1.remove_top()


        elif p1 == 0 and p2 > 0:
            

            if pile1.size() == 0:
                
                return

            card_value1 = pile1.peek_top()
            if pile2.size() != 0:
                card_value2 = pile2.peek_bottom()
            else:
                card_value2 = 0

            if card_value1 == card_value2 - 1 or pile2.size() == 0:
                
                pile2.add_bottom(card_value1)
                pile1.remove_top()
                


        elif p1 > 0 and p2 > 0:
            
            
            if pile1.size() == 0 or pile2.size() == 0:
                return

            card_value1 = pile1.peek_top()
            card_value2 = pile2.peek_bottom()

            if card_value1 == card_value2 - 1 or pile2.size() == 0:
                for count in range(pile1.size()):
                    
                    value = card_value1 = pile1.peek_top()
                    pile2.add_bottom(value)
                
                    pile1.remove_top()

        
            

            
    def play(self):
        print("********************** NEW GAME *****************************")
        move_number = 1
        while move_number <= self.__max_num_moves and not self.is_complete():
            self.display()
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row1 = int(input("Move from row no.:"),10)
            print("Round", move_number, "out of", self.__max_num_moves, end = ": ")
            row2 = int(input("Move to row no.:"),10)
            if row1 >= 0 and row2 >= 0 and row1 < self.__num_piles and row2 < self.__num_piles:
                self.move(row1, row2)
            move_number += 1
           
        if self.is_complete():
            print("You Win in", move_number - 1, "steps!\n")
        else:
            print("You Lose!\n")


    def is_complete(self):

        if (self.__piles[0]).size() == 0:
            pile1_empty = True

        else:
            pile1_empty = False
            
        count = 0
        for pile in self.__piles:
            if pile.size() > 0:
                count += 1

        if count == 1:
            single_pile = True
        else:
            single_pile = False

        if pile1_empty == True and single_pile == True:
            return True

        else:
            return False



                
            
            
            
            



    











        
            

        
