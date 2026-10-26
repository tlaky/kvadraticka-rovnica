import math

def main():
    a = int(input("zadaj a: "))
    b = int(input("zadaj b: "))
    c = int(input("zadaj c: "))

    print(f"tvar rovnice je: {a}x^2 {b:+}x {c:+} = 0")

    D = b**2 - 4*a*c
    
    if D < 0:
        print("Nema riesenie")
        return
    
    odm_D = math.sqrt(D)
    
    x1 = -b + odm_D / (2 * a)
    
    if disk == 0:
        print(f"x1 = x2 = {x}")
    else:
        x2 = -b - odm_D / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
        
if __name__ == "__main__":
    main()
