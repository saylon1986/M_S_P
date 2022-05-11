import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path
import textract
from pathlib import Path
import fitz
import re
import os
import pandas as pd
import chardet
import shutil
import time



# função principal

def Main():
   

   # cria as pastas para que o programa seja autônomo ao ser rodado

	try:
		os.mkdir("./imagens")
	except:
		pass
	try:
		os.mkdir("./convertidos_PNG")
	except:
		pass
	try:
		os.mkdir("./iniciais")      
	except:
		pass   

	z = input("Coloque as imagens na pasta 'imagens':")		
# # converte as imagens
	Conversor_OCR()


# Função que converte os casos da pasta imagens em PNG, para depois transformar em TXT com o Tesseract



def Conversor_OCR():

   print()
   print("-------------------------------")
   print("iniciando conversão das imagens")
   print("-------------------------------")
   print()


   # caminho do tesseract no computador
   pytesseract.tesseract_cmd ='C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

   # site pra baixar o tesseract
   # https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download


   # Path onde estão as imagens a serem convertidas
   path = r'./imagens'
   files = os.listdir(path)


   # path para onde vão as imagens convertidas de PDF para PNG
   trl = r'./convertidos_PNG'


   # convert as imagens de pdf imagem para um PNG
   for f in range(len(files)):
     if files[f].endswith('.pdf'):
          print("estamos no",f) # controle de cada documento
          # print(files[f])
          print()
          print("------------------")


          # cria uma pasta com o nome do arquivo para depositar as imagens de cada página

          nome_pasta = str(files[f][:-4])
          # print(nome_pasta)
          
          try:
            os.mkdir(trl+"/"+nome_pasta)
          except:
            pass
          
          # lê o arquivo e salva todas as imagens em uma lista

          n = os.path.join(path,files[f])
          img = convert_from_path(n, dpi=200)
          # img[-1].save(trl+str(f)+'.png', 'PNG') # salvava só a última página
          
          # print(len(img))
          
          # coverte e salva todas as páginas na pasta
          for j in range(len(img)):
               img[j].save(trl+"/"+nome_pasta+"/"+str(files[f])+"_"+str(j)+'.png', 'PNG')



   # path com as imagens convertidas em PNG
   path = r'./convertidos_PNG'
   files = os.listdir(path)


   # print(files)

   # Path para onde vão os TXT
   path_2 = r'./iniciais'


   # Lê cada um das imagens geradas pelas páginas do PDF, transforma em texto e junta em um artigo TXT
   for item in files:
        arqs = os.path.join(path,item)
        print("estamos no",arqs)
        print()
        pages = os.listdir(arqs)
        textos = []
        for m in range(len(pages)):
             im = os.path.join(arqs,pages[m])
             text = pytesseract.image_to_string(im, lang = 'por') # aciona o tesseract e coloca a linguagem em português
             textos.append(text)
             print("convertida a página", m)

        # salva os textos unificados em um único TXT
             
        texto_final = " ".join(textos)     
        x = open(path_2+'/{}.txt'.format(str(item)), "w+", encoding='utf-8')
        x.write(texto_final)
        x.close()
        print()
        print("                **************            ")


Main()