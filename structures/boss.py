from structures.character import Character


class Boss(Character):
    def __init__(self, down, up, left, right):
        super().__init__(down, up, left, right, "boss")
