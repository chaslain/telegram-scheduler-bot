

import math
import os
from random import random


class FileCandidateManager:
    def __init__(self, directory) -> None:
        self.directory = directory
    
    def getCandidateFileName(self, weekday: int):
        directory = FileCandidateManager.getWeekdayDirectory(weekday)

        files = os.listdir(self.directory + "/" + directory)

        if len(files) == 0:
            return None
        item = math.floor(random() * len(files))
        return self.directory + '/' + directory + '/' + files[item]

    def getWeekdayDirectory(weekday: int) -> str:
        map = {
            0: "monday",
            1: "tuesday",
            2: "wednesday",
            3: "thursday",
            4: "friday",
            5: "saturday",
            6: "sunday"
        }

        return map[weekday]