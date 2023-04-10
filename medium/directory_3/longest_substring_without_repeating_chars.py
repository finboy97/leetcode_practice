
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_chars = set()
        current_length=1
        longest_substring=0
        current_pos = 0
        len_s = len(s)
        while current_pos<len_s:
            if current_pos==0:
                longest_substring=1
            element_to_end = s[current_pos+1:]
            used_chars.add(s[current_pos])
            for cur_char in element_to_end:
                if cur_char in used_chars:
                    current_length=1
                    used_chars.clear()
                    break
                else:
                    used_chars.add(cur_char)
                    current_length+=1
                    if current_length > longest_substring:
                        longest_substring=current_length
            current_pos+=1
            if longest_substring > (len(s)-current_pos):
                break

        return longest_substring