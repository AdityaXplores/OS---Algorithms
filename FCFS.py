# FCFS Scheduling in Python

n = int(input("Enter number of processes: "))

processes = []
burst_time = []
arrival_time = []

for i in range(n):
    processes.append(i + 1)
    arrival_time.append(int(input(f"Enter arrival time for process {i+1}: ")))
    burst_time.append(int(input(f"Enter burst time for process {i+1}: ")))

process_info = sorted(zip(processes, arrival_time, burst_time), key=lambda x: x[1])
processes, arrival_time, burst_time = zip(*process_info)

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

current_time = 0
for i in range(n):
    if current_time < arrival_time[i]:
        current_time = arrival_time[i]
    current_time += burst_time[i]
    completion_time[i] = current_time
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t"
          f"{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

avg_tat = sum(turnaround_time) / n
avg_wt = sum(waiting_time) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
