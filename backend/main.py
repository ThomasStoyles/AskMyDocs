from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import faiss
import pypdf
import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#CORS Config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Globals Vars
chunks = []
embeddings = None

def get_text_from_pdf(file: UploadFile) -> str:
    reader = pypdf.PdfReader(file.file)
    return " ".join([page.extract_text() for page in reader.pages])

def chunk_text(text: str, max_tokens: int = 300) -> List[str]:
    words = text.split()
    return [" ".join(words[i:i+max_tokens]) for i in range(0, len(words), max_tokens)]

# Get OpenAI Embeddings
def embed(texts: List[str]):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    return [d.embedding for d in response.data]

#Endpoints
@app.post("/upload/")
async def upload_pdf(file: UploadFile):
    global chunks, embeddings
    text = get_text_from_pdf(file)
    chunks = chunk_text(text)
    vectors = embed(chunks)
    embeddings = faiss.IndexFlatL2(len(vectors[0]))
    embeddings.add(np.array(vectors).astype('float32'))
    return {"status": "uploaded", "chunks": len(chunks)}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    global chunks, embeddings
    question_vector = embed([question])[0]
    D, I = embeddings.search(np.array([question_vector]).astype('float32'), k=3)
    retrieved = "\n\n".join([chunks[i] for i in I[0]])

    prompt = f"Answer the question based on the following:\n\n{retrieved}\n\nQuestion: {question}"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {"answer": completion.choices[0].message.content}
