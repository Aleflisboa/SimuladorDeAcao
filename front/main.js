function atualizarSprite(){
    const bot = document.querySelector(".Gian");{
        if (humor === "FELIZ"){
            bot.styleBackgraoudImage = "url("/")"
        }
        else if(humor === "COM_RAIVA"){
            bot.styleBackgraoudImage = "url("/")"
        }   
        else if(humor === "ESPERANDO"){
            bot.styleBackgraoudImage = "url("/")"
        }
     }
}







async function atualizarCotacoes() {
    try {
        const resposta = await fetch("/bots", {
            cache: "no-store"
        });

        if (!resposta.ok) {
            throw new Error("Erro ao acessar a API");
        }

        const bots = await resposta.json();

        const personagens = [
            {
                nome: "MATHEUS",
                elemento: "cotacao-matheus"
            },
            {
                nome: "GIAN",
                elemento: "cotacao-gian"
            },
            {
                nome: "LISINHO",
                elemento: "cotacao-lisinho"
            }
        ];

        personagens.forEach(personagem => {

            const bot = bots.find(
                b => b.nome.toUpperCase() === personagem.nome
            );

            const elemento = document.getElementById(
                personagem.elemento
            );

            if (!bot || !elemento) return;

            const preco = Number(bot.preco);

            const cotacao = Number.isFinite(preco)
                ? preco.toLocaleString("pt-BR", {
                    style: "currency",
                    currency: "BRL"
                })
                : "Indisponível";

            elemento.textContent =
                `${bot.ativo} | ${cotacao}`;
        });

    } catch (erro) {
        console.error("Erro ao atualizar cotações:", erro);
    }
}

atualizarCotacoes();

setInterval(atualizarCotacoes, 30000);