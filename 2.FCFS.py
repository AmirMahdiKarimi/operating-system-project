def FCFS(procs):
    sorted_procs = sorted(process)
    k = len(procs)
    exit_t = []
    for i in range(k):
        if i == 0:
            exit_t.append(sorted_procs[i][1])
        else:
            exit_t.append(exit_t[i - 1] + sorted_procs[i][1])

    ret_t = []
    for i in range(k):
        ret_t.append(exit_t[i] - sorted_procs[i][0])

    wait_t = []
    for i in range(k):
        wait_t.append(ret_t[i] - sorted_procs[i][1])

    print("\nPi    exit return wait")
    print("----------------------")
    for i in range(k):
        print(f"P{sorted_procs[i][2] : <5} {exit_t[i] : <5} {ret_t[i] : <5} {wait_t[i] : <5}")

    print(f"\nexit average: {sum(exit_t)/k : .3f}")
    print(f"return average: {sum(ret_t)/k : .3f}")
    print(f"wait average: {sum(wait_t)/k : .3f}")




n = int(input("Enter count of process: "))

process = []


print("P  | in  cpu ")
print("------------------")
i = 0
while i < n:
    try:
        p = list(map(int, input(f"P{i + 1} : ").split()))
        if len(p) != 2:
            print("input is wrong!!")
            continue
        i += 1
        p.append(i)
        process.append(p)
    except:
        print("input is wrong!!")

FCFS(process)



# sample
# 0 4
# 1 8
# 3 2
# 10 6
# 12 5

# 12 5
# 0 4
# 3 2
# 10 6
# 1 8
#
# 1 5
# 0 4
# 3 3
# 2 5










