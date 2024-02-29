class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        ind, step = 0, 1

        for character in s:
            rows[ind] += character
            if ind == 0:
                step = 1
            elif ind == numRows - 1:
                step = -1
            ind += step

        return ''.join(rows)