# BAO CAO HOC TAP - BUOI 4
## Thuat Toan To Mau Do Thi - Graph Coloring

---

## THONG TIN

- **Tac gia:** hoangedu773
- **GitHub:** [https://github.com/hoangedu773](https://github.com/hoangedu773)
- **Ngay:** 2025-12-01
- **Mon hoc:** Tri Tue Nhan Tao (TH_TTNT)
- **Buoi hoc:** Buoi 4

---

## BAI TAP

**Bai 1:** Phat trien code de doc file ma tran ke dang txt bat ky va in ket qua to mau ra man hinh.

---

## TOM TAT NOI DUNG

Bai toan to mau do thi (Graph Coloring Problem) la bai toan NP-day du trong ly thuyet do thi:

- **Muc tieu:** Gan mau cho cac dinh sao cho 2 dinh ke nhau khong cung mau
- **Toi uu:** Su dung it mau nhat co the
- **Ung dung:** Lap lich, phan bo tan so, su do ban do,...

---

## LY THUYET BAI TOAN

### 1. Dinh nghia

**Bai toan to mau do thi:** Cho do thi G = (V, E), tim cach gan mau cho cac dinh sao cho:
- Hai dinh ke nhau (co canh noi) phai co mau khac nhau
- So luong mau su dung la it nhat

### 2. So mau sac (Chromatic Number)

**Chi so mau sac χ(G):** So mau toi thieu can thiet de to mau do thi G.

**Vi du:**
- Do thi day du K_n: χ(K_n) = n
- Do thi hai phia: χ(G) = 2
- Chu trinh chan: χ(C_n) = 2
- Chu trinh le: χ(C_n) = 3

### 3. Bai toan quyet dinh

**Input:** Do thi G va so nguyen k  
**Output:** Co the to mau G voi k mau hay khong?

Bai toan nay la NP-day du (khong co thuat toan da thuc cho moi truong hop).

---

## CAC PHUONG PHAP GIAI

### 1. Greedy Coloring (Tham an)

**Y tuong:**
- Duyet lan luot cac dinh
- Moi dinh chon mau nho nhat chua bi su dung boi cac dinh ke

**Thuat toan:**

```
1. Gan mau 1 cho dinh dau tien
2. For moi dinh v:
   a. Danh dau cac mau da su dung boi dinh ke
   b. Chon mau nho nhat chua bi danh dau
   c. Gan mau do cho v
```

**Uu diem:**
- Nhanh (O(V + E))
- Don gian

**Nhuoc diem:**
- Khong dam bao toi uu
- Phu thuoc vao thu tu duyet dinh

**Do phuc tap:** O(V^2) hoac O(V + E) neu dung danh sach ke

### 2. Backtracking (Quay lui)

**Y tuong:**
- Thu gan mau cho tung dinh
- Neu khong hop le thi quay lui
- Thu tat ca cac kha nang

**Thuat toan:**

```
graphColoring(graph, m, colors, vertex):
    if vertex == n:
        return True
    
    for color in 1 to m:
        if isSafe(vertex, color):
            colors[vertex] = color
            
            if graphColoring(graph, m, colors, vertex + 1):
                return True
            
            colors[vertex] = 0
    
    return False
```

**Uu diem:**
- Tim duoc loi giai toi uu (neu ton tai)
- Dam bao tinh chinh xac

**Nhuoc diem:**
- Cham (exponential time)
- Chi phu hop voi do thi nho

**Do phuc tap:** O(m^V) trong truong hop xau nhat

---

## CAI DAT

### 1. Cau truc file ma tran ke

File `graph.txt` chua ma tran ke:

```
0 1 1 1 0
1 0 1 0 1
1 1 0 1 1
1 0 1 0 1
0 1 1 1 0
```

Trong do:
- `graph[i][j] = 1`: Co canh noi dinh i va dinh j
- `graph[i][j] = 0`: Khong co canh
- Ma tran doi xung: `graph[i][j] = graph[j][i]`

### 2. Cac ham chinh

| Ham | Mo ta |
|-----|-------|
| `read_adjacency_matrix(filename)` | Doc ma tran ke tu file |
| `greedy_coloring(graph)` | To mau bang phuong phap tham an |
| `graph_coloring(graph, m)` | To mau bang backtracking voi m mau |
| `is_safe(graph, vertex, color, colors)` | Kiem tra mau co hop le |
| `verify_coloring(graph, colors)` | Xac thuc ket qua to mau |
| `print_coloring_result(colors)` | Hien thi ket qua |

### 3. Ham Greedy Coloring

```python
def greedy_coloring(graph):
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
```

### 4. Ham Backtracking

```python
def graph_coloring_util(graph, m, colors, vertex):
    if vertex == len(graph):
        return True
    
    for color in range(1, m + 1):
        if is_safe(graph, vertex, color, colors):
            colors[vertex] = color
            
            if graph_coloring_util(graph, m, colors, vertex + 1):
                return True
            
            colors[vertex] = 0
    
    return False
```

---

## CACH SU DUNG

### 1. Chuan bi file input

Tao file `graph.txt` voi ma tran ke, vi du:

```
0 1 1 0
1 0 1 1
1 1 0 1
0 1 1 0
```

### 2. Chay chuong trinh

```bash
cd c:\work-space\TH_TTNT\Buoi_4
python main.py
```

### 3. Ket qua mau

```
==================================================
BUOI 4: TO MAU DO THI - GRAPH COLORING
==================================================

Doc file thanh cong: graph.txt
So dinh: 5

Ma tran ke:
   0  1  2  3  4
0: 0  1  1  1  0
1: 1  0  1  0  1
2: 1  1  0  1  1
3: 1  0  1  0  1
4: 0  1  1  1  0

==================================================
PHUONG PHAP 1: GREEDY COLORING
==================================================

Ket qua to mau:
----------------------------------------
Dinh 0: Mau 1
Dinh 1: Mau 2
Dinh 2: Mau 3
Dinh 3: Mau 2
Dinh 4: Mau 1
----------------------------------------
So mau su dung: 3

Cac dinh cung mau:
Mau 1: [0, 4]
Mau 2: [1, 3]
Mau 3: [2]

Kiem tra: HOP LE
```

---

## PHAN TICH KET QUA

### 1. Do phuc tap

| Thuat toan | Thoi gian | Khong gian | Toi uu |
|------------|-----------|------------|--------|
| **Greedy** | O(V^2) | O(V) | Khong |
| **Backtracking** | O(m^V) | O(V) | Co |

### 2. So sanh

**Greedy:**
- Nhanh, hieu qua cho do thi lon
- Ket qua phu thuoc vao thu tu dinh
- Khong dam bao it mau nhat

**Backtracking:**
- Cham, chi phu hop do thi nho
- Tim duoc loi giai toi uu
- Dam bao chinh xac

### 3. Vi du so sanh

**Do thi:** 5 dinh nhu tren

**Greedy:**
- So mau: 3
- Thoi gian: rat nhanh

**Backtracking (m=3):**
- So mau: 3
- Thoi gian: cham hon nhung van chap nhan duoc

**Ket luan:** Voi do thi nho, ca hai cho ket qua giong nhau.

---

## KET QUA THU NGHIEM

### Test Case 1: Do thi 4 dinh (Cycle)

**Input:**
```
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
```

**Ket qua:**
- So mau toi thieu: 2
- Greedy: 2 mau
- Backtracking (m=2): Thanh cong

### Test Case 2: Do thi day du K4

**Input:**
```
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
```

**Ket qua:**
- So mau toi thieu: 4 (moi dinh mot mau)
- Greedy: 4 mau
- Backtracking (m=3): That bai

### Test Case 3: Do thi hai phia

**Input:**
```
0 1 1 0
1 0 0 1
1 0 0 1
0 1 1 0
```

**Ket qua:**
- So mau toi thieu: 2
- Greedy: 2 mau
- Backtracking (m=2): Thanh cong

---

## UNG DUNG THUC TE

### 1. Lap lich (Scheduling)

**Bai toan:** Sap xep lich thi cho sinh vien
- Dinh: Mon thi
- Canh: Co sinh vien thi ca 2 mon
- Mau: Ca thi

**Muc tieu:** It ca thi nhat

### 2. Phan bo tan so (Frequency Assignment)

**Bai toan:** Phan tan so cho cac tram phat song
- Dinh: Tram phat
- Canh: Tram gan nhau (can tan so khac nhau)
- Mau: Tan so

**Muc tieu:** It tan so nhat

### 3. Su do ban do (Map Coloring)

**Bai toan:** To mau cac nuoc tren ban do
- Dinh: Quoc gia
- Canh: Co chung bien gioi
- Mau: Mau sac

**Dinh ly 4 mau:** Moi ban do phang can toi da 4 mau

### 4. Phan bo thanh ghi (Register Allocation)

**Bai toan:** Gan bien vao thanh ghi CPU
- Dinh: Bien
- Canh: Bien dung cung luc
- Mau: Thanh ghi

**Muc tieu:** It thanh ghi nhat

---

## TOI UU VA CAI TIEN

### 1. Welsh-Powell Algorithm

Thu tu dinh theo bac giam dan truoc khi to mau:

```python
def welsh_powell(graph):
    degrees = [(i, sum(graph[i])) for i in range(len(graph))]
    degrees.sort(key=lambda x: x[1], reverse=True)
    # ... to mau theo thu tu nay
```

### 2. DSatur (Degree of Saturation)

Uu tien dinh co nhieu mau ke nhau:

- Chon dinh chua to co bac bao hoa cao nhat
- Bac bao hoa = so mau khac nhau cua cac dinh ke

### 3. Pruning va Heuristics

Trong Backtracking:
- Chon mau xuat hien it nhat truoc
- Cat tia som neu vuot qua gioi han

---

## NHAN XET VA RUT KINH NGHIEM

### 1. Uu diem

- Greedy nhanh, phu hop thuc te
- Backtracking chinh xac cho do thi nho
- De cai dat va mo rong

### 2. Nhuoc diem

- Bai toan NP-day du, kho giai toi uu
- Greedy khong dam bao toi uu
- Backtracking qua cham voi do thi lon

### 3. Bai hoc

1. **Thu tu quan trong:** Greedy phu thuoc vao thu tu duyet
2. **Trade-off:** Toc do vs Do chinh xac
3. **Thuc te:** Nghiem gan toi uu thuong du tot
4. **Ket hop:** Su dung ca 2 phuong phap de kiem chung

---

## HUONG PHAT TRIEN

### 1. Mo rong

- Cai dat Welsh-Powell va DSatur
- Hien thi truc quan bang do hoa (matplotlib, networkx)
- Ho tro doc nhieu dinh dang (ma tran ke, danh sach canh, ...)

### 2. Toi uu

- Parallel Backtracking (da luong)
- Genetic Algorithm
- Simulated Annealing

### 3. Ung dung

- Xay dung cong cu lap lich tu dong
- Phan mem phan bo tai nguyen
- Visualize graph coloring

---

## TAI LIEU THAM KHAO

1. **Cormen, T. H., et al.** (2009). *Introduction to Algorithms* (3rd ed.)
2. **Russell, S. & Norvig, P.** (2020). *Artificial Intelligence: A Modern Approach*
3. **Wikipedia:** [Graph Coloring](https://en.wikipedia.org/wiki/Graph_coloring)
4. **GeeksforGeeks:** [Graph Coloring Algorithm](https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/)

---

## KET LUAN

Bai tap da giup toi:

1. Hieu ro bai toan to mau do thi
2. Cai dat Greedy va Backtracking
3. So sanh hieu suat cac phuong phap
4. Nhan thuc ung dung thuc te
5. Ren luyen ky nang xu ly file va do thi

To mau do thi la bai toan co dien trong AI va CS:
- Nen tang cho nhieu bai toan thuc te
- Minh hoa tot cho bai toan NP
- Ket hop nhieu ky thuat (Greedy, Backtracking, Heuristic)

---

**Signature:**
```
/**
 * Author: hoangedu773
 * GitHub: https://github.com/hoangedu773
 * Date: 2025-12-01
 */
```

---

**Cam on thay/co da huong dan!**
