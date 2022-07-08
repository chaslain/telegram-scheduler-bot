import unittest
import os
import FileCandidateManager

class TestWeekdayPicker(unittest.TestCase):

    def testWeekday(self):
        weekday = 0
        fcm = FileCandidateManager.FileCandidateManager("weekday_file_test_data/data")
        file = fcm.getCandidateFileName(weekday)
        assert(os.path.exists(file))


        