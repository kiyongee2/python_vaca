
class Dog:
    kind = "진돗개"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"강아지 이름: {self.name}"