# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.get_peak(mountain_arr)
        start, end = 0, peak

        # check left (since it wants the minimum index)
        while start <= end:
            mid = (start+end)//2
            my_mid = mountain_arr.get(mid)
            if my_mid == target:
                return mid
            elif my_mid < target:
                start = mid+1
            else:
                end = mid-1

        # check right 
        start, end = peak, mountain_arr.length()-1
        while start <= end:
            mid = (start+end)//2
            my_mid = mountain_arr.get(mid)
            if my_mid == target:
                return mid
            elif my_mid > target:
                start = mid+1
            else:
                end = mid-1
        return -1

    # find the peak
    def get_peak(self, mountain_arr: 'MountainArray') -> int:
        start, end, n = 0, mountain_arr.length()-1, mountain_arr.length()

        while start <= end:
            mid = (start+end)//2
            my_mid = mountain_arr.get(mid)
            if 0 <= mid-1 and mid+1 < n and mountain_arr.get(mid-1) < my_mid > mountain_arr.get(mid+1):
                return mid
            elif mid+1 < n and my_mid < mountain_arr.get(mid+1):
                start = mid + 1
            elif 0 <= mid-1 and mountain_arr.get(mid-1) > my_mid:
                end = mid - 1
        return -1