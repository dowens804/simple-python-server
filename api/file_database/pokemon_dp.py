

from api.util.readFile import FileReader, AppFileReader
from api.models.Pokemon import *
from typing import cast
from dataclasses import dataclass
import time 
from flask import Flask
from functools import singledispatchmethod
from dacite import from_dict

@dataclass
class QueryResponse:
    results: list[MyCardInfo]
    count: int = 0
    queryTime: float = 0

#region Query Functions 

class QueryFunction:
    def __call__(self, item : PokemonCard | TrainerCard | None) -> bool:
        pass 

class IsType(QueryFunction):
    def __init__(self, type:str):
        self.type = type

    def __call__(self, item : PokemonCard | TrainerCard | None):
        try :
            if item is not None and item.category == "Pokemon":
                actualCard = cast(PokemonCard, item)#PokemonCard(item)
                if(actualCard.types != None):
                    cardTypes = actualCard.types
                    return self.type in cardTypes
                else:
                    return False
            else:
                return False
        except Exception as inst:
            return False

class IsCategory(QueryFunction):
    def __init__(self, category:str):
        self.category = category

    def __call__(self, item : PokemonCard | TrainerCard | None):
        return item is not None and item.category == self.category
    
class IsWeakTo(QueryFunction):
    def __init__(self, type: str):
        self.type = type

    def __call__(self, item : PokemonCard | TrainerCard | None):
        if item is not None and item.category == "Pokemon":
            actualCard = cast(PokemonCard, item)#PokemonCard(item)
            weaknesses = actualCard.weaknesses
            return weaknesses != None and self.type in list(map(lambda x: x.type, weaknesses))  
        else:
            return False

#endregion 

class PokemonDatabase:
    @singledispatchmethod
    def __init__(self, arg):
        raise TypeError("Unsupported argument type")

    @__init__.register(str)
    def _from_string(self, appRootPath: str):
        fr = FileReader(appRootPath=appRootPath)
        rawData = fr.readJsonFile("my-cards")
        self.my_cards = from_dict(MyCards, rawData)#cast(MyCards, rawData) #MyCards.fr#.schema().loads(rawData)#cast(MyCards, rawData);

    @__init__.register(Flask)
    def _from_app(self, app:Flask):
        
        #this has the init_bd action  
        fr = AppFileReader(app)
        rawData = fr.readJsonFile("my-cards")
        self.my_cards = from_dict(MyCards, rawData)#MyCards(lastUpdate=rawData["lastUpdate"], cards=rawData['cards'])#cast(MyCards, rawData);

    def queryFile(self, queryFunc: QueryFunction ) -> QueryResponse:
        start_time = time.perf_counter()
        
        resultList: list[MyCardInfo] = []
        cards = list(self.my_cards.cards.values())
        for card in cards:
            if queryFunc(card.fullCardInfo):
                resultList.append(card)


        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return QueryResponse(results=resultList, count=len(resultList), queryTime=elapsed_time )


        # start_time = time.perf_counter()
        # result = [card for card in list(self.my_cards.cards.values()) if(queryFunc(card.fullCardInfo))]
        # end_time = time.perf_counter()
        # elapsed_time = end_time - start_time
        # return QueryResponse(results=result, count=len(result), queryTime=elapsed_time )

    def queryFileRand(self):
        pass

    def getRandomPokemonByType(self, type:str):
        return self.queryFile(IsType(type))

    def getRandomTrainer(self):
        return self.queryFile(IsCategory("Trainer"))

    def getAllFirePokemon(self):
        return self.queryFile(IsType("fire"))

    def getAllWaterPokemon(self,):
        return self.queryFile(IsType("water"))