# BAO CAO HOC TAP - BUOI 5
## Thuat Toan K-Means va K-NN

---

## THONG TIN

- **Tac gia:** hoangedu773
- **GitHub:** [https://github.com/hoangedu773](https://github.com/hoangedu773)
- **Ngay:** 2025-12-14
- **Mon hoc:** Tri Tue Nhan Tao (TH_TTNT)
- **Buoi hoc:** Buoi 5

---

## BAI TAP

### III. Bai tap o lop
- **Bai 1:** Cai dat thuat toan K-means
- **Bai 2:** Cai dat thuat toan K-NN voi 2 cach danh gia trong so k
- **Bai 3:** Cai dat ung dung demo cho 2 thuat toan tren

### IV. Bai tap ve nha
- **Bai 4:** Mo ta ung dung va cai dat demo ung dung voi 2 thuat toan tren
- **Bai 5:** Mo ta ung dung va cai dat demo voi cac thuat toan duoc hoc tren lop ly thuyet

---

## LY THUYET

### 1. Thuat toan K-Means Clustering

#### 1.1. Gioi thieu
K-Means la thuat toan **hoc khong giam sat (unsupervised learning)** dung de phan cum du lieu thanh k nhom.

#### 1.2. Y tuong
1. Chon ngau nhien k diem lam tam cum (centroids)
2. Gan moi diem du lieu vao cum co tam gan nhat
3. Cap nhat tam cum = trung binh cac diem trong cum
4. Lap lai buoc 2-3 cho den khi hoi tu

#### 1.3. Cong thuc

**Khoang cach Euclidean:**
```
d(x, y) = sqrt(sum((xi - yi)^2))
```

**Cap nhat tam cum:**
```
centroid_k = (1/n_k) * sum(xi)  voi xi thuoc cum k
```

**Ham muc tieu (SSE - Sum of Squared Errors):**
```
J = sum(sum(||xi - centroid_k||^2))
```

#### 1.4. Uu nhuoc diem

| Uu diem | Nhuoc diem |
|---------|------------|
| Don gian, de cai dat | Phai chon truoc so cum k |
| Nhanh voi du lieu lon | Nhay cam voi diem khoi tao |
| Hieu qua voi cum hinh cau | Khong tot voi cum hinh dang phuc tap |

---

### 2. Thuat toan K-NN (K-Nearest Neighbors)

#### 2.1. Gioi thieu
K-NN la thuat toan **hoc co giam sat (supervised learning)** dung de phan lop du lieu dua tren k lang gieng gan nhat.

#### 2.2. Y tuong
1. Tinh khoang cach tu diem can phan lop den tat ca diem trong tap huan luyen
2. Chon k diem gan nhat
3. Phan lop theo da so (majority voting)

#### 2.3. Hai cach danh gia trong so k

**Cach 1: Uniform Weights (Trong so bang nhau)**
- Tat ca k lang gieng co trong so = 1
- Phan lop bang majority voting don gian
```
y = argmax(count(yi))  voi yi la nhan cua k lang gieng
```

**Cach 2: Distance Weights (Trong so theo khoang cach)**
- Lang gieng gan hon co trong so lon hon
- Trong so = 1 / khoang cach
```
w_i = 1 / d(x, x_i)
y = argmax(sum(w_i * I(yi = c)))  voi moi lop c
```

#### 2.4. So sanh 2 cach

| Tieu chi | Uniform | Distance |
|----------|---------|----------|
| Y tuong | Binh dang | Gan = quan trong hon |
| Tinh toan | Don gian | Phuc tap hon |
| Hieu qua | Tot khi du lieu deu | Tot khi du lieu lech |
| Outliers | Nhay cam | It nhay cam hon |

#### 2.5. Chon k phu hop
- k nho: Nhay cam voi nhieu
- k lon: Mat ranh gioi phan lop
- Thuong chon k le de tranh hoa

---

## CAI DAT

### 1. Class KMeans

```python
class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
        self.labels = None
    
    def fit(self, X):
        # 1. Khoi tao tam cum ngau nhien
        # 2. Lap: gan diem vao cum + cap nhat tam
        # 3. Dung khi hoi tu
        
    def predict(self, X):
        # Gan diem moi vao cum gan nhat
```

### 2. Class KNN

```python
class KNN:
    def __init__(self, k=3, weights='uniform'):
        self.k = k
        self.weights = weights  # 'uniform' hoac 'distance'
    
    def fit(self, X, y):
        # Luu tap huan luyen
        
    def predict(self, X):
        # Voi moi diem: tim k lang gieng + voting
```

---

## CACH SU DUNG

### 1. Cai dat thu vien

```bash
pip install numpy matplotlib
```

### 2. Chay chuong trinh

```bash
python main.py
```

### 3. Menu chuong trinh

```
==================================================
BUOI 5: THUAT TOAN K-MEANS VA K-NN
==================================================

Chon bai tap de chay:
1. Bai 1: Demo K-Means Clustering
2. Bai 2: Demo K-NN Classification
3. Chay tat ca
0. Thoat

Nhap lua chon (0-3): 
```

### 4. Input dong

**K-Means:**
- So diem du lieu (mac dinh 150)
- So cum k (mac dinh 3)

**K-NN:**
- So lang gieng k (mac dinh 5)
- Cach tinh trong so (uniform/distance)

---

## KET QUA DEMO

### Demo K-Means

```
BAI 1: DEMO K-MEANS CLUSTERING
==================================================

Nhap so diem du lieu: 150
Nhap so cum k: 3

Tao 150 diem du lieu...
Chay K-Means voi k=3...
Hoi tu sau 5 lan lap

KET QUA K-MEANS:
----------------------------------------
So cum: 3
SSE (Inertia): 245.67

Tam cum (Centroids):
  Cum 0: (2.05, 1.98)
  Cum 1: (7.93, 2.12)
  Cum 2: (4.98, 7.89)

So diem moi cum:
  Cum 0: 50 diem
  Cum 1: 50 diem
  Cum 2: 50 diem
```

### Demo K-NN

```
BAI 2: DEMO K-NN CLASSIFICATION
==================================================

Nhap so lang gieng k: 5
Chon trong so (1=uniform, 2=distance): 1

Tap huan luyen: 96 mau
Tap kiem tra: 24 mau

KET QUA K-NN:
----------------------------------------
So lang gieng k: 5

Cach 1 - Uniform weights:
  Do chinh xac: 95.83%

Cach 2 - Distance weights:
  Do chinh xac: 95.83%

=> Hai cach cho ket qua nhu nhau!
```

---

## PHAN TICH

### 1. K-Means

**Anh huong cua k:**
- k qua nho: Cum qua lon, mat thong tin
- k qua lon: Cum qua nho, over-fitting
- Dung Elbow Method de chon k toi uu

**Anh huong cua khoi tao:**
- Khoi tao ngau nhien co the cho ket qua khac nhau
- Giai phap: K-Means++ de chon tam tot hon

### 2. K-NN

**So sanh 2 cach trong so:**
- Uniform: Don gian, tot voi du lieu deu
- Distance: Phuc tap hon, tot voi du lieu lech

**Anh huong cua k:**
- k = 1: Nhay cam voi nhieu, de overfit
- k qua lon: Underfitting, mat ranh gioi
- Chon k bang Cross-Validation

---

## UNG DUNG THUC TE

### K-Means
1. **Phan khuc khach hang** - Marketing
2. **Nen anh** - Image compression
3. **Phat hien bat thuong** - Anomaly detection
4. **Gom nhom van ban** - Document clustering

### K-NN
1. **Nhan dang chu viet tay** - OCR
2. **He thong goi y** - Recommendation
3. **Chan doan benh** - Medical diagnosis
4. **Phan loai email** - Spam detection

---

## TOI UU VA CAI TIEN

### K-Means
- **K-Means++**: Khoi tao tam cum thong minh hon
- **Mini-batch K-Means**: Xu ly du lieu lon
- **Elbow Method**: Chon k toi uu

### K-NN
- **KD-Tree**: Tang toc tim kiem
- **Ball Tree**: Tot voi chieu cao
- **Cross-Validation**: Chon k toi uu

---

## TAI LIEU THAM KHAO

1. **Bishop, C.M.** (2006). *Pattern Recognition and Machine Learning*
2. **Hastie, T. et al.** (2009). *The Elements of Statistical Learning*
3. **Scikit-learn Documentation**: [K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
4. **Scikit-learn Documentation**: [KNN](https://scikit-learn.org/stable/modules/neighbors.html)

---

## KET LUAN

Bai tap da giup toi:

1. Hieu ro thuat toan K-Means va K-NN
2. Cai dat thanh cong ca 2 thuat toan tu dau
3. So sanh 2 cach danh gia trong so trong K-NN
4. Tao ung dung demo voi input dong
5. Hieu ung dung thuc te cua Machine Learning

**K-Means** va **K-NN** la 2 thuat toan co ban nhung rat quan trong trong Machine Learning, la nen tang de hoc cac thuat toan phuc tap hon.

---

**Signature:**
```
/**
 * Author: hoangedu773
 * GitHub: https://github.com/hoangedu773
 * Date: 2025-12-14
 */
```

---

**Cam on thay/co da huong dan!**
