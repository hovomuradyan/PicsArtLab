import random
import sys
from PyQt5 import QtGui, QtTest, uic
from PyQt5.QtWidgets import *


class firstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWindow = None
        uic.loadUi("design1.ui", self)  # initializing design for mode choosing menu
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.setWindowIcon(QtGui.QIcon('txeturka.png'))
        self.easyButton = self.findChild(QPushButton, "pushButton_1")
        self.hardButton = self.findChild(QPushButton, "pushButton_2")
        self.easyButton.clicked.connect(self.openEasyMode)
        self.hardButton.clicked.connect(self.openHardMode)
        self.show()

    def openEasyMode(self):
        self.secondWindow = easyMode()
        self.secondWindow.show()
        self.hide()

    def openHardMode(self):
        self.secondWindow = hardMode()
        self.secondWindow.show()
        self.hide()


class easyMode(QMainWindow):
    def __init__(self):
        self.gameOver = 0
        super(easyMode, self).__init__()
        uic.loadUi("design.ui", self)  # initializing design for easy mode
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.setWindowTitle("Tic Tac Toe EASY v1.0.0 for PicsArt Lab")
        self.setWindowIcon(QtGui.QIcon('txeturka.png'))
        self.cell1 = self.findChild(QPushButton, "pushButton_1")
        self.cell2 = self.findChild(QPushButton, "pushButton_2")
        self.cell3 = self.findChild(QPushButton, "pushButton_3")
        self.cell4 = self.findChild(QPushButton, "pushButton_4")
        self.cell5 = self.findChild(QPushButton, "pushButton_5")
        self.cell6 = self.findChild(QPushButton, "pushButton_6")
        self.cell7 = self.findChild(QPushButton, "pushButton_7")
        self.cell8 = self.findChild(QPushButton, "pushButton_8")
        self.cell9 = self.findChild(QPushButton, "pushButton_9")
        self.startButton = self.findChild(QPushButton, "pushButton_10")
        self.label = self.findChild(QLabel, "label")
        self.cell1.clicked.connect(lambda: self.clicker(self.cell1))
        self.cell2.clicked.connect(lambda: self.clicker(self.cell2))
        self.cell3.clicked.connect(lambda: self.clicker(self.cell3))
        self.cell4.clicked.connect(lambda: self.clicker(self.cell4))
        self.cell5.clicked.connect(lambda: self.clicker(self.cell5))
        self.cell6.clicked.connect(lambda: self.clicker(self.cell6))
        self.cell7.clicked.connect(lambda: self.clicker(self.cell7))
        self.cell8.clicked.connect(lambda: self.clicker(self.cell8))
        self.cell9.clicked.connect(lambda: self.clicker(self.cell9))
        self.startButton.clicked.connect(self.reset)
        self.show()

    """
    checkWin function checking if the someone win this game
    """
    def checkWin(self):
        if self.cell1.text() == self.cell4.text() and self.cell1.text() == self.cell7.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell4, self.cell7)
            return self.cell1.text()
        elif self.cell2.text() == self.cell5.text() and self.cell2.text() == self.cell8.text() and \
                self.cell2.text() != "":
            self.win(self.cell2, self.cell5, self.cell8)
            return self.cell2.text()
        elif self.cell3.text() == self.cell6.text() and self.cell3.text() == self.cell9.text() and \
                self.cell3.text() != "":
            self.win(self.cell3, self.cell6, self.cell9)
            return self.cell3.text()
        elif self.cell1.text() == self.cell2.text() and self.cell1.text() == self.cell3.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell2, self.cell3)
            return self.cell1.text()
        elif self.cell4.text() == self.cell5.text() and self.cell4.text() == self.cell6.text() and \
                self.cell4.text() != "":
            self.win(self.cell4, self.cell5, self.cell6)
            return self.cell4.text()
        elif self.cell7.text() == self.cell8.text() and self.cell7.text() == self.cell9.text() and \
                self.cell7.text() != "":
            self.win(self.cell7, self.cell8, self.cell9)
            return self.cell7.text()
        elif self.cell1.text() == self.cell5.text() and self.cell1.text() == self.cell9.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell5, self.cell9)
            return self.cell1.text()
        elif self.cell3.text() == self.cell5.text() and self.cell3.text() == self.cell7.text() and \
                self.cell3.text() != "":
            self.win(self.cell3, self.cell5, self.cell7)
            return self.cell3.text()

    """
    win function change the style of sheet if someone win
    
    :param firstCell: first cell of winner sign
    :param secondCell: second cell of winner sign
    :param thirdCell: third cell of winner sign
    :return winner sign 
    """
    def win(self, firstCell, secondCell, thirdCell):
        self.gameOver = 1
        firstCell.setStyleSheet('QPushButton {color: black;}')
        secondCell.setStyleSheet('QPushButton {color: black;}')
        thirdCell.setStyleSheet('QPushButton {color: black;}')
        self.label.setText(f"{firstCell.text()} Win!")
        self.disable()
        return firstCell.text

    """
    disable function disable all buttons, if the game overed
    """
    def disable(self):
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                      self.cell9]
        for button in buttonList:
            button.setEnabled(False)


    #getAvailableCell function give's us a free cells, where AI can take put the sign
    def getAvailableCells(self):
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        emptyCells = []
        for button in buttonList:
            if button.text() == "":
                emptyCells.append(button)
        return emptyCells

    def AITurn(self):
        QtTest.QTest.qWait(180)
        empyCells = self.getAvailableCells()
        if empyCells and self.gameOver == 0:
            self.label.setText("X's Turn")
            clickedButton = random.choice(empyCells)
            clickedButton.setText("O")
            clickedButton.setEnabled(False)
        else:
            self.label.setText("Tie! Well played.")

    """
    clicker function is for changing style, then the player click on button
    
    :param clickedButton
    :return none
    """
    def clicker(self, clickedButton):
        self.label.setText("O's Turn")
        clickedButton.setText("X")
        clickedButton.setEnabled(False)
        self.checkWin()
        self.AITurn()
        self.checkWin()

    """
    reset function is for setting againg available cells and returning modechoosing menu
    """
    def reset(self):
        self.gameOver = 0
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for button in buttonList:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet('QPushButton {color: gray;}')
        self.label.setText("Click on any cell to start game")
        self.hide()
        self.openChooseMenu()

    """
    openChooseMenu function is for opening mode choosing menu
    """
    def openChooseMenu(self):
        self.firstWindow = firstWindow()
        self.firstWindow.show()


