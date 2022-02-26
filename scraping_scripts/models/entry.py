
class entry:
    def __init__(self, title, rank, comments, score):
        self.title = title
        self.rank = rank
        self.comments = comments
        self.score = score

    def print_entry(self):
        return self.rank + " | " + self.title + \
            " | " + self.comments + " | " + self.score


