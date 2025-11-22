from manager import Manager
import json
import os

REPO = "data_base.json"

class Context:
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_root():
        root = os.path.join(
            r"C:\Users\Kevin Emilio\Programación\Python\Projects\Recomendador-de-Cursos\backend",
            REPO
        )
        return root

    @staticmethod
    def get_json() -> Manager:
        root = Context.get_root()
        with open(root, "r", encoding="utf-8") as file:
            if os.path.getsize(root)==0:
                return Manager([])
            try:
               json_data = json.load(file)
               return Manager.read_json(json_data)
            except:
                raise Exception("Error al cargar el json")
    
    @staticmethod
    def save_json(manager: Manager):
        root = Context.get_root()
        with open(root, "w", encoding="utf-8") as file:
            json.dump(manager.to_json(), file, ensure_ascii=False ,indent=4)
