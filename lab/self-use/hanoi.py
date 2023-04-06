def move_disk(disk_number, from_peg, to_peg):
    print("Move disk" + str(disk_number) + " from peg " \
        + str(from_peg) + " to peg " + str(to_peg) + ".")


# it shows really the power and beauty of recursion and it also gave me an excuse to show you what exponential growth
def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move_dis(n, start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        solve_hanoi(n - 1, start_peg, spare_peg)
        move_disk(n, start_peg, end_peg)
        solve_hanoi(n - 1, spare_peg, end_peg)
