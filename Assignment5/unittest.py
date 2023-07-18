import unittest
from APC_Task5 import User, admin, instructor, student

class testUser(unittest.TestCase):

    def test_addcourse(self):
        newtoni = student('Isaac', 'Newton', 10001)
        newtoni.addcourse(34285)
        self.assertEqual(newtoni.getschedule(), 34285)


if __name__ == '__main__':
    unittest.main()
