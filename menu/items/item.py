class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_item(self):
        return f"{self.name} {self.description}"
