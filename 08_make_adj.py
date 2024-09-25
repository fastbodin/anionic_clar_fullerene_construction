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
    # add top cap to bottom cap
    if num_rings == 0:
        # the starting vertex needs to match on the top and bottom cap
        # the bottom cap vertices are listed in counter clockwise order
        # since the vertices of the top cap list neighbors in clockwise order
        # things get twisted otherwise
        if cap_type == 10:
            prev_r_v = shift_by_turns(
                [-3, -5, -6, -8, -9, -10, -12, -1, -2], cap_turn
            )
        elif cap_type == 11:
            prev_r_v = shift_by_turns(
                [-13, -1, -2, -4, -6, -7, -8, -10, -11], cap_turn
            )
        elif cap_type == 12:
            prev_r_v = shift_by_turns(
                [-5, -7, -9, -11, -13, -14, -16, -1, -3], cap_turn
            )
        elif cap_type == 13:
            prev_r_v = shift_by_turns(
                [-14, -1, -2, -4, -6, -7, -9, -11, -13], cap_turn
            )
        elif cap_type == 14:
            prev_r_v = shift_by_turns(
                [-14, -1, -2, -4, -6, -7, -9, -11, -13], cap_turn
            )
        elif cap_type == 15:
            prev_r_v = shift_by_turns(
                [-5, -7, -8, -10, -12, -14, -15, -1, -3], cap_turn
            )
        elif cap_type == 16:
            prev_r_v = shift_by_turns(
                [-5, -7, -8, -10, -12, -14, -16, -1, -3], cap_turn
            )
        elif cap_type == 17:
            prev_r_v = shift_by_turns(
                [-5, -7, -8, -10, -12, -14, -16, -1, -3], cap_turn
            )
        elif cap_type == 18:
            prev_r_v = shift_by_turns(
                [-16, -1, -2, -4, -6, -8, -10, -12, -14], cap_turn
            )
        else:
            print("bad cap_type")
            exit(0)
    elif num_rings % 3 == 1:
        prev_r_v = shift_by_turns(
            [-1, -3, -5, -7, -9, -11, -13, -15, -17], cap_turn
        )
    elif num_rings % 3 == 2:
        prev_r_v = shift_by_turns(
            [-3, -5, -7, -9, -11, -13, -15, -17, -1], cap_turn
        )
    elif num_rings % 3 == 0:
        prev_r_v = shift_by_turns(
            [-5, -7, -9, -11, -13, -15, -17, -1, -3], cap_turn
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
        [0, 1, 16, prev_r_v[0]],
        [1, 2, 17, 0],
        [2, 3, 1, prev_r_v[1]],
        [3, 4, 19, 2],
        [4, 5, 3, prev_r_v[2]],
        [5, 6, 21, 4],
        [6, 7, 5, prev_r_v[3]],
        [7, 8, 22, 6],
        [8, 9, 7, prev_r_v[4]],
        [9, 10, 24, 8],
        [10, 11, 9, prev_r_v[5]],
        [11, 12, 26, 10],
        [12, 13, 11, prev_r_v[6]],
        [13, 14, 28, 12],
        [14, 15, 13, prev_r_v[7]],
        [15, 16, 14, prev_r_v[8]],
        [16, 0, 29, 15],
        [17, 1, 18, 30],
        [18, 19, 33, 17],
        [19, 3, 20, 18],
        [20, 21, 34, 19],
        [21, 20, 5, 22],
        [22, 21, 7, 23],
        [23, 22, 24, 35],
        [24, 23, 9, 25],
        [25, 24, 26, 36],
        [26, 25, 11, 27],
        [27, 31, 26, 28],
        [28, 29, 27, 13],
        [29, 30, 28, 16],
        [30, 17, 31, 29],
        [31, 32, 27, 30],
        [32, 33, 36, 31],
        [33, 18, 34, 32],
        [34, 20, 35, 33],
        [35, 34, 23, 36],
        [36, 35, 25, 32],
    ]
    return new_edges


def add_ring(G, cap_type, v_index, ring_num):
    new_edges = []
    # ring is added to bottom cap
    if ring_num == 1:
        # vertices missing edges on bottom cap are listed (w/ relative numbering)
        # in clock-wise order
        if cap_type == 10:
            prev_r_v = [-1, -12, -10, -9, -8, -6, -5, -3, -2]
        elif cap_type == 11:
            prev_r_v = [-1, -13, -11, -10, -8, -7, -6, -4, -2]
        elif cap_type == 12:
            prev_r_v = [-1, -16, -14, -13, -11, -9, -7, -5, -3]
        elif cap_type == 13:
            prev_r_v = [-1, -14, -13, -11, -9, -7, -6, -4, -2]
        elif cap_type == 14:
            prev_r_v = [-1, -14, -13, -11, -9, -7, -6, -4, -2]
        elif cap_type == 15:
            prev_r_v = [-1, -15, -14, -12, -10, -8, -7, -5, -3]
        elif cap_type == 16:
            prev_r_v = [-1, -16, -14, -12, -10, -8, -7, -5, -3]
        elif cap_type == 17:
            prev_r_v = [-1, -16, -14, -12, -10, -8, -7, -5, -3]
        elif cap_type == 18:
            prev_r_v = [-1, -16, -14, -12, -10, -8, -6, -4, -2]
        else:
            print("bad cap_type")
            exit(0)
    # ring is added to another ring
    else:
        # vertices in privious ring missing edges are listed (w/ relative numbering)
        # in clock-wise order
        prev_r_v = [-1, -17, -15, -13, -11, -9, -7, -5, -3]
    # same numbering system for all rings
    new_edges = [
        [0, 17, 1, prev_r_v[0]],
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
        [17, 0, 16],
    ]

    add_edges(G, v_index, new_edges)


