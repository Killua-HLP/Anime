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
        new_rate = (f"#Updated {self.name}'s Rating is changed to {self.rate}/5.0 ")
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
    with open("anime1_db.txt", "w")as file:
        for anime in my_list:
            if isinstance(Anime,Movie):
                file.write(f"Movie, {anime.name}, {anime.genre}, {anime.rate}, {anime.duration}\n")
            else:
                file.write(f"Anime, {anime.name}, {anime.genre}, {anime.rate}\n")
                print("___Database Saved Successfully___")

my_list =[]

while True:
    choice = input("Do u wanna add new (a)nime or (m)ovie? type (n) to quit: ")
    if choice == "n":
        break
    if choice not in ["a", "m" or "n"]:
        print("Invalid input! Please input the (a),(m) or (n) to quit:")
        continue

    name = input("Name: ")
    genre = input("Genre: ")
    rate =float(input("Rating: "))

    if choice == "m":
        duration = input("Duration (mins): ")
        my_list.append(Movie(name, genre, rate, duration))

    else:
        my_list.append(Anime(name, genre, rate))

for anime in my_list:
    anime.love()

for anime in my_list:
    c = input(f"Do u wanna change the rating? y/n: ")
    if c == "n":
        break
    else:
        new_rate = float(input(f"Enter the new rate of {anime.name}: "))
        anime.update_rating(new_rate)

for anime in my_list:
    anime.masterpiece()

save_data(my_list)