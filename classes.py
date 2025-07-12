from abc import abstractmethod


class Papers:
    def __init__(self, name, description, creator):
        self.name = name
        self.description = description
        self.creator = creator

    @abstractmethod
    def get_all_papers(self):
        pass


class Contract(Papers):
    def __init__(self, name, description, creator, sign):
        super().__init__(self, name, description, creator)
        self.sign = sign

    def get_all_papers(self):

        return f"Contract: {self.name} /*/ {self.sign} /*/ {self.description} /*/ {self.creator} /*/ {self.sign}"

class Extract(Papers):
    def __init__(self, name, description, creator, num_of_pages):
        super().__init__(name, description, creator, num_of_pages)
        self.num_of_pages = num_of_pages


    def get_all_papers(self):
        return f"Extract: {self.name} /*/ {self.description} /*/ {self.creator} /*/ {self.num_of_pages}"

class Invoice(Papers):

    def __init__(self, name, description, creator, price, created_for):
        super().__init__(name, description, creator)
        self.price = price
        self.created_for = created_for

    def get_all_papers(self):
        return f"Extract: {self.name} /*/ {self.description} /*/ {self.creator} /*/ {self.price} /*/ {self.created_for}"


class List_of_papers:
    list_of_papers = []

    def __init__(self, papers):
        self.papers = papers
        List_of_papers.list_of_papers.append(self.papers)

    @abstractmethod
    def get_all_papers(self):
        for list in List_of_papers.list_of_papers:
            print(list.get_all_papers())
