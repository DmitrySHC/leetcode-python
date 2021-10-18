"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
"""


def find_median_sorted_arrays(nums1, nums2):
    merge = []
    i = j = 0
    while True:
        if len(nums1) == i:
            merge += nums2[j:]
            break
        elif len(nums2) == j:
            merge += nums1[i:]
            break
        if nums1[i] >= nums2[j]:
            merge += [nums2[j]]
            j += 1
        else:
            merge += [nums1[i]]
            i += 1
    if not len(merge) % 2:
        return (merge[(len(merge) // 2) - 1] + merge[(len(merge) // 2)]) / 2
    else:
        return merge[(len(merge) // 2)]


def find_median_sorted_arrays_2(nums1, nums2):
    merge = sorted(nums1 + nums2)
    if not len(merge) % 2:
        return (merge[(len(merge) // 2) - 1] + merge[(len(merge) // 2)]) / 2
    else:
        return merge[(len(merge) // 2)]


first_list, second_list = [-10, 0, 3, 5, 16, 88, 100], [0, 2, 7, 42, 77, 99]

print(find_median_sorted_arrays_2(nums1=first_list, nums2=second_list))
print(find_median_sorted_arrays(nums1=first_list, nums2=second_list))
