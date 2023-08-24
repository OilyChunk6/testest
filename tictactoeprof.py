class TicTacToeBoard:

    def __init__(self):
        self._board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._player = "X"

    def __str__(self):
        strReturn = ""
        strReturn += str(self._board[0]) + " | " + str(self._board[1]) + " | " + str(self._board[2]) + "\n"
        strReturn += str(self._board[3]) + " | " + str(self._board[4]) + " | " + str(self._board[5]) + "\n"
        strReturn += str(self._board[6]) + " | " + str(self._board[7]) + " | " + str(self._board[8]) + "\n"
        return strReturn

    def _coup_possible(self, case):
        if case < 1 or case > 9:
            return False
        if self._board[case - 1] == "X" or self._board[case - 1] == "O":
            return False
        else:
            return True

    def play(self, case):
        if not self._coup_possible(case):
            return False

        self._board[case - 1] = self._player
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"
        return True

    def _check_game(self):
        for i in range(0, 9, 3):
            if self._board[i] == self._board[i+1] == self._board[i+2]:
                return self._board[i]
            for i in range(0, 3):
                if self._board[i] == self._board[i+3] == self._board[i+6]:
                    return self._board[i]
            if self._board[0] == self._board[4] == self._board[8]:
                return self._board[0]
            if self._board[2] == self._board[4] == self._board[6]:
                return self._board[2]

            return None


game = TicTacToeBoard()
print(game)

while game._check_game() is None:
    case = int(input("Choisissez une case: "))
    if not game.play(case):
        print("Case invalide")
    print(game)

print("Le joueur " + str(game._check_game()) + " a gagné")



