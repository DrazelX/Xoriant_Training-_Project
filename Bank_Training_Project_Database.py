import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client['Bank_Project']
collection = db['Sample']
BankList = [
    {'user_id': '1', 'Name': 'ABC', 'Address': 'aaa aaa aaa', 'Phone': '11111-11111', 'City': 'Pune', 'state': 'Maharashtra'},
    {'user_id': '2', 'Name': 'DEF', 'Address': 'bbb bbb bbb', 'Phone': '22222-22222', 'City': 'Bangalore', 'state': 'Karnataka'},
    {'user_id': '3', 'Name': 'GHI', 'Address': 'ccc ccc ccc', 'Phone': '33333-33333', 'City': 'Mumbai', 'state': 'Maharashtra'},
    {'user_id': '4', 'Name': 'JKL', 'Address': 'ddd ddd ddd', 'Phone': '44444-44444', 'City': 'Pune', 'state': 'Maharashtra'},
    {'user_id': '5', 'Name': 'MNO', 'Address': 'eee eee eee', 'Phone': '55555-55555', 'City': 'Pune', 'state': 'Maharashtra'},
    {'user_id': '6', 'Name': 'PQR', 'Address': 'fff fff fff', 'Phone': '66666-66666', 'City': 'Bangalore', 'state': 'Karnataka'},
    {'user_id': '7', 'Name': 'STU', 'Address': 'ggg ggg ggg', 'Phone': '77777-77777', 'City': 'Mumbai', 'state': 'Maharashtra'},
    {'user_id': '8', 'Name': 'VWX', 'Address': 'hhh hhh hhh', 'Phone': '88888-88888', 'City': 'Pune', 'state': 'Maharashtra'}
]
collection.insert_many(BankList)

all_document = collection.find()
for each_record in all_document:
    print("doc",each_record)

