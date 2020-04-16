class Matrix:
    def __init__(self, l_list):
        self.l_list = l_list

    def __str__(self):
        for row in self.l_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.l_list)):
            for i_2 in range(len(other.l_list[i])):
                self.l_list[i][i_2] = self.l_list[i][i_2] + other.l_list[i][i_2]
        return Matrix.__str__(self)



m = Matrix([[-1, 0, 1], [1, 1, 1], [-1, 1, 0]])
new_m = Matrix([[-2, 0, 2], [2, 2, 2], [-2, 2, 0]])
print(m.__add__(new_m))