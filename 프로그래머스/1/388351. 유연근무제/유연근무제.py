def after_10min(schedule):
    h, m = schedule // 100, schedule % 100
    m += 10
    if m >= 60:
        h += 1
        m -= 60
        # if h >= 24:
        #     h -= 24
    return h * 100 + m


def solution(schedules, timelogs, startday):
    print(startday)
    startday -= 1
    for i, schedule in enumerate(schedules):
        schedules[i] = after_10min(schedule)
        
    chk_log = [True] * len(schedules)
    
    for i, logs in enumerate(zip(*timelogs)):
        if (startday + i) % 7 + 1 >= 6:
            continue
            
        for j, log in enumerate(logs):
            if not chk_log[j]:
                continue
            if schedules[j] >= log:
                continue
            chk_log[j] = False
    print(chk_log)
    return sum(chk_log)