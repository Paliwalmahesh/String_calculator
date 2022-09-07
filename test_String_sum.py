import unittest
import String_sum
class TestString_sum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(String_sum.StrSum(""),0)
        

if __name__ == '__main__':
    unittest.main()
