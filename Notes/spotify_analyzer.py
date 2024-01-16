# Spotify Data Analyzer
# Author: Roop Jaswal
# 16 January 2024

# Version 0.1
#   - From the data set, get all the songs
#     performed my Drake

import csv

def find_all_songs(artist: str) -> list:
    """Returns a list of all songs from a given artist"""
# Open up the file
with open("./spotify.csv") as f:
    # ---- Look for all songs performed by Drake
    #      Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    songs = []

    # for every song in the .csv file
    for line in csv_reader:
        # if this song is sung by Drake
        if artist.lower() in line["artist"]:

        # add it to the Drake's songs list
            songs.append((line["artist"], line["song_title"], line["danceability"]))
            
            for song in songs:
                if float (song[-1]) >= 0.6: 
                    print(song)