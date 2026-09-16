from reader import extrair_texto_pdf
from filters import aplicar_filtros_deterministicos
from cliente import analisar_perfil_com_ia

def executar_pipeline_triagem_rh():
    print("=== SISTEMA DE TRIAGEM AUTOMATIZADA DE CURRÍCULOS (RH TECH) ===")
    
    # reqs
    exp_minima_exigida = 1       
    orcamento_maximo_vaga = 3000 
    
    detalhes_vaga = (
        "Vaga: Desenvolvedor Backend Senior (Python)\n"
        "Requisitos: Mínimo de 1 ano de experiência com Python, APIs REST, Docker e AWS.\n"
        "Teto Salarial: R$ 3.000,00"
    )
    
    caminho_pdf = "curriculo_dev.pdf"
    
    # LEITURA DO PDF
    print(f"\n[Passo 1] Carregando e extraindo PDF: {caminho_pdf}...")
    texto_curriculo = extrair_texto_pdf(caminho_pdf)
    
    if not texto_curriculo.strip():
        print("-> PDF não encontrado ou sem texto. Usando currículo simulado...")
        texto_curriculo = (
            "Nome: Lucas Silva. Experiência: 1 ano de experiência com Python e AWS. "
            "Prepensão salarial: R$ 3000. Habilidades: Python, FastApi, Docker."
        )
    else:
        print("-> Texto extraído com sucesso!")

    # FILTROS
    print("\n[Passo 2] Aplicando Regras Determinísticas (Anos de Exp e Salário)...")
    aprovado_regras, motivos = aplicar_filtros_deterministicos(
        texto_curriculo, 
        exp_minima_exigida, 
        orcamento_maximo_vaga
    )
    
    if not aprovado_regras:
        print("-> Status: REPROVADO na camada determinística.")
        for m in motivos:
            print(f"   - {m}")
        print("-> Processo encerrado. Nenhum recurso de IA foi consumido.")
        return

    print("-> Status: APROVADO na triagem determinística! Encaminhando para IA...")

    # GENERATIVA E MONITORAÇÃO DE TOKENS
    print("\n[Passo 3 & 4] Executando Análise Generativa e Contabilização de Tokens...")
    try:
        parecer, relatorio_tokens = analisar_perfil_com_ia(texto_curriculo, detalhes_vaga)
        
        print("\n" + "="*50)
        print(parecer)
        print("="*50)
        
        print("\n" + "="*50)
        print("     RELATÓRIO DE USO DE TOKENS E CUSTO COMPUTACIONAL   ")
        print("="*50)
        print(f"• Modelo Utilizado          : {relatorio_tokens['modelo']}")
        print(f"• Tokens de Entrada (Prompt): {relatorio_tokens['tokens_entrada']}")
        print(f"• Tokens de Saída (Output)  : {relatorio_tokens['tokens_saida']}")
        print(f"• Total de Tokens Consumidos: {relatorio_tokens['tokens_totais']}")
        print(f"• Estimativa de Custo (USD) : ${relatorio_tokens['custo_estimado_usd']:.6f}")
        print("="*50)

    except Exception as e:
        print(f"[Erro Crítico] Falha na camada generativa: {e}")

if __name__ == "__main__":
    executar_pipeline_triagem_rh()