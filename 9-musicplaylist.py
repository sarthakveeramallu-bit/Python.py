class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready.")

    def add_song(self, song):
        self.songs.append(song)
        print(f" '{song}' added to'{self.name}'")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f" '{song}' removed.")

        else:
            print(f" '{song}' not found in the playlist.")

    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")

            else:
                print("No songs yet. Add some songs")

    def _del__(self):
        print(f"Playlist '{self.name}' has been deleted. Good bye!")

My_playlist = Playlist("Road Trip Mix", "Pop")
while True:
    print("\n1. Add Song 2. Remove Song 3. View Playlist 4. Delete")
    choice = input("Enter your choice: ")
    if choice == "1":
        song = input("Enter the song name: ")
        My_playlist.add_song(song)

    elif choice == "2":
        song = input("Enter the song name: ")
        My_playlist.remove_song(song)

    elif choice == "3":
        My_playlist.display()

    elif choice == "4":
        My_playlist._del__()
        break

    else:
        print("Invalid choice. Please enter 1,2,3, or 4.")
