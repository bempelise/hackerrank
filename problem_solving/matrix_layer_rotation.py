"""
HackerRank - Matrix Layer Rotation

https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

"""

class Matrix():
    """ Class to handle matrix rotation """
    def __init__(self, matrix):
        self.x = len(matrix)
        self.y = len(matrix[0])
        self.matrix = matrix
        self.stripes = []
        i = 0
        while i < min(self.x, self.y)/2:
            self.get_strip(i)
            i += 1
        # print(self)
        # print(self.stripes)


    def get_strip(self, index):
        """ Gets an inner strip from the matrix """
        # First line
        strip = self.matrix[index][index: self.y - index]
        # Last column
        for i in range(index + 1, self.x - index):
            strip.append(self.matrix[i][self.y - index - 1])
        # Last line
        reverse_last_row = self.matrix[self.x - index - 1][::-1]
        strip.extend(reverse_last_row[index + 1: self.y - index])
        # First column
        for i in range(self.x - index - 2, index, -1):
            strip.append(self.matrix[i][index])
        self.stripes.append(strip)

    def rotate(self, times):
        """ Rotates the matrix times times"""
        newstripes = []
        for strip in self.stripes:
            offset = times % len(strip)
            # Shift right
            # newstripe = strip[-offset:]
            # newstripe.extend(strip[: -offset])
            # Shift left
            newstripe = strip[offset:]
            newstripe.extend(strip[:offset])
            newstripes.append(newstripe)
        self.stripes = newstripes

        # print(self.stripes)
        self.update_matrix()

    def update_matrix(self):
        """ Updates the matrix using the stripe contents """
        i = 0
        while i < min(self.x, self.y)/2:
            self.update_strip(i)
            i += 1

    def update_strip(self, index):
        """ Updates the matrix using the strip at index """
        strip = self.stripes[index]
        # First line
        offset = 0
        for i in range(index, self.y - index):
            self.matrix[index][i] = strip[offset % len(strip)]
            offset += 1

        # Last column
        for i in range(index + 1, self.x - index):
            self.matrix[i][self.y - index - 1] = strip[offset % len(strip)]
            offset += 1

        # Last line
        for i in range(self.y - index - 2, index - 1, -1):
            self.matrix[self.x - index - 1][i] = strip[offset % len(strip)]
            offset += 1

        # First column
        for i in range(self.x - index - 2, index, -1):
            self.matrix[i][index] = strip[offset % len(strip)]
            offset += 1

    def __str__(self):
        matrix_string = ""
        for i in range(0, self.x):
            for j in range(0, self.y):
                matrix_string += str(self.matrix[i][j]) + "\t"
            matrix_string = matrix_string[:-1] + "\n"
        return matrix_string


def rotate(matrix, times):
    """ Rotates matrix r times """
    mat = Matrix(matrix)
    mat.rotate(times)
    print(mat)


def main():
    """ main """
    matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    rotate(matrix, 1)

    matrix = [
        [1, 2, 3, 4],
        [14, 15, 16, 5],
        [13, 20, 17, 6],
        [12, 19, 18, 7],
        [11, 10, 9, 8]
    ]
    rotate(matrix, 1)

    matrix = [
        [1, 2, 3, 4, 5],
        [14, 15, 16, 17, 6],
        [13, 20, 19, 18, 7],
        [12, 11, 10, 9, 8]
    ]
    rotate(matrix, 1)


if __name__ == "__main__":
    main()
