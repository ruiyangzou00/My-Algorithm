from datetime import datetime
# O(n) Optimized
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        rmax = -1
        for i in range(len(arr))[::-1]:
            res.insert(0, rmax)
            rmax = max(arr[i], rmax)
        return res


# O(N2) Original
# class Solution(object):
#     def replaceElements(self, arr):
#         for i in range(len(arr)-1):
#             arr[i] = max(arr[i+1:])
#         arr[-1] = -1
#         return arr

if __name__ == '__main__':
    arr = [5, 6, 5, 9, 3, 1]
    print(Solution().replaceElements(arr))
