from curse import Curse

class Manager:
    def __init__(self, curse_list: list[Curse]):
        self.curse_list = curse_list

    @staticmethod
    def read_json(data: dict) -> "Manager":
        curse_list: list[Curse]=[]
        for name in data.keys():
            curse_list.append(Curse.read_json(data[name]))
        return Manager(curse_list)
    
    def to_json(self):
        data = {}
        for c in self.curse_list:
            data[c.name] = c.to_json()
        return data
