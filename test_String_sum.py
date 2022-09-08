import unittest
import String_sum


class TestString_sum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(String_sum.str_opration(""), 0)

    def test_first(self):
        self.assertEqual(String_sum.str_opration("1"), 1)
        self.assertEqual(String_sum.str_opration("1,2"), 3)

    def test_Bigger_1000(self):
        self.assertEqual(String_sum.str_opration("1,2000,1"), 2)
        self.assertEqual(String_sum.str_opration("1,2002,5,20"), 26)

    def test_Negative(self):
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

    def test_multiply_first(self):
        self.assertEqual(String_sum.str_opration("*1"), 1)
        self.assertEqual(String_sum.str_opration("*1,2"), 2)

    def test_multiply(self):
        self.assertEqual(String_sum.str_opration("*1\n3,3"), 9)
        self.assertEqual(String_sum.str_opration("*1\n1000,3"), 3)


if __name__ == '__main__':
    unittest.main()
