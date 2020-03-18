class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

        if s == '':
            return True
        else:
            return False



if __name__ == "__main__":
    s = '[(])'
    re = Solution()
    print re.isValid(s)
