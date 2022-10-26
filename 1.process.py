def single(progs):
    cpu = 0
    total = 0
    # for prog in progs:
    #     cpu += sum(prog[0::2])
    #     # cpu += prog[0] + prog[2]
    #     total += sum(prog)

    for prog in progs:
        cpu += prog[1]
        total += sum(prog)

    print(f"cpu time: {cpu}")
    print(f"total time: {total}")
    print(f"Efficiency: {cpu / total * 100:.3f}")


def multi(progs):
    cpu = 0
    total = 0
    # for j in range(2):
    #     for prog in progs:
    #         cpu += prog[j * 2]
    #         if j > 0:
    #             if sum(prog[:j + 1]) > total:
    #                 total = sum(prog[:j + 1])
    #         total += prog[j * 2]

    inp_curs = 0
    cpu_curs = 0
    out_curs = 0
    for prog in progs:
        cpu += prog[1]
        if out_curs == 0 :
            inp_curs += prog[0]
            cpu_curs += sum(prog[:2])
            out_curs += sum(prog)
        else:
            inp_curs += prog[0]
            if inp_curs <= cpu_curs:
                cpu_curs += prog[1]
            else:
                cpu_curs = inp_curs + prog[1]
            if cpu_curs <= out_curs:
                out_curs += prog[2]
            else:
                out_curs = cpu_curs + prog[2]
    total = out_curs

    print(f"cpu time: {cpu}")
    print(f"total time: {total}")
    print(f"Efficiency: {cpu / total * 100:.3f}")


n = int(input("Enter count of process: "))

programs = []

print("P  in cpu out")
print("------------------")
i = 0
while i < n:
    try:
        p = list(map(int, input(f"P{i + 1} : ").split()))
        if len(p) != 3:
            print("input is wrong!!")
            continue
        programs.append(p)
        i += 1

    except:
        print("input is wrong!!")


print("\nwithout multi process:")
single(programs)
print("--------------------")
print("multi process:")
multi(programs)

# sample:
# 2 1 3
# 1 3 2
# 3 1 2

# smap 2
# 5 4 1
# 2 2 3
# 6 3 2