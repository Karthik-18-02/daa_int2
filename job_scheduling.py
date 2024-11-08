class Job:
    def __init__(self, id, profit, deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    slots = [-1] * max_deadline
    scheduled_jobs = []

    for job in jobs:
        for slot in range(job.deadline-1, -1, -1):
            if slots[slot] == -1:
                slots[slot] = job.id
                scheduled_jobs.append(job)
                break

    return scheduled_jobs, sum(job.profit for job in scheduled_jobs)

jobs = [
    Job(1, 20, 2),
    Job(2, 15, 2),
    Job(3, 10, 1),
    Job(4, 5, 3),
    Job(5, 1, 3)
]

scheduled_jobs, profits = job_scheduling(jobs)
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job ID: {job.id}, Profits: {job.profit}, Deadline: {job.deadline}")
print(f"Total Profits: {profits}")