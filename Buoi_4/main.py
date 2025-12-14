"""
Author: hoangedu773
GitHub: https://github.com/hoangedu773
Date: 2025-12-14
Description: Buoi 4 - To mau do thi va Nguoi ban hang (TSP)

BAI TAP:
    Bai 1: Doc file ma tran ke dang txt bat ky va in ket qua to mau ra man hinh
    Bai 2: Phat trien code thanh cac chuong trinh con phu hop
    Bai 3: Cai dat thuat toan nguoi ban hang (TSP) - tim chu trinh qua n thanh pho
           moi thanh pho qua 1 lan voi chi phi toi thieu
"""

import matplotlib.pyplot as plt
import networkx as nx
import itertools
import sys

# ==============================================================================
# BAI 1: DOC FILE MA TRAN KE VA TO MAU DO THI
# ==============================================================================

def read_adjacency_matrix(filename):
    """
    Bai 1: Doc ma tran ke tu file txt
    Input: Duong dan file chua ma tran ke (cac so cach nhau boi dau cach)
    Output: Ma tran ke dang list 2 chieu
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    matrix = []
    for line in lines:
        line = line.strip()
        if line:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    
    return matrix


def read_distance_matrix(filename):
    """
    Bai 3: Doc ma tran khoang cach tu file txt cho bai toan TSP
    Input: Duong dan file chua ma tran khoang cach
    Output: Ma tran khoang cach dang list 2 chieu
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    matrix = []
    for line in lines:
        line = line.strip()
        if line:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    
    return matrix


# ==============================================================================
# BAI 2: CAC CHUONG TRINH CON CHO TO MAU DO THI
# ==============================================================================

# --- 2.1: Kiem tra tinh hop le cua mau ---
def is_safe_color(graph, vertex, color, colors):
    """
    Bai 2: Kiem tra xem co the gan mau 'color' cho dinh 'vertex' khong
    Dieu kien: Khong co dinh ke nao cung mau
    """
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True


# --- 2.2: Thuat toan Backtracking de to mau ---
def graph_coloring_backtrack(graph, m, colors, vertex):
    """
    Bai 2: Thuat toan Backtracking de to mau do thi
    Input: 
        - graph: ma tran ke
        - m: so mau toi da
        - colors: mang luu mau cua tung dinh
        - vertex: dinh dang xet
    Output: True neu to mau thanh cong, False neu khong
    """
    if vertex == len(graph):
        return True
    
    for color in range(1, m + 1):
        if is_safe_color(graph, vertex, color, colors):
            colors[vertex] = color
            
            if graph_coloring_backtrack(graph, m, colors, vertex + 1):
                return True
            
            colors[vertex] = 0
    
    return False


def graph_coloring(graph, m):
    """
    Bai 2: Ham chinh de to mau do thi voi toi da m mau
    Input: graph - ma tran ke, m - so mau toi da
    Output: Mang mau cua cac dinh hoac None neu khong the to mau
    """
    n = len(graph)
    colors = [0] * n
    
    if graph_coloring_backtrack(graph, m, colors, 0):
        return colors
    else:
        return None


# --- 2.3: Thuat toan Greedy de to mau ---
def greedy_coloring(graph):
    """
    Bai 2: Thuat toan Greedy de to mau do thi
    Y tuong: Duyet tung dinh, gan mau nho nhat chua duoc su dung boi cac dinh ke
    Input: graph - ma tran ke
    Output: Mang mau cua cac dinh
    """
    n = len(graph)
    colors = [-1] * n
    
    colors[0] = 0
    
    for vertex in range(1, n):
        available = [True] * n
        
        for i in range(n):
            if graph[vertex][i] == 1 and colors[i] != -1:
                available[colors[i]] = False
        
        for color in range(n):
            if available[color]:
                colors[vertex] = color
                break
    
    return [c + 1 for c in colors]


# --- 2.4: Kiem tra ket qua to mau ---
def verify_coloring(graph, colors):
    """
    Bai 2: Kiem tra xem ket qua to mau co hop le khong
    Hop le: Khong co 2 dinh ke nao cung mau
    """
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1 and colors[i] == colors[j]:
                return False
    return True


