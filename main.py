import os
import time
import random

class Grid:

    os.system('color 0a')

    def __init__(self):
        self.grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.haveWinner = False
        self.winner = ' '

    def printGrid(self):
        os.system('cls')
        print()
        print(self.grid[0][0] + " | " + self.grid[0][1] + " | " + self.grid[0][2] + " : 1")
        print("--+---+--")
        print(self.grid[1][0] + " | " + self.grid[1][1] + " | " + self.grid[1][2] + " : 2")
        print("--+---+--")
        print(self.grid[2][0] + " | " + self.grid[2][1] + " | " + self.grid[2][2] + " : 3")
        print("A   B   C")

    def setPos(self, player, cpu):
        if cpu:
            row = random.randint(0,2)
            col = random.randint(0,2)
            while self.grid[row][col] != ' ':
                row = random.randint(0,2)
                col = random.randint(0,2)
            self.grid[row][col] = player
            return self.CheckWinner(player)


        row = int(input("Enter the row number : ")) - 1
        col = input("Enter the column letter : ")
        if col == "A" or col == "a":
            col = 0
        elif col == "B" or col == "b":
            col = 1
        elif col == "C" or col == "c":
            col = 2
        while self.grid[row][col] != ' ':
            print("Invalid Input! Position already taken!")
            row = int(input("Enter the row number : ")) - 1
            col = input("Enter the column letter : ")
            if col == "A" or col == "a":
                col = 0
            elif col == "B" or col == "b":
                col = 1
            elif col == "C" or col == "c":
                col = 2
        self.grid[row][col] = player
        return self.CheckWinner(player)

    def CheckWinner(self, player):
        diag1 = self.grid[0][0] + self.grid[1][1] + self.grid[2][2]
        if diag1[0] == diag1[1] == diag1[2] == player:
            self.haveWinner = True
            return True

        diag2 = self.grid[0][2] + self.grid[1][1] + self.grid[2][0]
        if diag2[0] == diag2[1] == diag2[2] == player:
            self.haveWinner = True
            return True

        for vert in range(0,3):
            vert = self.grid[0][vert] + self.grid[1][vert] + self.grid[2][vert]
            if vert[0] == vert[1] == vert[2] == player:
                self.haveWinner = True
                return True

        for horiz in range(0,3):
            horiz = self.grid[horiz][0] + self.grid[horiz][1] + self.grid[horiz][2]
            if horiz[0] == horiz[1] == horiz[2] == player:
                self.haveWinner = True
                return True

        return False


def playerTurn(grid):
    grid.printGrid()
    if grid.setPos('X', False):
        grid.winner = 'X'


def cpuTurn(grid):
    grid.printGrid()
    if( grid.setPos('O', True)):
        grid.winner = 'O'
    time.sleep(1)

