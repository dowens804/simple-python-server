from dataclasses import dataclass
from .BaseCard import BaseCard

@dataclass
class PokemonWeakness:
    type: str
    value: str

@dataclass
class PokemonAttack:
    cost: list[str]
    name: str
    damage: int

@dataclass
class PokemonItem:
    name: str | None 
    effect: str | None 

@dataclass
class PokemonCard(BaseCard):
    dexId: list[int] | None
    hp: int | None 
    types: list[str] | None 
    evolveFrom: str | None 
    stage: str | None 
    attacks: list[PokemonAttack] | None 
    weaknesses: list[PokemonWeakness]| None 
    retreat: int| None 
    item: list[PokemonItem] | None 
