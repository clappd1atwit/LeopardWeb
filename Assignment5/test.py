import unittest
import re
from APC_Task5 import *

class testUser(unittest.TestCase):

    #Adam
    def test_addcourse(self):
        newtoni = student('Isaac', 'Newton', 10001)
        newtoni.addcourse(34285)
        self.assertEqual(int(re.sub('\W', '', newtoni.getschedule())), 34285)
       
    #Adam 
    def test_removecourse(self):
        newtoni = student('Isaac', 'Newton', 10001)
        newtoni.addcourse(34285)
        newtoni.removecourse('34285')
        self.assertEqual(str(re.sub('\W', '', str(newtoni.getschedule()))), 'None')
       
    #Liam 
    def test_printroster(self):
        nelsonp = instructor('Nelson', 'Patrick', 20002)
        self.assertEqual(str(nelsonp.getcourselist()), '[]')
    
    #Dan    
    def test_addcourseadmin(self):
        hamiltonm = admin('Margaret', 'Hamilton', 30001)
        hamiltonm.addcourse(12345, 'test', 'test', 'test', 'test', 'test', 2023, 4, 'test')
        cur.execute("""SELECT CRN FROM Course WHERE CRN = '%d'""" % 12345)
        query_result = cur.fetchone()
        self.assertEqual(str(query_result[0]), '12345')
       
    #Dan    
    def test_removecourseadmin(self):
        hamiltonm = admin('Margaret', 'Hamilton', 30001)
        hamiltonm.removecourse(12345)
        cur.execute("""SELECT CRN FROM Course WHERE CRN = '%d'""" % 12345)
        query_result = cur.fetchone()
        self.assertEqual(str(query_result), 'None')

    #Liam
    def test_login(self):
        self.assertEqual(login('newtoni'), 'Student')
    
    # There is no logout function to test, currently the loop just ends

    #Dan
    def test_searchall(self):
        user1 = student('test', 'test', 1)
        result = user1.searchall()
        self.assertEqual(str(result), "(34285, 'Advanced Digital', 'BSCO', '12:30', 'MF', 'Summer', 2023, 4, 'Pilin')")
    

if __name__ == '__main__':
    unittest.main()
