def multiples(m,n,below):
    sum_mtps = sum(i for i in range(1,below) if i%3==0 or i%5==0)
    return sum_mtps

print(multiples(3, 5, 10))
