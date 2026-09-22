import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):

    def test_initial_values(self):
        fine = DuckFine("M001")

        self.assertEqual(fine.member_id, "M001")
        self.assertEqual(fine.total_owed, 0.0)

    def test_grace_period(self):
        fine = DuckFine("M001")

        self.assertEqual(fine.charge(2), 0.0)
        self.assertEqual(fine.total_owed, 0.0)

    def test_regular_charge(self):
        fine = DuckFine("M001")

        self.assertEqual(fine.charge(5), 1.50)
        self.assertEqual(fine.total_owed, 1.50)

    def test_deluxe_charge(self):
        fine = DuckFine("M001")

        self.assertEqual(fine.charge(5, deluxe=True), 3.00)
        self.assertEqual(fine.total_owed, 3.00)

    def test_maximum_fee(self):
        fine = DuckFine("M001")

        self.assertEqual(fine.charge(20), 5.00)
        self.assertEqual(fine.total_owed, 5.00)

    def test_negative_days_raise_error(self):
        fine = DuckFine("M001")

        with self.assertRaises(ValueError):
            fine.charge(-1)

    def test_total_owed_accumulates(self):
        fine = DuckFine("M001")

        fine.charge(3)
        fine.charge(4)

        self.assertEqual(fine.total_owed, 1.50)


if __name__ == "__main__":
    unittest.main()