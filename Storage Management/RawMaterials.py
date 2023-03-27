from abc import ABC, abstractmethod

class RawMaterials(ABC):
    def __init__(self, name, dateOfPurchase, nameOfSupplier, storageExpDate, storageCode, description):
        self.__name = name
        self.__dateOfPurchase = dateOfPurchase
        self.__nameOfSupplier = nameOfSupplier
        self.__storageExpDate = storageExpDate
        self.__storageCode = storageCode
        self.__description = description
    
    # getters for abstract
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def getDateOfPurchase(self):
        pass
    @abstractmethod
    def getNameOfSupplier(self):
        pass
    @abstractmethod
    def getStorageExpDate(self):
        pass
    @abstractmethod
    def getStorageCode(self):
        pass
    @abstractmethod
    def getDescription(self):
        pass

    # setters for abstract
    @abstractmethod
    def setName(self, name):
        pass
    @abstractmethod
    def setDateOfPurchase(self, dateOfPurchase):
        pass
    @abstractmethod
    def setNameOfSupplier(self, nameOfSupplier):
        pass
    @abstractmethod
    def setStorageExpDate(self, storageExpDate):
        pass
    @abstractmethod
    def setStorageCode(self, storageCode):
        pass
    @abstractmethod
    def setDescription(self, description):
        pass

    # getters for properties
    def getName(self):
        return self.__name
    def getDateOfPurchase(self):
        return self.__dateOfPurchase
    def getNameOfSupplier(self):
        return self.__nameOfSupplier
    def getStorageExpDate(self):
        return self.__storageExpDate
    def getStorageCode(self):
        return self.__storageCode
    def getDescription(self):
        return self.__description

    # setters for properties
    def setName(self, name):
        self.__name = name
    def setDateOfPurchase(self, dateOfPurchase):
        self.__dateOfPurchase = dateOfPurchase
    def setNameOfSupplier(self, nameOfSupplier):
        self.__nameOfSupplier = nameOfSupplier
    def setStorageExpDate(self, storageExpDate):
        self.__storageExpDate = storageExpDate
    def setStorageCode(self, storageCode):
        self.__storageCode = storageCode
    def setDescription(self, description):
        self.__description = description