def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
    
    
print("-KALKULATOR CHIKO-")
print("Menu Kalkulator:")
print("1. Tambah")
print("2. Kurang")
print("3. Perkalian")
print("4. Pembagian")

choice = input("Masukan Pilihan Anda (1-4): ")


if choice in ['1', '2', '3', '4']:
    num1 = float(input("Masukkan Angka Pertama: "))
    num2 = float(input("Masukan Angka Kedua: "))

    if choice == '1':
        print("Hasil:", add(num1, num2))
    elif choice == '2':
        print("Hasil:", subtract(num1, num2))
    elif choice == '3':
        print("Hasil:", multiply(num1, num2))
    else:
        print("Hasil:", divide(num1, num2))
else:
    print("Pilihan Anda Tidak Cocok!")