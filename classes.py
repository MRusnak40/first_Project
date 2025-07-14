import random
from abc import abstractmethod


class Worker:
    list=[]
    def __init__(self, name, ID, position):
        self.name = name
        self.ID = ID
        self.position = position
        Worker.list.append(self)
    def get_workers(self):
        return f"Worker: {self.name} /*/ {self.ID} /*/ {self.position}"

    def __str__(self):
        return f"Worker: {self.name} /*/ {self.ID} /*/ {self.position}"

"""
class List_of_Workers:
    list_of_Workers = list

    def __init__(self, workers):
        self.workers = workers
        List_of_Workers.list_of_Workers.append(self.workers)

   
    def get_all_Workers(self):
        for list in List_of_Workers.list_of_Workers:
            print(list.ge)
"""

class Papers(Worker):
    list_of_papers=[]

    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator

    @abstractmethod
    def __str__(self):
       pass


    @abstractmethod
    def get_all_papers(self):
        pass


class Contract(Papers):

    def __init__(self, name, description, creator, sign):
        Papers.__init__(self, name, description, creator)
        self.sign = str(sign).upper()
        Papers.list_of_papers.append(self)


    def __str__(self):
        return f"{self.name} {self.description} {self.creator} {self.sign}"
    def get_all_papers(self):
        return f"Contract: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.sign}"


class Extract(Papers):
    def __init__(self, name, description, creator, num_of_pages):
        super().__init__(name, description, creator)
        self.num_of_pages = num_of_pages
        Papers.list_of_papers.append(self)

    def __str__(self):
        return f"{self.name} {self.description} {self.creator} {self.num_of_pages} "
    def get_all_papers(self):
        return f"Extract: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.num_of_pages}"


class Invoice(Papers):

    def __init__(self, name, description, creator, price, created_for):
        super().__init__(name, description, creator)
        self.price = price
        self.created_for = created_for
        Papers.list_of_papers.append(self)


    def __str__(self):
        return f"{self.name} {self.description} {self.creator} {self.price} {self.created_for}"

    def get_all_papers(self):
        return f"Invoice: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.price:.2f}$ /*/ {Worker.get_workers(self.created_for)}"




worker_1 = Worker("Franta", 1558, "Manager")
worker_2 = Worker("Karel", 4568, "Worker")
worker_3 = Worker("Jiri", 4568, "Servis")




paper_1 = Contract("Paper 1", "Work contract", random.choice(Worker.list), "KAREL")
paper_2 = Invoice("Paper 2", "Invoice for fridge", random.choice(Worker.list), 150, random.choice(Worker.list))
paper_3 = Extract(name="Paper 3", description="Extract from archive", creator=random.choice(Worker.list), num_of_pages=20)
# for x in range(10):

for worker in Worker.list:
    print(worker)

for paper in Papers.list_of_papers:
    print(paper)