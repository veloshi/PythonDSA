from collections import Counter
import heapq
nums = "abcdddssassasfhjm"
res =""
dict1 = Counter(nums)
while dict1:
    x = str(heapq.nlargest(1,dict1.keys()))
    dict1.remove(x)
print(dict1)

# https://leetcode.com/problems/last-stone-weight/ >> done
# https://leetcode.com/problems/third-maximum-number/ >> done
# https://leetcode.com/problems/kth-largest-element-in-a-stream/ done
# https://leetcode.com/problems/k-closest-points-to-origin/ doubt
# https://leetcode.com/problems/sort-characters-by-frequency/ doubt
# https://leetcode.com/problems/top-k-frequent-elements/ done
# https://leetcode.com/problems/kth-largest-element-in-an-array/ done
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/  >> done
# https://leetcode.com/problems/top-k-frequent-words/ done
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ doubt
# https://leetcode.com/problems/merge-k-sorted-lists/ hard
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/ hard
# https://leetcode.com/problems/find-median-from-data-stream/ hard
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/ >> hard
# https://leetcode.com/problems/car-pooling/
# https://leetcode.com/problems/meeting-rooms/ >> done
# https://leetcode.com/problems/meeting-rooms-ii/ >> Premium