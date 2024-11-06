class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_nums1, idx_nums2 = m - 1, n - 1
      
        merge_idx = m + n - 1
      
        while idx_nums2 >= 0:

            if idx_nums1 >= 0 and nums1[idx_nums1] > nums2[idx_nums2]:
                nums1[merge_idx] = nums1[idx_nums1]
                idx_nums1 -= 1 
            else:
                nums1[merge_idx] = nums2[idx_nums2]
                idx_nums2 -= 1 
            merge_idx -= 1