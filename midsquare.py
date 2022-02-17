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


def get_middle_number(seed,d):
    cadena = str(seed)
    n = len(cadena)
    mid = int(n/2)
    mid_d = int(d/2)
    return cadena[mid-mid_d:mid+mid_d]


def midsquare(seed):
    d = len(str(seed))
    if d > 3:

        y0 = seed**2
        print(y0)
        x1 = get_middle_number(y0,d)
        r1 = "0." + x1
        print(r1)

        y1 = int(x1)**2
        print(y1)
        x2 = get_middle_number(y1,d)
        r2 = "0." + x2
        print(r2)

midsquare(1234)

