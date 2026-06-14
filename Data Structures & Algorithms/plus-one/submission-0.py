class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        for i in range(len(digits)-1, -1, -1):
            print(i, digits[i])
            ans = ans + (digits[i] * (10 ** (len(digits)-1-i)))
        ans = ans + 1
        str_ans = str(ans)
        res = []
        for letter in str_ans:
            res.append(letter)
        return res
