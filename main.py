import math

def main():
    a = float(input("zadaj a: "))
    
    if a == 0:
        print("Rovnice nie je kvadraticka, ale linearna!")
        return
        
    b = float(input("zadaj b: "))
    c = float(input("zadaj c: "))

    print(f"tvar rovnice je: {a}x²{b:+}x{c:+} = 0")

    D = b**2 - 4*a*c
    
    if D < 0:
        print("Nema riesenie")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x1 = x2 = {x}")
    else:
        odm_D = math.sqrt(D)
        x1 = (-b + odm_D) / (2 * a)
        x2 = (-b - odm_D) / (2 * a)
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
        
if __name__ == "__main__":
    main()
