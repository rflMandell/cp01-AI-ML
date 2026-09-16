from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def criar_curriculo_pdf():
    nome_arquivo = "curriculo_dev.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    largura, altura = letter
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, "CURRICULO PROFISSIONAL - DEV")
    
    c.setFont("Helvetica", 11)
    c.drawString(50, altura - 80, "------------------------------------------------------------------------------------------------")
    c.drawString(50, altura - 110, "Nome: Reginaldo Matheus")
    c.drawString(50, altura - 130, "Cargo Desejado: Desenvolvedor Backend Junior")
    c.drawString(50, altura - 150, "Tempo de Experiencia: 1 anos em desenvolvimento Python/Django e FastApi")
    c.drawString(50, altura - 170, "Pretensao Salarial: R$ 3.000")
    c.drawString(50, altura - 190, "Habilidades: Python, PostgreSQL, Docker, AWS, Git, Arquitetura de Microservicos")
    c.drawString(50, altura - 210, "Resumo: Desenvolvedor proativo, com experiencia tecnica de equipes agil e foco em performance.")
    c.drawString(50, altura - 230, "------------------------------------------------------------------------------------------------")
    
    c.save()
    print(f"o arquivo '{nome_arquivo}' foi criado para testes.")
    
if __name__ == "__main__":
    criar_curriculo_pdf()