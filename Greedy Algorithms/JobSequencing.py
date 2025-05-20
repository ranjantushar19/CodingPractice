def jobSequenceing(deadline, profit):
    n = len(deadline)
    profit_deadline_pair = sorted(zip(profit, deadline), reverse=True)

    job_set = set()
    total_profit = 0
    for i in range(n):
        for j in range(profit_deadline_pair[i][1], 0, -1):
            if j not in job_set:
                job_set.add(j)
                total_profit += profit_deadline_pair[i][0]
                print(f"profit from current job : {total_profit} on day : {j}")
                break

    return total_profit


job_deadline = [4, 5, 6, 6, 4, 2, 2, 2]
job_profit = [20, 60, 70, 65, 25, 80, 10, 22]
print(jobSequenceing(job_deadline, job_profit))
