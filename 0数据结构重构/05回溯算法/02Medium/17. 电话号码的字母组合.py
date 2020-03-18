# encoding:utf8

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", \
                    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        if not digits:
            return []

        def helper(item, digits):
            if digits:
                for i in num_dict[digits[0]]:
                    helper(item + i, digits[1:])
            else:
                result.append(item)

        helper('', digits)
        return result


if __name__ == '__main__':
    digits = '23'



