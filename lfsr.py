
# [0,1,2]
# [s2,s1,s0]
# [1,0,0]

# [s0,s1,s2]
# [0,0,1]

def lfsr(sinitial):
    cont = 0
    scurrent = []
    while sinitial!=scurrent:
        if cont==0:
            scurrent = sinitial.copy()
            cont = cont +1
        s2 = scurrent[0]
        # [1,0,0]
        scurrent[0] = scurrent[1]^scurrent[2]
        # [0,0,0]
        scurrent[2] = scurrent[1]
        # [0,0,0]
        scurrent[1]= s2
        # [0,1,0]
        print(scurrent)
        yield scurrent[2]


if __name__ == '__main__':
    print([1,0,0])
    for _ in lfsr([1,0,0]):
        pass