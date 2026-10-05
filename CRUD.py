from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

from db import get_conexao


# ============================================================
# CONFIGURAÇÃO
# ============================================================

app = FastAPI(title="API Bots Analistas")

BASE_DIR = Path(__file__).resolve().parent
FRONT_DIR = BASE_DIR / "front"

app.mount(
    "/static",
    StaticFiles(directory=FRONT_DIR),
    name="static"
)


# ============================================================
# FRONTEND
# ============================================================

@app.get("/")
def pagina_inicial():
    return FileResponse(FRONT_DIR / "index.html")


# ============================================================
# MODELO
# ============================================================

class BotRequest(BaseModel):
    nome: str
    ativo: str


# ============================================================
# CREATE
# ============================================================

@app.post("/bots")
def criar_bot(dado: BotRequest):

    conn = get_conexao()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO bots (nome, ativo)
            VALUES (%s, %s)
            """,
            (dado.nome, dado.ativo)
        )

        conn.commit()

        novo_id = cur.lastrowid

        return {
            "mensagem": "Bot criado com sucesso",
            "id": novo_id,
            "nome": dado.nome,
            "ativo": dado.ativo
        }

    except Exception as e:
        conn.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    finally:
        cur.close()
        conn.close()


# ============================================================
# READ - LISTAR TODOS
# ============================================================

@app.get("/bots")
def listar_bots():

    conn = get_conexao()
    cur = conn.cursor(dictionary=True)

    try:
        cur.execute(
            """
            SELECT
                id,
                nome,
                ativo,
                preco,
                humor,
                status_acao,
                criado_em
            FROM bots
            """
        )

        resultado = cur.fetchall()

        return resultado

    finally:
        cur.close()
        conn.close()


# ============================================================
# READ - BUSCAR POR ID
# ============================================================

@app.get("/bots/{bot_id}")
def buscar_bot(bot_id: int):

    conn = get_conexao()
    cur = conn.cursor(dictionary=True)

    try:
        cur.execute(
            """
            SELECT
                id,
                nome,
                ativo,
                preco,
                humor,
                status_acao,
                criado_em
            FROM bots
            WHERE id = %s
            """,
            (bot_id,)
        )

        bot = cur.fetchone()

        if not bot:
            raise HTTPException(
                status_code=404,
                detail="Bot não encontrado"
            )

        return bot

    finally:
        cur.close()
        conn.close()


# ============================================================
# UPDATE
# ============================================================

@app.put("/bots/{bot_id}")
def editar_bot(bot_id: int, dados: BotRequest):

    conn = get_conexao()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            UPDATE bots
            SET nome = %s,
                ativo = %s
            WHERE id = %s
            """,
            (
                dados.nome,
                dados.ativo,
                bot_id
            )
        )

        if cur.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Bot não encontrado"
            )

        conn.commit()

        return {
            "mensagem": "Bot atualizado com sucesso",
            "id": bot_id,
            "nome": dados.nome,
            "ativo": dados.ativo
        }

    except HTTPException:
        conn.rollback()
        raise

    except Exception as e:
        conn.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    finally:
        cur.close()
        conn.close()


# ============================================================
# DELETE
# ============================================================

@app.delete("/bots/{bot_id}")
def deletar_bot(bot_id: int):

    conn = get_conexao()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            DELETE FROM bots
            WHERE id = %s
            """,
            (bot_id,)
        )

        if cur.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Bot não encontrado"
            )

        conn.commit()

        return {
            "mensagem": f"Bot {bot_id} removido com sucesso"
        }

    except HTTPException:
        conn.rollback()
        raise

    except Exception as e:
        conn.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    finally:
        cur.close()
        conn.close()


# ============================================================
# HISTÓRICO DE ANÁLISES
# ============================================================

@app.get("/bots/{bot_id}/historico")
def historico_bot(
    bot_id: int,
    limite: int = 50
):

    conn = get_conexao()
    cur = conn.cursor(dictionary=True)

    try:
        cur.execute(
            """
            SELECT
                id,
                preco,
                humor,
                status_acao,
                data_hora
            FROM historico_analises
            WHERE bot_id = %s
            ORDER BY data_hora DESC
            LIMIT %s
            """,
            (bot_id, limite)
        )

        resultado = cur.fetchall()

        return resultado

    finally:
        cur.close()
        conn.close()