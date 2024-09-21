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
        #mystr = "{:3d}".format(v)
        for u in range(len(G[v])):
            mystr += " {:3d}".format(G[v][u])
            v_deg +=1
        if (v_deg != 3):
            print('bad degree = {}'.format(v_deg))

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
                mystr += "~{:3d} but {:3d}!~{:3d} {}".format(G[v][i],G[v][i],v,num_v)
                print(mystr)

# because of the rings, when you flip the top cap over, you have to also shift
# it by one else the faces do not line up properly
def shift_one(input_list):
    temp_list = []
    # given an original list [0,1,2,3,4,....,10],
    # output [0,1,2,4,...,10,1]
    for i in range(1, len(input_list)):
        temp_list.append(input_list[i])
    temp_list.append(input_list[0])
    return temp_list

def shift_by_turns(input_list, num_turns):
    if num_turns == 0:
        return input_list
    else:
        temp_list = []
        # given an original list [0,1,2,3,4,....,10]
        # each turn shifts first two vertices in front to back
        # i.e. one turn gives [2,3,4,....,10,0,1]
        # two turns gives [4,5,....,10,0,1,2,3]
        for i in range(2*num_turns, len(input_list)):
            temp_list.append(input_list[i])
        for i in range(0,2*num_turns):
            temp_list.append(input_list[i])
    return temp_list

def r_cycle(input_list):
    input_list = shift_one(input_list)
    temp_list = []
    temp_list.append(input_list[0])
    # by starting at the first vertex, you can either read the list forward
    # or backward. In this case, you read the list backwards (representing a flip
    # of a cap)
    for i in range(len(input_list)-1, 0,-1):
        temp_list.append(input_list[i])
    return temp_list

def add_cap(cap_turn, cap_flip):
    prev_r_v = shift_by_turns([-14,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13], cap_turn)

    # preform a flip
    if cap_flip == 1:
        prev_r_v = r_cycle(prev_r_v)

    # top cap
    # clockwise order
    new_edges = [[0,14,13,prev_r_v[0]],
                 [1,2,15,prev_r_v[1]],
                 [2,18,1,prev_r_v[2]],
                 [3,4,19,prev_r_v[3]],
                 [4,22,3,prev_r_v[4]],
                 [5,6,23,prev_r_v[5]],
                 [6,26,5,prev_r_v[6]],
                 [7,8,27,prev_r_v[7]],
                 [8,30,7,prev_r_v[8]],
                 [9,10,31,prev_r_v[9]],
                 [10,34,9,prev_r_v[10]],
                 [11,12,35,prev_r_v[11]],
                 [12,38,11,prev_r_v[12]],
                 [13,0,39,prev_r_v[13]],
                 [14,15,41,0],
                 [15,1,16,14],
                 [16,17,43,15],
                 [17,44,16,18],
                 [18,19,17,2],
                 [19,20,18,3],
                 [20,21,44,19],
                 [21,22,45,20],
                 [22,23,21,4],
                 [23,5,24,22],
                 [24,23,25,45],
                 [25,26,46,24],
                 [26,27,25,6],
                 [27,7,28,26],
                 [28,29,47,27],
                 [29,28,30,48],
                 [30,29,8,31],
                 [31,32,30,9],
                 [32,48,31,33],
                 [33,32,34,49],
                 [34,33,10,35],
                 [35,36,34,11],
                 [36,49,35,37],
                 [37,50,36,38],
                 [38,37,12,39],
                 [39,40,38,13],
                 [40,41,50,39],
                 [41,14,42,40],
                 [42,43,51,41],
                 [43,16,52,42],
                 [44,20,53,17],
                 [45,24,54,21],
                 [46,25,47,55],
                 [47,46,28,58],
                 [48,29,32,59],
                 [49,33,36,60],
                 [50,61,37,40],
                 [51,42,57,61],
                 [52,53,56,43],
                 [53,44,54,52],
                 [54,45,55,53],
                 [55,54,46,56],
                 [56,55,57,52],
                 [57,56,58,51],
                 [58,47,59,57],
                 [59,58,48,60],
                 [60,59,49,61],
                 [61,51,60,50]
                ]
    return new_edges

