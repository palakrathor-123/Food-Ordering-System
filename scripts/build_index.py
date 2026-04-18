import json
import numpy as np
import faiss
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.embedding_service import get_embedding

with open("data/menu.json", "r") as f:
    menu = json.load(f)

print("Generating embeddings (FREE AI)...")

vectors = []

for item in menu:
    emb = get_embedding(item["name"])
    vectors.append(emb[0])

vectors = np.array(vectors).astype("float32")
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectors)

faiss.write_index(index, "menu.index")

print("FAISS index created using FREE AI ✅")