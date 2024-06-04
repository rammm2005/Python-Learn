import numpy as np

def solve_linear_equations(A, b):
    """
    Menyelesaikan sistem persamaan linear Ax = b
    :param A: Matriks koefisien (numpy array)
    :param b: Vektor konstanta (numpy array)
    :return: Vektor solusi x (numpy array) atau pesan kesalahan
    """
    try:
        det_A = np.linalg.det(A)
        if np.isclose(det_A, 0):
            return "Singular matrix"
        else:
            x = np.linalg.solve(A, b)
            return x
    except np.linalg.LinAlgError as e:
        return f"Error dalam menyelesaikan sistem persamaan linear: {e}"

def get_user_input():
    try:
        n = int(input("Masukkan jumlah variabel: "))

        print("Masukkan elemen-elemen matriks A:")
        A = []
        for i in range(n):
            row = list(map(float, input(f"Masukkan baris ke-{i + 1} (pisahkan dengan spasi): ").split()))
            if len(row) != n:
                print(f"Baris ke-{i + 1} harus memiliki {n} elemen.")
                return None, None
            A.append(row)

        print("Masukkan elemen-elemen vektor b:")
        b = list(map(float, input("Masukkan elemen-elemen vektor b (pisahkan dengan spasi): ").split()))
        if len(b) != n:
            print(f"Vektor b harus memiliki {n} elemen.")
            return None, None

        return np.array(A), np.array(b)
    except ValueError as e:
        print("Input tidak valid:", e)
        return None, None

def main():
    A, b = get_user_input()

    if A is None or b is None:
        print("Input tidak valid. Program berhenti.")
        return

    result = solve_linear_equations(A, b)

    if isinstance(result, np.ndarray):
        print("Solusi dari sistem persamaan linear adalah:", result)
    else:
        print("Persamaan di atas merupakan persamaan : ", result)

# Panggil main function
if __name__ == "__main__":
    main()
