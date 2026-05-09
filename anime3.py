class Anime:
    def __init__(self,name,genre,rate):
        self.name = name
        self.genre = genre
        self.rate = rate

    def love(self):
        print(f"Name : {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Rating : {self.rate}")
        print("-" * 20)

    def update_rating(self,new_rate):
        self.rate = new_rate
        print(f"#Updated {self.name}'s rating is {self.rate}/5.0 ")
        print("=" * 30)

    def masterpiece(self):
        if self.rate >= 4.9:
            print(f"{self.name} is a MASTERPIECE!!")
            print("-" * 20)
        else:
            print(f"{self.name} is also a GREAT Anime!")
            print("-" * 20)

class Movie(Anime):
    def __init__(self,name,genre,rate,duration):
        super().__init__(name,genre,rate)
        self.duration = duration

my_list =[]

while True:
    choice = input("Add new (a)nime or (m)ovie. type (n) to quit: ")
    if choice == "n":
        break
    if choice not in ["a","m"]:
        print("Invalid input!!. Please Type (a),(m) or (n) to quit!")
        continue

    name = input("Name: ")
    genre = input("Genre: ")
    rate = float(input("Rating: "))

    if choice == "m":
        duration = input("Duration (mins): ")
        my_list.append(Movie(name,genre,rate,duration))
    else:
        my_list.append(Anime(name,genre,rate))

for anime in my_list:
    anime.love()

for anime in my_list:
    c = input("Do u wanna change to new rating? y/n: ")
    if c != "y":
        continue
    else:
        new_rate = float(input(f"Enter the new rating of {anime.name}: "))
        anime.update_rating(new_rate)

for anime in my_list:
    anime.masterpiece()