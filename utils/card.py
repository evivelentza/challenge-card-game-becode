class Symbol:
    def __init__(self, color: str, icon):
        self.color = color
        self.icon = icon
    
class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)
        self.value = value

