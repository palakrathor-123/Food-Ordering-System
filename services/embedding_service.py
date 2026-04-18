from sentence_transformers import SentenceTransformer
import numpy as np

# load model (first time thoda time lagega)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    embedding = model.encode(text)
    return np.array(embedding).astype("float32").reshape(1, -1)