def main(cap_type, cap_turn, cap_flip, num_rings, max_n):
    # bottom cap type
    if cap_type == 10:
        bc_v = 15
        new_edges = [
            [0, 1, 4, 8],
            [1, 0, 11, 2],
            [2, 14, 3, 1],
            [3, 4, 2],
            [4, 5, 0, 3],
            [5, 6, 4],
            [6, 7, 5],
            [7, 8, 6],
            [8, 9, 0, 7],
            [9, 10, 8],
            [10, 11, 9],
            [11, 12, 1, 10],
            [12, 13, 11],
            [13, 14, 12],
            [14, 2, 13],
        ]
    elif cap_type == 11:
        bc_v = 17
        new_edges = [
            [0, 1, 8, 12],
            [1, 2, 5, 0],
            [2, 14, 3, 1],
            [3, 16, 4, 2],
            [4, 5, 3],
            [5, 4, 6, 1],
            [6, 7, 5],
            [7, 8, 6],
            [8, 7, 9, 0],
            [9, 10, 8],
            [10, 11, 9],
            [11, 12, 10],
            [12, 13, 0, 11],
            [13, 14, 12],
            [14, 15, 2, 13],
            [15, 16, 14],
            [16, 3, 15],
        ]
    elif cap_type == 12:
        bc_v = 37
        new_edges = [
            [0, 1, 5, 9],
            [1, 2, 0, 11],
            [2, 1, 13, 3],
            [3, 2, 16, 4],
            [4, 3, 18, 5],
            [5, 4, 6, 0],
            [6, 5, 19, 7],
            [7, 8, 6, 22],
            [8, 9, 7, 25],
            [9, 10, 0, 8],
            [10, 9, 27, 11],
            [11, 12, 1, 10],
            [12, 13, 11, 29],
            [13, 14, 2, 12],
            [14, 31, 15, 13],
            [15, 14, 33, 16],
            [16, 15, 17, 3],
            [17, 16, 35, 18],
            [18, 17, 19, 4],
            [19, 18, 20, 6],
            [20, 19, 36, 21],
            [21, 22, 20],
            [22, 23, 7, 21],
            [23, 24, 22],
            [24, 25, 23],
            [25, 26, 8, 24],
            [26, 27, 25],
            [27, 28, 10, 26],
            [28, 29, 27],
            [29, 30, 12, 28],
            [30, 31, 29],
            [31, 32, 14, 30],
            [32, 33, 31],
            [33, 32, 34, 15],
            [34, 35, 33],
            [35, 34, 36, 17],
            [36, 20, 35],
        ]
    elif cap_type == 13:
        bc_v = 21
        new_edges = [
            [0, 1, 5, 9],
            [1, 2, 0, 11],
            [2, 1, 13, 3],
            [3, 2, 16, 4],
            [4, 3, 18, 5],
            [5, 4, 6, 0],
            [6, 5, 20, 7],
            [7, 8, 6],
            [8, 9, 7],
            [9, 10, 0, 8],
            [10, 11, 9],
            [11, 12, 1, 10],
            [12, 13, 11],
            [13, 14, 2, 12],
            [14, 15, 13],
            [15, 16, 14],
            [16, 17, 3, 15],
            [17, 18, 16],
            [18, 17, 19, 4],
            [19, 20, 18],
            [20, 6, 19],
        ]
    elif cap_type == 14:
        bc_v = 23
        new_edges = [
            [0, 1, 7, 11],
            [1, 2, 5, 0],
            [2, 3, 1, 13],
            [3, 4, 2, 15],
            [4, 18, 5, 3],
            [5, 6, 1, 4],
            [6, 20, 7, 5],
            [7, 6, 8, 0],
            [8, 7, 22, 9],
            [9, 10, 8],
            [10, 11, 9],
            [11, 12, 0, 10],
            [12, 13, 11],
            [13, 14, 2, 12],
            [14, 15, 13],
            [15, 16, 3, 14],
            [16, 17, 15],
            [17, 18, 16],
            [18, 19, 4, 17],
            [19, 20, 18],
            [20, 21, 6, 19],
            [21, 22, 20],
            [22, 8, 21],
        ]
    elif cap_type == 15:
        bc_v = 25
        new_edges = [
            [0, 1, 8, 12],
            [1, 2, 6, 0],
            [2, 3, 1, 14],
            [3, 2, 16, 4],
            [4, 5, 3, 19],
            [5, 6, 4, 21],
            [6, 7, 1, 5],
            [7, 8, 6, 23],
            [8, 0, 7, 9],
            [9, 24, 10, 8],
            [10, 11, 9],
            [11, 12, 10],
            [12, 13, 0, 11],
            [13, 14, 12],
            [14, 15, 2, 13],
            [15, 16, 14],
            [16, 17, 3, 15],
            [17, 18, 16],
            [18, 19, 17],
            [19, 20, 4, 18],
            [20, 21, 19],
            [21, 22, 5, 20],
            [22, 23, 21],
            [23, 24, 7, 22],
            [24, 9, 23],
        ]
    elif cap_type == 16:
        bc_v = 27
        new_edges = [
            [0, 1, 9, 12],
            [1, 2, 0, 14],
            [2, 3, 7, 1],
            [3, 4, 2, 16],
            [4, 5, 3, 18],
            [5, 6, 4, 21],
            [6, 7, 5, 23],
            [7, 8, 2, 6],
            [8, 9, 7, 25],
            [9, 10, 0, 8],
            [10, 11, 9, 26],
            [11, 12, 10],
            [12, 13, 0, 11],
            [13, 14, 12],
            [14, 15, 1, 13],
            [15, 16, 14],
            [16, 17, 3, 15],
            [17, 18, 16],
            [18, 19, 4, 17],
            [19, 20, 18],
            [20, 21, 19],
            [21, 22, 5, 20],
            [22, 23, 21],
            [23, 24, 6, 22],
            [24, 25, 23],
            [25, 26, 8, 24],
            [26, 10, 25],
        ]
    elif cap_type == 17:
        bc_v = 29
        new_edges = [
            [0, 3, 7, 10],
            [1, 2, 11, 14],
            [2, 3, 1, 16],
            [3, 4, 0, 2],
            [4, 3, 18, 5],
            [5, 6, 4, 20],
            [6, 7, 5, 23],
            [7, 8, 0, 6],
            [8, 9, 7, 25],
            [9, 8, 27, 10],
            [10, 9, 11, 0],
            [11, 10, 12, 1],
            [12, 11, 28, 13],
            [13, 14, 12],
            [14, 15, 1, 13],
            [15, 16, 14],
            [16, 17, 2, 15],
            [17, 18, 16],
            [18, 19, 4, 17],
            [19, 20, 18],
            [20, 21, 5, 19],
            [21, 22, 20],
            [22, 23, 21],
            [23, 24, 6, 22],
            [24, 25, 23],
            [25, 26, 8, 24],
            [26, 27, 25],
            [27, 28, 9, 26],
            [28, 12, 27],
        ]
    elif cap_type == 18:
        bc_v = 31
        new_edges = [
            [0, 1, 5, 8],
            [1, 3, 0, 11],
            [2, 13, 16, 3],
            [3, 1, 2, 4],
            [4, 3, 18, 5],
            [5, 4, 6, 0],
            [6, 5, 20, 7],
            [7, 8, 6, 22],
            [8, 0, 7, 9],
            [9, 10, 8, 24],
            [10, 11, 9, 26],
            [11, 12, 1, 10],
            [12, 13, 11, 28],
            [13, 2, 12, 14],
            [14, 15, 13, 30],
            [15, 16, 14],
            [16, 17, 2, 15],
            [17, 18, 16],
            [18, 19, 4, 17],
            [19, 20, 18],
            [20, 21, 6, 19],
            [21, 22, 20],
            [22, 23, 7, 21],
            [23, 24, 22],
            [24, 25, 9, 23],
            [25, 26, 24],
            [26, 27, 10, 25],
            [27, 28, 26],
            [28, 29, 12, 27],
            [29, 30, 28],
            [30, 14, 29],
        ]
    else:
        print("Invalid cap_type")
        exit(0)

    # num vertices in top cap for p = 6
    tc_v = 37
    # num vertices in a ring
    ring_v = 18
    # total vertices in graph G
    num_v = bc_v + ring_v * num_rings + tc_v
    if num_v > max_n:
        return 0
    G = [[] for _ in range(num_v)]

    # fill in info for bottom cap (common cap)
    add_edges(G, 0, new_edges)

    # index of next vertex
    v_index = bc_v
    # add the rings
    if num_rings > 0:
        for ring in range(1, num_rings + 1):
            add_ring(G, cap_type, v_index, ring)
            v_index += ring_v

    ## it is now time to complete the top cap
    new_edges = add_cap(cap_type, cap_turn, cap_flip, num_rings)
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

for cap_type in range(10, 19):
    if cap_type == 10:
        pass
    elif cap_type == 11:
        pass
    elif cap_type == 12:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 13:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 14:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 15:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 16:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 17:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 18:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    else:
        sys.exit(0)

    # the top cap has the dihedral group
    # there are three possible rotations of the top cap given the ring
    for cap_turn in [0, 1, 2]:
        # you can also flip the top cap
        for cap_flip in [0, 1]:
            # for each number of rings
            num_rings = 1
            while main(cap_type, cap_turn, cap_flip, num_rings, max_n):
                num_rings += 1