# --- 2.5: Hien thi ket qua ---
def print_graph(graph):
    """Bai 2: In ma tran ke ra man hinh"""
    print("\nMa tran ke:")
    print("  ", end="")
    for i in range(len(graph)):
        print(f"{i:3}", end="")
    print()
    
    for i, row in enumerate(graph):
        print(f"{i}: ", end="")
        for val in row:
            print(f"{val:3}", end="")
        print()


def print_coloring_result(colors):
    """Bai 2: In ket qua to mau ra man hinh"""
    print("\nKet qua to mau:")
    print("-" * 40)
    for vertex, color in enumerate(colors):
        print(f"Dinh {vertex}: Mau {color}")
    print("-" * 40)
    
    num_colors = len(set(colors))
    print(f"So mau su dung: {num_colors}")
    
    color_groups = {}
    for vertex, color in enumerate(colors):
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(vertex)
    
    print("\nCac dinh cung mau:")
    for color, vertices in sorted(color_groups.items()):
        print(f"Mau {color}: {vertices}")


# --- 2.6: Truc quan hoa do thi ---
def visualize_graph(graph, colors, title="Graph Coloring", filename=None):
    """Bai 2: Ve do thi voi mau da to bang NetworkX va Matplotlib"""
    G = nx.Graph()
    n = len(graph)
    
    for i in range(n):
        G.add_node(i)
    
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    
    color_map_dict = {
        1: '#FF6B6B', 2: '#4ECDC4', 3: '#45B7D1', 4: '#FFA07A',
        5: '#98D8C8', 6: '#F7DC6F', 7: '#BB8FCE', 8: '#85C1E2'
    }
    
    node_colors = [color_map_dict.get(colors[i], '#CCCCCC') for i in range(n)]
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=800, alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    
    labels = {i: f"{i}\n(M{colors[i]})" for i in range(n)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\nDa luu anh: {filename}")
    
    plt.show()


# ==============================================================================
# BAI 3: THUAT TOAN NGUOI BAN HANG (TRAVELING SALESMAN PROBLEM - TSP)
# ==============================================================================

def tsp_brute_force(dist_matrix):
    """
    Bai 3: Thuat toan vet can (Brute Force) cho TSP
    Tim chu trinh Hamilton co chi phi nho nhat
    
    Input: dist_matrix - ma tran khoang cach giua cac thanh pho
    Output: (best_path, best_cost) - duong di tot nhat va chi phi
    
    Do phuc tap: O(n!) - chi phu hop voi so thanh pho nho (n <= 10)
    """
    n = len(dist_matrix)
    cities = list(range(n))
    
    best_path = None
    best_cost = float('inf')
    
    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        
        cost = 0
        for i in range(len(path) - 1):
            cost += dist_matrix[path[i]][path[i + 1]]
        
        if cost < best_cost:
            best_cost = cost
            best_path = path
    
    return best_path, best_cost


def tsp_nearest_neighbor(dist_matrix, start=0):
    """
    Bai 3: Thuat toan Greedy (Nearest Neighbor) cho TSP
    Tai moi buoc, chon thanh pho chua tham gan nhat
    
    Input: 
        - dist_matrix: ma tran khoang cach
        - start: thanh pho bat dau (mac dinh la 0)
    Output: (path, cost) - duong di va chi phi
    
    Do phuc tap: O(n^2) - nhanh nhung khong dam bao toi uu
    """
    n = len(dist_matrix)
    visited = [False] * n
    path = [start]
    visited[start] = True
    cost = 0
    current = start
    
    for _ in range(n - 1):
        nearest = None
        nearest_dist = float('inf')
        
        for city in range(n):
            if not visited[city] and dist_matrix[current][city] < nearest_dist:
                nearest = city
                nearest_dist = dist_matrix[current][city]
        
        path.append(nearest)
        visited[nearest] = True
        cost += nearest_dist
        current = nearest
    
    cost += dist_matrix[current][start]
    path.append(start)
    
    return path, cost


def tsp_dynamic_programming(dist_matrix):
    """
    Bai 3: Thuat toan Quy hoach dong (Held-Karp) cho TSP
    Su dung bitmask de luu trang thai cac thanh pho da tham
    
    Input: dist_matrix - ma tran khoang cach
    Output: (best_path, best_cost) - duong di toi uu va chi phi
    
    Do phuc tap: O(n^2 * 2^n) - toi uu hon brute force nhung van exponential
    """
    n = len(dist_matrix)
    
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    dp[1][0] = 0
    
    for mask in range(1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            if dp[mask][last] == float('inf'):
                continue
                
            for next_city in range(n):
                if mask & (1 << next_city):
                    continue
                    
                new_mask = mask | (1 << next_city)
                new_cost = dp[mask][last] + dist_matrix[last][next_city]
                
                if new_cost < dp[new_mask][next_city]:
                    dp[new_mask][next_city] = new_cost
                    parent[new_mask][next_city] = last
    
    full_mask = (1 << n) - 1
    best_cost = float('inf')
    last_city = -1
    
    for city in range(n):
        cost = dp[full_mask][city] + dist_matrix[city][0]
        if cost < best_cost:
            best_cost = cost
            last_city = city
    
    path = []
    mask = full_mask
    current = last_city
    
    while current != -1:
        path.append(current)
        next_current = parent[mask][current]
        mask = mask ^ (1 << current)
        current = next_current
    
    path = path[::-1]
    path.append(0)
    
    return path, best_cost


def print_tsp_result(path, cost, method_name):
    """Bai 3: In ket qua TSP ra man hinh"""
    print(f"\n{method_name}:")
    print("-" * 40)
    print(f"Duong di: {' -> '.join(map(str, path))}")
    print(f"Chi phi toi thieu: {cost}")
    print("-" * 40)


def visualize_tsp(dist_matrix, path, title="TSP Solution", filename=None):
    """Bai 3: Ve do thi TSP voi duong di toi uu"""
    n = len(dist_matrix)
    G = nx.Graph()
    
    for i in range(n):
        G.add_node(i)
    
    for i in range(n):
        for j in range(i + 1, n):
            if dist_matrix[i][j] > 0 and dist_matrix[i][j] < float('inf'):
                G.add_edge(i, j, weight=dist_matrix[i][j])
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    nx.draw_networkx_nodes(G, pos, node_color='#45B7D1', 
                          node_size=800, alpha=0.9)
    
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.3, style='dashed')
    
    tsp_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=tsp_edges, 
                          width=3, alpha=0.8, edge_color='#FF6B6B')
    
    labels = {i: f"TP{i}" for i in range(n)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')
    
    edge_labels = {(path[i], path[i+1]): f"{dist_matrix[path[i]][path[i+1]]:.0f}" 
                   for i in range(len(path)-1)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\nDa luu anh: {filename}")
    
    plt.show()


# ==============================================================================
# HAM MAIN - CHAY CAC BAI TAP
# ==============================================================================

def run_graph_coloring():
    """Chay Bai 1 va Bai 2: To mau do thi"""
    print("\n" + "=" * 60)
    print("BAI 1 & 2: TO MAU DO THI")
    print("=" * 60)
    
    filename = "graph.txt"
    
    try:
        graph = read_adjacency_matrix(filename)
        print(f"\nDoc file thanh cong: {filename}")
        print(f"So dinh: {len(graph)}")
        
        print_graph(graph)
        
        print("\n" + "-" * 40)
        print("PHUONG PHAP 1: GREEDY COLORING")
        print("-" * 40)
        
        colors_greedy = greedy_coloring(graph)
        print_coloring_result(colors_greedy)
        
        if verify_coloring(graph, colors_greedy):
            print("\nKiem tra: HOP LE")
        else:
            print("\nKiem tra: KHONG HOP LE")
        
        print("\n" + "-" * 40)
        print("PHUONG PHAP 2: BACKTRACKING (m=3)")
        print("-" * 40)
        
        m = 3
        colors_backtrack = graph_coloring(graph, m)
        
        if colors_backtrack:
            print(f"\nCo the to mau voi {m} mau:")
            print_coloring_result(colors_backtrack)
            
            if verify_coloring(graph, colors_backtrack):
                print("\nKiem tra: HOP LE")
            else:
                print("\nKiem tra: KHONG HOP LE")
        else:
            print(f"\nKhong the to mau voi {m} mau!")
        
        print("\nVe do thi voi mau...")
        visualize_graph(graph, colors_greedy, 
                       title="Graph Coloring - Greedy Algorithm",
                       filename="graph_greedy.png")
        
    except FileNotFoundError:
        print(f"\nLoi: Khong tim thay file '{filename}'")
        print("Tao file mau...")
        
        sample_graph = [
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0]
        ]
        
        with open(filename, 'w') as f:
            for row in sample_graph:
                f.write(' '.join(map(str, row)) + '\n')
        
        print(f"Da tao file '{filename}'")
        print("Vui long chay lai chuong trinh!")


def run_tsp():
    """Chay Bai 3: Nguoi ban hang (TSP)"""
    print("\n" + "=" * 60)
    print("BAI 3: NGUOI BAN HANG (TRAVELING SALESMAN PROBLEM)")
    print("=" * 60)
    
    filename = "tsp.txt"
    
    try:
        dist_matrix = read_distance_matrix(filename)
        n = len(dist_matrix)
        print(f"\nDoc file thanh cong: {filename}")
        print(f"So thanh pho: {n}")
        
        print("\nMa tran khoang cach:")
        for i, row in enumerate(dist_matrix):
            print(f"TP{i}: {row}")
        
    except FileNotFoundError:
        print(f"\nKhong tim thay file '{filename}', tao ma tran mau...")
        
        dist_matrix = [
            [0, 10, 15, 20, 25],
            [10, 0, 35, 25, 30],
            [15, 35, 0, 30, 20],
            [20, 25, 30, 0, 15],
            [25, 30, 20, 15, 0]
        ]
        n = len(dist_matrix)
        
        with open(filename, 'w') as f:
            for row in dist_matrix:
                f.write(' '.join(map(str, row)) + '\n')
        
        print(f"Da tao file '{filename}' voi {n} thanh pho")
        print("\nMa tran khoang cach:")
        for i, row in enumerate(dist_matrix):
            print(f"TP{i}: {row}")
    
    print("\n" + "-" * 40)
    print("PHUONG PHAP 1: NEAREST NEIGHBOR (GREEDY)")
    print("-" * 40)
    path_nn, cost_nn = tsp_nearest_neighbor(dist_matrix)
    print_tsp_result(path_nn, cost_nn, "Nearest Neighbor")
    
    print("\n" + "-" * 40)
    print("PHUONG PHAP 2: QUY HOACH DONG (HELD-KARP)")
    print("-" * 40)
    path_dp, cost_dp = tsp_dynamic_programming(dist_matrix)
    print_tsp_result(path_dp, cost_dp, "Dynamic Programming")
    
    if n <= 8:
        print("\n" + "-" * 40)
        print("PHUONG PHAP 3: VET CAN (BRUTE FORCE)")
        print("-" * 40)
        path_bf, cost_bf = tsp_brute_force(dist_matrix)
        print_tsp_result(path_bf, cost_bf, "Brute Force")
    else:
        print(f"\nBo qua Brute Force vi so thanh pho ({n}) qua lon!")
    
    print("\nVe do thi TSP voi duong di toi uu...")
    visualize_tsp(dist_matrix, path_dp, 
                  title=f"TSP Solution - Chi phi: {cost_dp}",
                  filename="tsp_solution.png")


def main():
    """Ham chinh - Menu chon bai tap"""
    print("=" * 60)
    print("BUOI 4: TO MAU DO THI VA NGUOI BAN HANG")
    print("Author: hoangedu773")
    print("=" * 60)
    
    print("\nChon bai tap de chay:")
    print("1. Bai 1 & 2: To mau do thi")
    print("2. Bai 3: Nguoi ban hang (TSP)")
    print("3. Chay tat ca")
    print("0. Thoat")
    
    choice = input("\nNhap lua chon (0-3): ").strip()
    
    if choice == '1':
        run_graph_coloring()
    elif choice == '2':
        run_tsp()
    elif choice == '3':
        run_graph_coloring()
        run_tsp()
    elif choice == '0':
        print("\nTam biet!")
        sys.exit(0)
    else:
        print("\nLua chon khong hop le! Chay tat ca mac dinh...")
        run_graph_coloring()
        run_tsp()


if __name__ == "__main__":
    main()
