class Song:
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            #This line increments the value associated with the artist key by 1.
            #  This is because we've encountered another song by the same artist, 
            # so we want to increase the count.
            cls.artist_count[artist] += 1
        else:
            #This line creates a new entry 
            # in the cls.artist_count dictionary with the artist
            #  as the key and sets the count to 1. 
            # This is the first song we've encountered by this artist, so the count starts at 1.
            cls.artist_count[artist] = 1


