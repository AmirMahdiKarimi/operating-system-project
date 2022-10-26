import sys

def req(cap, x, id):
    check = True
    for i in range(len(cap)):
        l = cap[i][1]-cap[i][0]+1
        if cap[i][2] == False and x <= l:
            check = False
            while x <= l/2:
                l =int(l/2)
                cap.insert(i, [cap[i][0]+l, cap[i][1], False])
                cap.insert(i, [cap[i+1][0], cap[i+1][1]-l, False])
                cap.pop(i+2)
            cap[i][2] = id
            break
    if check:
        print(f"Capacity has not enough for P{id}!")
        sys.exit()
    return cap

def freeing(cap, id):
    check = True
    for i in range(len(cap)):
        k = i
        if cap[i][2] == id:
            check = False
            cap[i][2] = False
            while True:
                if k > 0 and cap[k-1][2] == False and cap[k-1][1] - cap[k-1][0] == cap[k][1] - cap[k][0]:
                    cap[k - 1][1] = cap[k][1]
                    cap.pop(k)
                    k -= 1
                elif k < len(cap)-1 and cap[k+1][2] == False and cap[k][1] - cap[k][0] == cap[k+1][1] - cap[k+1][0]:
                    cap[k][1] = cap[k+1][1]
                    cap.pop(k+1)
                else:
                    break
            break
    if check:
        print(f"There is not P{id} in memory!")
    return cap
.



n = int(input("Enter Capacity power of two: "))
k = bin(n)[2:]
if k[0] == "1" and int(k[1:]) == 0:
    cap = [[0, n-1, False]]
    k=0
    while True:
        print("1.Request space:")
        print("2.Freeing space:")
        temp = int(input("1 or 2 : "))
        if temp == 1:
            k += 1
            print("Enter request :")
            x = int(input(f"Size of P{k}: "))
            cap = req(cap, x, k)
            print(cap)
        elif temp == 2:
            print("Enter freeing :")
            x = int(input(f"id of Process: "))
            cap = freeing(cap, x)
            print(cap)
else:
    print(f"{n} is not power of 2")


#samp
# 1024
# 1
# 100
# 1
# 240
# 1
# 64
# 1
# 256
# 2
# 2
# 2
# 1
# 1
# 75
# 2
# 3
# 2
# 5
# 2
# 4
