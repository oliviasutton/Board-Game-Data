
class BoardGame:
    def __init__(self, items: list):
        self.name = items[0]
        self.gib_rating = float(items[1])
        self.ppl_rating = float(items[2])
        self.year = int(items[3])
        self.minplayers = int(items[4])
        self.maxplaytime = int(items[5])
    
    def __str__(self):
        return f"{self.name} ({self.year}) [GR={self.gib_rating}, PR={self.ppl_rating}, MP={self.minplayers}, MT={self.maxplaytime}]"