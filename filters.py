import re

def aplicar_filtros_deterministicos(texto_curriculo, exp_minima_anos, orcamento_maximo_vaga):

    texto_lower = texto_curriculo.lower()
    aprovado = True
    motivos_reprovacao = []
    
    # validar anos de exp
    padrao_exp = r'(\d+)\s*(?:anos?|yrs?)\s*(?:de\s*)?(?:experi[êe]ncia|exp)'
    match_exp = re.search(padrao_exp, texto_lower)
    
    exp_encontrada = 0
    if match_exp:
        exp_encontrada = int(match_exp.group(1))
    else:
        # uma buscazinha padrao pra se o outro validador n funcionar
        match_num = re.search(r'(\d+)\s*anos?', texto_lower)
        if match_num:
            exp_encontrada = int(match_num.group(1))

    if exp_encontrada < exp_minima_anos:
        aprovado = False
        motivos_reprovacao.append(
            f"Experiência insuficiente: Candidato possui {exp_encontrada} ano(s), o mínimo exigido é de {exp_minima_anos} ano(s)."
        )

    # v a faixa salarial se ta de acordo ou n
    padrao_salario = r'(?:r\$|\$)?\s*(\d{1,3}(?:\.\d{3})*|\d+)'
    correspondencias = re.findall(padrao_salario, texto_lower)
    
    valores_encontrados = []
    for val in correspondencias:
        val_limpo = val.replace('.', '')
        if val_limpo.isdigit():
            val_int = int(val_limpo)
            if val_int >= 2000:
                valores_encontrados.append(val_int)
                
    if valores_encontrados:
        pretensao_candidato = max(valores_encontrados)
        if pretensao_candidato > orcamento_maximo_vaga:
            aprovado = False
            motivos_reprovacao.append(
                f"Pretensão salarial acima do orçamento: Candidato pede R$ {pretensao_candidato}, teto da vaga é R$ {orcamento_maximo_vaga}."
            )

    return aprovado, motivos_reprovacao