def add_ring(G, v_index):
    # vertices in previous ring missing edges are listed (w/ relative numbering)
    # in clock-wise order
    prev_r_v = [-1,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2]
    # same numbering system for all rings
    new_edges = [[0,13,14,prev_r_v[0]],
                 [1,15,2,prev_r_v[1]],
                 [2,1,16,prev_r_v[2]],
                 [3,17,4,prev_r_v[3]],
                 [4,3,18,prev_r_v[4]],
                 [5,19,6,prev_r_v[5]],
                 [6,5,20,prev_r_v[6]],
                 [7,21,8,prev_r_v[7]],
                 [8,7,22,prev_r_v[8]],
                 [9,23,10,prev_r_v[9]],
                 [10,9,24,prev_r_v[10]],
                 [11,25,12,prev_r_v[11]],
                 [12,11,26,prev_r_v[12]],
                 [13,27,0,prev_r_v[13]],
                 [14,0,28,15],
                 [15,14,29,1],
                 [16,2,30,17],
                 [17,3,16,31],
                 [18,4,32,19],
                 [19,5,18,33],
                 [20,6,34,21],
                 [21,7,20,35],
                 [22,8,36,23],
                 [23,9,22,37],
                 [24,25,10,38],
                 [25,24,39,11],
                 [26,40,27,12],
                 [27,26,41,13],
                 [28,14,41],
                 [29,30,15],
                 [30,16,29],
                 [31,32,17],
                 [32,18,31],
                 [33,34,19],
                 [34,20,33],
                 [35,36,21],
                 [36,22,35],
                 [37,38,23],
                 [38,24,37],
                 [39,40,25],
                 [40,26,39],
                 [41,28,27]
                ]

    add_edges(G, v_index, new_edges)


