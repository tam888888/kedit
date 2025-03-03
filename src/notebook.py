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