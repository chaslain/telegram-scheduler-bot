import unittest
import os
import bot.FileCandidateManager

class TestWeekdayPicker(unittest.TestCase):

    def testWeekday(self):
        weekday = 0
        fcm = bot.FileCandidateManager.FileCandidateManager("test/weekday_file_test_data/data")
        file = fcm.getCandidateFileName(weekday)
        assert(os.path.exists(file))


        