from menu.items import item


class SelectionItem(item):

    def __init__(self, name, description):
        super().__init__(name=name, description=description)
