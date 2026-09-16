# Triagem Automática de Currículos

Este projeto foi desenvolvido para o **Checkpoint 1** da disciplina **IA & ML** do curso de **Engenharia de Software (FIAP)**.

O sistema simula o funcionamento de uma agência de empregos focada no ecossistema de tecnologia. Ele automatiza o processo de triagem de currículos em formato PDF combinando **validações determinísticas (filtros rígidos)** com **análise de IA generativa**, além de realizar o monitoramento rigoroso e estimativa de custos do consumo de recursos computacionais através da contagem de tokens.

---

## Desenvolvedores

- **Luis Filipe Crivellaro** – RM: 560877
- **Felipe Silva do Prado Lima** – RM: 559848
- **Rafael Mandel** – RM: 560333

**Turma**: 3ESPA  
**Professor**: Wellington Cidade Silva  
**Instituição**: FIAP - Engenharia de Software  

---

## Estrutura de Pastas

```text
meu-projeto-rh-tech/
│
├── pdfs/                   
│   └── curriculo_dev.pdf     
│
├── gerar_pdf.py             
├── reader.py                
├── filters.py            
├── token_tracker.py       
├── cliente.py                
├── main.py                  
├── requirements.txt        
├── integrantes.txt           
└── README.md                
```

---

## Como Executar

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.10+** instalado em sua máquina.

### 2. Clonar o Repositório
```bash
git clone <https://github.com/rflMandell/cp01-AI-ML>
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Gerar o Currículo de Teste
Execute o script para criar o arquivo `curriculo_dev.pdf` na pasta do projeto:
```bash
python gerar_pdf.py
```

### 5. Executar o Pipeline Principal
Rode o orquestrador do sistema para ver a triagem em ação:
```bash
python main.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **pypdf**: Extração de texto bruto de PDFs.
- **tiktoken**: Tokenização exata para modelos de IA da OpenAI.
- **ReportLab**: Geração pragmática de relatórios em formato PDF para simulação de currículos.
