

class NextPermutation:
    def next_permutation(self, nums):

        # Extreme Case:
        if len(nums) <= 1:
            return

        for i in range(len(nums)-2, -1, -1):
            if (nums[i] < nums[i+1]):
                break
        idx1 = nums[i]
        print(idx1)

        idx2 = 0
        for i in range(len(nums)-1, -1, -1):
            if(nums[i] > nums[idx1]):
                idx2 = nums[i]
                break
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


if __name__ == "__main__":
    a = NextPermutation()
    list = [4, 1, 5, 3, 2]
    b = a.next_permutation(list)

    # print(b)
