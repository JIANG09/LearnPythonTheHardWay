class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

twinkle_star = Song(["Twinkle twinkle little star",
                     "满天都是小星星"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

twinkle_star.sing_me_a_song()

blow_wind_song = ['how many roads must a man walk down',
                  'before they call him a man',
                  'how many seas must a white dove sail',
                  'before she sleeps in the sand',
                  'how many times must the cannon calls fly',
                  'before they\'re forever banned',
                  'the answer my friend is blowing in the wind']

blow_wind = Song(blow_wind_song)
blow_wind.sing_me_a_song()
