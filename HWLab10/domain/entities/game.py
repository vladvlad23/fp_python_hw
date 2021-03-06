"""
    @author: Matko Gabriel
    @email:  ytgabi98@gmail.com
    @date:   12/17/2017 13:46
"""
from random import randint
from tkinter import Tk

from domain.entities.dot import Dot
from domain.entities.player import Player
from ui.ui import UI
from ui.ui_handler import UiHandler
from utils.ai_computer import AIComputer
from utils.utils import Utils


class Game(object):

    def __init__(self, board):
        self.__board = board
        self.__player = Player("human")
        self.__computer = Player("computer")
        self.__isPlayerTurn = True
        self.__ai = AIComputer(self.__board)

    def startGame(self):
        print(self.board)
        print("Width: " + str(self.board.width))
        print("Height: " + str(self.board.height))
        print("You: \033[31m" + "RED" + "\033[0m")
        print("Computer: \033[34m" + "BLUE" + "\033[0m")
        # print("Choose UI:")
        # option = None
        # while True:
        #     try:
        #         option = UI.chooseUI()
        #         break
        #     except Exception as ex:
        #         print(ex)
        option = 1
        if option == 1:
            while not self.isOver():
                if self.isPlayerTurn:
                    column = UI.readPlayerInput(self.board.width) - 1

                    if not self.board.isAnyDotAvaiable(column):
                        print("There is no dot available in this column!")
                        continue

                    self.board.makeMove(column, Dot(1))
                    self.isPlayerTurn = False
                    print("Your move on C" + str(column+1) + ":")
                    print(self.board)
                else:
                    computer = AIComputer(self.board)
                    column = computer.computeMove()
                    if not self.board.isAnyDotAvaiable(column):
                        print("Computer chose a move that is not available")
                        continue

                    self.board.makeMove(column, Dot(2))
                    self.isPlayerTurn = True

                    print("Computer made a move on C" + str(column+1) + ":")
                    print(self.board)
            if not self.isPlayerTurn:
                print("Congratulations! You won the game!")
            else:
                print("GAME OVER\nSorry but the computer is way more smarter than you :D")
            print("Game finished!")

        elif option == 2:
            root = Tk()
            handler = UiHandler(root)
            handler.openUi()
            root.mainloop()
    def isOver(self):
        return Utils.isGameFinished(self.board) or Utils.isGameDraw(self.board)

    @property
    def isPlayerTurn(self):
        return self.__isPlayerTurn

    @isPlayerTurn.setter
    def isPlayerTurn(self, turn):
        self.__isPlayerTurn = turn

    @property
    def board(self):
        return self.__board

    @property
    def AI(self):
        return self.__ai
