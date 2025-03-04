def input_student_data():
    num_students = int(input("Masukkan jumlah siswa: "))
    student_data = {}

    for i in range(num_students):
        name = input(f"Masukkan nama siswa ke-{i+1}: ")
        grade = int(input(f"Masukkan nilai untuk {name}: "))
        student_data[name] = grade

    return student_data

student_data = input_student_data()
print("dictionary =", student_data)
