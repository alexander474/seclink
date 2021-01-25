from menu.items.item import Item


class Menu(object):

    def __init__(self, title=None, subtitle=None, description=None):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.selected_option = -1
        self.should_exit = False
        self.should_exit_program = False
        self.items = list()
        self.append_selection_item(Item("a", "n"))
        self.append_selection_item(Item("a2", "n"))
        self.append_selection_item(Item("a3", "n"))

    def run(self):
        if len(self.items) == 0:
            print("There is no items in the menu")
            return
        print("MENU")
        self.print_items()

        while not self.should_exit and not self.should_exit_program and self.selected_option == -1:
            input_value = int(input("Please select a mode: "))  # Should add try catch for input
            if isinstance(input_value, int):
                found = self.items[input_value - 1]
                if isinstance(found, Item):
                    self.selected_option = found  # Found a valid mode
                else:
                    print("Could not determine you're mode")
            else:
                print("Value could not be parsed as an int")
        print(f"Selection is done and you selected: {self.selected_option.print_item()}")
        return self.selected_option

    def print_items(self):
        for i in range(len(self.items)):
            found = self.items[i]
            if isinstance(found, Item):
                print(f"[{i + 1}] {found.print_item()}")

    def append_selection_item(self, item: Item):
        self.items.append(item)
        return True
