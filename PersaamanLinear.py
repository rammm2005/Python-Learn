import numpy as nps

def solve_linear_equations(A, B) :
    """
    Menyelesaikan sistem persamaan linear Ax = b
    :param A: Matriks koefisien (numpy array)
    :param b: Vektor konstanta (numpy array)
    :return: Vektor solusi x (numpy array)
    """
    try :
        x = nps.linalg.solve(A, B);
        return x;
    except nps.linalg.LinAlgError as e :
        print("Error dalam menyelesaikan sistem persamaan linear:", e)
        return None
    
    
    
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
        
        return nps.array(A), nps.array(b)
    except ValueError as e:
        print("Input tidak valid:", e)
        return None, None

def main():
    A, b = get_user_input()
    
    if A is None or b is None:
        print("Input tidak valid. Program berhenti.")
        return
    
    x = solve_linear_equations(A, b)
    
    if x is not None:
        print("Solusi dari sistem persamaan linear adalah:", x)
    else:
        print("Tidak dapat menyelesaikan sistem persamaan linear.")

# for call main xixxi
if __name__ == "__main__":
    main()