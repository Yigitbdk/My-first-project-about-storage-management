#  library importation for sql db usage
import sqlite3
from sqlite3 import Cursor
import Products
from RawMaterials import RawMaterials

# sql connection function
db = sqlite3.connect("DataBase.db")

# instance creation for usage of executer
dbCursor = db.cursor()

# sql to create table

# commend = "CREATE TABLE raw_materials(id,name,dateOfPurchase ,nameOfSupplier ,storageExpDate ,storageCode,description)"
# commend = "CREATE TABLE products(id,pName,pDateOfProduction ,pNameOfCustomer ,pStorageExpDate ,pStorageCode,pListOfMatCodes,pDescription)"

# executer function
# dbCursor.execute(commend)

def fetchMaterials():
    command = """SELECT * FROM raw_materials"""
    materialResponse  = dbCursor.execute(command)
    materialList = []
    for material in materialResponse:
        materialList.append(material)
    return materialList

def postProduct(product):
    dbCursor.execute("insert into products values (null,?,?,?,?,?,?,?)", (product))
    db.commit()

def getProducts():
    command = """SELECT * FROM products"""
    productResponse = dbCursor.execute(command)
    productList = []
    for product in productResponse:
        productList.append(product)
    return productList

def getMaterials():
    command = """SELECT * FROM raw_materials"""
    materialResponse = dbCursor.execute(command)
    materialList = []
    for material in materialResponse:
        materialList.append(material)
    return materialList

def getProductById(id):
    command = """SELECT * FROM products WHERE id =?"""
    productResponse = dbCursor.execute(command, (id,))
    return productResponse

def getMaterialById(id):
    command = """SELECT * FROM raw_materials WHERE id =?"""
    materialResponse = dbCursor.execute(command, (id,))
    return materialResponse