from dataclasses import dataclass
from .BaseCard import BaseCard

@dataclass
class TrainerCard(BaseCard):
    effect: str | None 
    trainerType: str | None 