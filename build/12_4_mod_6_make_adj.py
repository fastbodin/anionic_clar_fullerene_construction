import sys


def add_neighbor(G, u, v):
    G[u].append(v)


def add_edges(G, shift, new_edges):
    for edges in new_edges:
        for i in range(1, len(edges)):
            add_neighbor(G, edges[0] + shift, edges[i] + shift)
            if edges[i] < 0:
                add_neighbor(G, edges[i] + shift, edges[0] + shift)


def print_adj_list(G):
    num_v = len(G)
    print("{}".format(len(G)))
    for v in range(num_v):
        v_deg = 0
        mystr = "3"
        # mystr = "{:3d}".format(v)
        for u in range(len(G[v])):
            mystr += " {:3d}".format(G[v][u])
            v_deg += 1
        if v_deg != 3:
            print("bad degree = {}".format(v_deg))

        print(mystr)


# check the graph is symmetric
def check(G):
    num_v = len(G)
    for v in range(num_v):
        mystr = "{:3d}".format(v)
        for i in range(len(G[v])):
            u = G[v][i]
            u_adj_v = 0
            for j in range(len(G[u])):
                if G[u][j] == v:
                    u_adj_v = 1
            if u_adj_v != 1:
                mystr += "~{:3d} but {:3d}!~{:3d} {}".format(
                    G[v][i], G[v][i], v, num_v
                )
                print(mystr)


def r_cycle(input_list):
    temp_list = []
    temp_list.append(input_list[0])
    # by starting at the first verex, you can either read the list forward
    # or backward. In this case, you read the list backwards (representing a flip
    # of a cap)
    for i in range(len(input_list) - 1, 0, -1):
        temp_list.append(input_list[i])
    return temp_list


def shift_by_turns(input_list, num_turns):
    if num_turns == 0:
        return input_list
    else:
        temp_list = []
        # given an original list [0,1,2,3,4,....,10]
        # each turn shifts first three vertices in front to back
        # i.e. one turn gives [3,4,....,10,0,1,2]
        # two turns gives [6,7,....,10,0,1,2,3,4,5]
        for i in range(3 * num_turns, len(input_list)):
            temp_list.append(input_list[i])
        for i in range(0, 3 * num_turns):
            temp_list.append(input_list[i])
    return temp_list


def add_cap(cap_type, cap_turn, cap_flip, num_rings):
    # there is always a ring between the caps as I have defined the top cap
    if num_rings % 3 == 1:
        prev_r_v = shift_by_turns(
            [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23], cap_turn
        )
    elif num_rings % 3 == 2:
        prev_r_v = shift_by_turns(
            [-3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -1], cap_turn
        )
    elif num_rings % 3 == 0:
        prev_r_v = shift_by_turns(
            [-5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -1, -3], cap_turn
        )
    else:
        print("bad num_rings")
        exit(0)

    # preform a flip
    if cap_flip == 1:
        prev_r_v = r_cycle(prev_r_v)

    # top cap
    # clockwise order
    new_edges = [
        [0, 1, 19, prev_r_v[0]],
        [1, 2, 22, 0],
        [2, 3, 1, prev_r_v[1]],
        [3, 4, 2, prev_r_v[2]],
        [4, 5, 23, 3],
        [5, 6, 4, prev_r_v[3]],
        [6, 7, 25, 5],
        [7, 8, 6, prev_r_v[4]],
        [8, 9, 7, prev_r_v[5]],
        [9, 10, 26, 8],
        [10, 11, 9, prev_r_v[6]],
        [11, 12, 28, 10],
        [12, 13, 11, prev_r_v[7]],
        [13, 14, 12, prev_r_v[8]],
        [14, 15, 29, 13],
        [15, 16, 14, prev_r_v[9]],
        [16, 17, 31, 15],
        [17, 18, 16, prev_r_v[10]],
        [18, 19, 17, prev_r_v[11]],
        [19, 0, 20, 18],
        [20, 19, 21, 31],
        [21, 22, 32, 20],
        [22, 23, 21, 1],
        [23, 4, 24, 22],
        [24, 25, 33, 23],
        [25, 6, 26, 24],
        [26, 9, 27, 25],
        [27, 26, 28, 33],
        [28, 27, 11, 29],
        [29, 28, 14, 30],
        [30, 29, 31, 32],
        [31, 20, 30, 16],
        [32, 33, 30, 21],
        [33, 27, 32, 24],
    ]
    return new_edges


