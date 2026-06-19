from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import torch
import sentencepiece as spm
from model import RapformerLangModel

app = FastAPI(title="Rapformer API")

app.mount("/static", StaticFiles(directory="static"), name="static")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print("Loading tokenizer...")
sp = spm.SentencePieceProcessor(model_file='tokrap.model')

print("Loading Rapformer weights...")
model = RapformerLangModel()
model.load_state_dict(torch.load('rapformer_v0.pth', map_location=device))
model.to(device)
model.eval()

class GenerateRequest(BaseModel):
    start_phrase: str
    temperature: float = 0.8
    top_k: int = 50

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/generate")
def generate_lyrics(req: GenerateRequest):
    start_text = req.start_phrase if req.start_phrase else "Yeah"
    context_tokens = sp.encode(start_text, out_type=int)
    context = torch.tensor([context_tokens], dtype=torch.long, device=device)
    with torch.no_grad():
        generated_tokens = model.generate(
            idx=context, 
            max_new_tokens=300, 
            temperature=req.temperature, 
            top_k=req.top_k
        )[0].tolist()
    decoded_text = sp.decode(generated_tokens)
    return {"lyrics": decoded_text}