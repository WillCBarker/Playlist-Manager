d = {}
pdict = {}

def main ():
    print("Please select an option\n")
    menu = "1. Create Playlist\n2. Delete Playlist\n3. Select Playlist\n4. Display Playlists\n5. Quit\n"
    maininput = int(input(menu))
    if maininput == 1:
        playlist_name = input("Enter a playlist name: ")
        create_playlist(playlist_name)
    elif maininput == 2:
        playlist_name = input("Enter playlist name to delete: ")
        delete_playlist(playlist_name)
    elif maininput == 3:
        playlist_name = input("Enter playlist name to select: ")
        select_playlist(playlist_name)
    elif maininput == 4:
        print("All current playlists: ")
        display_playlists()
    elif maininput == 5:
        print("Exiting Program...")
        quit

def create_dict():
    f = open("Playlists.txt", "r")
    temp = f.readlines()
    f.close()
    if len(temp) > 0: 
        for line in temp:
            strippedline = line[:-5]
            d[strippedline] = line[:-1]
            pdict[strippedline] = []
            for i in d.values():
                f = open(i, "r")
                collection = f.readlines()
                for line in collection:
                    song, artist = line.split(" by ")
                    pdict[strippedline].append(song + " by " + artist)
                f.close()



    
def create_playlist(playlist_name):
    if playlist_name in d.keys():
        print("Playlist already exists, returning to menu")
        main()
    d[playlist_name] = str(playlist_name) + ".txt"
    f = open(d[playlist_name], "w")
    f.close()
    f = open("Playlists.txt", "a")
    f.write(d[playlist_name] + "\n")
    f.close()
    pdict[playlist_name] = []
    print("Playlist created, returning to menu...")
    main()

def delete_playlist(playlist_name):
    if playlist_name in d.keys():
        del d[playlist_name]
        del pdict[playlist_name]
        f = open("Playlists.txt", "w")    
        for line in d.values():
            f.write(line + "\n")        
        f.close()
        print("Playlist deleted, returning to menu")
    else:
        print("Playlist doesn't exist, returning to menu")
    main()

def select_playlist(playlist_name):
    if playlist_name in d.keys():
        print("What would you like to do?")
        selectinput = int(input("1. Add Song\n2. Delete Song\n3. Playlist Details\n4. Return to menu\n"))
        if selectinput == 1:
            add_song(playlist_name)
        elif selectinput == 2:
            delete_song(playlist_name)        
        elif selectinput == 3:
            playlist_details(playlist_name)               
        elif selectinput == 4:
            print("Returning to menu...")
            main()
    else:
        print("Playlist does not exist, returning to menu...")
        main()

def add_song(playlist_name):
    f = open(d[playlist_name], "a")
    song = input("Enter song to add: ")
    artist = input("Enter the artist of the song: ")
    f.write(song + " by " + artist + "\n")
    pdict[playlist_name].append(song + " by " + artist)
    f.close()
    select_playlist(playlist_name)

def delete_song(playlist_name):
    song = input("Enter song to delete: ")
    artist = input("Enter artist of song to delete")
    title = song + " by " + artist
    if title in pdict[playlist_name]:
        f = open(d[playlist_name], "r")
        readplaylist = f.readlines()
        f.close()
        f = open(d[playlist_name], "w")    
        for item in pdict[playlist_name]:
            if item == title:
                pdict[playlist_name].remove(item)
        for line in pdict[playlist_name]:
            f.write(line)        
        f.close()
        select_playlist(playlist_name)
    else:
        print("Song is not in playlist, returning to select playlist menu... \n")
        select_playlist(playlist_name)

def playlist_details(playlist_name):
    f = open(d[playlist_name], "r")
    playlist = f.readlines()
    print("Playlist name: ", playlist_name, "\n")
    print("Playlist songs: \n")
    for item in playlist:
         print(item)
    f.close()
    select_playlist(playlist_name)
    
def display_playlists():
    for playlist in pdict.keys():
        print(playlist)
    print("\nReturning to menu...")
    main()
    
create_dict()
main()
