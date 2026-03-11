# Practical MST 
## Longest Mountain in Array - leetcode 845
```
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestMountain(vector<int>& arr) {
        
        int n = arr.size();
        int i = 0;
        int result = 0;

        while (i < n - 1) {

            int asc_by = 0;
            int desc_by = 0;

            while (i < n - 1 && arr[i] < arr[i + 1]) {
                asc_by++;
                i++;
            }

            while (i < n - 1 && arr[i] > arr[i + 1]) {
                desc_by++;
                i++;
            }

            if (asc_by > 0 && desc_by > 0) {
                result = max(result, asc_by + desc_by + 1);
            }

            if (asc_by == 0 && desc_by == 0) {
                i++;
            }
        }

        return result;
    }
};
```
### screenshot
<img width="1919" height="1017" alt="leetcode_845" src="https://github.com/user-attachments/assets/e3c44ac2-d4b0-4441-a3a4-4ea7953a5a7e" />


## Minimum limit of balls in a bag - leetcode 1760

```
class Solution:
    def minimumSize(self, nums, maxOperations):
        
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            operations = 0

            for x in nums:
                operations += (x - 1) // mid

            if operations <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left
```
### screenshot
<img width="1914" height="1013" alt="leetcode_1760" src="https://github.com/user-attachments/assets/8f884497-ed20-4cd1-a003-801342f1f956" />
