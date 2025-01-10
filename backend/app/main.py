from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Permitir que o frontend se comunique com o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_crendentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/vlibras-widget")
async def generate_vlibras_widget(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Texto não pode estar vazio.")
    widget_code = f"""
    <div id="vlibras-widget">
        <p>{text}</p>
        <script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script>
    </div>
    """
    return {"widget": widget_code}
