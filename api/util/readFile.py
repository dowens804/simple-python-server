import os
import json
from dataclasses import dataclass
#from typing import IO, #AnyStr, TextIOWrapper, _WrappedBuffer
from flask import Flask
from flask import current_app
from dacite import from_dict 

from api.models.Pokemon.MyCardsSchema import MyCards #g, open_resource

@dataclass
class FileReaderOptions:
    ext: str = ".txt"
    encoding: str = 'utf-8'

class FileReader:
    def __init__(self, appRootPath:str):
        self.appRootPath = appRootPath

    def _readFile(self, fileName: str, options: FileReaderOptions):
        file_path = os.path.join(self.appRootPath,'static/data', f'{fileName}{options.ext}')
        
        file_content = ""
        with open(file_path, 'r', encoding=options.encoding) as f:
            file_content = f.read()
        
        return file_content

    def readJsonFile(self, fileName: str):
        options = FileReaderOptions(ext= ".json")

        fileData = self._readFile(fileName, options)
        return json.loads(fileData)
        
    def readCsvFile(self, fileName: str):
        options = FileReaderOptions(ext= ".csv")
        fileData = self._readFile(fileName, options)
        return fileData
    

class AppFileReader:
    def __init__(self, flaskApp: Flask):
        self.app = flaskApp

    def _relativeFilePath(self, fileName:str, options: FileReaderOptions):
        return f'static/data/{fileName}{options.ext}'

    def _readFile(self, fileName: str, options: FileReaderOptions) -> str:
        file_content: str = ""
        with current_app.open_resource(self._relativeFilePath(fileName, options), mode="r", encoding=options.encoding) as file: # type: ignore
            file_content = str(object=file.read()) # type: ignore
        
        return file_content
    
    def readFile(self, fileName: str, options: FileReaderOptions) -> str:
        return self._readFile(fileName, options)

    def readJsonFile(self, fileName: str):
        options = FileReaderOptions(ext= ".json")

        fileData = self._readFile(fileName, options)
        return json.loads(fileData)
    
class MyCardsFileReader:
    def __init__(self, flaskApp: Flask):
        self.app = flaskApp
        self.fileReader = AppFileReader(flaskApp);
        self.fileName = "my-cards"

    def _getFileData(self) -> str:
        options = FileReaderOptions(ext= ".json")
        dataString = self.fileReader.readFile(self.fileName, options)
        return dataString
    
    def _getJsonData(self) :
        return self.fileReader.readJsonFile(self.fileName)

    def getCards(self) ->  MyCards:
        dataString = self._getJsonData()
        return from_dict(MyCards, dataString)
    
# pip show dataclasses_json