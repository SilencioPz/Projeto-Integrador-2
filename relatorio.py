from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black
from reportlab.platypus import Image
from modelos import Livro
from app import app
import os

def generate_pdf(livros):
    caminho_completo = "relatorio_livros.pdf"  # Generate a filename for the report
    c = canvas.Canvas(caminho_completo, pagesize=letter)

    # Add the title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1*inch, 10.5*inch, "Relatório Quie Isso Livros")
    
    # Add the fields for each book
    y = 9.5*inch
    for livro in livros:
        c.setFont("Helvetica", 12)
        c.drawString(1*inch, y, "Título: " + livro.titulo)
        c.drawString(1*inch, y-0.2*inch, "Autor: " + livro.autor)
        c.drawString(1*inch, y-0.4*inch, "Ano de Publicação: " + str(livro.ano_publicacao))
        y -= 0.8*inch

    c.showPage()
    c.save()
    return caminho_completo