def main(cap_type, cap_turn, cap_flip, num_rings, max_n):

    # bottom cap type
    if cap_type == 23:
        bc_v = 48
        new_edges = [[0,10,14,7],
                     [1,6,15,2],
                     [2,3,1,18],
                     [3,4,2,21],
                     [4,5,3,24],
                     [5,6,4,27],
                     [6,7,1,5],
                     [7,8,0,6],
                     [8,9,7,28],
                     [9,10,8,31],
                     [10,11,0,9],
                     [11,12,10,33],
                     [12,13,11,34],
                     [13,12,35,14],
                     [14,13,15,0],
                     [15,14,16,1],
                     [16,15,36,17],
                     [17,16,37,18],
                     [18,2,17,19],
                     [19,18,38,20],
                     [20,21,19,39],
                     [21,3,20,22],
                     [22,21,40,23],
                     [23,24,22,41],
                     [24,25,4,23],
                     [25,26,24,42],
                     [26,43,27,25],
                     [27,28,5,26],
                     [28,29,8,27],
                     [29,30,28,44],
                     [30,31,29,45],
                     [31,32,9,30],
                     [32,33,31,46],
                     [33,11,32,47],
                     [34,12,47],
                     [35,36,13],
                     [36,16,35],
                     [37,38,17],
                     [38,19,37],
                     [39,40,20],
                     [40,22,39],
                     [41,42,23],
                     [42,25,41],
                     [43,44,26],
                     [44,29,43],
                     [45,46,30],
                     [46,32,45],
                     [47,34,33]
                     ]

    elif cap_type == 24:
        bc_v = 54
        new_edges = [
                    [53,40,14],
                    [40,15,53],
                    [41,42,16],
                    [42,17,41],
                    [43,44,18],
                    [44,19,43],
                    [45,46,20],
                    [46,21,45],
                    [47,48,22],
                    [48,23,47],
                    [49,50,24],
                    [50,25,49],
                    [51,52,26],
                    [52,27,51],
                    [14,28,27,53],
                    [15,29,40,16],
                    [16,30,15,41],
                    [17,30,42,18],
                    [18,31,17,43],
                    [19,20,31,44],
                    [20,32,19,45],
                    [21,22,33,46],
                    [22,47,34,21],
                    [23,48,24,34],
                    [24,49,35,23],
                    [25,50,26,36],
                    [26,51,37,25],
                    [27,52,14,37],
                    [28,5,14,29],
                    [29,28,15,38],
                    [30,39,16,17],
                    [31,1,18,19],
                    [32,33,2,20],
                    [33,11,32,21],
                    [34,23,12,22],
                    [35,36,13,24],
                    [36,35,25,8],
                    [37,27,9,26],
                    [38,4,29,39],
                    [39,38,30,1],
                    [1,2,39,31],
                    [2,32,3,1],
                    [3,10,4,2],
                    [4,3,6,38],
                    [5,6,9,28],
                    [6,4,7,5],
                    [7,0,8,6],
                    [8,7,36,9],
                    [9,8,37,5],
                    [10,11,0,3],
                    [11,12,10,33],
                    [12,34,13,11],
                    [13,12,35,0],
                    [0,13,7,10],
                    ]

    elif cap_type == 25:
        bc_v = 60
        new_edges = [
                    [59,46,14],
                    [46,15,59],
                    [47,48,16],
                    [48,17,47],
                    [49,50,18],
                    [50,19,49],
                    [51,52,20],
                    [52,21,51],
                    [53,54,22],
                    [54,23,53],
                    [55,56,24],
                    [56,25,55],
                    [57,58,26],
                    [58,27,57],
                    [14,28,27,59],
                    [15,28,46,16],
                    [16,29,15,47],
                    [17,30,48,18],
                    [18,31,17,49],
                    [19,20,32,50],
                    [20,33,19,51],
                    [21,22,33,52],
                    [22,53,34,21],
                    [23,54,24,35],
                    [24,55,36,23],
                    [25,56,26,36],
                    [26,57,37,25],
                    [27,58,14,38],
                    [28,39,14,15],
                    [29,30,40,16],
                    [30,41,29,17],
                    [31,32,42,18],
                    [32,43,31,19],
                    [33,21,44,20],
                    [34,22,35,45],
                    [35,23,1,34],
                    [36,24,25,2],
                    [37,38,3,26],
                    [38,4,37,27],
                    [39,4,28,40],
                    [40,6,39,29],
                    [41,42,7,30],
                    [42,8,41,31],
                    [43,44,9,32],
                    [44,33,45,43],
                    [45,34,10,44],
                    [1,35,2,11],
                    [2,1,36,3],
                    [3,2,37,12],
                    [4,38,39,5],
                    [5,12,4,6],
                    [6,7,5,40],
                    [7,0,6,41],
                    [8,9,0,42],
                    [9,43,10,8],
                    [10,45,11,9],
                    [11,1,13,10],
                    [12,3,5,13],
                    [13,11,12,0],
                    [0,13,7,8],
                    ]

    elif cap_type == 26:
        bc_v = 66
        new_edges = [
                    [65,52,14],
                    [52,15,65],
                    [53,54,16],
                    [54,17,53],
                    [55,56,18],
                    [56,19,55],
                    [57,58,20],
                    [58,21,57],
                    [59,60,22],
                    [60,23,59],
                    [61,62,24],
                    [62,25,61],
                    [63,64,26],
                    [64,27,63],
                    [14,28,27,65],
                    [15,28,52,16],
                    [16,29,15,53],
                    [17,30,54,18],
                    [18,31,17,55],
                    [19,20,32,56],
                    [20,33,19,57],
                    [21,22,33,58],
                    [22,59,34,21],
                    [23,60,24,35],
                    [24,61,36,23],
                    [25,62,26,37],
                    [26,63,38,25],
                    [27,64,14,39],
                    [28,41,14,15],
                    [29,30,42,16],
                    [30,43,29,17],
                    [31,32,44,18],
                    [32,45,31,19],
                    [33,21,46,20],
                    [34,22,35,47],
                    [35,23,48,34],
                    [36,24,37,49],
                    [37,25,50,36],
                    [38,26,39,51],
                    [39,40,38,27],
                    [40,1,39,41],
                    [41,42,40,28],
                    [42,2,41,29],
                    [43,44,3,30],
                    [44,4,43,31],
                    [45,46,5,32],
                    [46,47,45,33],
                    [47,34,6,46],
                    [48,35,49,7],
                    [49,48,36,8],
                    [50,51,9,37],
                    [51,38,10,50],
                    [1,10,40,2],
                    [2,1,42,3],
                    [3,12,2,43],
                    [4,5,13,44],
                    [5,6,4,45],
                    [6,47,7,5],
                    [7,48,0,6],
                    [8,49,9,0],
                    [9,50,11,8],
                    [10,11,51,1],
                    [11,12,9,10],
                    [12,13,11,3],
                    [13,0,12,4],
                    [0,8,13,7],
                    ]

    elif cap_type == 27:
        bc_v = 72
        new_edges = [
                    [71,58,14],
                    [58,15,71],
                    [59,60,16],
                    [60,17,59],
                    [61,62,18],
                    [62,19,61],
                    [63,64,20],
                    [64,21,63],
                    [65,66,22],
                    [66,23,65],
                    [67,68,24],
                    [68,25,67],
                    [69,70,26],
                    [70,27,69],
                    [14,28,27,71],
                    [15,29,58,16],
                    [16,30,15,59],
                    [17,31,60,18],
                    [18,32,17,61],
                    [19,20,33,62],
                    [20,34,19,63],
                    [21,22,35,64],
                    [22,65,36,21],
                    [23,66,24,36],
                    [24,67,37,23],
                    [25,68,26,38],
                    [26,69,39,25],
                    [27,70,14,39],
                    [28,53,14,29],
                    [29,40,28,15],
                    [30,41,16,31],
                    [31,42,30,17],
                    [32,33,43,18],
                    [33,44,32,19],
                    [34,35,45,20],
                    [35,21,46,34],
                    [36,23,47,22],
                    [37,24,38,48],
                    [38,25,51,37],
                    [39,26,27,52],
                    [40,54,29,41],
                    [41,55,40,30],
                    [42,43,56,31],
                    [43,57,42,32],
                    [44,45,1,33],
                    [45,34,2,44],
                    [46,47,3,35],
                    [47,36,48,46],
                    [48,37,49,47],
                    [49,48,50,4],
                    [50,51,5,49],
                    [51,38,52,50],
                    [52,51,39,53],
                    [53,52,28,6],
                    [54,6,40,7],
                    [55,56,7,41],
                    [56,8,55,42],
                    [57,1,8,43],
                    [1,9,57,44],
                    [2,3,9,45],
                    [3,46,4,2],
                    [4,49,10,3],
                    [5,50,6,11],
                    [6,5,53,54],
                    [7,12,54,55],
                    [8,13,56,57],
                    [9,2,0,1],
                    [10,4,11,0],
                    [11,5,12,10],
                    [12,11,7,13],
                    [13,12,8,0],
                    [0,10,13,9],
                    ]

    elif cap_type == 28:
        bc_v = 78
        new_edges = [
                    [77,64,14],
                    [64,15,77],
                    [65,66,16],
                    [66,17,65],
                    [67,68,18],
                    [68,19,67],
                    [69,70,20],
                    [70,21,69],
                    [71,72,22],
                    [72,23,71],
                    [73,74,24],
                    [74,25,73],
                    [75,76,26],
                    [76,27,75],
                    [14,28,27,77],
                    [15,29,64,16],
                    [16,30,15,65],
                    [17,31,66,18],
                    [18,32,17,67],
                    [19,20,33,68],
                    [20,34,19,69],
                    [21,22,35,70],
                    [22,71,36,21],
                    [23,72,24,37],
                    [24,73,38,23],
                    [25,74,26,38],
                    [26,75,39,25],
                    [27,76,14,40],
                    [28,54,14,29],
                    [29,41,28,15],
                    [30,42,16,31],
                    [31,43,30,17],
                    [32,33,44,18],
                    [33,45,32,19],
                    [34,35,46,20],
                    [35,21,47,34],
                    [36,37,48,22],
                    [37,36,23,49],
                    [38,24,25,50],
                    [39,26,40,51],
                    [40,39,27,53],
                    [41,55,29,42],
                    [42,56,41,30],
                    [43,44,57,31],
                    [44,58,43,32],
                    [45,59,33,46],
                    [46,34,60,45],
                    [47,48,61,35],
                    [48,36,62,47],
                    [49,37,50,63],
                    [50,38,51,49],
                    [51,50,39,1],
                    [52,1,53,8],
                    [53,52,40,54],
                    [54,53,28,2],
                    [55,2,41,3],
                    [56,3,42,57],
                    [57,4,56,43],
                    [58,59,4,44],
                    [59,45,5,58],
                    [60,61,5,46],
                    [61,47,6,60],
                    [62,63,7,48],
                    [63,49,1,62],
                    [1,51,52,63],
                    [2,9,54,55],
                    [3,11,55,56],
                    [4,12,57,58],
                    [5,60,13,59],
                    [6,7,0,61],
                    [7,62,8,6],
                    [8,7,52,9],
                    [9,2,10,8],
                    [10,0,9,11],
                    [11,10,3,12],
                    [12,13,11,4],
                    [13,5,0,12],
                    [0,6,10,13],
                    ]

    elif cap_type == 29:
        bc_v = 84
        new_edges = [
                    [83,70,14],
                    [70,15,83],
                    [71,72,16],
                    [72,17,71],
                    [73,74,18],
                    [74,19,73],
                    [75,76,20],
                    [76,21,75],
                    [77,78,22],
                    [78,23,77],
                    [79,80,24],
                    [80,25,79],
                    [81,82,26],
                    [82,27,81],
                    [14,28,27,83],
                    [15,29,70,16],
                    [16,30,15,71],
                    [17,31,72,18],
                    [18,32,17,73],
                    [19,20,33,74],
                    [20,34,19,75],
                    [21,22,35,76],
                    [22,77,36,21],
                    [23,78,24,37],
                    [24,79,38,23],
                    [25,80,26,38],
                    [26,81,39,25],
                    [27,82,14,40],
                    [28,53,14,29],
                    [29,41,28,15],
                    [30,42,16,31],
                    [31,43,30,17],
                    [32,33,44,18],
                    [33,45,32,19],
                    [34,35,46,20],
                    [35,21,47,34],
                    [36,37,48,22],
                    [37,36,23,49],
                    [38,24,25,50],
                    [39,26,40,51],
                    [40,39,27,52],
                    [41,54,29,42],
                    [42,55,41,30],
                    [43,44,56,31],
                    [44,57,43,32],
                    [45,58,33,46],
                    [46,34,59,45],
                    [47,48,60,35],
                    [48,36,61,47],
                    [49,37,50,62],
                    [50,38,51,49],
                    [51,50,39,63],
                    [52,64,40,53],
                    [53,52,28,65],
                    [54,65,41,66],
                    [55,66,42,56],
                    [56,67,55,43],
                    [57,58,67,44],
                    [58,45,68,57],
                    [59,60,69,46],
                    [60,47,1,59],
                    [61,48,62,1],
                    [62,49,2,61],
                    [63,51,64,2],
                    [64,63,52,3],
                    [65,4,53,54],
                    [66,5,54,55],
                    [67,6,56,57],
                    [68,69,7,58],
                    [69,8,68,59],
                    [1,61,9,60],
                    [2,62,63,10],
                    [3,64,4,11],
                    [4,3,65,12],
                    [5,12,66,6],
                    [6,7,5,67],
                    [7,13,6,68],
                    [8,9,0,69],
                    [9,1,10,8],
                    [10,2,11,9],
                    [11,10,3,0],
                    [12,13,4,5],
                    [13,0,12,7],
                    [0,8,11,13],
                    ]
    else:
        print("Invalid cap_type")
        exit(0)

    # num vertices in top cap for p = 12 and n == 2 (mod 6)
    tc_v = 62
    # num vertices in a ring
    ring_v = 42
    # total vertices in graph G
    num_v = bc_v + ring_v*num_rings + tc_v
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
    for ring in range(num_rings):
        add_ring(G, v_index)
        v_index += ring_v

    ## it is now time to complete the top cap
    new_edges = add_cap(cap_turn, cap_flip)
    for edges in new_edges:
        if cap_flip == 0:
            # clock wise order
            order = [1,2,3]
        else:
            # counter clock wise order
            order = [1,3,2]
        for i in order:
            add_neighbor(G, edges[0] + v_index, edges[i] + v_index)
            if edges[i] < 0:
                add_neighbor(G, edges[i] + v_index, edges[0] + v_index)

    print_adj_list(G)
    check(G)
    print("\n")
    return 1

max_n = int(sys.argv[1])

for cap_type in range(23, 30):
    for cap_turn in [0,1,2,3,4,5,6]:
        # you can also flip the top cap 
        for cap_flip in [0,1]:
            # for each number of rings
            num_rings = 0
            while main(cap_type, cap_turn, cap_flip, num_rings, max_n):
                num_rings += 1
