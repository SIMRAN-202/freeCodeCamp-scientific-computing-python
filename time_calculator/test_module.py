import unittest
from main import add_time

class TestAddTime(unittest.TestCase):
    def test_no_day_change(self):
        self.assertEqual(add_time("3:30 PM", "2:12"), "5:42 PM")

    def test_am_to_pm_transition(self):
        self.assertEqual(add_time("11:55 AM", "3:12"), "3:07 PM")

    def test_next_day(self):
        self.assertEqual(add_time("11:59 PM", "24:05"), "12:04 AM (2 days later)")

    def test_next_day_with_weekday(self):
        self.assertEqual(add_time("11:59 PM", "24:05", "Wednesday"), "12:04 AM, Friday (2 days later)")

    def test_large_duration(self):
        self.assertEqual(add_time("8:16 PM", "466:02"), "6:18 AM (20 days later)")

    def test_large_duration_with_weekday(self):
        self.assertEqual(add_time("8:16 PM", "466:02", "Tuesday"), "6:18 AM, Monday (20 days later)")

    def test_no_duration(self):
        self.assertEqual(add_time("8:16 PM", "0:00"), "8:16 PM")

    def test_weekday_capitalization(self):
        self.assertEqual(add_time("2:59 AM", "24:00", "saturDay"), "2:59 AM, Sunday (next day)")

    def test_12_hour_format(self):
        self.assertEqual(add_time("12:00 PM", "0:00"), "12:00 PM")

if __name__ == "__main__":
    unittest.main()
