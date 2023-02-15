import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://TuanNguyen:Tuan150901@ac-nazxr98-shard-00-00.cas1oue.mongodb.net:27017,ac-nazxr98-shard-00-01.cas1oue.mongodb.net:27017,ac-nazxr98-shard-00-02.cas1oue.mongodb.net:27017/?ssl=true&replicaSet=atlas-9xwzc3-shard-0&authSource=admin&retryWrites=true&w=majority")

# Select the database you want to work with
db = client["SDN_data"]

# Create a collection
collection = db.create_collection("Reward_data")

# # Select the collection you want to work with
# collection = db["MAB_data"]

# # Run a query to find all documents in the collection
# docs = list(collection.find())


# # Print the result
# for doc in docs:
#     print(doc)
