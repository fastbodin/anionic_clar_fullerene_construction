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
        # mystr = "3"
        mystr = "{:3d}".format(v)
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
                mystr += "~{:3d} but {:3d}!~{:3d}".format(G[v][i], G[v][i], v)
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
        if cap_type == 1:
            prev_r_v = shift_by_turns([-14, -1, -3, -5, -6, -7, -9, -11, -13], cap_turn)
        elif cap_type == 2:
            prev_r_v = shift_by_turns(
                [-14, -1, -3, -5, -7, -8, -10, -12, -13], cap_turn
            )
        elif cap_type == 3:
            prev_r_v = shift_by_turns(
                [-5, -7, -9, -11, -13, -15, -16, -1, -3], cap_turn
            )
        elif cap_type == 4:
            prev_r_v = shift_by_turns(
                [-5, -7, -9, -11, -13, -14, -15, -1, -3], cap_turn
            )
        elif cap_type == 5:
            prev_r_v = shift_by_turns(
                [-5, -7, -9, -11, -13, -15, -16, -1, -3], cap_turn
            )
        elif cap_type == 6:
            prev_r_v = shift_by_turns(
                [-5, -7, -8, -10, -12, -13, -15, -1, -3], cap_turn
            )
        elif cap_type == 7:
            prev_r_v = shift_by_turns(
                [-5, -7, -9, -11, -13, -14, -16, -1, -3], cap_turn
            )
        elif cap_type == 8:
            prev_r_v = shift_by_turns(
                [-4, -6, -8, -10, -12, -13, -15, -1, -2], cap_turn
            )
        elif cap_type == 9:
            prev_r_v = shift_by_turns(
                [-10, -12, -14, -16, -1, -2, -4, -6, -8], cap_turn
            )

        else:
            print("bad cap_type")
            exit(0)
    elif num_rings % 3 == 1:
        prev_r_v = shift_by_turns([-1, -3, -5, -7, -9, -11, -13, -15, -17], cap_turn)
    elif num_rings % 3 == 2:
        prev_r_v = shift_by_turns([-3, -5, -7, -9, -11, -13, -15, -17, -1], cap_turn)
    elif num_rings % 3 == 0:
        prev_r_v = shift_by_turns([-5, -7, -9, -11, -13, -15, -17, -1, -3], cap_turn)
    else:
        print("bad num_rings")
        exit(0)

    # preform a flip
    if cap_flip == 1:
        prev_r_v = r_cycle(prev_r_v)

    if cap_type == 3:
        new_edges = [
            [0, 1, 15, prev_r_v[0]],
            [1, 2, 18, 0],
            [2, 3, 1, prev_r_v[1]],
            [3, 4, 2, prev_r_v[2]],
            [4, 5, 19, 3],
            [5, 6, 4, prev_r_v[3]],
            [6, 7, 21, 5],
            [7, 8, 6, prev_r_v[4]],
            [8, 9, 22, 7],
            [9, 10, 8, prev_r_v[5]],
            [10, 11, 24, 9],
            [11, 12, 10, prev_r_v[6]],
            [12, 13, 26, 11],
            [13, 14, 12, prev_r_v[7]],
            [14, 15, 13, prev_r_v[8]],
            [15, 0, 16, 14],
            [16, 17, 26, 15],
            [17, 18, 27, 16],
            [18, 19, 17, 1],
            [19, 4, 20, 18],
            [20, 19, 21, 28],
            [21, 20, 6, 22],
            [22, 21, 8, 23],
            [23, 22, 24, 28],
            [24, 23, 10, 25],
            [25, 27, 24, 26],
            [26, 25, 12, 16],
            [27, 28, 25, 17],
            [28, 20, 23, 27],
        ]
    else:
        # top cap
        new_edges = [
            [0, 1, 14, prev_r_v[0]],
            [1, 0, 2, 15],
            [2, 1, prev_r_v[1], 3],
            [3, 2, 4, 16],
            [4, 3, prev_r_v[2], 5],
            [5, 6, 17, 4],
            [6, 7, 5, prev_r_v[3]],
            [7, 8, 6, prev_r_v[4]],
            [8, 9, 18, 7],
            [9, 8, prev_r_v[5], 10],
            [10, 9, 11, 19],
            [11, 10, prev_r_v[6], 12],
            [12, 11, prev_r_v[7], 13],
            [13, 12, 14, 20],
            [14, 13, prev_r_v[8], 0],
            [15, 1, 16, 20],
            [16, 3, 17, 15],
            [17, 5, 18, 16],
            [18, 8, 19, 17],
            [19, 10, 20, 18],
            [20, 19, 13, 15],
        ]
    return new_edges