class hardMode(QMainWindow):
    def __init__(self):
        self.gameOver = 0
        super(hardMode, self).__init__()
        uic.loadUi("design.ui", self)
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        self.setWindowTitle("Tic Tac Toe HARD v1.0.0 for PicsArt Lab")
        self.setWindowIcon(QtGui.QIcon('txeturka.png'))
        self.cell1 = self.findChild(QPushButton, "pushButton_1")
        self.cell2 = self.findChild(QPushButton, "pushButton_2")
        self.cell3 = self.findChild(QPushButton, "pushButton_3")
        self.cell4 = self.findChild(QPushButton, "pushButton_4")
        self.cell5 = self.findChild(QPushButton, "pushButton_5")
        self.cell6 = self.findChild(QPushButton, "pushButton_6")
        self.cell7 = self.findChild(QPushButton, "pushButton_7")
        self.cell8 = self.findChild(QPushButton, "pushButton_8")
        self.cell9 = self.findChild(QPushButton, "pushButton_9")
        self.startButton = self.findChild(QPushButton, "pushButton_10")
        self.label = self.findChild(QLabel, "label")
        self.cell1.clicked.connect(lambda: self.clicker(self.cell1))
        self.cell2.clicked.connect(lambda: self.clicker(self.cell2))
        self.cell3.clicked.connect(lambda: self.clicker(self.cell3))
        self.cell4.clicked.connect(lambda: self.clicker(self.cell4))
        self.cell5.clicked.connect(lambda: self.clicker(self.cell5))
        self.cell6.clicked.connect(lambda: self.clicker(self.cell6))
        self.cell7.clicked.connect(lambda: self.clicker(self.cell7))
        self.cell8.clicked.connect(lambda: self.clicker(self.cell8))
        self.cell9.clicked.connect(lambda: self.clicker(self.cell9))
        self.startButton.clicked.connect(self.reset)
        self.show()

    def checkWin(self):
        if self.cell1.text() == self.cell4.text() and self.cell1.text() == self.cell7.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell4, self.cell7)
            return self.cell1.text()
        elif self.cell2.text() == self.cell5.text() and self.cell2.text() == self.cell8.text() and \
                self.cell2.text() != "":
            self.win(self.cell2, self.cell5, self.cell8)
            return self.cell2.text()
        elif self.cell3.text() == self.cell6.text() and self.cell3.text() == self.cell9.text() and \
                self.cell3.text() != "":
            self.win(self.cell3, self.cell6, self.cell9)
            return self.cell3.text()
        elif self.cell1.text() == self.cell2.text() and self.cell1.text() == self.cell3.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell2, self.cell3)
            return self.cell1.text()
        elif self.cell4.text() == self.cell5.text() and self.cell4.text() == self.cell6.text() and \
                self.cell4.text() != "":
            self.win(self.cell4, self.cell5, self.cell6)
            return self.cell4.text()
        elif self.cell7.text() == self.cell8.text() and self.cell7.text() == self.cell9.text() and \
                self.cell7.text() != "":
            self.win(self.cell7, self.cell8, self.cell9)
            return self.cell7.text()
        elif self.cell1.text() == self.cell5.text() and self.cell1.text() == self.cell9.text() and \
                self.cell1.text() != "":
            self.win(self.cell1, self.cell5, self.cell9)
            return self.cell1.text()
        elif self.cell3.text() == self.cell5.text() and self.cell3.text() == self.cell7.text() and \
                self.cell3.text() != "":
            self.win(self.cell3, self.cell5, self.cell7)
            return self.cell3.text()
        if not self.getAvailableCells():
            self.label.setText("TIE, well played")

    """
    checkWin2 function checking if any player win without calling function win(). Calling in minimax algorithm.
    
    :param none
    :return winner sign
    """
    def checkWin2(self):
        if self.cell1.text() == self.cell4.text() and self.cell1.text() == self.cell7.text() and \
                self.cell1.text() != "":
            return self.cell1.text()
        elif self.cell2.text() == self.cell5.text() and self.cell2.text() == self.cell8.text() and \
                self.cell2.text() != "":
            return self.cell2.text()
        elif self.cell3.text() == self.cell6.text() and self.cell3.text() == self.cell9.text() and \
                self.cell3.text() != "":
            return self.cell3.text()
        elif self.cell1.text() == self.cell2.text() and self.cell1.text() == self.cell3.text() and \
                self.cell1.text() != "":
            return self.cell1.text()
        elif self.cell4.text() == self.cell5.text() and self.cell4.text() == self.cell6.text() and \
                self.cell4.text() != "":
            return self.cell4.text()
        elif self.cell7.text() == self.cell8.text() and self.cell7.text() == self.cell9.text() and \
                self.cell7.text() != "":
            return self.cell7.text()
        elif self.cell1.text() == self.cell5.text() and self.cell1.text() == self.cell9.text() and \
                self.cell1.text() != "":
            return self.cell1.text()
        elif self.cell3.text() == self.cell5.text() and self.cell3.text() == self.cell7.text() and \
                self.cell3.text() != "":
            return self.cell3.text()
        else:
            return "d"

    """
    checkWin function checking if the someone win this game
    
    :param none
    :return winner's sign
    """
    def win(self, firstCell, secondCell, thirdCell):
        self.gameOver = 1
        firstCell.setStyleSheet('QPushButton {color: black;}')
        secondCell.setStyleSheet('QPushButton {color: black;}')
        thirdCell.setStyleSheet('QPushButton {color: black;}')
        self.label.setText(f"{firstCell.text()} Win!")
        self.disable()
        return firstCell.text

    """
    disable function is for disabling buttons after game over
    
    :param none
    :return none 
    """
    def disable(self):
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for button in buttonList:
            button.setEnabled(False)

    """
    getAvailableCells function checking list of available buttons
    
    :param none
    :return list of available cells
    """
    def getAvailableCells(self):
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        emptyCells = []
        for button in buttonList:
            if button.text() == "":
                emptyCells.append(button)
        return emptyCells

    """
    clicker function is for setting sign on clicked button
    :param clickedButton
    :return none
    """
    def clicker(self, clickedButton):
        self.label.setText("O's Turn")
        clickedButton.setText("X")
        clickedButton.setEnabled(False)
        self.checkWin()
        self.AITurn()
        self.checkWin()

    """
    reset function for reseting design after game over
    
    :param none
    :return none
    """
    def reset(self):
        self.gameOver = 0
        buttonList = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for button in buttonList:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet('QPushButton {color: gray;}')
        self.label.setText("Click on any cell to start game")
        self.hide()
        self.openChooseMenu()

    """
    openChooseMenu is for opening modechoosing menu
    
    :param none
    :return none
    """
    def openChooseMenu(self):
        self.firstWindow = firstWindow()
        self.firstWindow.show()

    """
    getScore function is for game situation rating
    :param none
    :return rate of game situation
    """
    def getScore(self):
        winner = self.checkWin2()
        if winner == "X":
            return -1
        elif winner == "0":
            return 1
        else:
            return 0

    """
    miniMax function get best choose for putting sign by minimax algorithm. Minimax algorithm is generating all variations and by getScore() function choose the best variation.
    
    :param currentPlay
    :return button for best move
    """
    def miniMax(self, currentPlayer):
        score = self.getScore()
        if score != 0:
            return score
        elif not self.getAvailableCells():
            return 0
        if currentPlayer == 1:
            bestMove = -1000000
            for cell in self.getAvailableCells():
                cell.setText("0")
                bestMove = max(bestMove, self.miniMax(1 - currentPlayer))
                cell.setText("")
            return bestMove
        else:
            bestMove = 100000000
            for cell in self.getAvailableCells():
                cell.setText("X")
                bestMove = min(bestMove, self.miniMax(1 - currentPlayer))
                cell.setText("")
            return bestMove

    """
    AITurn is function, that by minimax() function put sign 
    
    :param none
    :return none
    """
    def AITurn(self):
        QtTest.QTest.qWait(180)
        emptyCells = self.getAvailableCells()
        bestMove = -100000
        if not emptyCells:
            return
        button = emptyCells[0]
        for cell in emptyCells:
            cell.setText("0")
            currentScore = self.miniMax(0)
            cell.setText("")
            if currentScore > bestMove:
                bestMove = currentScore
                button = cell
        self.label.setText("X's turn")
        button.setText("0")
        button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = firstWindow()
    app.exec_()
