from playsound import playsound

class AudioPlayer():
    def __init__(self, file_path=None):
        self.file_path = file_path

    def play(self):
        if self.file_path is not None:
            playsound(self.file_path)

    def pause(self):
        pass

    def stop(self):
        pass

    def set_file_path(self, file_path):
        self.file_path = file_path
