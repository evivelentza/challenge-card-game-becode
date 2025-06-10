class Symbol:
    def __init__(self, color: str, icon):
        self.color = color
        self.icon = icon

    def __str__(self) -> str:
        return self.icon  
class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}{self.icon}"
#creating two new classes to define the card
