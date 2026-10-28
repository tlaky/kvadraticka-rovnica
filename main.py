# Ctibor

import math
from common.utils import get_number

def vypocitaj_diskriminant(a: float, b: float, c: float):
    return b**2 - 4*a*c

def vypocitaj_vysledok(a: float, b: float, c: float):
    """
    Vypocita diskriminant a podla neho vypocita koren rovnice
    
    a, b, c: float - koeficienty
    
    vratna hodnota: None ak nema koren, inak koren
    """
    
    D = vypocitaj_diskriminant(a, b, c)
    if D < 0:
        return None, None
    elif D == 0:
        x = -b / (2 * a)
        return x, None
    else:
        odm_D = math.sqrt(D)
        x1 = (-b + odm_D) / (2 * a)
        x2 = (-b - odm_D) / (2 * a)
        return x1, x2

def main():
    a = get_number("Zadaj a", nulaPovolena=False)
    b = get_number("Zadaj b", nulaPovolena=True)
    c = get_number("Zadaj c", nulaPovolena=True)

    print(f"tvar rovnice je: {a}x²{b:+}x{c:+} = 0")

    x1, x2 = vypocitaj_vysledok(a, b, c)
    koren = ""
    
    if x2 is not None:
        koren = f"{x1:.2f}, {x2:.2f}"
    elif x1 is not None:
        koren = f"{x1:.2f}"
        
        
    print(f"Koren = {{{koren}}}")
        
if __name__ == "__main__":
    main()
