import unittest
from strings import (
    concatenate_strings, string_length, string_slice,
    find_substring, replace_substring, remove_whitespace,
    string_to_list, list_to_string, is_palindrome
)

class TestStringOperations(unittest.TestCase):
    
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("hello", " world"), "hello world")
        self.assertEqual(concatenate_strings("", "world"), "world")
        self.assertEqual(concatenate_strings("hello", ""), "hello")
        
    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length(" "), 1)
        
    def test_string_slice(self):
        self.assertEqual(string_slice("hello world", 0, 5), "hello")
        self.assertEqual(string_slice("hello world", 6, 11), "world")
        self.assertEqual(string_slice("hello world", 3, 8), "lo wo")
        
    def test_find_substring(self):
        self.assertEqual(find_substring("hello world", "world"), 6)
        self.assertEqual(find_substring("hello world", "hello"), 0)
        self.assertEqual(find_substring("hello world", "test"), -1)
        
    def test_replace_substring(self):
        self.assertEqual(replace_substring("hello world", "world", "there"), "hello there")
        self.assertEqual(replace_substring("hello hello", "hello", "hi"), "hi hi")
        self.assertEqual(replace_substring("hello world", "test", "replace"), "hello world")
        
    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("  hello world  "), "hello world")
        self.assertEqual(remove_whitespace("hello"), "hello")
        self.assertEqual(remove_whitespace("  "), "")
        
    def test_string_to_list(self):
        self.assertEqual(string_to_list("hello,world", ","), ["hello", "world"])
        self.assertEqual(string_to_list("one|two|three", "|"), ["one", "two", "three"])
        self.assertEqual(string_to_list("no delimiter", ","), ["no delimiter"])
        
    def test_list_to_string(self):
        self.assertEqual(list_to_string(["hello", "world"], " "), "hello world")
        self.assertEqual(list_to_string(["one", "two", "three"], "|"), "one|two|three")
        self.assertEqual(list_to_string([], ","), "")
        
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
