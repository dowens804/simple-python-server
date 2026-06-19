from dataclasses import dataclass

from api.models.Pokemon import PokemonCard, TrainerCard
from api.models.Pokemon.MyCardsSchema import MyCardInfo
from typing import cast

@dataclass
class SingleCardTemplateModel:
    name:str
    category:str
    count:int

def buildCardModel(cardData: MyCardInfo) -> SingleCardTemplateModel:
    isPoke = isinstance(cardData.fullCardInfo, PokemonCard)
    isTrain = isinstance(cardData.fullCardInfo, TrainerCard)

    name:str = "No Card"
    category:str = "You failed"
    count:int = 0

    if(isPoke):
        card = cast(PokemonCard, cardData.fullCardInfo)
        name = card.name
        count = cardData.cardCount
        category = card.category

    elif(isTrain):
        card = cast(TrainerCard, cardData.fullCardInfo)
        name= card.name
        count = cardData.cardCount
        category = card.trainerType or "No trainer type"

    return SingleCardTemplateModel(name,category, count )

    
