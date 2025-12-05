class Song:
    # Class attributes to track all songs, artists, and genres
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level counts
        Song.count += 1

        # Add genre if not already present
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Add artist if not already present
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Count the number of songs per genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Count the number of songs per artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    def __str__(self):
        return f"{self.name} by {self.artist} ({self.genre})"
