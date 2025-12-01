# BAO CAO HOC TAP - BUOI 3
## Giai Thuat Tim Kiem Doi Khang: Minimax va Alpha-Beta

---

## THONG TIN

- **Tac gia:** hoangedu773
- **GitHub:** [https://github.com/hoangedu773](https://github.com/hoangedu773)
- **Buoi hoc:** Buoi 3

---

## TOM TAT NOI DUNG

Buoi thuc hanh gioi thieu giai thuat tim kiem doi khang trong tro choi hai nguoi (TicTacToe, co vua, co tuong):

- Mo hinh hoa tro choi hai nguoi duoi dang bai toan tim kiem
- Thuat toan **Minimax** de chon nuoc di toi uu
- Ky thuat **cat tia Alpha-Beta** tang toc Minimax
- Ap dung vao tro choi TicTacToe (3x3)

---

## MUC TIEU BAI HOC

### Muc tieu kien thuc

1. Hieu khai niem tim kiem doi khang (adversarial search)
2. Nam ro nguyen ly hoat dong cua Minimax
3. Hieu y tuong va dieu kien cat tia alpha (α) va beta (β)
4. Phan biet Minimax thuan va Minimax co cat tia

### Muc tieu ky nang

1. Biet mo hinh hoa tro choi (trang thai, hanh dong, loi ich)
2. Cai dat Minimax va Alpha-Beta cho TicTacToe 3x3
3. Mo rong cho ban co lon hon (5x5, 10x10, NxN)

---

## MO HINH BAI TOAN TRO CHOI DOI KHANG

Mot tro choi hai nguoi duoc mo hinh hoa boi:

### 1. Trang thai ban dau (Initial State)
- Mo ta ban co luc dau (tat ca o deu rong)
- Chi ra nguoi choi nao di truoc (X di truoc)

### 2. Trang thai ket thuc (Terminal State)
Tro choi ket thuc khi:
- Mot nguoi thang (dat duoc cau hinh thang)
- Khong con nuoc di hop le (hoa)

### 3. Ham chuyen trang thai (Actions/Successor)
- Tu trang thai hien tai, liet ke tat ca nuoc di hop le
- Moi nuoc di ung voi mot trang thai moi

### 4. Ham loi ich (Utility Function)
Gan gia tri so cho trang thai ket thuc:

```
U(s) = { +1  neu X thang
       { -1  neu O thang
       {  0  neu hoa
```

### 5. Ham luong gia (Heuristic)
Dung khi khong the duyet het cay tro choi:

```
E(n) = X(n) - O(n)
```

Trong do:
- X(n): so dong thang tiem nang cho X
- O(n): so dong thang tiem nang cho O

---

## THUAT TOAN MINIMAX

### 1. Y tuong truc quan

Minimax ap dung cho tro choi hai nguoi luan phien:
- Mot nguoi dong vai **MAX** (muon toi da hoa ham loi ich)
- Doi thu la **MIN** (muon toi thieu hoa ham loi ich)

Gia su ca hai deu choi toi uu:
- O luot MAX: chon nuoc di cho gia tri tot nhat (lon nhat)
- O luot MIN: chon nuoc di cho gia tri xau nhat (nho nhat)

### 2. Ma gia Minimax

```python
def maxValue(state):
    if terminal(state):
        return utility(state)
    
    v = -infinity
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v

def minValue(state):
    if terminal(state):
        return utility(state)
    
    v = +infinity
    for action in actions(state):
        v = min(v, maxValue(result(state, action)))
    return v

def minimax(board):
    # Duyet qua tat ca action(board)
    # Dung maxValue/minValue de tinh gia tri
    # Chon action tot nhat
```

### 3. Vi du don gian

Xet cay tro choi:

```
        (MAX) S
         /     \
    (MIN) A   (MIN) B
```

- A co 3 con la: [3, 5, 2]
- B co 3 con la: [9, 1, 4]

Duyet Minimax tu duoi len:

1. Tai nut MIN A: `value(A) = min(3, 5, 2) = 2`
2. Tai nut MIN B: `value(B) = min(9, 1, 4) = 1`
3. Tai nut MAX S: `value(S) = max(2, 1) = 2`

**Ket luan:** MAX nen chon nhanh A voi gia tri toi uu la 2.

---

## KY THUAT CAT TIA ALPHA-BETA

### 1. Y tuong

Alpha-Beta la phien ban toi uu cua Minimax:
- **Khong lam thay doi ket qua cuoi cung**
- **Giam so nut can duyet** bang cach cat tia cac nhanh khong the anh huong den quyet dinh

### 2. Dinh nghia Alpha va Beta

- **Alpha (α):** Gia tri tot nhat (lon nhat) ma MAX tim duoc den thoi diem hien tai
- **Beta (β):** Gia tri tot nhat (nho nhat) ma MIN tim duoc den thoi diem hien tai

### 3. Dieu kien cat tia

**Tai nut MAX:**
- Neu `v >= beta`: cat tia (MIN khong chon nhanh nay)

**Tai nut MIN:**
- Neu `v <= alpha`: cat tia (MAX khong chon nhanh nay)

### 4. Ma gia Alpha-Beta

```python
def maxValueAB(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = -infinity
    for action in actions(state):
        v = max(v, minValueAB(result(state, action), alpha, beta))
        if v >= beta:
            return v  # Cat tia
        alpha = max(alpha, v)
    return v

def minValueAB(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = +infinity
    for action in actions(state):
        v = min(v, maxValueAB(result(state, action), alpha, beta))
        if v <= alpha:
            return v  # Cat tia
        beta = min(beta, v)
    return v
```

---

## CAI DAT CHO TICTACTOE 3x3

### 1. Cau truc du lieu

```python
X = "X"
O = "O"
EMPTY = None

board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]
```

### 2. Cac ham chinh

| Ham | Mo ta |
|-----|-------|
| `initial_state()` | Tao ban co rong ban dau |
| `player(board)` | Xac dinh nguoi choi tiep theo |
| `actions(board)` | Liet ke cac nuoc di hop le |
| `result(board, action)` | Tra ve trang thai sau khi thuc hien hanh dong |
| `winner(board)` | Kiem tra nguoi choi thang |
| `terminal(board)` | Kiem tra trang thai ket thuc |
| `utility(board)` | Tra ve gia tri loi ich (+1, -1, 0) |
| `minimax(board)` | Tra ve nuoc di toi uu (Minimax) |
| `alphabeta(board)` | Tra ve nuoc di toi uu (Alpha-Beta) |

### 3. Ham kiem tra thang

Kiem tra 8 truong hop thang:
- 3 hang ngang
- 3 cot doc
- 2 duong cheo

```python
def winner(board):
    # Kiem tra hang ngang
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
    
    # Kiem tra cot doc
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != None:
            return board[0][j]
    
    # Kiem tra duong cheo
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    
    return None
```

---

## CACH SU DUNG

### 1. Chay chuong trinh

```bash
python main.py
```

### 2. Ket qua mau

```
==================================================
TIC TAC TOE - MINIMAX vs ALPHA-BETA
==================================================
Thuat toan: Minimax

   |   |  
  -----------
   |   |  
  -----------
   |   |  

Luot cua: X
Nuoc di 1: (0, 0)

 X |   |  
  -----------
   |   |  
  -----------
   |   |  

...

==========================================
Ket qua: HOA!
==========================================
```

---

## PHAN TICH KET QUA

### 1. Do phuc tap

**Minimax:**
- **Thoi gian:** O(b^m)
  - b: branching factor (so nuoc di trung binh)
  - m: do sau toi da cua cay

**Alpha-Beta:**
- **Thoi gian tot nhat:** O(b^(m/2))
- **Thoi gian xau nhat:** O(b^m) (giong Minimax)

### 2. So sanh hieu suat

| Thuat toan | So nut duyet | Ket qua | Toc do |
|------------|--------------|---------|--------|
| **Minimax** | Duyet het cay | Toi uu | Cham |
| **Alpha-Beta** | Cat tia mot phan | Toi uu | **Nhanh hon** |

### 3. TicTacToe 3x3

- Tong so trang thai: ~5,478
- Minimax duyet het tat ca
- Alpha-Beta cat duoc 30-70% nut (tuy thu tu nuoc di)

---

## KET QUA THU NGHIEM

### Test Case 1: Game hoan chinh

**Cau hinh:**
- X di truoc (AI su dung Minimax)
- O di sau (AI su dung Minimax)

**Ket qua:**
- Tat ca game deu HOA (do ca hai choi toi uu)

### Test Case 2: Trang thai giua chung

**Board:**
```
X | O | X
---------
O | X |  
---------
  |   | O
```

**Minimax:**
- Nuoc di tot nhat: (1, 2) hoac (2, 0)

**Alpha-Beta:**
- Nuoc di tot nhat: (1, 2) hoac (2, 0)
- **Ket luan:** Giong Minimax nhung nhanh hon!

---

## NHAN XET VA RUT KINH NGHIEM

### 1. Uu diem Minimax

- **Toi uu:** Luon tim duoc nuoc di tot nhat
- **Don gian:** De hieu va cai dat
- **Chinh xac:** Dam bao choi tot nhat neu co the duyet het

### 2. Uu diem Alpha-Beta

- **Nhanh hon:** Cat tia nut khong can thiet
- **Ket qua giong Minimax:** Khong thay doi ket qua
- **Tiet kiem tai nguyen:** Giam thoi gian va bo nho

### 3. Nhuoc diem chung

- **Chi phu hop tro choi nho:** TicTacToe 3x3, Connect4, ...
- **Khong ap dung cho tro choi lon:** Co vua, co tuong (can ket hop heuristic)
- **Phu thuoc vao thu tu:** Alpha-Beta hieu qua tuy vao thu tu duyet

### 4. Bai hoc

1. **Cat tia quan trong:** Giam dang ke do phuc tap
2. **Thu tu quan trong:** Duyet nuoc di tot truoc -> cat nhieu hon
3. **Heuristic can thiet:** Cho tro choi phuc tap (khong duyet het duoc)

---

## HUONG PHAT TRIEN

### 1. Mo rong ban co

- TicTacToe 5x5, 10x10
- Thay doi dieu kien thang: 4 hoac 5 o lien tiep
- Can bo sung ham heuristic de cat som

### 2. Toi uu Alpha-Beta

- **Move Ordering:** Sap xep nuoc di theo do tot
- **Transposition Table:** Luu trang thai da tinh
- **Iterative Deepening:** Tang dan do sau

### 3. Ap dung cho tro choi khac

- Connect Four
- Checkers
- Chess (ket hop voi heuristic phuc tap)

---

## TAI LIEU THAM KHAO

1. **Russell, S. & Norvig, P.** (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
   - Chapter 5: Adversarial Search
2. **Wikipedia:** [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
3. **Wikipedia:** [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
4. **GeeksforGeeks:** [Minimax Algorithm in Game Theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)

---

## KET LUAN

Bai tap da giup toi:

1. Hieu sau ve thuat toan Minimax va Alpha-Beta
2. Cai dat thanh cong cho TicTacToe 3x3
3. Phan tich va so sanh hieu suat hai thuat toan
4. Nhan thuc duoc ung dung thuc te cua AI trong tro choi

Minimax va Alpha-Beta la nen tang quan trong trong:
- Game AI (chess, checkers, go)
- Decision making
- Competitive programming
- Game theory

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
