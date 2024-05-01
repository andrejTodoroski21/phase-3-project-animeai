from . import CONN, CURSOR
from lib.models import Recommondations
class App:

    def __init__(self):
        self.user_input = ""
        DadJoke.create_table()

    def run(self):
        print("Hello and welcome to AnimeAi")

    def main_menu(self):
        print("MAIN MENU")
        print("1. Want anime recommondation?")
        print("2. Talk to me about anime?")
        print("3. My favorite animes")
        print("4. Exit program")

        while self.user_input not in ["1","2","3","4"]:
            self.user_input = input(">>> ")
            if self.user_input not in ["1","2","3"]:
                print("Invalid option please choose a better one")
            if self.user_input == "1":
                self.see_dad_jokes()
            if self.user_input == "2":
                self.add_dad_joke()
            if self.user_input == "3":
                self.delete_dad_joke
            if self.user_input == "4":
                self.exit_program()

    def anime_recommondations(self):
        all_animes = Recommondations.read_all()
        for anime in all_animes:
            print(f"\n {anime0},{anime[1]}")
        self.user_input = ''


    def add_dad_joke(self):
        print("Add a new dad joke")
        self.user_input = input(">>> ")
        new_joke = DadJoke(content=self.user_input)
        new_joke.create()
        print("your joke has been added! returnung you back to the menu...")


    def delete_dad_joke(self):
        all_jokes = DadJoke.read()
        print("choose which joke to delete by id")
        while self.user_input not in [str(j[0]) for j in all_jokes]:
            print('Invalid id')
            self.user_input = input(">>> ")
        DadJoke.delete_by_id(self.user_input)
        print("dad joke deleted")
        self.user_input = ''


    def exit_program(self):
        print("see you later!")