def create_file():
    
    name = input("Masukkan Nama Kamu: ")
    nim = input("Masukkan NIM Kamu: ")
    resolution = input("Masukkan Resolusi kamu di Tahun Ini: ")

    
    with open('Me.txt', 'w') as file:
        file.write(f"Nama: {name}\n")
        file.write(f"NIM: {nim}\n")
        file.write(f"Resolusi: {resolution}\n")

    print("File Me.txt telah berhasil dibuat!")


create_file()
