"""
Author: hoangedu773
GitHub: https://github.com/hoangedu773
Date: 2025-12-14
Description: Buoi 5 - Thuat toan K-Means va K-NN

BAI TAP:
    Bai 1: Cai dat thuat toan K-means
    Bai 2: Cai dat thuat toan K-NN voi 2 cach danh gia trong so k
    Bai 3: Cai dat ung dung demo cho 2 thuat toan tren
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math

# ==============================================================================
# BAI 1: THUAT TOAN K-MEANS CLUSTERING
# ==============================================================================

class KMeans:
    """
    Bai 1: Thuat toan K-Means de phan cum du lieu
    
    Y tuong:
        1. Chon ngau nhien k diem lam tam cum (centroids)
        2. Gan moi diem du lieu vao cum co tam gan nhat
        3. Cap nhat lai tam cum = trung binh cac diem trong cum
        4. Lap lai buoc 2-3 cho den khi hoi tu
    """
    
    def __init__(self, k=3, max_iters=100, random_state=None):
        """
        Khoi tao thuat toan K-Means
        
        Parameters:
            k: So cum can phan chia
            max_iters: So lan lap toi da
            random_state: Seed cho random (de ket qua lap lai duoc)
        """
        self.k = k
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = None
        self.labels = None
        
    def euclidean_distance(self, x1, x2):
        """Tinh khoang cach Euclidean giua 2 diem"""
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    def fit(self, X):
        """
        Huan luyen thuat toan K-Means
        
        Parameters:
            X: Du lieu dau vao (numpy array)
        """
        if self.random_state:
            np.random.seed(self.random_state)
        
        n_samples = X.shape[0]
        
        # Buoc 1: Chon ngau nhien k diem lam tam cum ban dau
        random_indices = np.random.choice(n_samples, self.k, replace=False)
        self.centroids = X[random_indices].copy()
        
        for iteration in range(self.max_iters):
            # Buoc 2: Gan moi diem vao cum gan nhat
            self.labels = self._assign_clusters(X)
            
            # Buoc 3: Cap nhat tam cum
            new_centroids = self._update_centroids(X)
            
            # Kiem tra hoi tu (tam cum khong doi)
            if np.allclose(self.centroids, new_centroids):
                print(f"Hoi tu sau {iteration + 1} lan lap")
                break
                
            self.centroids = new_centroids
        
        return self
    
    def _assign_clusters(self, X):
        """Gan moi diem vao cum co tam gan nhat"""
        labels = []
        for point in X:
            distances = [self.euclidean_distance(point, centroid) 
                        for centroid in self.centroids]
            labels.append(np.argmin(distances))
        return np.array(labels)
    
    def _update_centroids(self, X):
        """Cap nhat tam cum = trung binh cac diem trong cum"""
        new_centroids = np.zeros((self.k, X.shape[1]))
        for i in range(self.k):
            cluster_points = X[self.labels == i]
            if len(cluster_points) > 0:
                new_centroids[i] = np.mean(cluster_points, axis=0)
            else:
                new_centroids[i] = self.centroids[i]
        return new_centroids
    
    def predict(self, X):
        """Du doan cum cho du lieu moi"""
        return self._assign_clusters(X)
    
    def get_inertia(self, X):
        """Tinh tong binh phuong khoang cach tu cac diem den tam cum (SSE)"""
        inertia = 0
        for i, point in enumerate(X):
            centroid = self.centroids[self.labels[i]]
            inertia += self.euclidean_distance(point, centroid) ** 2
        return inertia


# ==============================================================================
# BAI 2: THUAT TOAN K-NN (K-NEAREST NEIGHBORS)
# ==============================================================================

class KNN:
    """
    Bai 2: Thuat toan K-NN de phan lop du lieu
    
    Y tuong:
        1. Tinh khoang cach tu diem can phan lop den tat ca diem trong tap huan luyen
        2. Chon k diem gan nhat
        3. Phan lop theo da so (majority voting)
    
    2 cach danh gia trong so k:
        - Uniform: Tat ca k lang gieng co trong so bang nhau
        - Distance: Lang gieng gan hon co trong so lon hon (1/distance)
    """
    
    def __init__(self, k=3, weights='uniform'):
        """
        Khoi tao thuat toan K-NN
        
        Parameters:
            k: So lang gieng gan nhat
            weights: Cach tinh trong so
                - 'uniform': Trong so bang nhau
                - 'distance': Trong so theo khoang cach (1/d)
        """
        self.k = k
        self.weights = weights
        self.X_train = None
        self.y_train = None
        
    def euclidean_distance(self, x1, x2):
        """Tinh khoang cach Euclidean giua 2 diem"""
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    def fit(self, X, y):
        """
        Huan luyen K-NN (chi luu lai du lieu)
        
        Parameters:
            X: Du lieu dau vao
            y: Nhan tuong ung
        """
        self.X_train = np.array(X)
        self.y_train = np.array(y)
        return self
    
    def predict(self, X):
        """Du doan nhan cho du lieu moi"""
        X = np.array(X)
        predictions = []
        for x in X:
            prediction = self._predict_single(x)
            predictions.append(prediction)
        return np.array(predictions)
    
    def _predict_single(self, x):
        """Du doan nhan cho mot diem du lieu"""
        # Tinh khoang cach den tat ca diem trong tap huan luyen
        distances = [self.euclidean_distance(x, x_train) 
                    for x_train in self.X_train]
        
        # Lay chi so cua k diem gan nhat
        k_indices = np.argsort(distances)[:self.k]
        k_labels = self.y_train[k_indices]
        k_distances = np.array(distances)[k_indices]
        
        if self.weights == 'uniform':
            # Cach 1: Trong so bang nhau - majority voting
            return self._majority_vote(k_labels)
        else:
            # Cach 2: Trong so theo khoang cach
            return self._weighted_vote(k_labels, k_distances)
    
    def _majority_vote(self, labels):
        """Cach 1: Bau chon da so (trong so bang nhau)"""
        counter = Counter(labels)
        return counter.most_common(1)[0][0]
    
    def _weighted_vote(self, labels, distances):
        """Cach 2: Bau chon co trong so theo khoang cach"""
        # Tranh chia cho 0
        weights = np.where(distances == 0, 1e10, 1.0 / distances)
        
        # Tinh tong trong so cho moi nhan
        weighted_votes = {}
        for label, weight in zip(labels, weights):
            if label not in weighted_votes:
                weighted_votes[label] = 0
            weighted_votes[label] += weight
        
        # Tra ve nhan co tong trong so lon nhat
        return max(weighted_votes, key=weighted_votes.get)
    
    def score(self, X, y):
        """Tinh do chinh xac (accuracy)"""
        predictions = self.predict(X)
        return np.mean(predictions == y)


# ==============================================================================
# BAI 3: UNG DUNG DEMO
# ==============================================================================

def generate_sample_data(n_samples=100, n_clusters=3, random_state=42):
    """Tao du lieu mau de demo"""
    np.random.seed(random_state)
    
    # Tao cac cum du lieu
    data = []
    labels = []
    
    centers = [(2, 2), (8, 2), (5, 8)]
    
    for i in range(n_clusters):
        n = n_samples // n_clusters
        x = np.random.randn(n) + centers[i][0]
        y = np.random.randn(n) + centers[i][1]
        data.extend(zip(x, y))
        labels.extend([i] * n)
    
    return np.array(data), np.array(labels)


def visualize_kmeans(X, kmeans, title="K-Means Clustering"):
    """Bai 3: Truc quan hoa ket qua K-Means"""
    plt.figure(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    for i in range(kmeans.k):
        cluster_points = X[kmeans.labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                   c=colors[i % len(colors)], label=f'Cum {i}', alpha=0.6, s=50)
    
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], 
               c='black', marker='X', s=200, label='Tam cum')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('kmeans_result.png', dpi=300, bbox_inches='tight')
    print("\nDa luu anh: kmeans_result.png")
    plt.show()


def visualize_knn(X_train, y_train, X_test, y_pred, title="K-NN Classification"):
    """Bai 3: Truc quan hoa ket qua K-NN"""
    plt.figure(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    markers = ['o', 's', '^']
    
    # Ve diem train
    for i in np.unique(y_train):
        mask = y_train == i
        plt.scatter(X_train[mask, 0], X_train[mask, 1], 
                   c=colors[i % len(colors)], marker=markers[i % len(markers)],
                   label=f'Train - Lop {i}', alpha=0.5, s=50)
    
    # Ve diem test
    for i in np.unique(y_pred):
        mask = y_pred == i
        plt.scatter(X_test[mask, 0], X_test[mask, 1], 
                   c=colors[i % len(colors)], marker='*',
                   label=f'Test - Du doan Lop {i}', s=200, edgecolors='black')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('knn_result.png', dpi=300, bbox_inches='tight')
    print("\nDa luu anh: knn_result.png")
    plt.show()


def demo_kmeans():
    """Demo thuat toan K-Means"""
    print("\n" + "=" * 60)
    print("BAI 1: DEMO K-MEANS CLUSTERING")
    print("=" * 60)
    
    # Nhap tham so tu nguoi dung
    try:
        n_samples = int(input("\nNhap so diem du lieu (mac dinh 150): ") or "150")
        k = int(input("Nhap so cum k (mac dinh 3): ") or "3")
    except ValueError:
        n_samples, k = 150, 3
    
    # Tao du lieu mau
    print(f"\nTao {n_samples} diem du lieu...")
    X, _ = generate_sample_data(n_samples=n_samples, n_clusters=3)
    
    # Chay K-Means
    print(f"Chay K-Means voi k={k}...")
    kmeans = KMeans(k=k, max_iters=100, random_state=42)
    kmeans.fit(X)
    
    # In ket qua
    print("\n" + "-" * 40)
    print("KET QUA K-MEANS:")
    print("-" * 40)
    print(f"So cum: {k}")
    print(f"SSE (Inertia): {kmeans.get_inertia(X):.2f}")
    print("\nTam cum (Centroids):")
    for i, centroid in enumerate(kmeans.centroids):
        print(f"  Cum {i}: ({centroid[0]:.2f}, {centroid[1]:.2f})")
    
    print("\nSo diem moi cum:")
    for i in range(k):
        count = np.sum(kmeans.labels == i)
        print(f"  Cum {i}: {count} diem")
    
    # Visualization
    visualize_kmeans(X, kmeans, f"K-Means Clustering (k={k})")


def demo_knn():
    """Demo thuat toan K-NN"""
    print("\n" + "=" * 60)
    print("BAI 2: DEMO K-NN CLASSIFICATION")
    print("=" * 60)
    
    # Nhap tham so tu nguoi dung
    try:
        k = int(input("\nNhap so lang gieng k (mac dinh 5): ") or "5")
        weight_choice = input("Chon trong so (1=uniform, 2=distance, mac dinh 1): ") or "1"
        weights = 'distance' if weight_choice == '2' else 'uniform'
    except ValueError:
        k, weights = 5, 'uniform'
    
    # Tao du lieu
    print("\nTao du lieu huan luyen va kiem tra...")
    X, y = generate_sample_data(n_samples=120, n_clusters=3)
    
    # Chia train/test
    np.random.seed(42)
    indices = np.random.permutation(len(X))
    split = int(0.8 * len(X))
    
    X_train, X_test = X[indices[:split]], X[indices[split:]]
    y_train, y_test = y[indices[:split]], y[indices[split:]]
    
    print(f"Tap huan luyen: {len(X_train)} mau")
    print(f"Tap kiem tra: {len(X_test)} mau")
    
    # Chay K-NN voi ca 2 cach danh gia trong so
    print(f"\nChay K-NN voi k={k}, weights={weights}...")
    
    # Uniform weights
    knn_uniform = KNN(k=k, weights='uniform')
    knn_uniform.fit(X_train, y_train)
    acc_uniform = knn_uniform.score(X_test, y_test)
    
    # Distance weights
    knn_distance = KNN(k=k, weights='distance')
    knn_distance.fit(X_train, y_train)
    acc_distance = knn_distance.score(X_test, y_test)
    
    # In ket qua
    print("\n" + "-" * 40)
    print("KET QUA K-NN:")
    print("-" * 40)
    print(f"So lang gieng k: {k}")
    print(f"\nCach 1 - Uniform weights:")
    print(f"  Do chinh xac: {acc_uniform * 100:.2f}%")
    print(f"\nCach 2 - Distance weights:")
    print(f"  Do chinh xac: {acc_distance * 100:.2f}%")
    
    # So sanh
    if acc_distance > acc_uniform:
        print("\n=> Distance weights tot hon!")
    elif acc_uniform > acc_distance:
        print("\n=> Uniform weights tot hon!")
    else:
        print("\n=> Hai cach cho ket qua nhu nhau!")
    
    # Visualization
    knn = knn_uniform if weights == 'uniform' else knn_distance
    y_pred = knn.predict(X_test)
    visualize_knn(X_train, y_train, X_test, y_pred, 
                  f"K-NN Classification (k={k}, weights={weights})")


def main():
    """Ham chinh - Menu chon bai tap"""
    print("=" * 60)
    print("BUOI 5: THUAT TOAN K-MEANS VA K-NN")
    print("Author: hoangedu773")
    print("=" * 60)
    
    while True:
        print("\nChon bai tap de chay:")
        print("1. Bai 1: Demo K-Means Clustering")
        print("2. Bai 2: Demo K-NN Classification")
        print("3. Chay tat ca")
        print("0. Thoat")
        
        choice = input("\nNhap lua chon (0-3): ").strip()
        
        if choice == '1':
            demo_kmeans()
        elif choice == '2':
            demo_knn()
        elif choice == '3':
            demo_kmeans()
            demo_knn()
        elif choice == '0':
            print("\nTam biet!")
            break
        else:
            print("\nLua chon khong hop le!")


if __name__ == "__main__":
    main()