def add_ring(G, cap_type, v_index, ring_num):
    new_edges = []
    # ring is added to bottom cap
    if ring_num == 1:
        # vertices missing edges on bottom cap are listed (w/ relative numbering)
        # in clock-wise order
        if cap_type == 1:
            prev_r_v = [-1, -14, -13, -11, -9, -7, -6, -5, -3]
        elif cap_type == 2:
            prev_r_v = [-1, -14, -13, -12, -10, -8, -7, -5, -3]
        elif cap_type == 3:
            prev_r_v = [-1, -16, -15, -13, -11, -9, -7, -5, -3]
        elif cap_type == 4:
            prev_r_v = [-1, -15, -14, -13, -11, -9, -7, -5, -3]
        elif cap_type == 5:
            prev_r_v = [-1, -16, -15, -13, -11, -9, -7, -5, -3]
        elif cap_type == 6:
            prev_r_v = [-1, -15, -13, -12, -10, -8, -7, -5, -3]
        elif cap_type == 7:
            prev_r_v = [-1, -16, -14, -13, -11, -9, -7, -5, -3]
        elif cap_type == 8:
            prev_r_v = [-1, -15, -13, -12, -10, -8, -6, -4, -2]
        elif cap_type == 9:
            prev_r_v = [-6, -4, -2, -1, -16, -14, -12, -10, -8]

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
    if cap_type == 1:
        bc_v = 19
        new_edges = [
            [0, 1, 11, 15],
            [1, 0, 2, 9],
            [2, 3, 1, 17],
            [3, 2, 4, 7],
            [4, 5, 3, 18],
            [5, 6, 4],
            [6, 7, 5],
            [7, 8, 3, 6],
            [8, 9, 7],
            [9, 10, 1, 8],
            [10, 11, 9],
            [11, 12, 0, 10],
            [12, 13, 11],
            [13, 14, 12],
            [14, 15, 13],
            [15, 16, 0, 14],
            [16, 17, 15],
            [17, 18, 2, 16],
            [18, 4, 17],
        ]
    elif cap_type == 2:
        bc_v = 21
        new_edges = [
            [0, 1, 4, 12],
            [1, 0, 15, 2],
            [2, 1, 17, 3],
            [3, 2, 19, 4],
            [4, 0, 3, 5],
            [5, 4, 6, 10],
            [6, 7, 5, 20],
            [7, 8, 6],
            [8, 9, 7],
            [9, 10, 8],
            [10, 11, 5, 9],
            [11, 12, 10],
            [12, 13, 0, 11],
            [13, 14, 12],
            [14, 15, 13],
            [15, 16, 1, 14],
            [16, 17, 15],
            [17, 18, 2, 16],
            [18, 19, 17],
            [19, 20, 3, 18],
            [20, 6, 19],
        ]
    elif cap_type == 3:
        bc_v = 33
        new_edges = [
            [0, 1, 4, 23],
            [1, 0, 25, 2],
            [2, 1, 8, 3],
            [3, 2, 7, 4],
            [4, 0, 3, 5],
            [5, 4, 6, 21],
            [6, 5, 10, 13],
            [7, 3, 9, 10],
            [8, 2, 27, 9],
            [9, 8, 11, 7],
            [10, 7, 12, 6],
            [11, 9, 29, 12],
            [12, 11, 15, 10],
            [13, 6, 14, 19],
            [14, 15, 16, 13],
            [15, 12, 31, 14],
            [16, 14, 32, 17],
            [17, 18, 16],
            [18, 19, 17],
            [19, 20, 13, 18],
            [20, 21, 19],
            [21, 22, 5, 20],
            [22, 23, 21],
            [23, 24, 0, 22],
            [24, 25, 23],
            [25, 26, 1, 24],
            [26, 27, 25],
            [27, 28, 8, 26],
            [28, 29, 27],
            [29, 30, 11, 28],
            [30, 31, 29],
            [31, 32, 15, 30],
            [32, 16, 31],
        ]
    elif cap_type == 4:
        bc_v = 25
        new_edges = [
            [0, 1, 3, 17],
            [1, 0, 19, 2],
            [2, 4, 1, 21],
            [3, 0, 4, 5],
            [4, 2, 6, 3],
            [5, 3, 7, 15],
            [6, 4, 23, 7],
            [7, 6, 8, 5],
            [8, 7, 9, 13],
            [9, 10, 8, 24],
            [10, 11, 9],
            [11, 12, 10],
            [12, 13, 11],
            [13, 14, 8, 12],
            [14, 15, 13],
            [15, 16, 5, 14],
            [16, 17, 15],
            [17, 18, 0, 16],
            [18, 19, 17],
            [19, 20, 1, 18],
            [20, 21, 19],
            [21, 22, 2, 20],
            [22, 23, 21],
            [23, 24, 6, 22],
            [24, 9, 23],
        ]
    elif cap_type == 5:
        bc_v = 27
        new_edges = [
            [0, 19, 1, 3],
            [1, 0, 21, 2],
            [2, 1, 23, 4],
            [3, 0, 4, 5],
            [4, 2, 8, 3],
            [5, 3, 6, 17],
            [6, 5, 7, 15],
            [7, 8, 9, 6],
            [8, 4, 25, 7],
            [9, 7, 10, 13],
            [10, 9, 26, 11],
            [11, 12, 10],
            [12, 13, 11],
            [13, 14, 9, 12],
            [14, 15, 13],
            [15, 16, 6, 14],
            [16, 17, 15],
            [17, 18, 5, 16],
            [18, 19, 17],
            [19, 20, 0, 18],
            [20, 21, 19],
            [21, 22, 1, 20],
            [22, 23, 21],
            [23, 24, 2, 22],
            [24, 25, 23],
            [25, 26, 8, 24],
            [26, 10, 25],
        ]
    elif cap_type == 6:
        bc_v = 29
        new_edges = [
            [0, 1, 5, 20],
            [1, 0, 23, 2],
            [2, 1, 12, 3],
            [3, 2, 10, 4],
            [4, 3, 8, 5],
            [5, 0, 4, 6],
            [6, 5, 7, 18],
            [7, 6, 8, 15],
            [8, 4, 9, 7],
            [9, 8, 10, 13],
            [10, 9, 3, 11],
            [11, 10, 12, 27],
            [12, 11, 2, 25],
            [13, 9, 28, 14],
            [14, 15, 13],
            [15, 16, 7, 14],
            [16, 17, 15],
            [17, 18, 16],
            [18, 19, 6, 17],
            [19, 20, 18],
            [20, 21, 0, 19],
            [21, 22, 20],
            [22, 23, 21],
            [23, 24, 1, 22],
            [24, 25, 23],
            [25, 26, 12, 24],
            [26, 27, 25],
            [27, 28, 11, 26],
            [28, 13, 27],
        ]
    elif cap_type == 7:
        bc_v = 31
        new_edges = [
            [0, 1, 4, 23],
            [1, 0, 25, 2],
            [2, 1, 8, 3],
            [3, 2, 7, 4],
            [4, 0, 3, 5],
            [5, 21, 4, 6],
            [6, 5, 7, 11],
            [7, 3, 10, 6],
            [8, 2, 27, 9],
            [9, 8, 29, 10],
            [10, 9, 13, 7],
            [11, 6, 12, 19],
            [12, 11, 13, 16],
            [13, 12, 10, 14],
            [14, 15, 13, 30],
            [15, 16, 14],
            [16, 17, 12, 15],
            [17, 18, 16],
            [18, 19, 17],
            [19, 20, 11, 18],
            [20, 21, 19],
            [21, 22, 5, 20],
            [22, 23, 21],
            [23, 24, 0, 22],
            [24, 25, 23],
            [25, 26, 1, 24],
            [26, 27, 25],
            [27, 28, 8, 26],
            [28, 29, 27],
            [29, 30, 9, 28],
            [30, 14, 29],
        ]
    elif cap_type == 8:
        bc_v = 33
        new_edges = [
            [0, 1, 9, 24],
            [1, 0, 2, 8],
            [2, 1, 26, 3],
            [3, 2, 4, 7],
            [4, 3, 28, 5],
            [5, 4, 13, 6],
            [6, 5, 11, 7],
            [7, 3, 6, 8],
            [8, 1, 7, 10],
            [9, 0, 10, 16],
            [10, 8, 11, 9],
            [11, 10, 6, 12],
            [12, 11, 14, 15],
            [13, 5, 30, 14],
            [14, 13, 17, 12],
            [15, 12, 19, 16],
            [16, 9, 15, 22],
            [17, 14, 32, 18],
            [18, 19, 17],
            [19, 20, 15, 18],
            [20, 21, 19],
            [21, 22, 20],
            [22, 23, 16, 21],
            [23, 24, 22],
            [24, 25, 0, 23],
            [25, 26, 24],
            [26, 27, 2, 25],
            [27, 28, 26],
            [28, 29, 4, 27],
            [29, 30, 28],
            [30, 31, 13, 29],
            [31, 32, 30],
            [32, 17, 31],
        ]
    elif cap_type == 9:
        bc_v = 35
        new_edges = [
            [0, 1, 4, 7],
            [1, 0, 10, 2],
            [2, 1, 13, 3],
            [3, 4, 2, 15],
            [4, 0, 3, 5],
            [5, 6, 4, 17],
            [6, 7, 5, 20],
            [7, 8, 0, 6],
            [8, 9, 7, 22],
            [9, 24, 10, 8],
            [10, 11, 1, 9],
            [11, 26, 12, 10],
            [12, 28, 13, 11],
            [13, 12, 14, 2],
            [14, 13, 30, 15],
            [15, 3, 14, 16],
            [16, 15, 32, 17],
            [17, 5, 16, 18],
            [18, 17, 34, 19],
            [19, 20, 18],
            [20, 21, 6, 19],
            [21, 22, 20],
            [22, 23, 8, 21],
            [23, 24, 22],
            [24, 25, 9, 23],
            [25, 26, 24],
            [26, 27, 11, 25],
            [27, 28, 26],
            [28, 29, 12, 27],
            [29, 30, 28],
            [30, 31, 14, 29],
            [31, 32, 30],
            [32, 33, 16, 31],
            [33, 34, 32],
            [34, 18, 33],
        ]
    else:
        print("Invalid cap_type")
        exit(0)

    # num vertices in top cap for p = 4
    if cap_type == 3:
        tc_v = 29
    else:
        tc_v = 21
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

for cap_type in range(1, 10):
    if cap_type == 1:
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
    elif cap_type == 2:
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
    elif cap_type == 3:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 4:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 5:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 6:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 7:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 8:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
        main(cap_type, 1, 1, 0, max_n)
        main(cap_type, 2, 1, 0, max_n)
    elif cap_type == 9:
        main(cap_type, 0, 0, 0, max_n)
        main(cap_type, 1, 0, 0, max_n)
        main(cap_type, 2, 0, 0, max_n)
        main(cap_type, 0, 1, 0, max_n)
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
