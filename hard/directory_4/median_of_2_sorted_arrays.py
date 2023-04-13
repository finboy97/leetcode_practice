# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# where m = nums1.length and n = nums2.length

import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        new_list = []
        if len_1>len_2:
            for element in nums2:
                nums1.append(element)
            new_list=nums1
        else:
            for element in nums1:
                nums2.append(element)
            new_list=nums2
        new_list.sort()
        if (len(new_list) %2 == 0):
            upper = math.floor(len(new_list)/2)
            print(upper)
            lower = upper-1
            print(upper)
            median = (new_list[upper] + new_list[lower])/2
            return median
        else:
            mid_pos = (len(new_list)-1)/2
            return float(new_list[int(round(mid_pos,0))])

        #RESULT: 91ms, beats 76.78% (nice)