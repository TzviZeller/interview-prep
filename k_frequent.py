# https://leetcode.com/problems/top-k-frequent-elements/

def k_frequent(nums,k):
    num_dict = {}
    k_list = []

    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    k_list = sorted(num_dict.items(), key=lambda _: _[1], reverse=True)[:k]
    return [k for k,v in k_list]


nums = [1,1,1,2,2,3]
k = 2
assert k_frequent(nums,k) == [1,2]