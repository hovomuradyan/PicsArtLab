import random
from PyQt5 import QtGui, QtTest, uic
from PyQt5.QtWidgets import *
import sys


class firstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design1.ui", self)
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
        uic.loadUi("design.ui", self)
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

    def win(self, a, b, c):
        self.gameOver = 1
        a.setStyleSheet('QPushButton {color: black;}')
        b.setStyleSheet('QPushButton {color: black;}')
        c.setStyleSheet('QPushButton {color: black;}')
        self.label.setText(f"{a.text()} Win!")
        self.disable()
        return a.text

    def disable(self):
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for b in button_list:
            b.setEnabled(False)

    def getAvailableCells(self):
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        emptyCells = []
        for i in button_list:
            if i.text() == "":
                emptyCells.append(i)
        return emptyCells

    def AITurn(self):
        QtTest.QTest.qWait(180)
        empyCells = self.getAvailableCells()
        if empyCells and self.gameOver == 0:
            clicked_button = random.choice(empyCells)
            clicked_button.setText("O")
            clicked_button.setEnabled(False)
            self.label.setText("X's Turn")
        else:
            self.label.setText("Tie! Well played.")

    def clicker(self, clicked_button):
        self.label.setText("O's Turn")
        clicked_button.setText("X")
        clicked_button.setEnabled(False)
        self.checkWin()
        self.AITurn()
        self.checkWin()

    def reset(self):
        self.gameOver = 0
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for button in button_list:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet('QPushButton {color: gray;}')
        self.label.setText("Click on any cell to start game")


class hardMode(QMainWindow):
    def __init__(self):
        self.gameOver = 0
        super(hardMode, self).__init__()
        uic.loadUi("design.ui", self)
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
        if self.getAvailableCells() == []:
            self.label.setText("TIE, well played")

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

    def win(self, a, b, c):
        self.gameOver = 1
        a.setStyleSheet('QPushButton {color: black;}')
        b.setStyleSheet('QPushButton {color: black;}')
        c.setStyleSheet('QPushButton {color: black;}')
        self.label.setText(f"{a.text()} Win!")
        self.disable()
        return a.text

    def disable(self):
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for b in button_list:
            b.setEnabled(False)

    def getAvailableCells(self):
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        emptyCells = []
        for i in button_list:
            if i.text() == "":
                emptyCells.append(i)
        return emptyCells

    def clicker(self, clicked_button):
        clicked_button.setText("X")
        clicked_button.setEnabled(False)
        self.checkWin()
        self.label.setText("O's Turn")
        self.AITurn()
        self.checkWin()

    def reset(self):
        self.gameOver = 0
        button_list = [self.cell1, self.cell2, self.cell3, self.cell4, self.cell5, self.cell6, self.cell7, self.cell8,
                       self.cell9]
        for button in button_list:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet('QPushButton {color: gray;}')
        self.label.setText("Click on any cell to start game")

    def getScore(self):
        winner = self.checkWin2()
        if winner == "X":
            return -1
        elif winner == "0":
            return 1
        else:
            return 0

    def miniMax(self, currentPlayer):
        score = self.getScore()
        if score != 0:
            return score
        elif self.getAvailableCells() == []:
            return 0
        if currentPlayer == 1:
            bestMove = -1000000
            for i in self.getAvailableCells():
                i.setText("0")
                bestMove = max(bestMove, self.miniMax(1 - currentPlayer))
                i.setText("")
            return bestMove
        else:
            bestMove = 100000000
            for i in self.getAvailableCells():
                i.setText("X")
                bestMove = min(bestMove, self.miniMax(1 - currentPlayer))
                i.setText("")
            return bestMove

    def AITurn(self):
        QtTest.QTest.qWait(180)
        emptyCells = self.getAvailableCells()
        bestMove = -100000
        if emptyCells == []:
            return
        a = emptyCells[0]
        for i in emptyCells:
            i.setText("0")
            current_score = self.miniMax(0)
            i.setText("")
            if current_score > bestMove:
                bestMove = current_score
                a = i
        a.setText("0")
        a.setEnabled(False)
        self.label.setText("X's turn")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = firstWindow()
    app.exec_()
