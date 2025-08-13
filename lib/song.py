class Song:
    # Class attributes to store global info
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update counters and lists whenever a song is created
        Song.count += 1

        Song.artists.append(artist)
        Song.genres.append(genre)

        # Update genre_count dictionary
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count dictionary
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_artists(cls):
        return list(set(cls.artists))  # unique artists

    @classmethod
    def get_genres(cls):
        return list(set(cls.genres))  # unique genres

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count

