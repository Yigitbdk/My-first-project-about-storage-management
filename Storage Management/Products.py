from abc import ABC, abstractmethod
from RawMaterials import RawMaterials

class Products( RawMaterials,ABC):
    def __init__(self, pName, pDateOfProduction, pNameOfCustomer, pStorageExpDate, pStorageCode, pListOfMatCodes, pDescription):
        self.__pName = pName
        self.__pDateOfProduction = pDateOfProduction
        self.__pNameOfCustomer = pNameOfCustomer
        self.__pStorageExpDate = pStorageExpDate
        self.__pStorageCode = pStorageCode
        self.__pListOfMatCodes = pListOfMatCodes
        self.__pDescription = pDescription


    # getters for properties
    def getPName(self):
        return self.__pName
    def getPDateOfProduction(self):
        return self.__pDateOfProduction
    def getPNameOfCustomer(self):
        return self.__pNameOfCustomer
    def getPStorageExpDate(self):
        return self.__pStorageExpDate
    def getPStorageCode(self):
        return self.__pStorageCode
    def getPListOfMatCodes(self):
        return self.__pListOfMatCodes
    def getPDescription(self):
        return self.__pDescription


    # setters for properties
    def setPName(self, pName):
        self.__pName = pName
    def setPDateOfProduction(self, pDateOfProduction):
        self.__pDateOfProduction = pDateOfProduction
    def setPNameOfCustomer(self, pNameOfCustomer):
        self.__pNameOfCustomer = pNameOfCustomer
    def setPStorageExpDate(self, pStorageExpDate):
        self.__pStorageExpDate = pStorageExpDate
    def setPStorageCode(self, pStorageCode):
        self.__pStorageCode = pStorageCode
    def setPListOfMatCodes(self, pListOfMatCodes):
        self.__pListOfMatCodes = pListOfMatCodes
    def setPDescription(self, pDescription):
        self.__pDescription = pDescription