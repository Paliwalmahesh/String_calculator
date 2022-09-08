import unittest
import String_sum


class TestStringSum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(String_sum.str_opration(""), 0)

    def test_first(self):
        self.assertEqual(String_sum.str_opration("1"), 1)
        self.assertEqual(String_sum.str_opration("1,2"), 3)

    def test_bigger_1000(self):
        self.assertEqual(String_sum.str_opration("1,2000,1"), 2)
        self.assertEqual(String_sum.str_opration("1,2002,5,20"), 26)

    def test_negative(self):
        stri = "Negatives not allowed : -1 -3"
        self.assertEqual(String_sum.str_opration("//[***]\n-1***2***-3"), stri)
        stri = "Negatives not allowed : -1 "
        self.assertEqual(String_sum.str_opration("//[***]\n-1***2***3"), stri)

    def test_alphabet(self):
        self.assertEqual(String_sum.str_opration("1,2,a,c"), 7)
        self.assertEqual(String_sum.str_opration("1,2,a,c,d"), 11)

    def test_delimiter(self):
        self.assertEqual(String_sum.str_opration("//;\n1;2,"), 3)

    def test_line_space(self):
        self.assertEqual(String_sum.str_opration("1\n2,3"), 6)
    

    def test_multiplication_first(self):
        self.assertEqual(String_sum.str_opration("*1"), 1)
        self.assertEqual(String_sum.str_opration("*1,2"), 2)
    
    def test_multiplication_bigger_1000(self):
        self.assertEqual(String_sum.str_opration("*1,2000,1"), 1)
        self.assertEqual(String_sum.str_opration("*1,2002,5,20"), 100)

    def test_multiplication_alphabet(self):
        self.assertEqual(String_sum.str_opration("*1,2,a,c"), 6)
        self.assertEqual(String_sum.str_opration("*1,2,a,c,d"), 24)

    def test_multiplication_delimiter(self):
        self.assertEqual(String_sum.str_opration("*//;\n1;2,"), 2)

    def test_multiplication_line_space(self):
        self.assertEqual(String_sum.str_opration("*1\n2,3,2"), 12)

    def test_multiplication_negative(self):
        stri = "Negatives not allowed : -1 -3"
        self.assertEqual(String_sum.str_opration("*//[***]\n-1***2***-3"), stri)
        stri = "Negatives not allowed : -1 "
        self.assertEqual(String_sum.str_opration("*//[***]\n-1***2***3"), stri)

    


if __name__ == '__main__':
    unittest.main()
