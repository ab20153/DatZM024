import sys

filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename,'r') as f:
    data = f.read().split()
    n = int(data[0])    # number of vertices
    edges = []          # trios of edges (w, a, b)
    i = 1
    while i < len(data):
        a = int(data[i])
        b = int(data[i+1])
        w = int(data[i+2])
        edges.append((w, a, b))
        i += 3

# sort paths (edges) by difficulty in descending order
edges.sort(reverse=True)

### ========= Union-Find algorithm ========= ###
# geeksforgeeks.org - Introduction to Disjoint Set (Union-Find Data Structure)
# https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

parent = list(range(n+1))

# Function to find the root node of a tree
def find(i):
    # If i is already root/representative
    if parent[i] == i: return i
    # Otherwise, find the representative recursively
    return find(parent[i])

# Function to combine two trees
def union(i, j):
    # Find representatives of the sets containint i and j
    iRep, jRep = find(i), find(j)
    # Make the representative of i's set the representative of j's set
    # if they are different to make sure no cycles are formed in the forest
    if iRep != jRep:
        parent[iRep] = jRep
        return True
    return False
### ======================================== ###

# Construct a forest with no cycles with maximised total difficulty
forest_sum = 0
honey = []
# Use Union-Find to add edges to the forest such that the forest has no cycles
for w, a, b in edges:
    if union(a, b):
        forest_sum += w
    else:
        # Edges not added to the forest would form a cycle
        # so add honey along these edges
        honey.append((a, b))

# Total difficulty sum of all edges
total_sum = sum(w for w, _, _ in edges)

# The total difficulty of all honey edges will be
# the overall difficulty minus the total difficulty
# of the forest we just constructed
honey_sum = total_sum - forest_sum

# Output to file
with open('output.txt', 'w') as f:
    f.write(f"{honey_sum}\t")
    f.write(f"{len(honey)}\n")
    for a, b in honey:
        f.write(f"{a} {b}\t")