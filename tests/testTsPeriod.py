import unittest

from models import TsPeriod, Frequency
from datetime import date


class TestTsPeriod(unittest.TestCase):
    def test_to_date(self):
        self.assertEqual(date(2022, 1, 1),
                         TsPeriod(year=2022, position=0, frequency=Frequency.MONTHLY).to_date())

    def test_to_date_3rd_position(self):
        self.assertEqual(date(2022, 4, 1),
                         TsPeriod(year=2022, position=3, frequency=Frequency.MONTHLY).to_date())

    def test_to_date_quarterly(self):
        self.assertEqual(date(2023, 4, 1),
                         TsPeriod(year=2022, position=5, frequency=Frequency.QUARTERLY).to_date())