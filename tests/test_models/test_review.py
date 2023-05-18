#!/usr/bin/python3
import unittest
import models.review import Review


class TestBase(unittest.TestCase):
    def test_initialization(delf):
        review = Review()
        self.assertEqual(
            str(type(review)), "<class 'models.review.Review'>")
        self.assertEqual(review.text, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")


    if __name__ == "__main__":
        unittest.main()
