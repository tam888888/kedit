import nest_asyncio

nest_asyncio.apply()

import qdrant_client

collection_name="chat_with_docs"

client = qdrant_client.QdrantClient(
    host="localhost",
    port=6333
)

from llama_index.core import SimpleDirectoryReader

input_dir_path = './docs'

print("ABC")

loader = SimpleDirectoryReader(
            input_dir = input_dir_path,
            required_exts=[".pdf"],
            recursive=True
        )
docs = loader.load_data()


from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext

def create_index(documents):

    vector_store = QdrantVectorStore(client=client,
                                     collection_name=collection_name)
    
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    index = VectorStoreIndex.from_documents(documents,
                                            storage_context=storage_context)
    
    return index