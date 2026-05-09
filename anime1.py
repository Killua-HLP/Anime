class Anime:

    def __init__(self,name,genre,rate):
        self.name = name
        self.genre = genre
        self.rate = rate

    def update_rating(self,new_rate):
        self.rate = new_rate
        print(f"Updated {self.name} has now the rating of {self.rate}/5.0")

    def love(self):
        print(f"{self.name} ,{self.genre} is a pouplar Anime on world wide!!")
        print(f"It has the rating of {self.rate}/5.0 and absolute fire!!")

re_zero = Anime("Re:Zero", "Isekai, Dark Fantasy, Psychology", 4.9)
mahiru = Anime("Otonari no Tenshi sama", "Romance, School Live, Icha Icha",4.8)

re_zero.love()
mahiru.love()

re_zero.update_rating(4.7)