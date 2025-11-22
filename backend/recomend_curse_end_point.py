from context import Context

class RecommendCurse:
    def __init__(self, client_name: str, curse_description):
        self.client_name: str = client_name
        self.curse_description: str = curse_description
    
    def recommend_curse(self) -> list[str]:
        tags = self.curse_description.split(" ")
        match_curses: list[str] = []
        manager = Context.get_json()
        for curse in manager.curse_list:
            for tag in tags:
                if tag in curse.tags:
                    match_curses.append(curse.name)
                    break
        return match_curses
