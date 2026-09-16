from token_tracker import calcular_tokens, estimar_custo

def analisar_perfil_com_ia(texto_curriculo, detalhes_vaga):
    """
    Gera o parecer qualitativo e o resumo executivo, monitorando o consumo de tokens.
    """
    modelo_utilizado = "gpt-4o-mini"
    
    prompt_sistema = (
        "Você é um Recrutador Tech Sênior e Especialista em Aquisição de Talentos. "
        "Sua função é analisar currículos, identificar soft skills implícitas, avaliar a senioridade "
        "e elaborar resumos executivos objetivos para gerentes de contratação."
    )
    
    prompt_usuario = f"""
    Com base no currículo e nos requisitos da vaga fornecidos, gere:
    1. Um parecer qualitativo detalhando a senioridade e as soft skills implícitas.
    2. Um resumo executivo customizado para o recrutador da empresa contratante.

    --- REQUISITOS DA VAGA ---
    {detalhes_vaga}
    
    --- CURRÍCULO DO CANDIDATO ---
    {texto_curriculo}
    """
    
    # entrada de tokens
    texto_total_entrada = prompt_sistema + prompt_usuario
    tokens_entrada = calcular_tokens(texto_total_entrada, modelo_utilizado)
    
    # simulacao de api da IA funcionando pq eu ainda n to rico o bastante pra usar IA em um projeto academico
    texto_resposta = (
        "--- ANÁLISE QUALITATIVA & PARECER DE IA ---\n\n"
        "1. PARECER DE SENIORIDADE E SOFT SKILLS:\n"
        "• Senioridade: Confirmada Senioridade/Pleno Alto. Demonstra sólida vivência em ecossistemas Python/Django e arquitetura em nuvem.\n"
        "• Soft Skills Implícitas: Liderança técnica de equipes ágeis, orientação a resultados, capacidade de comunicação e proatividade focalizada em performance.\n\n"
        "2. RESUMO EXECUTIVO PARA O RECRUTADOR:\n"
        "Candidato Lucas Silva apresenta perfil altamente compatível com a posição de Backend Sênior. Possui 5 anos de experiência prática comprovada, pretensão salarial alinhada ao orçamento e domínio nas tecnologias centrais exigidas (Python, FastApi, Docker e AWS). Recomendo o avanço para a etapa de entrevista técnica."
    )
    
    # saida
    tokens_saida = calcular_tokens(texto_resposta, modelo_utilizado)
    tokens_totais = tokens_entrada + tokens_saida
    custo_estimado = estimar_custo(tokens_entrada, tokens_saida, modelo_utilizado)
    
    relatorio_tokens = {
        "modelo": modelo_utilizado,
        "tokens_entrada": tokens_entrada,
        "tokens_saida": tokens_saida,
        "tokens_totais": tokens_totais,
        "custo_estimado_usd": custo_estimado
    }

    return texto_resposta, relatorio_tokens