from collections import defaultdict

def solution(friends, gifts):
    send_dic = defaultdict(int)
    gnum_dic = defaultdict(int)
    
    for g in gifts:
        a, b = g.split()
        send_dic[g] += 1
        gnum_dic[a] += 1
        gnum_dic[b] -= 1
    
    cnt_dic = defaultdict(int)
    for i, a in enumerate(friends):
        for b in friends[i:]:
            
            g_ab = a + ' ' + b
            g_ba = b + ' ' + a
            send_ab = send_dic[g_ab]
            send_ba = send_dic[g_ba]
            
            if send_ab > send_ba:
                cnt_dic[a] += 1
            elif send_ab < send_ba:
                cnt_dic[b] += 1
            else:
                gnum_a = gnum_dic[a]
                gnum_b = gnum_dic[b]
                
                if gnum_a > gnum_b:
                    cnt_dic[a] += 1
                    
                elif gnum_a < gnum_b:
                    cnt_dic[b] += 1
    
    result = 0
    for f in cnt_dic:
        result = max(result, cnt_dic[f])
    
    return result