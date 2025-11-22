class Curse:
    def __init__(self, name: str, duracion: str, tags: list[str]):
        self.name = name
        self.duracion = duracion
        self.tags: list = tags

    def add_tags(self, new_tags: list[str]):
        for nt in new_tags:
            if not nt in self.tags:
                self.tags.append(nt)

    @staticmethod
    def read_json(data: dict) -> "Curse":
        return Curse(name=data["name"],
              duracion= data["duracion"],
              tags= data["tags"]
              )
    def to_json(self)->dict:
        data={}
        data["name"]= self.name
        data["duracion"]= self.duracion
        data["tags"]= self.tags
        return data
