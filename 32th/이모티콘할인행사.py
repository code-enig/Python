# 100*(7^4) ~240,100 => 완전탐색......
def solution(users, emoticons):
    answer = []
    percent_comb = h_combination([10,20,30,40],len(emoticons))
    max_users = 0
    max_profit = 0
    
    for percent_list in percent_comb: # 가능한 모든 할인율에 대해 탐색한다.
        n_users,profit = n_signed_and_profit(users, emoticons, percent_list)
        if n_users > max_users: # 가입자 수 우선 
            max_users = n_users
            max_profit = profit
        elif n_users == max_users: # 같다면 이익 우선
            max_profit = max(max_profit, profit)    
    answer = [max_users,max_profit]
       
    return answer

def h_combination(_list,n,ret_lists = [[]]): # itertool의 중복조합(combinations_with_replacement)사용하면 된다.
    nxt_ret_lists = []
    for ret_list in ret_lists:
        for obj in _list:
            nxt_ret_lists.append(ret_list+[obj])
    if n == 1:
        return nxt_ret_lists
    else:
        return h_combination(_list,n-1,nxt_ret_lists)

def n_signed_and_profit(users, emoticons, percents): # 가입한 유저수와 이익을 돌려주는 함수
    n_signed_users = 0 # 가입한유저수
    profit = 0 # 이익
    for i in range(len(users)):
        money = 0 # 이모티콘을 구입하는데 필요한 비용
        for j in range(len(emoticons)):
            if users[i][0] <= percents[j]: #할인율이 주어진 값보다 크다면 구입한다.
                money += (emoticons[j]*(100-percents[j]))//100 # 어차피 나누어 떨어지므로 //100으로하여 정수형으로 놔둔다.
                    
        if money >= users[i][1]: # 비용이 주어진 값보다 크다면
            n_signed_users += 1 # 가입한다.
        else:
            profit += money # 아니라면 비용을 이익에 더해준다.
         
    return n_signed_users, profit

users, emoticons = [[40, 2900],[23, 10000],[11, 5200],[5, 5900],[40, 3100],[27, 9200],[32, 6900]],[1300, 1500, 1600, 4900]
print(solution(users, emoticons))