def add_ring(G, cap_type, v_index, ring_num):
    new_edges = []
    # ring is added to bottom cap
    if ring_num == 0:
        # vertices missing edges on bottom cap are listed (w/ relative numbering)
        # in clock-wise order
        if cap_type == 19:
            prev_r_v = [-1, -19, -17, -16, -14, -12, -11, -9, -7, -6, -4, -2]
        elif cap_type == 20:
            prev_r_v = [-1, -21, -19, -18, -16, -14, -12, -10, -8, -7, -5, -3]
        elif cap_type == 21:
            prev_r_v = [-1, -21, -19, -17, -15, -13, -12, -10, -8, -6, -4, -2]
        elif cap_type == 22:
            prev_r_v = [-1, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2]
        else:
            print("bad cap_type")
            exit(0)
    # ring is added to another ring
    else:
        # vertices in previous ring missing edges are listed (w/ relative numbering)
        # in clock-wise order
        prev_r_v = [-1, -23, -21, -19, -17, -15, -13, -11, -9, -7, -5, -3]
    # same numbering system for all rings
    new_edges = [
        [0, 23, 1, prev_r_v[0]],
        [1, 2, 0],
        [2, 3, prev_r_v[1], 1],
        [3, 4, 2],
        [4, 5, prev_r_v[2], 3],
        [5, 6, 4],
        [6, 7, prev_r_v[3], 5],
        [7, 8, 6],
        [8, 9, prev_r_v[4], 7],
        [9, 10, 8],
        [10, 11, prev_r_v[5], 9],
        [11, 12, 10],
        [12, 13, prev_r_v[6], 11],
        [13, 14, 12],
        [14, 15, prev_r_v[7], 13],
        [15, 16, 14],
        [16, 17, prev_r_v[8], 15],
        [17, 18, 16],
        [18, 19, prev_r_v[9], 17],
        [19, 20, 18],
        [20, 21, prev_r_v[10], 19],
        [21, 22, 20],
        [22, 23, prev_r_v[11], 21],
        [23, 0, 22],
    ]

    add_edges(G, v_index, new_edges)


def unique_family(max_n, num_rings):
    # caps + rings
    num_v = 70 + 30 * num_rings
    if num_v > max_n:
        return 0

    # bottom cap
    new_edges = [
        [0, 4, 8, 1],
        [1, 0, 11, 2],
        [2, 1, 14, 3],
        [3, 2, 17, 4],
        [4, 3, 5, 0],
        [5, 4, 19, 6],
        [6, 7, 5],
        [7, 8, 6],
        [8, 7, 9, 0],
        [9, 10, 8],
        [10, 11, 9],
        [11, 10, 12, 1],
        [12, 13, 11],
        [13, 14, 12],
        [14, 13, 15, 2],
        [15, 16, 14],
        [16, 17, 15],
        [17, 16, 18, 3],
        [18, 19, 17],
        [19, 5, 18],
    ]

    G = [[] for _ in range(num_v)]

    # fill in info for bottom cap
    add_edges(G, 0, new_edges)

    previous = [-1, -2, -4, -5, -7, -8, -10, -11, -13, -14]

    new_edges = [
        [0, 19, 1, previous[0]],
        [1, 0, 2, previous[-1]],
        [2, 1, 21, 3],
        [3, 2, 22, 4],
        [4, 3, 5, previous[-2]],
        [5, 4, 6, previous[-3]],
        [6, 5, 23, 7],
        [7, 6, 24, 8],
        [8, 7, 9, previous[-4]],
        [9, 8, 10, previous[-5]],
        [10, 9, 25, 11],
        [11, 10, 26, 12],
        [12, 11, 13, previous[-6]],
        [13, 12, 14, previous[-7]],
        [14, 13, 27, 15],
        [15, 14, 28, 16],
        [16, 15, 17, previous[-8]],
        [17, 16, 18, previous[-9]],
        [18, 17, 29, 19],
        [19, 18, 20, 0],
        [20, 21, 19],
        [21, 2, 20],
        [22, 23, 3],
        [23, 6, 22],
        [24, 25, 7],
        [25, 10, 24],
        [26, 27, 11],
        [27, 14, 26],
        [28, 29, 15],
        [29, 18, 28],
    ]
    add_edges(G, 20, new_edges)

    # all the rings
    pos = 50
    for _ in range(1, num_rings + 1):
        previous = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        new_edges = [
            [0, 19, 1, previous[0]],
            [1, 0, 2, previous[-1]],
            [2, 1, 21, 3],
            [3, 2, 22, 4],
            [4, 3, 5, previous[-2]],
            [5, 4, 6, previous[-3]],
            [6, 5, 23, 7],
            [7, 6, 24, 8],
            [8, 7, 9, previous[-4]],
            [9, 8, 10, previous[-5]],
            [10, 9, 25, 11],
            [11, 10, 26, 12],
            [12, 11, 13, previous[-6]],
            [13, 12, 14, previous[-7]],
            [14, 13, 27, 15],
            [15, 14, 28, 16],
            [16, 15, 17, previous[-8]],
            [17, 16, 18, previous[-9]],
            [18, 17, 29, 19],
            [19, 18, 20, 0],
            [20, 21, 19],
            [21, 2, 20],
            [22, 23, 3],
            [23, 6, 22],
            [24, 25, 7],
            [25, 10, 24],
            [26, 27, 11],
            [27, 14, 26],
            [28, 29, 15],
            [29, 18, 28],
        ]
        add_edges(G, pos, new_edges)
        pos += 30

    # top cap
    previous = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    new_edges = [
        [0, 14, 1, previous[0]],
        [1, 0, 2, previous[-1]],
        [2, 1, 16, 3],
        [3, 2, 4, previous[-2]],
        [4, 3, 5, previous[-3]],
        [5, 4, 17, 6],
        [6, 5, 7, previous[-4]],
        [7, 6, 8, previous[-5]],
        [8, 7, 18, 9],
        [9, 8, 10, previous[-6]],
        [10, 9, 11, previous[-7]],
        [11, 10, 19, 12],
        [12, 11, 13, previous[-8]],
        [13, 12, 14, previous[-9]],
        [14, 0, 13, 15],
        [15, 14, 19, 16],
        [16, 2, 15, 17],
        [17, 5, 16, 18],
        [18, 8, 17, 19],
        [19, 11, 18, 15],
    ]
    add_edges(G, pos, new_edges)

    print_adj_list(G)
    check(G)
    print("\n")
    return 1


