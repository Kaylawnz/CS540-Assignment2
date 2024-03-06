import random

class Process:
    def __init__(self, pid, num_tickets):  
        self.pid = pid #set processes id number
        self.num_tickets = num_tickets #number of tickets per lottery number

class Scheduler:
    def __init__(self):  
        self.processes = [] #store processes
        self.total_tickets = 0

    def add_process(self, process):
        self.processes.append(process)
        self.total_tickets += process.num_tickets #update number of tickets

    def allocate_tickets(self):
        allocated_tickets = []
        for process in self.processes:
            for _ in range(process.num_tickets):
                allocated_tickets.append(process.pid)
        return allocated_tickets

    def select_winner(self):
        if not self.processes:
            return None
        
        tickets = self.allocate_tickets()
        winner_ticket = random.choice(tickets)
        
        for process in self.processes:
            if process.pid == winner_ticket:
                return process

if __name__ == "__main__":
    process1 = Process(1, 5)  
    process2 = Process(2, 3)
    process3 = Process(3, 7)

    scheduler = Scheduler()

    scheduler.add_process(process1)
    scheduler.add_process(process2)
    scheduler.add_process(process3)

    winner_process = scheduler.select_winner()

    if winner_process:
        print(f"Process {winner_process.pid} wins the lottery!")
    else:
        print("No process available to select.")
