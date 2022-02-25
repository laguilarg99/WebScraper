
class entry:
    def __init_(self, title, number_of_order, number_of_comments, points):
        self.title = title
        self.number_of_order = number_of_order
        self.number_of_comments = number_of_comments
        self.points = points

    def print_entry(self):
        print(self.number_of_order + " | " + self.title + 
                " | " + self.number_of_comments + " | " + self.points)
        

