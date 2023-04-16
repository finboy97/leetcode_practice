import pytest
from .longest_palindromic_substring import Solution

class TestLongestPalindrome:

    @pytest.fixture
    def setup_envt(self):
        return Solution()

    def test_palindrome_bab(self, setup_envt):
        test_str = "babad"
        assert setup_envt.longest_palindrome(test_str) == "bab"

    def test_palindrome_bb(self, setup_envt):
        test_str = "cbbd"
        assert setup_envt.longest_palindrome(test_str) == "bb"

    def test_reverse_present_but_not_palindrome(self, setup_envt):
        test_str = "aacabdkacaa"
        assert setup_envt.longest_palindrome(test_str) == "aca"
