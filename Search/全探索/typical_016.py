# ----- input ----- #
N = int(input())
A,B,C = sorted(list(map(int,input().split())))

# ----- Aで使う硬貨とBで使う硬貨の枚数が分かればCで使う効果の枚数は求まる ----- #
Ans = 10000
for i in range(10000):
    if i>=Ans:
        break
    for j in range(10000):
        if i+j>=Ans:
            break
        X = N-(A*i)-(B*j)
        if X%C==0:
            Ans = min(Ans, i+j+(X//C))

print(Ans)
