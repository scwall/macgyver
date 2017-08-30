from structures.character import Character


class Hero(Character):
    def __init__(self, down, up, left, right):
        self.objet = []

        super().__init__(down, up, left, right,"hero")

    def takeObjet(self):
        pass
