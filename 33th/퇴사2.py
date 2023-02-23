#DP?
from sys import stdin 
stdin = open("Python\\input",'r')
n = int(stdin.readline())
maximum_profits = [0 for _ in range(n+1)]
max_profit = 0
for day in range(1,n+1):
    t, p = map(int,stdin.readline().split())
    max_profit = max(max_profit, maximum_profits[day-1])
    if not maximum_profits[day]:
        maximum_profits[day] = max_profit
    if day + t - 1 > n :
        continue
    maximum_profits[day+t-1] = max(max_profit + p, maximum_profits[day+t-1])
print(max(max_profit,maximum_profits[-1]))