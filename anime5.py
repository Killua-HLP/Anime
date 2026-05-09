class Anime:
    def __init__(self, name, genre, rate):
        self.name = name
        self.genre = genre
        self.rate = rate

    def love(self):
        print(f"Name: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rate}")
        print("-" * 20)

    def update_rating(self, new_rate):
        self.rate = new_rate
        nr = (f"#Updated {self.name}'s Rating is changed to {self.rate}/5.0 ")
        print("=" * 30)
        print(nr)
        print("=" * 30)

    def masterpiece(self):
        if self.rate >= 4.9:
            print(f"{self.name} is a MASTERPIECE ANIME!!")
            print("_" * 20)
        else:
            print(f"{self.name} is a GREAT ANIME!!")
            print("_" * 20)

class Movie(Anime):
    def __init__(self, name, genre, rate, duration):
        super().__init__(name, genre, rate)
        self.duration = duration

def save_data(my_list):
    with open("anime2_db.txt", "w") as file:
        for anime in my_list:
            if isinstance(anime, Movie):
                file.write(f"Movie,{anime.name},{anime.genre},{anime.rate},{anime.duration}\n")
            else:
                file.write(f"Anime,{anime.name},{anime.genre},{anime.rate}\n")
    print("___Database Saved Successfully___")

def load_data():
    loaded_items = []
    try:
        with open("anime2_db.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                type_tag = data[0]

                if type_tag == "Movie":
                    new_obj = Movie(data[1], data[2], float(data[3]), data[4])
                else:
                    new_obj = Anime(data[1], data[2], float(data[3]))

                loaded_items.append(new_obj)
                
    except FileNotFoundError:
        print("No saved file found! starting fresh! ")
    return loaded_items

my_list = load_data()

while True:
    print("==========MAIN MENU===========")
    print("1 => Add the new Anime ")
    print("2 => Change the Rating ")
    print("3 => Show My List And MASTERPIECES ")
    print("4 => Save & Exit ")

    menu = input("What would you like to do (1-4): ")

    if menu == "1":
        choice = input("Add (a)anime, (m)ovie or (b) to back to menu: ").lower()
        if choice == "b":
            continue

        name = input("Name: ")
        genre = input("Genre: ")
        
        try:
            rate = float(input("Rating: "))
        except ValueError:
            print("Pls Enter a number!")
            continue

        if choice == "m":
            duration = input("Duration: ")
            my_list.append(Movie(name, genre, rate, duration))
        elif choice == "a":
            my_list.append(Anime(name, genre, rate))
        else:
            print("Invalid Choice")

    elif menu == "2":
        if not my_list:
            print("No anime/movies yet! Add some first.")
            continue
        
        for anime in my_list:
            c = input(f"Change rating for {anime.name}? (y/n): ").lower()
            if c == "y":
                try:
                    new_rate = float(input(f"Enter the new rate of {anime.name}: "))
                    anime.update_rating(new_rate)
                except ValueError:
                    print("Please enter a valid number!")

    elif menu == "3":
        if not my_list:
            print("No anime/movies yet!")
        else:
            for anime in my_list:
                anime.love()
                anime.masterpiece()

    elif menu == "4":
        save_data(my_list)
        print("Everything is saved! See u next time.")
        break

    else:
        print("Invalid choice! Please pick 1, 2, 3 or 4.")

save_data(my_list)