
class Matrix:
    def __init__(self, matrix_data):
        self.data = matrix_data

    def __str__(self):
        for el in self.data:
            for elem in el:
                print(elem, end=' ')
            print('\n')
        return f''

    def __add__(self, matrix):
        new_list = self.data
        try:
            for i in range(0, len(self.data)):
                for j in range(0, len(self.data[i])):
                    new_list[i][j] += matrix.data[i][j]
            return Matrix(new_list)
        except IndexError:
            print("Невозможно сложить эти матрицы")
            exit(0)


my_matrix_1 = Matrix([[1, 1], [1, 1]])
# my_matrix_1 = Matrix([[1, 1], [1, 1], [1, 1])
my_matrix_2 = Matrix([[2, 2], [2, 2]])
print(my_matrix_1 + my_matrix_2)

