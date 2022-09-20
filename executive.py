from boardgame import BoardGame

class Executive:
    def __init__(self, file_name):
        with open(file_name, 'r') as f: lines = f.readlines()
        self.gamelist = []
        for line in lines:
            items = line.split()
            self.gamelist.append(BoardGame(items))

    def run(self):
        self.print_menu()
        print("\n")
        choice = input("Enter a choice: ")
        if choice == '1': self.gibbons_rating()
        elif choice == '2': self.print_by_year()
        elif choice == '3': self.time_for_game()
        elif choice == '4': self.ppl_vs_gibbons()
        elif choice == '5': self.printrank()
        elif choice == '6': self.exitprogram()
        else: print("You entered an invalid choice")



    def print_menu(self):
        print('-' * 60)
        print("1. Print all games from highest Gbbons rating to lowest")
        print("2. Print all games from a year")
        print("3. Time for a game?")
        print("4. The People VS Dr. Gibbons")
        print("5. Print based on ranking")
        print("6. Exit the program")

    def gibbons_rating(self):
        gamelist2 = self.gamelist.copy()
        gamelist2.sort(reverse=True, key = lambda game: game.gib_rating)
        for game in gamelist2: print(game)

    def print_by_year(self):
        year = int(input("Enter the year: "))
        games = [game for game in self.gamelist if game.year == year]
        if len(games) > 0:
            print("\n")
            games.sort(reverse=True, key = lambda game: game.year)
            for game in games: print(game)
        else:
            print("\n")
            print("No games found")

    def time_for_game(self):
        time = int(input("How many minutes do you have to play a game? "))
        games = [game for game in self.gamelist if time >= game.maxplaytime]
        if len(games) > 0:
            games.sort(reverse=True, key = lambda game: game.maxplaytime)
            for game in games: print(game)
        else:
            print("There are no games for you")

    def ppl_vs_gibbons(self):
        user_num = float(input("Enter rating number difference: "))
        games = [game for game in self.gamelist if abs(game.gib_rating - game.ppl_rating) >= (user_num)]
        if len(games) > 0:
            for game in games: print(game)
        else:
            print("No games have that rating difference")


    def printrank(self):
        user_rank = float(input("Enter a ranking: "))
        games = [game for game in self.gamelist if user_rank <= game.gib_rating]
        if len(games) > 0:
            games.sort(reverse = True, key = lambda game: game.gib_rating)
            for game in games: print(game)
        else:
            print("No games have that ranking or higher")

    def exitprogram(self):
        quit()