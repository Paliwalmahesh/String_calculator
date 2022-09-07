import unittest
import String_sum
class TestString_sum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(String_sum.StrSum(""),0)
    def test_first(self):
        self.assertEqual(String_sum.StrSum("1"),1)
        self.assertEqual(String_sum.StrSum("1,2"),3) 
        

if __name__ == '__main__':
    unittest.main()