def main(cap_type, cap_turn, cap_flip, num_rings, max_n):
    # bottom cap type
    if cap_type == 19:
        bc_v = 30
        new_edges = [
            [0, 1, 27, 9],
            [1, 2, 25, 0],
            [2, 22, 1, 3],
            [3, 2, 8, 4],
            [4, 3, 5, 20],
            [5, 4, 6, 17],
            [6, 5, 7, 15],
            [7, 6, 8, 12],
            [8, 3, 9, 7],
            [9, 0, 10, 8],
            [10, 29, 11, 9],
            [11, 12, 10],
            [12, 13, 7, 11],
            [13, 14, 12],
            [14, 15, 13],
            [15, 16, 6, 14],
            [16, 17, 15],
            [17, 18, 5, 16],
            [18, 19, 17],
            [19, 20, 18],
            [20, 21, 4, 19],
            [21, 22, 20],
            [22, 23, 2, 21],
            [23, 24, 22],
            [24, 25, 23],
            [25, 26, 1, 24],
            [26, 27, 25],
            [27, 28, 0, 26],
            [28, 29, 27],
            [29, 10, 28],
        ]
    elif cap_type == 20:
        bc_v = 36
        new_edges = [
            [0, 1, 13, 16],
            [1, 2, 0, 19],
            [2, 3, 1, 21],
            [3, 4, 12, 2],
            [4, 5, 3, 23],
            [5, 6, 10, 4],
            [6, 7, 5, 25],
            [7, 8, 6, 27],
            [8, 7, 30, 9],
            [9, 8, 32, 10],
            [10, 9, 11, 5],
            [11, 10, 34, 12],
            [12, 11, 13, 3],
            [13, 12, 14, 0],
            [14, 13, 35, 15],
            [15, 16, 14],
            [16, 17, 0, 15],
            [17, 18, 16],
            [18, 19, 17],
            [19, 20, 1, 18],
            [20, 21, 19],
            [21, 22, 2, 20],
            [22, 23, 21],
            [23, 24, 4, 22],
            [24, 25, 23],
            [25, 26, 6, 24],
            [26, 27, 25],
            [27, 28, 7, 26],
            [28, 29, 27],
            [29, 30, 28],
            [30, 31, 8, 29],
            [31, 32, 30],
            [32, 33, 9, 31],
            [33, 34, 32],
            [34, 35, 11, 33],
            [35, 14, 34],
        ]
    elif cap_type == 21:
        bc_v = 42
        new_edges = [
            [0, 1, 39, 15],
            [1, 2, 37, 0],
            [2, 3, 1, 14],
            [3, 2, 4, 35],
            [4, 3, 13, 5],
            [5, 4, 6, 33],
            [6, 5, 11, 7],
            [7, 6, 8, 31],
            [8, 7, 9, 28],
            [9, 8, 10, 26],
            [10, 11, 17, 9],
            [11, 12, 10, 6],
            [12, 13, 18, 11],
            [13, 14, 12, 4],
            [14, 2, 16, 13],
            [15, 0, 20, 16],
            [16, 14, 15, 19],
            [17, 10, 18, 24],
            [18, 12, 19, 17],
            [19, 18, 16, 22],
            [20, 21, 15, 41],
            [21, 22, 20],
            [22, 23, 19, 21],
            [23, 24, 22],
            [24, 25, 17, 23],
            [25, 26, 24],
            [26, 27, 9, 25],
            [27, 28, 26],
            [28, 29, 8, 27],
            [29, 30, 28],
            [30, 31, 29],
            [31, 32, 7, 30],
            [32, 33, 31],
            [33, 34, 5, 32],
            [34, 35, 33],
            [35, 36, 3, 34],
            [36, 37, 35],
            [37, 38, 1, 36],
            [38, 39, 37],
            [39, 40, 0, 38],
            [40, 41, 39],
            [41, 20, 40],
        ]
    elif cap_type == 22:
        bc_v = 48
        new_edges = [
            [0, 1, 5, 8],
            [1, 18, 2, 0],
            [2, 1, 21, 3],
            [3, 2, 24, 4],
            [4, 3, 27, 5],
            [5, 0, 4, 6],
            [6, 5, 29, 7],
            [7, 8, 6, 9],
            [8, 13, 0, 7],
            [9, 7, 31, 10],
            [10, 11, 9, 33],
            [11, 12, 13, 10],
            [12, 14, 11, 35],
            [13, 15, 8, 11],
            [14, 16, 15, 12],
            [15, 18, 13, 14],
            [16, 17, 14, 37],
            [17, 19, 16, 39],
            [18, 1, 15, 19],
            [19, 20, 18, 17],
            [20, 21, 19, 41],
            [21, 22, 2, 20],
            [22, 23, 21, 43],
            [23, 22, 45, 24],
            [24, 23, 25, 3],
            [25, 47, 26, 24],
            [26, 27, 25],
            [27, 28, 4, 26],
            [28, 29, 27],
            [29, 30, 6, 28],
            [30, 31, 29],
            [31, 32, 9, 30],
            [32, 33, 31],
            [33, 34, 10, 32],
            [34, 35, 33],
            [35, 36, 12, 34],
            [36, 37, 35],
            [37, 38, 16, 36],
            [38, 39, 37],
            [39, 40, 17, 38],
            [40, 41, 39],
            [41, 42, 20, 40],
            [42, 43, 41],
            [43, 44, 22, 42],
            [44, 45, 43],
            [45, 46, 23, 44],
            [46, 47, 45],
            [47, 25, 46],
        ]
    else:
        print("Invalid cap_type")
        exit(0)

    # num vertices in top cap for p = 12 and n == 4 (mod 6)
    tc_v = 34 + 24
    # num vertices in a ring
    ring_v = 24
    # total vertices in graph G
    num_v = bc_v + ring_v * num_rings + tc_v
    if num_v > max_n:
        return 0
    if (num_v - 70) % 30 == 0:
        return 1
    G = [[] for _ in range(num_v)]

    # fill in info for bottom cap (common cap)
    add_edges(G, 0, new_edges)

    # index of next vertex
    v_index = bc_v
    # add the rings (always at least one ring)
    for ring in range(num_rings + 1):
        add_ring(G, cap_type, v_index, ring)
        v_index += ring_v

    ## it is now time to complete the top cap
    new_edges = add_cap(cap_type, cap_turn, cap_flip, num_rings + 1)
    for edges in new_edges:
        if cap_flip == 0:
            # clock wise order
            order = [1, 2, 3]
        else:
            # counter clock wise order
            order = [1, 3, 2]
        for i in order:
            add_neighbor(G, edges[0] + v_index, edges[i] + v_index)
            if edges[i] < 0:
                add_neighbor(G, edges[i] + v_index, edges[0] + v_index)

    print_adj_list(G)
    check(G)
    print("\n")
    return 1


max_n = int(sys.argv[1])

for cap_type in range(19, 23):
    for cap_turn in [0, 1, 2, 3]:
        # you can also flip the top cap
        for cap_flip in [0, 1]:
            num_rings = 0
            while main(cap_type, cap_turn, cap_flip, num_rings, max_n):
                num_rings += 1

num_rings = 0
while unique_family(max_n, num_rings):
    num_rings += 1
