def print_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)


height = int(input("Masukkan tinggi segitiga: "))
print_triangle(height)
