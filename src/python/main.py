
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle  
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib import colors  

def gerar_pdf(filename="relatorio.pdf"): 
    # Configurações do documento PDF
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)  
    styles =getSampleStyleSheet();
    story = [] 
    # Conteúdo do relatório
    story.append(Paragraph("<b>Relatório de Entrega:</b> Módulo de Exportação PDF", styles['Heading1']))  
    story.append(Paragraph("<b>Desenvolvedor:</b> Wellington Cidade", styles['Normal'])) 
    story.append(Spacer(1, 15))  

    dados = [  # Cria uma matriz (lista de listas) contendo as linhas e colunas que preencherão a tabela de dados.
        ["Métrica", "Valor"], 
        ["Horas de Desenvolvimento", "16.0h"], 
        ["Horas Perdidas (Bugs)", "3.5h"],
        ["Valor Líquido Gerado", "R$ 5.950,00"]  
    ]

    tabela = Table(dados, colWidths=[250, 250])  # Cria o objeto Table do ReportLab passando os dados estruturados e definindo a largura de 250 pontos para cada uma das duas colunas.
    tabela.setStyle(TableStyle([  
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),  
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])  
    ]))

    story.append(tabela)  # Insere a tabela estilizada na lista de elementos do documento.
    doc.build(story) 
    print(f"PDF gerado com sucesso: {filename}")  

if __name__ == "__main__": 
    gerar_pdf() 
