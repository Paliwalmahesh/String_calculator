import unittest
import String_sum
class TestString_sum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(String_sum.StrSum(""),0)
    def test_first(self):
        self.assertEqual(String_sum.StrSum("1"),1)
        self.assertEqual(String_sum.StrSum("1,2"),3)
    def test_Bigger_1000(self):
        self.assertEqual(String_sum.StrSum("1,2000,1"),2)
    def test_Negative(self):
        stri="Negatives not allowed : -1 -3"
        self.assertEqual(String_sum.StrSum("//[***]\n-1***2***-3"),stri)
        stri="Negatives not allowed : -1 "
        self.assertEqual(String_sum.StrSum("//[***]\n-1***2***3"),stri)
        

if __name__ == '__main__':
    unittest.main()
