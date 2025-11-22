from curse import Curse
from context import Context

class CreateCurse:
    def __init__(self, name: str, duration: str, tags: str):
        self.name = name 
        self.duration = duration 
        self.tags = self.create_tags(tags)

    def create_tags(self, tags: str):
        return tags.split(", ")
    
    def create_curse(self) -> str:
       manager = Context.get_json()
       curse = Curse(self.name, self.duration, self.tags)
       manager.curse_list.append(curse)
       Context.save_json(manager)
       return "Se ha creado correctamente el curso"