def playAgain():
    os.system('cls')
    print("                    ...;;;;;;;;;;;;;;;;;;;;;;;;;;;...")
    print("                 ,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.")
    print("               .;;;;;;;|;;;|;;|;;;;;;|;;|;;;|;;;|;;;;;:;;;")
    print("             .;;:::::::::|:::|::||::::::::::::::::::; ;;;;`;")
    print("           ;;;:::::::|:|:::|::|:||::|::|::||::|::::;   ;::::`;")
    print("          ;::::::::::::::|:::|::||::::|:|::::|::::,' .;;;;;;;;;")
    print("         ;;:::::::::`:|:::::::::'`;;;;;;;;;;;;;'     :;;;);;;;;;")
    print("        ;;;::::(:::;  ``````````  ''''''''''''        :;;;(;;;;;")
    print("       ;;;::::):;;'                                   ``.;;);;;;;")
    print("      ;;;:::(::;                                        `;;;(;;;;;")
    print("     ;;;::::::; %          .             .               :;;;;;;;;")
    print("    _;;;;;;);;  %%,          .    .   .                  :;;;;;;;;")
    print("    \;;;;;;;;' %%%%   :::                                 :;);;;;")
    print("     \;;;;(;: %%%  '   :::   ,         \"                  :(;;;;;")
    print("    _  \;;;|             ::  x. |  |,'                    :;);;;  _")
    print("    )\  \;;:    `%##%#%       Xx :  #%        %####%.,,    :;;;  /(")
    print("    \ (_ \;|        ;###%.   XX    :##%.     ,##.   \"      |;; _) /")
    print("     \  \_::`  _   .%########:;  ;  `###########h.,- _   ,  :_/  /")
    print("      \  ]|:: = XX%x < (_)  )``""   \`%( (_)  >      _ =    |[  /")
    print("       :  |::. ~  %   `----'x#|      ; %`----'        ~     |  :")
    print("       :  |:::     %        X#:      `  xXx                 |  :")
    print("      |   |:::      `xxxxd'  #|         ` `dxxxxx\"          |  |")
    print("      |   |::'              x#|                             |  |")
    print("      |   |::.           __ X#:      ;::::;;;;              |` |")
    print("       \_ |::::.       ,;;;;x#|       \"\"\"\ ;;;              |_/")
    print("         \_:::::      .;;(CCc%:           |;;;::::::::;""  |/")
    print("           :%:::......;' `CCc`-.        ,-'  `:::::::'     :")
    print("           `%%%%::~~~~         `.    _,'       ~~~~~ ;;    ;")
    print("            `;%;:'               `--'            .   ))   ,'")
    print("             `;;' ::::'_    ______\"\"______    _,%;  ;:'  ,'")
    print("         _____`,  :::  )`--'\    /`' \    `--'( `;  '   ,____")
    print("      __/######`,  `:   \----\  /-----\  /---/   `     ,'####\\")
    print("     /##########`,   `   `--._\/_______\/,--'        ,'#######\\")
    print("   _/############`-.__        , ~~~~~~`         __,-'#####x####\\")
    print("  /#########x#########`-._             `    _,-'|##########x####\\")
    print(" /#########x#########/|@@@`-._     ^     _,'@@|n|###########x#####\\")
    print("/#########x#########/ |@@@@@@@`----'`---'@@@@@@|n|###########x####/")
    print("\##########x#######|n |@@@@@@@@@|aaaaa|@@@@@@@@|nN|#########x####/")
    print("  \#########x######|nN |@@@@@@@@|aaaaa|@@@@@@@@|nNn|#######x####/")
    print("     \#######x#####|nN |@@@@@@@@|aaaaa|@@@@@@@@|nNn|#####x####/")
    print("      \###########|nNNn|@@@@/~~~`aaaaa'~~~\@@@@|nNn|########/")
    print("          \#######|nNNN ~~~~+++++~~~~~ +++ ~~~~~nNNn|####/")
    print("         _/#######|nNNNN|a`.++++++++++++++,'aa|NNNNn|####\_")
    print("      __/########|nNNNNN|aaa\_++++++++++_/aaaa|NNNNn|######\__")
    print("     /###########|nNNNNN|aaaaa\_++++++_/aaaaaa|NNNNNn|########\__")
    print("   _/###########|nNNNNNNN|aaaaaaa\__/aaaaaaaa|NNNNNNn|###########\_")
    print("  /#############|nNNNNNNN|aaaaaaaa 0 aaaaaaaa|NNNNNNn|#############")
    print(" ###############|nNNNNNNN|aaaaaaaa o aaaaaaaa|NNNNNNn|#############")
    print(" ##############|nNNNNNNNN|aaaaa __/_\__ aaaaa|NNNNNNNn|############")
    print(" ##############|nNNNNNNNN|aaaa o (( )) `o aaa|NNNNNNNn|############")
    print(" #############|nNNNNNNNNN|aaaaa `-.~ .-' aaaa|NNNNNNNnN|###########)")
    ui = input("Would you like to play again?(Y/N) -> ")
    if(ui == "y" or ui == "Y"):
        return True
    else:
        return False

def mainGame():
    playGrid = Grid()
    playGrid.printGrid()
    coinChoice = str(input("Choose heads or tails (h/t): "))
    coin = random.randint(0, 1)
    pFirst = False
    if coin == 0:
        if coinChoice == "h":
            print("Heads! You get to go first.")
            pFirst = True
        elif coinChoice == "t":
            print("Heads! The computer goes first.")
    elif coin == 1:
        if coinChoice == "h":
            print("Tails! The computer goes first.")
        elif coinChoice == "t":
            print("Tails! You get to go first.")
            pFirst = True
    time.sleep(2)
    while not playGrid.haveWinner:
        if pFirst:
            playerTurn(playGrid)
            if not playGrid.haveWinner:
                cpuTurn(playGrid)
        else:
            cpuTurn(playGrid)
            if not playGrid.haveWinner:
                playerTurn(playGrid)
    playGrid.printGrid()

    if playGrid.winner == 'X':
        print("You have defeated the cpu! Congratulations!")
    else:
        print("You have been defeated by the cpu!")
    time.sleep(2)

mainGame()

while playAgain():
    mainGame()
