import random
from abc import abstractmethod


class Worker:

    def __init__(self, name, ID, position):
        self.name = name
        self.ID = ID
        self.position = position

    def get_workers(self):
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
class List_of_papers:
    list_of_papers = list



    @staticmethod
    def get_all_papers_in_one(list_of_papers):
        for list in list_of_papers:
            print(list.get_all_papers())


class Papers(Worker,List_of_papers):
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator

    @abstractmethod
    def get_all_papers(self):
        pass


class Contract(Papers):

    def __init__(self, name, description, creator, sign):
        Papers.__init__(self, name, description, creator)
        self.sign = str(sign).upper()

    def get_all_papers(self):
        return f"Contract: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.sign}"


class Extract(Papers):
    def __init__(self, name, description, creator, num_of_pages):
        super().__init__(name, description, creator)
        self.num_of_pages = num_of_pages

    def get_all_papers(self):
        return f"Extract: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.num_of_pages}"


class Invoice(Papers):

    def __init__(self, name, description, creator, price, created_for):
        super().__init__(name, description, creator)
        self.price = price
        self.created_for = created_for

    def get_all_papers(self):
        return f"Extract: {self.name} /*/ {self.description} /*/ {Worker.get_workers(self.creator)} /*/ {self.price:.2f}$ /*/ {self.created_for}"




worker_1 = Worker("Franta", 1558, "Manager")
worker_2 = Worker("Karel", 4568, "Worker")
worker_3 = Worker("Jiri", 4568, "Servis")

list_of_Workers = [worker_1, worker_2, worker_3]

for worker in list_of_Workers:
    print(worker.get_workers())

print(random.choice(list_of_Workers))
paper_1 = Contract("Paper 1", "Work contract", random.choice(list_of_Workers), "KAREL")
paper_2 = Invoice("Paper 2", "Invoice for fridge", random.choice(list_of_Workers), 150, random.choice(list_of_Workers))
paper_3 = Extract(name="Paper 3", description="Extract from archive", creator=random.choice(list_of_Workers), num_of_pages=20)
# for x in range(10):
List_of_papers.list_of_papers.append(paper_1, paper_2,paper_3)


