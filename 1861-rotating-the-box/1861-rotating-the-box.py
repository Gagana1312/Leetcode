class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """



        m, n = len(box), len(box[0])
        rotated_box = [['.' for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if box[i][j] == '#':
                    empty = j
                    while empty + 1 < n and rotated_box[empty + 1][m - i - 1] == '.':
                        empty += 1
                    rotated_box[empty][m - i - 1] = '#'

                elif box[i][j] == '*':
                    rotated_box[j][m - i - 1] = '*'

        return rotated_box
            