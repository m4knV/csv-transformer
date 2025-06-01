import unittest

from transformers.convert_timestamp import convert_timestamp


class TestConvertTimestamp(unittest.TestCase):
    def test_convert_full_datetime_with_timezone(self):
        timestamp = "2023-10-01 12:00:00 UTC"
        self.assertEqual(convert_timestamp(timestamp), "2023-10-01")

    def test_convert_full_datetime_without_timezone(self):
        timestamp = "2023-10-01 12:00:00"
        self.assertEqual(convert_timestamp(timestamp), "2023-10-01")

    def test_convert_year_month_day(self):
        timestamp = "2023-Oct-01"
        self.assertEqual(convert_timestamp(timestamp), "2023-10-01")

    def test_invalid_format(self):
        timestamp = "01-10-2023"
        self.assertEqual(convert_timestamp(timestamp), "2023-01-10")


if __name__ == "__main__":
    unittest.main()
