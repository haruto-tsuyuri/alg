from pprint import pprint


class IsoscelesTriangle:
    def __init__(self):
        pprint("Show isosceles triangles.")
        self.isosceles_triangle_length = self.input_isosceles_triangle_length()

        for space in range(self.isosceles_triangle_length):
            for _ in range(self.isosceles_triangle_length - space - 1):
                print(' ', end='')
            for _ in range(space + 1):
                print('*', end='')
            print('\n')

    @staticmethod
    def input_isosceles_triangle_length():
        isosceles_triangle_length = int(input('input length: '))
        return isosceles_triangle_length
