import tiktoken

def calcular_tokens(texto, modelo="gpt-4o-mini"):
    """
    Calcula o num exato de tokens consumidos por um texto.
    """
    try:
        codificador = tiktoken.encoding_for_model(modelo)
        tokens_lista = codificador.encode(texto)
        return len(tokens_lista)
    except Exception as e:
        print(f"Aviso: Erro ao calcular tokens via tiktoken ({e}). Usando aproximação.")
        return len(texto) // 4

def estimar_custo(tokens_entrada, tokens_saida, modelo="gpt-4o-mini"):
    """
    Estima o custo financeiro aproximado com base nas taxas do modelo.
    precos tirados de uma simples pesquisa no google, se ta certo ou n e muito dificil dizer, mas deve ta pensando no 4o mini
    """
    preco_entrada_por_1m = 0.15   # US$ 0.15 por 1M tokens de entrada
    preco_saida_por_1m = 0.60     # US$ 0.60 por 1M tokens de saída
    
    custo_entrada = (tokens_entrada / 1_000_000) * preco_entrada_por_1m
    custo_saida = (tokens_saida / 1_000_000) * preco_saida_por_1m
    
    return custo_entrada + custo_saida