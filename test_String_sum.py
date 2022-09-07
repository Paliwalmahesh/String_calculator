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
    def test_alphabet(self):
        self.assertEqual(String_sum.StrSum("1,2,a,c"),7)
        self.assertEqual(String_sum.StrSum("1,2,a,c,d"),11) 
    def test_delimiter(self):
        self.assertEqual(String_sum.StrSum("//;\n1;2,"),3) 
    def test_line_space(self):
        self.assertEqual(String_sum.StrSum("1\n2,3"),6)
        

if __name__ == '__main__':
    unittest.main()
