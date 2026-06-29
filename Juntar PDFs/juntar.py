import PyPDF2 # Biblioteca para manipulação de PDFs
import os

mesclar = PyPDF2.PdfMerger() #Essa função é da biblioteca e usamos para mesclar os arquivos

lista_arquivos = os.listdir("PDFs") # Função para listar arquivos
lista_arquivos.sort() # Aqui você organiza a lista

for arquivo in lista_arquivos: # Para cada arquivo na lista
    if arquivo.endswith(".pdf"): # Se ele for PDF (se for outro, não junta)
        mesclar.append(f"PDFs/{arquivo}") # Aqui você vai mesclar e adicionar no caminho do arquivo

nome_pdf_final = input("Digite o nome final do PDF: ")

if not nome_pdf_final.endswith(".pdf"):
    nome_pdf_final += ".pdf"

with open(nome_pdf_final, "wb") as arquivo_saida:
    mesclar.write(arquivo_saida) # Aqui a gente grava de fato o arquivo no PC, porque estava em binário e não salvava

mesclar.close() # Fecha o mesclador para liberar memória RAM

print(f"PDF salvo como: {nome_pdf_final}")
print("Diretório Final:", os.listdir())