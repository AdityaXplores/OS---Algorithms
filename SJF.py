n = int(input("Enter number of processes: "))

processes = []
arrival_time = []
burst_time = []

for i in range(n):
    processes.append(i + 1)
    arrival_time.append(int(input(f"Enter arrival time for process {i+1}: ")))
    burst_time.append(int(input(f"Enter burst time for process {i+1}: ")))

completed = [False] * n
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

current_time = 0
completed_count = 0

while completed_count < n:
    idx = -1
    min_bt = float('inf')

    for i in range(n):
        if arrival_time[i] <= current_time and not completed[i]:
            if burst_time[i] < min_bt:
                min_bt = burst_time[i]
                idx = i

    if idx == -1:
        current_time += 1
        continue

    current_time += burst_time[idx]
    completion_time[idx] = current_time
    turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
    waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
    completed[idx] = True
    completed_count += 1

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t"
          f"{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

avg_tat = sum(turnaround_time) / n
avg_wt = sum(waiting_time) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
