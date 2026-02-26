

def penambahan(a, b):
    return a + b


def pengurangan(a, b):
    return a - b


def perkalian(a, b):
    return a * b


def pembagian(a, b):
    if b == 0:
        return "Pembagian tidak dapat dilakukan karena pembagi bernilai 0"
    return a / b


def modulus(a, b):
    return a % b


def fibonacci(n):
    if n <= 0:
        return []

    hasil = []
    a, b = 0, 1
    for i in range(n):
        hasil.append(a)
        a, b = b, a + b
    return hasil


# ===== PROGRAM UTAMA =====
if __name__ == "__main__":
    print("Penambahan:", penambahan(3, 5))
    print("Pengurangan:", pengurangan(10, 4))
    print("Perkalian:", perkalian(2, 6))
    print("Pembagian:", pembagian(8, 2))
    print("Pembagian (error):", pembagian(8, 0))
    print("Modulus:", modulus(10, 3))
    print("Fibonacci:", fibonacci(5))
