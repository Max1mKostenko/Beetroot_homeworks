class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss


boss1 = Boss(1, "John Doe", "XYZ Company")
boss2 = Boss(2, "Jane Smith", "ABC Corporation")
invalid_boss = Boss(3, "Invalid Boss", "Invalid Company")


worker1 = Worker(100, "Worker 1", "XYZ Company", boss1)
worker2 = Worker(102, "Worker 3", "ABC Corporation", boss2)

boss1.add_worker(worker1)
boss1.add_worker(worker2)

print(worker1.boss.name)
print(worker2.boss.name)
