# Given a string s, return the longest palindromic substring in s.
# E.g s = babad -> bab
# s = cbbd -> bb

class Solution:
    def longest_palindrome(self, s: str) -> str:
        source_str = s
        check_str = s[::-1]
        current_check_length = len(source_str)
        while current_check_length > 0:
            print("outer while loop")
            counter = current_check_length
            start_index = 0
            end_index = counter
            print(f"start index is {start_index}, finish is {end_index}, current check length is {current_check_length}")
            while counter <= len(source_str):
                print("inner while loop")
                current_substring = source_str[start_index:counter:]
                print(current_substring)
                if current_substring == check_str[len(check_str)-counter:len(check_str)-start_index]:
                    return current_substring
                start_index += 1
                counter += 1
            current_check_length -= 1

        # Success: 4879ms (beats 20%) - not great.
        # Oddly the memory usage was somehow better than 83% of people. But computing is more expensive than storage, so
        # still could be better.