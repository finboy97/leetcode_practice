from unittest import TestCase
from .longest_substring_without_repeating_chars import Solution

class TestSolution(TestCase):
    global test_solution
    test_solution= Solution()

    def test_length_of_all_same_character(self):
        test_str="bbb"
        self.assertEquals(Solution.lengthOfLongestSubstring(self,test_str),1)

    def test_string_with_backtracking_for_longest(self):
        test_str="dvdf"
        self.assertEquals(Solution.lengthOfLongestSubstring(self,test_str),3)

    def test_empty_string(self):
        test_str=""
        self.assertEquals(Solution.lengthOfLongestSubstring(self,test_str),0)