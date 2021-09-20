from collections import UserList


class Matrix(UserList):

    def fill_matrix_in_spiral_order(self, n):
        """
        Fills matrix from numbers from 1 till n*n in spiral order (destructive operation)
        :param n:
        """
        start = n * n + 1  # start from largest
        while start > 1:
            start, end = start - len(self.data), start
            self.data = [tuple(range(start, end))] + list(zip(*self.data[::-1]))

    def spiral_order(self):
        """
        Prints matrix in spiral order
        :return:
        """
        return self.data and list(self.data.pop(0)) + self.spiral_order(list(zip(*self.data))[::-1])

    def __repr__(self):
        return '\n'.join(['\t'.join(list(map(str, row))) for row in self])


matrix = Matrix()
matrix.fill_matrix_in_spiral_order(4)
print(matrix)
