from collections import deque


def main():
    H, W = map(int, input().split())
    sh, sw = map(int, input().split())  # スタート地点
    gh, gw = map(int, input().split())  # ゴール地点
    Field = [list(input()) for _ in range(H)]  # 迷路情報
    dist = [[-1] * W for _ in range(H)]  # 最短手数情報
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]

    sh, sw, gh, gw = sh - 1, sw - 1, gh - 1, gw - 1

    Q = deque()
    Q.append((sh, sw))
    dist[sh][sw] = 0
    while Q:
        h, w = Q.popleft()
        for i in range(4):
            next_h = h + dh[i]
            next_w = w + dw[i]
            if 0 <= next_h < H and 0 <= next_w < W and Field[next_h][next_w] == ".":
                if dist[next_h][next_w] == -1:
                    dist[next_h][next_w] = dist[h][w] + 1
                    Q.append((next_h, next_w))
    print(dist[gh][gw])


if __name__ == "__main__":
    main()
