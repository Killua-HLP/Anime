class Anime:

    def __init__(self,name,genre,rate):
        self.name = name
        self.genre = genre
        self.rate = rate

    def update_rating(self,new_rate):
        print(f"[System Has Been Updated!]")
        self.rate = new_rate
        print(f"{self.name}'s rating is change to {self.rate}/5.0")
        print("=" * 30)

    def love(self):
        print(f"Name: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rate}")
        print("-" * 20)

rezero = Anime("Re:Zero","Isekai, Dark Fantasy, Psychology", 4.8)
mahiru = Anime("Otonari no Tenshi sama", "Romance, School Live, Icha Icha", 4.8)

rezero.love()
mahiru.love()

rezero.update_rating(4.7)

