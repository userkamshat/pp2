import pygame
import os


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        self.music_folder = "music"

        self.songs = [
            "track1.mp3",
            "track2.mp3",
            "track3.mp3"
        ]

        self.current_song = 0
        self.is_playing = False

    def play(self):
        path = os.path.join(self.music_folder, self.songs[self.current_song])
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_song(self):
        self.current_song += 1

        if self.current_song >= len(self.songs):
            self.current_song = 0

        self.play()

    def previous_song(self):
        self.current_song -= 1

        if self.current_song < 0:
            self.current_song = len(self.songs) - 1

        self.play()

    def get_song_name(self):
        return self.songs[self.current_song]

    def get_position(self):
        return pygame.mixer.music.get_pos() // 1000