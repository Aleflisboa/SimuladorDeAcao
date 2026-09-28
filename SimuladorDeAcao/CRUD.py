from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import get_conexao

app = FastAPI(title="API Bots Analistas")


class BotRequest(BaseModel):
    nome: str
    acao: str


# ---------- CREATE ----------
@app.post("/bots")
def criar_bot(dado: BotRequest):
    conn = get_conexao()
    cur = conn.cursor()
    try:
        cur.execute(
    "INSERT INTO bots (nome, acao) VALUES (%s, %s)",
    (dado.nome, dado.acao)
)
        novo_id = cur.lastrowid
        return {
    "mensagem": "Bot criado com sucesso",
    "id": novo_id,
    "nome": dado.nome,
    "acao": dado.acao
}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()


# ---------- READ (lista) ----------
@app.get("/bots")
def listar_bots():
    conn = get_conexao()
    cur = conn.cursor(dictionary=True)
    cur.execute(
     "SELECT id, nome, acao, preco, humor, status_acao, criado_em FROM bots"
)
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado


# ---------- READ (por id) ----------
@app.get("/bots/{bot_id}")
@app.get("/bots/{bot_id}")
def buscar_bot(bot_id: int):
    conn = get_conexao()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT id, nome, acao, preco, humor, status_acao, criado_em
        FROM bots
        WHERE id = %s
    """, (bot_id,))

    bot = cur.fetchone()

    cur.close()
    conn.close()

    if not bot:
        raise HTTPException(
            status_code=404,
            detail="Bot não encontrado"
        )

    return bot


# ---------- UPDATE ----------
@app.put("/bots/{bot_id}")
def editar_bot(bot_id: int, dados: BotRequest):
    conn = get_conexao()
    cur = conn.cursor()
    cur.execute(
    "UPDATE bots SET nome = %s, acao = %s WHERE id = %s",
    (dados.nome, dados.acao, bot_id)
)
    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Bot não encontrado")
    cur.close()
    conn.close()
    return {"mensagem": "Bot atualizado com sucesso",
            "id": bot_id, "nome": dados.nome}


# ---------- DELETE ----------
@app.delete("/bots/{bot_id}")
def deletar_bot(bot_id: int):
    conn = get_conexao()
    cur = conn.cursor()
    cur.execute("DELETE FROM bots WHERE id = %s", (bot_id,))
    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Bot não encontrado")
    cur.close()
    conn.close()
    return {"mensagem": f"Bot {bot_id} removido com sucesso"}


# ---------- Histórico de análises (bônus) ----------
@app.get("/bots/{bot_id}/historico")
def historico_bot(bot_id: int, limite: int = 50):
    conn = get_conexao()
    cur = conn.cursor(dictionary=True)
    cur.execute("""SELECT id, preco, humor, status_acao, data_hora
                   FROM historico_analises
                   WHERE bot_id = %s
                   ORDER BY data_hora DESC
                   LIMIT %s""", (bot_id, limite))
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado