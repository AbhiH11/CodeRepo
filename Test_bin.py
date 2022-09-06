gap = 0
max_gap = 0
pos = [0,3,4,6,9]
for i in range(len(pos) - 1):
    # print(i)
    gap = (pos[i+1] - pos[i] - 1)
    print(gap)
    # if gap > max_gap:
    #     max_gap = gap
    #     print(max_gap)
