def first_fit(blocks, process):
    s = ""
    for block in blocks:
        s += f"| {block : <5}"
    print(f"\n\nProcess   Size	 Block  {s}")
    for i in range(len(process)):
        for j in range(len(blocks)):
            if blocks[j] >= process[i]:
                print(f" P{i + 1 : <6}  {process[i] : <7}  {j+1 : <5}", end="")
                blocks[j] -= process[i]
                break
            if j+1 == len(blocks):
                print(f" P{i + 1 : <6}  {process[i] : <7}  -    ", end="")
        s = ""
        for block in blocks:
            s += f"| {block : <5}"
        print(s)


len_p = int(input("Enter count of process: "))
len_b = int(input("Enter count of blocks: "))

process = []
blocks = []
print("\nmemory need of process: ")
i = 0
while i < len_p:
    try:
        p = int(input(f"P{i + 1} : "))
        i += 1
        process.append(p)
    except:
        print("input is wrong!!")

print("\nCapacity of blocks: ")
i = 0
while i < len_b:
    try:
        p = int(input(f"B{i + 1} : "))
        i += 1
        blocks.append(p)
    except:
        print("input is wrong!!")

first_fit(blocks, process)


#samp
# 4
# 5
# 212
# 417
# 112
# 426
# 100
# 500
# 200
# 300
# 600

# 4
# 4
# 19
# 20
# 6
# 13
# 40
# 20
# 70
# 12