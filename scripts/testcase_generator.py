#!/usr/bin/env python3
import math
import re
from pathlib import Path
import random
import string


def rand_int(a, b):
    """a<=x<=bを満たす整数xを生成する"""
    return random.randint(a, b)


def rand_list(n, a, b):
    """a<=A_i<=bを満たす要素数nの整数列Aを生成する"""
    return [rand_int(a, b) for _ in range(n)]


def rand_string(n, alphabet=string.ascii_lowercase):
    """長さnの文字列を生成する"""
    return ''.join(random.choice(alphabet) for _ in range(n))


def rand_tree(n):
    """辺の数がnのツリーを作成する"""
    edges = []
    for i in range(2, n + 1):
        p = rand_int(1, i - 1)
        edges.append((p, i))
    return edges


def rand_graph(n, m):
    """頂点数n辺数mの無向グラフを作成する"""
    # 全辺数
    K = n * (n - 1) // 2
    # m 個の番号をランダムに選ぶ（重複なし）
    chosen = random.sample(range(K), m)
    edges = []
    for x in chosen:
        # x を (u, v) に変換する
        # u < v を満たすように計算 O(1) で求まる
        # u = floor((sqrt(8x+1)-1)/2)
        u = int((math.isqrt(8*x + 1) - 1) // 2)
        v = x - u*(u+1)//2
        edges.append((v+1, u+2))
    return edges


def next_sample_filename(prefix="sample-", suffix=".in"):
    # カレントディレクトリのファイル一覧を取得
    base = Path("./tests")

    files = base.glob(f"{prefix}*{suffix}")

    max_num = 0
    pattern = re.compile(rf"{re.escape(prefix)}(\d+){re.escape(suffix)}$")

    for f in files:
        m = pattern.match(f.name)
        if m:
            num = int(m.group(1))
            max_num = max(max_num, num)

    # 次の番号
    next_num = max_num + 1
    return base / f"{prefix}{next_num}{suffix}"

# -----------------------------
# ここにテストケース生成ロジックを書く
# -----------------------------


def generate():
    # 例：N と N 個の整数
    N = 3*10**5
    A = rand_list(N, 1, 10**9)
    return str(N) + "\n" + " ".join(map(str, A))


# -----------------------------
# 実行
# -----------------------------
if __name__ == "__main__":
    filename = next_sample_filename()
    Path(filename).write_text(generate(), encoding="utf-8")
    print(f"{filename} を生成しました")
