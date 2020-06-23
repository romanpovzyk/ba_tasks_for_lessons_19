import unittest
import task_1


class DogTest(unittest.TestCase):
    def human_age_of_dog(self):
        years = task_1.human_age()
        self.assertEqual(years, 35)
        self.assertNotEqual(years, 42)


unittest.main()