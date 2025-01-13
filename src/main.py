from fastapi import FastAPI

app = FastAPI()

# Simulação de banco de dados baseado em um arquivo
video_texts = {}

# Carregar textos do arquivo texto.txt
def load_video_texts():
    global video_texts
    try:
        with open("texto.txt", "r", encoding="utf-8") as file:
            for line in file:
                # Espera-se o formato: id_video: texto
                if ":" in line:
                    id_video, text = line.split(":", 1)
                    video_texts[int(id_video.strip())] = text.strip()
    except FileNotFoundError:
        print("Arquivo texto.txt não encontrado.")

# Carrega os textos ao iniciar o aplicativo
load_video_texts()

@app.get("/get-text/{id_video}")
async def get_text(id_video: int):
    text = video_texts.get(id_video, "Texto não encontrado.")
    return {"text": text}