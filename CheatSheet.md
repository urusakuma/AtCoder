# Python 競プロ用チートシート

## 入出力

### 基本入力

- **1行1値（整数）**  
  `n = int(input())`

- **1行多値（整数）**  
  `a, b = map(int, input().split())`

- **1行配列（整数リスト）**  
  `A = list(map(int, input().split()))`

### 複数行入力

- **縦にN行（文字列）**  
  `rows = [input() for _ in range(N)]`

- **縦にN行（整数）**  
  `rows = [list(map(int, input().split())) for _ in range(N)]`

### 高速入力

- `import sys`  
- `input = sys.stdin.readline`

---

## 基本テクニック

### 最大・最小・合計

- `mx = max(A)`
- `mn = min(A)`
- `s = sum(A)`

### 並び替え

- **昇順**：`A.sort()`
- **降順**：`A.sort(reverse=True)`
- **別リストにソート結果**：`B = sorted(A)`

### enumerate / zip

- `for i, x in enumerate(A): ...`
- `for a, b in zip(A, B): ...`

---

## 文字列・リスト操作

### 文字列

- **分割**：`s.split()`
- **結合**：`" ".join(list_of_str)`
- **反転**：`s[::-1]`

### リスト内包表記

- `B = [x*x for x in A]`

### 2次元配列

- `grid = [[0]*W for _ in range(H)]`

⚠️ 注意：  
`[[0]*W]*H` は同じ行を共有するので **NG**

---

## よく使う標準ライブラリ

### math

- `import math`
- **切り上げ**：`math.ceil(x)`
- **切り捨て**：`math.floor(x)`
- **平方根**：`math.sqrt(x)`

### itertools

- `from itertools import permutations, combinations, product`
- **順列**：`permutations(A)`
- **組み合わせ**：`combinations(A, r)`

### collections

- `from collections import Counter, deque`
- **カウント**：`cnt = Counter(A)`
- **キュー / 両端キュー**：  
  `q = deque()`  
  `q.append(x)`  
  `q.popleft()`

---

## ソート・二分探索

### カスタムソート

- `A.sort(key=lambda x: x[1])`
- `A.sort(key=lambda x: (x[1], x[2]))`

### 二分探索（bisect）

- `import bisect`
- **左端**：`i = bisect.bisect_left(A, x)`
- **右端**：`j = bisect.bisect_right(A, x)`

---

## グラフ・グリッド

### 隣接リスト

- `G = [[] for _ in range(N)]`
- `G[a].append(b); G[b].append(a)`（無向グラフ）

### 4方向・8方向

- **4方向**  
  `dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]`

- **8方向**  
  `dirs8 = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]`

### 範囲チェック

- `0 <= ny < H and 0 <= nx < W`

---

## DP・その他テクニック用ひな型

### 1次元DP（例：長さN）

- `INF = 10**18`
- `dp = [INF]*(N+1)`
- `dp[0] = 0`

### 2次元DP（例：N×M）

- `dp = [[INF]*(M+1) for _ in range(N+1)]`
