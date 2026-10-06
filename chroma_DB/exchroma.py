import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="my_test_collection")


documnet = [
    ["id1", "id2"],
    ["This is a document about pineapple","This is a document about oranges"]
]

for index,id in enumerate(documnet[0]):
    collection.upsert(
        documents=[documnet[1][index]],
        ids=[id]
    )
    
print("Collection:", collection)

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print("-"*50)
print(results)
print("-"*50)