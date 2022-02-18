import math


def digitos(x):
    count = 0
    while (x != 0):
        x = x / 10
        ++count
    return count


'''
Long longcentro(long long Yi, int d) {
    long longx = Yi;
    int digits = digitos(x);
    int repeticiones = digits - d;
    int resta = x;
    for (int temp = repeticiones / 2; temp > 0; temp--){
        for (int temp1 = digits; temp1 > 1; temp1--) {
        resta = resta / 10;
    }
    for (int temp2 = digits; temp2 > 1; temp2--) {
        resta = resta * 10;
    }
    x=x - resta;
    resta=x;
    digits--;
    }
    for (int temp = (repeticiones+1) / 2; temp > 0; temp--) {
    x = x / 10;
    }
    return x;
}
'''


def get_middle_number(seed, d):
    cadena = str(seed)
    n = len(cadena)
    mid = int(n / 2)
    mid_d = int(d / 2)
    return cadena[mid - mid_d:mid + mid_d]


def midsquare(seed, n):
    d = len(str(seed))
    r = []
    if d > 3:
        xi = seed
        for _ in range(n):
            yi = xi ** 2
            xi = get_middle_number(yi, d)
            ri = "0." + xi
            xi = int(xi)
            r.append(float(ri))
    return r


print(midsquare(9999, 30))


def midproduct(seed1, seed2, n):
    d1 = len(str(seed1))
    d2 = len(str(seed2))
    r = []
    if d1 == d2 and d1 > 3:
        xi = seed1
        xi1 = seed2
        for _ in range(n):
            yi = xi * xi1
            xi2 = get_middle_number(yi, d1)
            ri = "0." + xi2
            xi2 = int(xi2)
            xi = xi1
            xi1 = xi2
            r.append(float(ri))
    return r


print(midproduct(5015,5734,5))

def constantmultiplier(seed, a, n):
    d = len(str(seed))
    r = []
    if d > 3:
        xi = seed
        for _ in range(n):
            yi = xi * a
            xi = get_middle_number(yi, d)
            ri = "0." + xi
            xi = int(xi)
            r.append(float(ri))
    return r


print(constantmultiplier(9803, 6965, 5))
