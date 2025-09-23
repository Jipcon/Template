MX = 10 ** 6 + 1
prime = []
LPF = [0] * MX
LPF[1] = 1
is_prime = [True] * MX
is_prime[1]=False
for i in range(2, MX):
    if is_prime[i]:
        LPF[i] = i
        prime.append(i)
    for p in prime:
        if i * p >= MX:
            break
        is_prime[i * p] = False
        LPF[i * p] = p
        if not i % p:  # p是i的最小质因子
            LPF[i] = p
            break
prime.extend((MX, MX))



PRIME_FACTORS=[[] for _ in range(MX)] #质因子
#PRIME_FACTORS[j]:j的所有质因子
for i in range(2,MX):
    if not PRIME_FACTORS[i]: #i是质数
        for j in range(i,MX,i):
            PRIME_FACTORS[j].append(i)

