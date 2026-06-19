from dataclasses import dataclass

@dataclass
class BaseCard:
    category:str
    id: str 
    name:str
    illustrator:str | None
    image:str | None
    rarity: str| None
    description: str| None 