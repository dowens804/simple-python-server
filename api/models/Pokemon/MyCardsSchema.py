from dataclasses import dataclass
from typing import Optional
from .PokemonCard import PokemonCard
from .TrainerCard import TrainerCard

@dataclass
class MyCardInfo:
    cardId: str 
    cardCount: int
    fullCardInfo: Optional[PokemonCard | TrainerCard] 

@dataclass
class MyCards:
    lastUpdate: str 
    cards: dict[str, MyCardInfo]
