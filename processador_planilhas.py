import os,re
import pandas as pd
from pathlib import Path
import glob
import fitz
import numpy as np


#################################                  unificador planilhas               ################################


def main():

	lista_planilhas_a_ler = glob.glob("./planilhas filtradas/*.xlsx")

	dados_planilhas_lidas = []

	todos_dados = pd.DataFrame()

	for planilha in lista_planilhas_a_ler:
	#	print("Nome da planilha a ler: ", planilha)
		dados_planilhas_lidas.append(pd.read_excel(planilha, dtype="object", engine ='openpyxl'))
	#	print("Lida!")

	todos_dados = todos_dados.append(dados_planilhas_lidas, ignore_index=True, sort=False)
	todos_dados["Tribunal"] = np.where(todos_dados['Tribunal'].isnull() == True, "TJ"+todos_dados["Estado"].str[:],todos_dados['Tribunal'])

	todos_dados["Checagem"] = "LAI"

	todos_dados.to_excel("Dados_compilados.xlsx", index=False)
	print(todos_dados)

# main()
# z= input("")



#################################                  1- AC               ##################################################


''' dúvidas: Origem dos dados do AC? Quais são do SEEU? sabemos?? '''



def dados_AC():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJAC_1.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJAC_2.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJAC_3.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])


	dados = pd.concat([planilha_1, planilha_2, planilha_3])


	corte = dados["Foro / Vara"].astype(str).str.split("/", n=1, expand = True)

	dados.drop(columns =["Foro / Vara"], inplace = True)

	dados["Comarca"] = corte[0]
	dados["Vara"] = corte[1]


	dados["Data Distribuição"] = dados["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados["Data da Movimentação"] = dados["Data da Movimentação"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	ano = dados["Data Distribuição"].astype(str).str.split("-", n=2, expand = True)[2]


	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "AC"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados.rename(columns={'Processo': 'Número do Processo', 
		'Data da Movimentação': 'Data da Sentença', 
		'Data Distribuição':'Data da Distribuição'},
	 inplace = True)

	dados["Competência"] = "Estadual"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AC.xlsx", index = False)

dados_AC()

#################################                  2- AM               ##################################################


def dados_AM():

	planilha = pd.read_excel(".\Planilhas tribunais\TJAM_1.xlsx", engine ='openpyxl')

	dados = planilha[["Foro","Vara","Processo","Data da Mov. Decisão", "Data de Recebimento"]]


	dados["Data de Recebimento"] = dados["Data de Recebimento"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	rgx = "-|/"
	cortados = dados["Data de Recebimento"].astype(str).str.split(rgx, n=2, expand = True)
	dados["Data da Mov. Decisão"] = dados["Data da Mov. Decisão"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	ano = dados["Data de Recebimento"].astype(str).str.split("-", n=1, expand = True)[0]

	# print(cortados)

	# até 806 SAJ projudi
	ano_p1 = cortados[0][0:806]

	# depois = SEEU
	ano_p2 = cortados[2][807:]

	anos = pd.concat([ano_p1,ano_p2])
	# print(anos)

	dados["Ano"] = anos.astype(int)
	dados["Estado"] = "AM"

	origem =[]
	for k in range(len(dados["Ano"])):
		if k < 806:
			origem.append("SAJ/PROJUDI")
		else:
			origem.append("SEEU")

	dados['Origem'] = origem
 

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados.rename(columns={'Processo': 'Número do Processo', 'Data da Mov. Decisão': 'Data da Sentença',
		'Data de Recebimento': 'Data da Distribuição', 'Foro':'Comarca'}, 
		inplace = True)


	dados["Comarca"] = dados["Comarca"].astype(str).str.split("-", n=1, expand = True)[1]
	cortados = dados["Vara"].astype(str).str.split("-", n=2, expand = True)
	cortados.columns = ["A","B","C"]
	cortados = cortados.reset_index()

	varas = []
	for k in range(len(cortados)):
		vara = cortados.loc[k,"B"]
		if vara == None:
			vara = cortados.loc[k,"A"]
			varas.append(vara)
		else:
			varas.append(vara)


	dados["Vara"] = varas

	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')



	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem","Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]

	# print(dados)


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AM.xlsx", index = False)


dados_AM()




#################################                  3- AP              ##################################################


def dados_AP():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJAP_1.xlsx", engine ='openpyxl')

	planilha_1 ["Origem"] = "Tucujuris"

	ano = planilha_1["Dt. Distrib."].astype(str).str.split("-", n=2, expand = True)[0]
	# print(ano)
	planilha_1["Ano"] = ano.astype(int)
		


	planilha_1["Dt. Distrib."] = planilha_1["Dt. Distrib."].astype(str).str.split(" ", n=1, expand = True)[0]
	planilha_1["Dt. Decisão"] = planilha_1["Dt. Decisão"].astype(str).str.split(" ", n=1, expand = True)[0]

	planilha_1.rename(columns={'FORO': 'Comarca',
		'VARA':'Vara', 'Número Único': 'Número do Processo', 
		'Dt. Decisão': 'Data da Sentença', 
		'Dt. Distrib.':'Data da Distribuição'},
	 inplace = True)



			#############        Parte 2               ##############



	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJAP_2.xlsx", engine ='openpyxl')

	planilha_2 ["Origem"] = "SEEU"

	corte = planilha_2["Vara"].astype(str).str.split("-", n=1, expand = True)
	planilha_2["Vara"] = corte[1]


	planilha_2["Data de Distribuicao"] = planilha_2["Data de Distribuicao"].astype(str).str.split(" ", n=1, expand = True)[0]
	planilha_2["Data da Movimentação"] = planilha_2["Data da Movimentação"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = planilha_2["Data de Distribuicao"].astype(str).str.split("-", n = 2, expand = True)[0]
	

	planilha_2["Ano"] = ano.astype(int)

	planilha_2.rename(columns={'Foro': 'Comarca', 
		'Data da Movimentação': 'Data da Sentença', 
		'Data de Distribuicao':'Data da Distribuição'},
	 inplace = True)

	# print(planilha_2)




	dados = pd.concat([planilha_1, planilha_2])

	dados["Estado"] = "AP"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados["Competência"] = "Estadual"


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AP.xlsx", index = False)



dados_AP()

#################################                  4 - MA               ##################################################


def dados_MA():

	planilha = pd.read_excel(".\Planilhas tribunais\TJMA_1.xlsx", engine ='openpyxl')

	dados = planilha[["Sistema","Número Único","Comarca","Vara", "Data Abertura","Data do Movimento"]]

	# print(dados ["Data do Movimento"])

	dados["Data Abertura"] = dados["Data Abertura"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data do Movimento"] = dados["Data do Movimento"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data Abertura"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MA"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Comarca"] = dados["Comarca"].astype(str).str.split("-", n=1, expand = True)[1]

	dados.rename(columns={'Número Único': 'Número do Processo','Sistema': 'Origem', 'Data do Movimento': 'Data da Sentença',
		'Data Abertura':'Data da Distribuição'}, 
		inplace = True)

	dados["Competência"] = "Estadual"


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]

	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MA.xlsx", index = False)

dados_MA()



#################################                 5 - MG               ##################################################


def dados_MG():

	planilha = pd.read_excel(".\Planilhas tribunais\TJMG_1.xlsx", engine ='openpyxl')

	dados = planilha[["Nº do Feito Único","Comarca","Vara","Origem dos Dados","Data da Distribuição","Data Sentença"]]

	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data Sentença"] = dados["Data Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data da Distribuição"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MG"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados.rename(columns={'Nº do Feito Único': 'Número do Processo','Origem dos Dados': 'Origem', 'Data Sentença': 'Data da Sentença'}, 
		inplace = True)

	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MG.xlsx", index = False)


dados_MG()




#################################                 6 - MS              ##################################################




#Mandou só as quantidades, não mandou os dados


#################################                 7 - MT               ##################################################

''' dúvidas: Origem dos dados do MT? Quais são do SEEU? sabemos?? '''



def dados_MT():

	planilha = pd.read_excel(".\Planilhas tribunais\TJMT_1.xlsx", engine ='openpyxl')

	dados = planilha

	dados["Data_Inicio_Tramite"] = dados["Data_Inicio_Tramite"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["DataDecisao"] = dados["DataDecisao"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data_Inicio_Tramite"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MT"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados.rename(columns={'NumeroUnico': 'Número do Processo', 'DataDecisao': 'Data da Sentença','Lotacao':'Vara',
		'Data_Inicio_Tramite':'Data da Distribuição'}, 
		inplace = True)

	dados["Competência"] = "Estadual"
	# print(dados)

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MT.xlsx", index = False)


dados_MT()


#################################                 8 - PA               ##################################################

''' dúvidas: Origem dos dados do PA? Quais são do SEEU? sabemos?? '''


def dados_PA():

	planilha = pd.read_excel(".\Planilhas tribunais\TJPA_1.xlsx", engine ='openpyxl')

	dados = planilha

	dados["DATA DISTRIBUIÇÃO"] = dados["DATA DISTRIBUIÇÃO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')
	dados["DATA EXTINÇÃO PUNIBILIDADE"] = dados["DATA EXTINÇÃO PUNIBILIDADE"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')

	# print(dados["DATA DISTRIBUIÇÃO"])
	# z= input("")

	ano = dados["DATA DISTRIBUIÇÃO"].astype(str).str.split("-", n=2, expand = True)[2]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "PA"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["PROCESSO"] = dados["PROCESSO"].astype(str)

	dados.rename(columns={'PROCESSO': 'Número do Processo', 'DATA EXTINÇÃO PUNIBILIDADE': 'Data da Sentença','UNIDADE SENTENÇA':'Vara',
		'DATA DISTRIBUIÇÃO':'Data da Distribuição', 'COMARCA': 'Comarca'}, 
		inplace = True)


	dados["Competência"] = "Estadual"
	# print(dados)

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')



	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência"]]

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PA.xlsx", index = False)


dados_PA()


#################################                 9 - PB              ##################################################

######## não tem dt distribuição e, logo, não tem ano nesse Estado, não tem origem

def dados_PB():
	cmn_arq = ".\Planilhas tribunais\TJPB_1.pdf"

	numeros= []
	data_sente =[]
	varas = []
	with fitz.open(cmn_arq) as arquivo:
	     for pagina in arquivo:
	        blocks = pagina.get_text('dict')['blocks']
	        for o in range(len(blocks)):
	        	# print(blocks[o])
	        	# z = input('')
	        	try:
	        		lines = blocks[o]["lines"]
	        		txt_block = []
	        		for x in range(len(lines)):
	        			spans = lines[x]["spans"]
	        			for u in spans:
	        				txt_block.append(u['text'])
	        		# print(txt_block)
	        		if re.match('[0-9]',txt_block[0]):
	        			numeros.append(txt_block[0].strip())
	        			data_sente.append(txt_block[1].strip())
	        			varas.append(txt_block[3].strip())
	        	except:
	        			pass


	dados = pd.DataFrame({"Número do Processo":numeros,"Vara":varas,"Data da Sentença":data_sente})

	corte = dados["Vara"].astype(str).str.split(" DE ", n=3, expand = True)


	comarcas = []
	for k in range(len(corte[3])):
		num = corte.loc[k,3]
		if num == None:
			num = corte.loc[k,2]
			comarcas.append(num.strip())
		else:
			comarcas.append(num.strip())	

	dados["Comarca"] = comarcas


	dados["Competência"] = "Estadual"
	dados["Estado"] = "PB"

	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.replace("/","-")


	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara","Data da Sentença", "Estado", "Competência"]]

	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PB.xlsx", index = False)


dados_PB()



#################################                 10 - PI              ##################################################

def dados_PI():

	''' dúvidas: Origem dos dados do PI? Quais são do SEEU? sabemos?? '''


	planilha = pd.read_excel(".\Planilhas tribunais\TJPI_1.xlsx", engine ='openpyxl')

	dados = planilha

	dados["Data Distribuição"] = dados["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data Julgamento"] = dados["Data Julgamento"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data Distribuição"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "PI"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados.rename(columns={'Processo': 'Número do Processo', 'Data Julgamento': 'Data da Sentença','Órgão Julgador':'Vara',
		'Data Distribuição':'Data da Distribuição'}, 
		inplace = True)


	dados.drop(columns =["Movimento"], inplace = True)

	# print(dados)
	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência"]]

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PI.xlsx", index = False)


dados_PI()


#################################                 11 - PR              ##################################################

#Não entendi os dados da Tabela, ver com a naty





#################################                 12 - RJ             ##################################################

# não tem nada




#################################                 13 - RO             ##################################################

def dados_RO():

	''' dúvidas: Origem dos dados do RO? Quais são do SEEU? sabemos?? '''


	planilha = pd.read_excel(".\Planilhas tribunais\TJRO_1.xlsx", engine ='openpyxl')

	dados = planilha

	dados["Data de Distribuição"] = dados["Data de Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data do movimento"] = dados["Data do movimento"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data de Distribuição"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "RO"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados.rename(columns={'Número Processo': 'Número do Processo', 'Data do movimento': 'Data da Sentença','Serventia':'Vara',
		'Data de Distribuição':'Data da Distribuição'}, 
		inplace = True)


	dados.drop(columns =["Número CNJ"], inplace = True)

	# print(dados)
	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência"]]

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_RO.xlsx", index = False)


dados_RO()


#################################                 14 - RR             ##################################################

#ver depois com a Naty...mandou de feminicídio???


#################################                 15 - RS             ##################################################

# não tem nada





#################################                 16 - SC             ##################################################

# não mandou os números dos processos




#################################                 17 - SP             ##################################################


def dados_SP():

	''' dúvidas: Origem dos dados do SP? Quais são do SEEU? sabemos?? AO que parece todos são do SAJ'''


	planilha = pd.read_excel(".\Planilhas tribunais\TJSP_1.xlsx", engine ='openpyxl')

	dados = planilha[["Número do Processo","Descrição do Foro","Descrição da Vara","Data Distribuição",
	"Data da Extinção da Punibilidade"]]


	dados["Data Distribuição"] = dados["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data da Extinção da Punibilidade"] = dados["Data da Extinção da Punibilidade"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Data Distribuição"].astype(str).str.split("-", n=1, expand = True)[0]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "SP"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Origem"] = "SAJ"


	dados.rename(columns={'Número do Processo': 'Número do Processo', 'Data da Extinção da Punibilidade': 'Data da Sentença','Descrição da Vara':'Vara',
		'Data Distribuição':'Data da Distribuição', 'Descrição do Foro': 'Comarca'}, 
		inplace = True)


	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_SP.xlsx", index = False)


dados_SP()


#################################                 18 - TO             ##################################################

def dados_TO():

	planilha = pd.read_excel(".\Planilhas tribunais\TJTO_1.xlsx", engine ='openpyxl')

	planilha_1 = planilha[["LOCALIDADE_JUDICIAL","VARA","PROCESSO","DATA_DISTRIBUICAO",
	"DATA_MOVIMENTO"]]


	planilha_1 ["Origem"] = "EPROC"

	# print(ano)
		


	planilha_1["DATA_DISTRIBUICAO"] = planilha_1["DATA_DISTRIBUICAO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	planilha_1["DATA_MOVIMENTO"] = planilha_1["DATA_MOVIMENTO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	
	

	ano = planilha_1["DATA_DISTRIBUICAO"].astype(str).str.split("-", n=2, expand = True)[2]
	planilha_1["Ano"] = ano.astype(int)

	planilha_1.rename(columns={'LOCALIDADE_JUDICIAL': 'Comarca',
		'VARA':'Vara', 'PROCESSO': 'Número do Processo', 
		'DATA_MOVIMENTO': 'Data da Sentença', 
		'DATA_DISTRIBUICAO':'Data da Distribuição'},
	 inplace = True)

	# print(planilha_1)


			#############        Parte 2               ##############

			#### processos da plainha do SEEU não tem a data de distribuição...o que
			## faremos com esses casos????




	planilha = pd.read_excel(".\Planilhas tribunais\TJTO_2.xlsx", engine ='openpyxl')

	planilha_2 = planilha[["PROCESSOS","DATA DO EVENTO"]]



	numeros = []
	dt_sente = []
	for k in range(len(planilha_2["PROCESSOS"])):
		num = planilha_2.loc[k,"PROCESSOS"]
		try:
			num, a = num.split(" ")
			if re.search("[0-9]",num):
				numeros.append(num)
				dt_sen = planilha_2.loc[k,"DATA DO EVENTO"]
				dt_sente.append(dt_sen)
				# print(num)
				# print(dt_sen)
		except:
			pass	


	planilha_2 = pd.DataFrame({"Número do Processo":numeros, "Data da Sentença":dt_sen})		
	planilha_2 ["Origem"] = "SEEU"

	planilha_2["Data da Sentença"] = planilha_2["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]

	# print(planilha_2)


	# corte = planilha_2["Vara"].astype(str).str.split("-", n=1, expand = True)
	# planilha_2["Vara"] = corte[1]


	# planilha_2["Data de Distribuicao"] = planilha_2["Data de Distribuicao"].astype(str).str.split(" ", n=1, expand = True)[0]
	# ano = planilha_2["Data de Distribuicao"].astype(str).str.split("-", n = 2, expand = True)[0]
	

	# planilha_2["Ano"] = ano.astype(int)

	# planilha_2.rename(columns={'Foro': 'Comarca', 
	# 	'Data da Movimentação': 'Data da Sentença', 
	# 	'Data de Distribuicao':'Data da Distribuição'},
	#  inplace = True)

	# print(planilha_2)


	dados = pd.concat([planilha_1, planilha_2])

	dados["Estado"] = "TO"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Competência"] = "Estadual"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TO.xlsx", index = False)


dados_TO()





#################################                 19 - TRF 1            ##################################################

# não tem






#################################                 20 - TRF 3            ##################################################



def dados_TRF3():

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3.xlsx", engine ='openpyxl')

	planilha_1 = planilha[["SEÇÃO","SUBSEÇÃO","DATA DISTRIBUIÇÃO","DATA DA FASE","NUMERO DO PROCESSO"]]

	planilha_1["DATA DISTRIBUIÇÃO"] = planilha_1["DATA DISTRIBUIÇÃO"].astype(str).str.split(" ", n=1, expand = True)[0]
	planilha_1["DATA DA FASE"] = planilha_1["DATA DA FASE"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = planilha_1["DATA DISTRIBUIÇÃO"].astype(str).str.split("-", n=1, expand = True)[0]

	planilha_1["Ano"] = ano.astype(int)
	planilha_1["Origem"] = "DW"
	

	df_filter = planilha_1 ["Ano"] >= 2017
	planilha_1 = planilha_1[df_filter]

	planilha_1.rename(columns={'SEÇÃO':'Estado','NUMERO DO PROCESSO': 'Número do Processo', 
		'DATA DA FASE': 'Data da Sentença','SUBSEÇÃO': "Comarca", 'DATA DISTRIBUIÇÃO':'Data da Distribuição'}, 
		inplace = True)



	###################### Não temos a data de distribuição dos processos do SEEU #######################


	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3.xlsx", engine ='openpyxl', sheet_name='SEEU _ Morte Agente')

	planilha_2 = planilha[["Seção Judiciária","Subseção Judiciária","Data Fase","Processo"]]


	planilha_2["Data Fase"] = planilha_2["Data Fase"].astype(str).str.split(" ", n=1, expand = True)[0]

	

	planilha_2["Origem"] = "SEEU"
	
	planilha_2.dropna(inplace = True)

	planilha_2.reset_index(inplace=True)

	planilha_2["Processo"] = planilha_2["Processo"].astype(str).str[:-3]
	# print(planilha_2)

	# print(planilha_2["Processo"])
	

	planilha_2.rename(columns={'Seção Judiciária':'Estado','Processo': 'Número do Processo', 
		'Data Fase': 'Data da Sentença','Subseção Judiciária': "Comarca"}, 
		inplace = True)


	dados = pd.concat([planilha_1, planilha_2])


	dados["Competência"] = "Federal - TRF3"

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')


	dados["Tribunal"] = "TRF3"

	dados = dados[["Número do Processo", "Comarca", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Tribunal","Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF_3.xlsx", index = False)


dados_TRF3()



#################################                 21 - TRF 4            #################################################

def dados_TRF4():

	# Não temos a origem dos casos desse Estado
	

	lista_est =["RS","SC","PR"]
	dfs =[]

	for k in range(len(lista_est)):

		planilha = pd.read_excel(".\Planilhas tribunais\TRF_4.xlsx", engine ='openpyxl', sheet_name=lista_est[k])

		planilha_1 = planilha[["Processo","Localidade","Vara Federal","Data Distribuição","Data Decisão"]]


		planilha_1["Data Distribuição"] = planilha_1["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
		planilha_1["Data Decisão"] = planilha_1["Data Decisão"].astype(str).str.split(" ", n=1, expand = True)[0]
		

		ano = planilha_1["Data Distribuição"].astype(str).str.split("-", n=2, expand = True)[0]
		planilha_1["Ano"] = ano.astype(int)
		planilha_1["Estado"] = lista_est[k]


		planilha_1.rename(columns={'Localidade':'Comarca','Processo': 'Número do Processo', 
			'Data Decisão': 'Data da Sentença','Vara Federal': "Vara", 'Data Distribuição':'Data da Distribuição'}, 
			inplace = True)

		dfs.append(planilha_1)

		# print(planilha_1)

	dados = pd.concat([dfs[0],dfs[1],dfs[2]])
	# print(dados)

	dados["Competência"] = "Federal"


	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])

	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime('%d-%m-%Y')

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = pd.to_datetime(dados['Data da Sentença'])

	dados['Data da Sentença'] = dados['Data da Sentença'].dt.strftime('%d-%m-%Y')

	dados["Tribunal"] = "TRF4"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Tribunal","Competência"]]
	# print(dados)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF_4.xlsx", index = False)



dados_TRF4()


main()