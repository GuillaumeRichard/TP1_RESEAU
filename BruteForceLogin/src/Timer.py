from time import time


class Timer:

    start_time = ""
    end_time = ""

    def start(self):
        self.start_time = time()

    def get_minutes_elapsed(self):
        self.end_time = time()
        hours, rem = divmod(self.end_time - self.start_time, 3600)
        minutes, seconds = divmod(rem, 60)
        return "{:0}".format(int(minutes))
