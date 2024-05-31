/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximizeSum = function(nums, k) {
    value = Math.max(...nums)
    ans = 0
    for (let i=0;i<k;i++){
        value = value + 1
        ans = ans + value
    }
    return ans - k
};