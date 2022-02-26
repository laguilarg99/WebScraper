
class entry:
    def __init__(self, title, rank, comment, score):
        self.title = title
        self.rank = rank
        self.comment = comment
        self.score = score

    def print_entry(self):
        return self.rank + " | " + self.title + \
            " | " + self.comment + " | " + self.score


