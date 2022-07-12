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
		dados_planilhas_lidas.append(pd.read_excel(planilha,engine ='openpyxl'))
	#	print("Lida!")

	todos_dados = todos_dados.append(dados_planilhas_lidas, ignore_index=True, sort=False)
	todos_dados["Tribunal"] = np.where(todos_dados['Tribunal'].isnull() == True, "TJ"+todos_dados["Estado"].str[:],todos_dados['Tribunal'])

	todos_dados["Origem_dados"] = "LAI"

	todos_dados["Comarca"] = todos_dados["Comarca"].str.lower() 
	todos_dados["Vara"] = todos_dados["Vara"].str.lower()

	df_filter = todos_dados["Ano"] < 2022
	todos_dados = todos_dados[df_filter]

	todos_dados.to_excel("Dados_compilados_3.xlsx", index=False)
	print(todos_dados)
	print(todos_dados.info())


# z= input("")



#################################                  1- AC               ##################################################


''' dúvidas: Origem dos dados do AC? Quais são do SEEU? sabemos??  não consegui resolver o problema do encode nas planilhas novas'''



def dados_AC():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJAC_1.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJAC_2.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJAC_3.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_4 = pd.read_excel(".\Planilhas tribunais\TJAC_4.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_5 = pd.read_excel(".\Planilhas tribunais\TJAC_5.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_6 = pd.read_excel(".\Planilhas tribunais\TJAC_6.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição"])
	planilha_7_1 = pd.read_excel(".\Planilhas tribunais\TJAC_7.xlsx", engine ='openpyxl', sheet_name= 'Ext Punibilidade_morte do agent', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_7_1['Planilha'] = "TJAC_7_1"
	planilha_7_2 = pd.read_excel(".\Planilhas tribunais\TJAC_7.xlsx", engine ='openpyxl', sheet_name= 'Ext Punibilidade_morte do a (2)', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_7_2['Planilha'] = "TJAC_7_2"
	planilha_7_3 = pd.read_excel(".\Planilhas tribunais\TJAC_7.xlsx", engine ='openpyxl', sheet_name= 'Ext Punibilidade_morte do a (3)', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_7_3['Planilha'] = "TJAC_7_3"
	planilha_7_4 = pd.read_excel(".\Planilhas tribunais\TJAC_7.xlsx", engine ='openpyxl', sheet_name= 'Ext Punibiilidade_morte do agen', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_7_4['Planilha'] = "TJAC_7_4"
	planilha_7_5 = pd.read_excel(".\Planilhas tribunais\TJAC_7.xlsx", engine ='openpyxl', sheet_name= 'Ext Punibilidade_morte do a (4)', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_7_5['Planilha'] = "TJAC_7_5"
	planilha_8 = pd.read_excel(".\Planilhas tribunais\TJAC_8.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_9 = pd.read_excel(".\Planilhas tribunais\TJAC_9.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])
	planilha_10 = pd.read_excel(".\Planilhas tribunais\TJAC_10.xlsx", engine ='openpyxl', 
		usecols = ["Processo","Foro / Vara","Data Distribuição","Data da Movimentação"])

	planilha_1["Planilha"] = "TJAC_1"
	planilha_2["Planilha"] = "TJAC_2"
	planilha_3['Planilha'] = "TJAC_3"
	planilha_4['Planilha'] = "TJAC_4"
	


	planilha_4["Data Distribuição"] = pd.to_datetime(planilha_4["Data Distribuição"])
	planilha_4["Data Distribuição"] = planilha_4["Data Distribuição"].dt.strftime("%d-%m-%Y %H:%M:%S")
	planilha_4["Data da Movimentação"] = pd.to_datetime(planilha_4["Data da Movimentação"])
	planilha_4["Data da Movimentação"] = pd.to_datetime(planilha_4["Data da Movimentação"]).dt.strftime("%d-%m-%Y %H:%M:%S")

	planilha_5['Planilha'] = "TJAC_5"
	planilha_6['Planilha'] = "TJAC_6"
	planilha_8['Planilha'] = "TJAC_8"

	planilha_8["Data Distribuição"] = pd.to_datetime(planilha_8["Data Distribuição"])
	planilha_8["Data Distribuição"] = planilha_8["Data Distribuição"].dt.strftime("%d-%m-%Y %H:%M:%S")
	planilha_8["Data da Movimentação"] = pd.to_datetime(planilha_8["Data da Movimentação"])
	planilha_8["Data da Movimentação"] = planilha_8["Data da Movimentação"].dt.strftime("%d-%m-%Y %H:%M:%S")
	
	planilha_9['Planilha'] = "TJAC_9"

	planilha_9["Data Distribuição"] = pd.to_datetime(planilha_9["Data Distribuição"])
	planilha_9["Data Distribuição"] = planilha_9["Data Distribuição"].dt.strftime("%d-%m-%Y %H:%M:%S")
	planilha_9["Data da Movimentação"] = pd.to_datetime(planilha_9["Data da Movimentação"])
	planilha_9["Data da Movimentação"] = planilha_9["Data da Movimentação"].dt.strftime("%d-%m-%Y %H:%M:%S")
	
	planilha_10['Planilha'] = "TJAC_10"

	planilha_10["Data Distribuição"] = pd.to_datetime(planilha_10["Data Distribuição"])
	planilha_10["Data Distribuição"] = planilha_10["Data Distribuição"].dt.strftime("%d-%m-%Y %H:%M:%S")
	planilha_10["Data da Movimentação"] = pd.to_datetime(planilha_10["Data da Movimentação"])
	planilha_10["Data da Movimentação"] = planilha_10["Data da Movimentação"].dt.strftime("%d-%m-%Y %H:%M:%S")

	# print(planilha_5['Data Distribuição'][0],"5")
	# print(planilha_6['Data Distribuição'][0],"6")
	# print(planilha_7_1['Data Distribuição'][0],"7_1")
	# print(planilha_7_2['Data Distribuição'][0],"7_2")
	# print(planilha_7_3['Data Distribuição'][0],"7_3")
	# print(planilha_7_4['Data Distribuição'][0],"7_4")
	# print(planilha_7_5['Data Distribuição'][0],"7_5")
	# print(planilha_8['Data Distribuição'][1],"8")
	# print(planilha_9['Data Distribuição'][1],"9")
	# print(planilha_10['Data Distribuição'][1],"10")
	# z = input("")

	dados = pd.concat([planilha_1, planilha_2, planilha_3,planilha_4,planilha_5,planilha_6, planilha_7_1,planilha_7_2,planilha_7_3,planilha_7_4,planilha_7_5,
		planilha_8,planilha_9,planilha_10])

	# print(dados)
	# z = input("")

	dados["Foro / Vara"] = dados["Foro / Vara"].str.encode('UTF-8').str.decode("utf-8")

	corte = dados["Foro / Vara"].astype(str).str.split("/", n=1, expand = True)

	dados.drop(columns =["Foro / Vara"], inplace = True)

	dados["Comarca"] = corte[0].str.strip()
	dados["Vara"] = corte[1].str.strip()





	dados["Data Distribuição"] = dados["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	try:
		dados["Data da Movimentação"] = dados["Data da Movimentação"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	except:
		dados["Data da Movimentação"] = None



	ano = dados["Processo"].astype(str).str.split(".", expand = True)[1]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "AC"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados.rename(columns={'Processo': 'Número do Processo', 
		'Data da Movimentação': 'Data da Sentença', 
		'Data Distribuição':'Data da Distribuição'},
	 inplace = True)

	dados["Competência"] = "Estadual"


	dados["Número do Processo"] = dados["Número do Processo"].astype(str).str.replace("-","")
	dados["Número do Processo"] = dados["Número do Processo"].astype(str).str.replace(".","")
	# print(dados)

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	

	dados.drop_duplicates(subset="Número do Processo", inplace = True)

	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]


	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AC.xlsx", index = False, encoding='iso-8859-1')




#################################                  2- Al               ##################################################


def dados_AL():

	planilha = pd.read_excel(".\Planilhas tribunais\TJAL_1.xlsx", engine ='openpyxl')

	dados = planilha[["Foro","Vara","Processo","Data da distribuição"]]

	dados["Data da distribuição"] = dados["Data da distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")

	
	dados["Data da Movimentação"] = None
	ano = dados["Processo"].astype(str).str.split(".", expand = True)[1]

	
	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "AL"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Foro"] = dados["Foro"].astype(str).str.replace("Foro de", "").str.strip()

	dados.rename(columns={'Processo': 'Número do Processo', 
		'Data da Movimentação': 'Data da Sentença', 
		'Data da distribuição':'Data da Distribuição', 'Foro': 'Comarca'},
	 inplace = True)

	


	# dados ["codigo"] = dados["Número do Processo"].astype(str).str.split(".", expand = True)[4]

	# print(dados ["codigo"])


	# doc = open("Array_aux_AL_com.txt","w", encoding = 'utf-8')
	# lista_cod =[]

	# for cod,com in zip(dados ["codigo"],dados["Comarca"]):
	# 	if com not in lista_cod:
	# 		lista_cod.append(com)
	# 		doc.write("['"+cod+"',0,'"+com.strip()+"'],\n")

	# doc.close()	

	dados["Competência"] = "Estadual"

	dados.drop_duplicates(subset="Número do Processo", inplace = True)

	dados["Planilha"] = "TJAL_1"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]
	

	dados["Número do Processo"] = dados["Número do Processo"].astype(str).str.replace("-","")
	dados["Número do Processo"] = dados["Número do Processo"].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AL.xlsx", index = False, encoding='iso-8859-1')







#################################                  3 - AM               ##################################################


def dados_AM():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJAM_1.xlsx", engine ='openpyxl', sheet_name ='Extinta-Puni-MorteAgente-VEP')
	
	planilha_1 = planilha_1[["Foro","Vara","Processo","Data da Mov. Decisão", "Data de Recebimento"]]

	planilha_1['Origem'] = "SAJ/PROJUDI"

	planilha_1["Planilha"] = "TJAM_1"



	p_1_1 = planilha_1.iloc[:768,:]

	p_1_2 = planilha_1.iloc[768:,:]




	p_1_1["Data da Mov. Decisão"] = pd.to_datetime(p_1_1["Data da Mov. Decisão"])
	p_1_1["Data da Mov. Decisão"] = p_1_1["Data da Mov. Decisão"].dt.strftime("%d-%m-%Y %H:%M:%S")
	p_1_1["Data de Recebimento"] = pd.to_datetime(p_1_1["Data de Recebimento"])
	p_1_1["Data de Recebimento"] = p_1_1["Data de Recebimento"].dt.strftime("%d-%m-%Y %H:%M:%S")




	planilha_1 = pd.concat([p_1_1,p_1_2])




	planilha_1_2 = pd.read_excel(".\Planilhas tribunais\TJAM_1.xlsx", engine ='openpyxl', sheet_name ='SEEU')
	
	planilha_1_2 = planilha_1_2[["Foro","Vara","Processo","Data da Mov. Decisão", "Data de Recebimento"]]
	
	planilha_1_2['Origem'] = "SEEU"

	planilha_1_2["Planilha"] = "TJAM_1_2"




	dados = pd.concat([planilha_1, planilha_1_2])

	dados["Estado"] = "AM"



	dados["Data de Recebimento"] = dados["Data de Recebimento"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados["Data da Mov. Decisão"] = dados["Data da Mov. Decisão"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")

	fim = dados["Processo"].astype(str).str[-4:]
	est = dados["Processo"].astype(str).str[-6:-4]
	just = dados["Processo"].astype(str).str[-7]
	ano_aj = dados["Processo"].astype(str).str[-11:-7]
	cod = dados["Processo"].astype(str).str[-13:-11]
	rest = dados["Processo"].astype(str).str[:-13]

	dados["Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	# print(dados["Processo"])

	ano = dados["Processo"].astype(str).str.split(".", expand = True)[1]

	dados ["Ano"] = ano.astype(int)
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

	
	
	## processamento da segunda planilha

	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJAM_2.xlsx", sheet_name= 'Morte do agente - SAJ', engine ='openpyxl')

	dados_2 = planilha_2[["Vara","Processo","Data da distribuição"]]

	dados_2["Data da distribuição"] = dados_2["Data da distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")


	ano_2 = dados_2["Processo"].astype(str).str.split(".", expand = True)[1]

	dados_2["Ano"] = ano_2.astype(int)
	dados_2["Estado"] = "AM"
	dados_2["Competência"] = "Estadual"
	dados_2['Origem'] = "SAJ"

	
	dados_2.rename(columns={'Processo': 'Número do Processo', 'Data da distribuição': 'Data da Distribuição'}, inplace = True)

	df_filter_2 = dados_2 ["Ano"] >= 2017
	dados_2 = dados_2[df_filter_2]
	
	dados_2["Planilha"] = "TJAM_2_1"


	## processamento da terceira planilha

	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJAM_2.xlsx", sheet_name= 'Morte do agente - Projudi', engine ='openpyxl',  dtype="object")

	dados_3 = planilha_3[["comarca","vara","processo","data da distribuição","data da movimentação"]]

	dados_3["data da distribuição"] = dados_3["data da distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados_3["data da movimentação"] = dados_3["data da movimentação"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")



	fim = dados_3["processo"].astype(str).str[-4:]
	est = dados_3["processo"].astype(str).str[-6:-4]
	just = dados_3["processo"].astype(str).str[-7]
	ano_aj = dados_3["processo"].astype(str).str[-11:-7]
	cod = dados_3["processo"].astype(str).str[-13:-11]
	rest = dados_3["processo"].astype(str).str[:-13]

	dados_3["processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	# print(dados_3["processo"])


	ano_3 = dados_3["processo"].astype(str).str.split(".", expand = True)[1]
	dados_3["Ano"] = ano_3.astype(int)
	dados_3["Estado"] = "AM"
	dados_3["Competência"] = "Estadual"
	dados_3['Origem'] = "Projudi"


	dados_3.rename(columns={'processo': 'Número do Processo', 'data da distribuição': 'Data da Distribuição', 'vara': 'Vara', 'data da movimentação':'Data da Sentença', 
		'comarca': 'Comarca'}, inplace = True)



	df_filter_3 = dados_3["Ano"] >= 2017
	dados_3 = dados_3[df_filter_3]

	dados_3["Planilha"] = "TJAM_2_2"


	#### processamento da quarta planilha

	planilha_4 = pd.read_excel(".\Planilhas tribunais\TJAM_2.xlsx", engine ='openpyxl', sheet_name= 'Morte do agente - VEPs')
	
	dados_4 = planilha_4[["Foro","Vara","Processo","Data da Mov. Decisão", "Data de Recebimento"]]
	

	dados_4["Data de Recebimento"] = dados_4["Data de Recebimento"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados_4["Data da Mov. Decisão"] = dados_4["Data da Mov. Decisão"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	
	dados_4["Processo"] = dados_4["Processo"].astype(str).str.replace("-","")
	dados_4["Processo"] = dados_4["Processo"].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados_4["Processo"].astype(str).str[-4:]
	est = dados_4["Processo"].astype(str).str[-6:-4]
	just = dados_4["Processo"].astype(str).str[-7]
	ano_aj = dados_4["Processo"].astype(str).str[-11:-7]
	cod = dados_4["Processo"].astype(str).str[-13:-11]
	rest = dados_4["Processo"].astype(str).str[:-13]

	dados_4 ["Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	# print(dados_4["Processo"])



	ano_4 = dados_4["Processo"].astype(str).str.split(".", expand = True)[1]


	dados_4["Ano"] = ano_4.astype(int)
	dados_4["Estado"] = "AM"

	origem_4 =[]
	for i in range(len(dados_4["Ano"])):
		if i < 86:
			origem_4.append("SAJ")
		else:
			origem_4.append("SEEU")

	dados_4['Origem'] = origem_4
 

	df_filter_4 = dados_4["Ano"] >= 2017
	dados_4 = dados_4[df_filter_4]

	dados_4.rename(columns={'Processo': 'Número do Processo', 'Data da Mov. Decisão': 'Data da Sentença',
		'Data de Recebimento': 'Data da Distribuição', 'Foro':'Comarca'}, 
		inplace = True)


	dados_4["Competência"] = "Estadual"


	dados_4["Planilha"] = "TJAM_2_3"


	dados_4['Data da Distribuição'] = pd.to_datetime(dados_4['Data da Distribuição'])
	dados_4['Data da Distribuição'] = dados_4['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados_4["Data da Sentença"] = pd.to_datetime(dados_4["Data da Sentença"])
	dados_4["Data da Sentença"] = dados_4["Data da Sentença"].dt.strftime("%d-%m-%Y")


	## união das planilhas 

	dados = pd.concat([dados, dados_2, dados_3, dados_4])

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem","Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	# print(dados)


	dados["Comarca"] = dados["Comarca"].replace(to_replace ="Fórum de|Comarca de", value = '', regex = True).str.strip()
	

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AM.xlsx", index = False)



#################################                  3- AP              ##################################################


def dados_AP():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJAP_1.xlsx", engine ='openpyxl')

	planilha_1 ["Origem"] = "Tucujuris"

	planilha_1["Dt. Distrib."] = planilha_1["Dt. Distrib."].astype(str).str.split(" ", n=1, expand = True)[0]
	planilha_1["Dt. Decisão"] = planilha_1["Dt. Decisão"].astype(str).str.split(" ", n=1, expand = True)[0]

	planilha_1.rename(columns={'FORO': 'Comarca',
		'VARA':'Vara', 'Número Único': 'Número do Processo', 
		'Dt. Decisão': 'Data da Sentença', 
		'Dt. Distrib.':'Data da Distribuição'},
	 inplace = True)

	planilha_1['Número do Processo'] = planilha_1['Número do Processo'].astype(str).str.replace("-","")
	planilha_1['Número do Processo'] = planilha_1['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = planilha_1['Número do Processo'].astype(str).str[-4:]
	est = planilha_1['Número do Processo'].astype(str).str[-6:-4]
	just = planilha_1['Número do Processo'].astype(str).str[-7]
	ano_aj = planilha_1['Número do Processo'].astype(str).str[-11:-7]
	cod = planilha_1['Número do Processo'].astype(str).str[-13:-11]
	rest = planilha_1['Número do Processo'].astype(str).str[:-13]

	planilha_1 ['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano = planilha_1['Número do Processo'].astype(str).str.split(".", expand = True)[1]
 
	planilha_1["Ano"] = ano.astype(int)

	planilha_1["Planilha"] = "TJAP_1"


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



	# ajuste no número do processo

	fim = planilha_2['Número do Processo'].astype(str).str[-4:]
	est = planilha_2['Número do Processo'].astype(str).str[-6:-4]
	just = planilha_2['Número do Processo'].astype(str).str[-7]
	ano_aj = planilha_2['Número do Processo'].astype(str).str[-11:-7]
	cod = planilha_2['Número do Processo'].astype(str).str[-13:-11]
	rest = planilha_2['Número do Processo'].astype(str).str[:-13]

	planilha_2 ['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_2 = planilha_2['Número do Processo'].astype(str).str.split(".", expand = True)[1]
 
	planilha_2 ["Ano"] = ano_2.astype(int)

	planilha_2["Planilha"] = "TJAP_2"


	############ parte 3 ######################


	## PLANILHA COM 3 ABAS

	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJAP_3.xlsx", engine ='openpyxl', sheet_name = 'Pergunta 1')

	planilha_3 ["Origem"] = "VEPs"


	planilha_3["Dt_distribuicao"] = planilha_3["Dt_distribuicao"].astype(str).str.replace("/","-")
	planilha_3["Data_decisao_extincao"] = planilha_3["Data_decisao_extincao"].astype(str).str.replace("/","-")
	# print(planilha_3["Dt_distribuicao"])
	# print(planilha_3["Data_decisao_extincao"])
	# z= input("")


	planilha_3.rename(columns={'Processo': 'Número do Processo', 
		'Data_decisao_extincao': 'Data da Sentença', 
		'Dt_distribuicao':'Data da Distribuição'},
	 inplace = True)



	planilha_3['Número do Processo'] = planilha_3['Número do Processo'].astype(str).str.replace("-","")
	planilha_3['Número do Processo'] = planilha_3['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = planilha_3['Número do Processo'].astype(str).str[-4:]
	est = planilha_3['Número do Processo'].astype(str).str[-6:-4]
	just = planilha_3['Número do Processo'].astype(str).str[-7]
	ano_aj = planilha_3['Número do Processo'].astype(str).str[-11:-7]
	cod = planilha_3['Número do Processo'].astype(str).str[-13:-11]
	rest = planilha_3['Número do Processo'].astype(str).str[:-13]

	planilha_3['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_3 = planilha_3['Número do Processo'].astype(str).str.split(".", expand = True)[1]
 
	planilha_3["Ano"] = ano_3.astype(int)

	planilha_3["Planilha"] = "TJAP_3_1"



	############ parte 4 ######################

	planilha_4 = pd.read_excel(".\Planilhas tribunais\TJAP_3.xlsx", engine ='openpyxl', sheet_name = 'Pergunta 1 - Sistema Seeu')

	planilha_4 ["Origem"] = "SEEU"


	planilha_4["Data do Julgamento"] = planilha_4["Data do Julgamento"].astype(str).str.split(" ", n=1, expand = True)[0]


	planilha_4.rename(columns={'Processo': 'Número do Processo', 
		'Data do Julgamento': 'Data da Sentença'},
	 inplace = True)


	planilha_4['Número do Processo'] = planilha_4['Número do Processo'].astype(str).str.replace("-","")
	planilha_4['Número do Processo'] = planilha_4['Número do Processo'].astype(str).str.replace(".","")
	planilha_4['Número do Processo'] = planilha_4['Número do Processo'].str.strip()

	# ajuste no número do processo

	fim = planilha_4['Número do Processo'].astype(str).str[-4:]
	est = planilha_4['Número do Processo'].astype(str).str[-6:-4]
	just = planilha_4['Número do Processo'].astype(str).str[-7]
	ano_aj = planilha_4['Número do Processo'].astype(str).str[-11:-7]
	cod = planilha_4['Número do Processo'].astype(str).str[-13:-11]
	rest = planilha_4['Número do Processo'].astype(str).str[:-13]

	planilha_4['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim



	ano_4 = planilha_4['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	planilha_4["Ano"] = ano_4.astype(int)

	planilha_4["Planilha"] = "TJAP_3_2"


	############ parte 5 ######################

	planilha_5 = pd.read_excel(".\Planilhas tribunais\TJAP_3.xlsx", engine ='openpyxl', sheet_name = 'Pergunta 2')

	planilha_5 ["Origem"] = "família ou cível"


	planilha_5["dt_distribuicao"] = planilha_5["dt_distribuicao"].astype(str).str.replace("/","-")
	planilha_5["data_decisao_extincao"] = planilha_5["data_decisao_extincao"].astype(str).str.replace("/","-")


	planilha_5.rename(columns={'processo': 'Número do Processo', 
		'data_decisao_extincao': 'Data da Sentença', 
		'dt_distribuicao':'Data da Distribuição'},
	 inplace = True)



	planilha_5['Número do Processo'] = planilha_5['Número do Processo'].astype(str).str.replace("-","")
	planilha_5['Número do Processo'] = planilha_5['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = planilha_5['Número do Processo'].astype(str).str[-4:]
	est = planilha_5['Número do Processo'].astype(str).str[-6:-4]
	just = planilha_5['Número do Processo'].astype(str).str[-7]
	ano_aj = planilha_5['Número do Processo'].astype(str).str[-11:-7]
	cod = planilha_5['Número do Processo'].astype(str).str[-13:-11]
	rest = planilha_5['Número do Processo'].astype(str).str[:-13]

	planilha_5['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_5 = planilha_5['Número do Processo'].astype(str).str.split(".", expand = True)[1]
 
	planilha_5["Ano"] = ano_5.astype(int)

	planilha_5["Planilha"] = "TJAP_3_3"


	################# unificação geral ###############

	dados = pd.concat([planilha_1, planilha_2, planilha_3, planilha_4, planilha_5])

	dados["Estado"] = "AP"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	dados["Competência"] = "Estadual"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]
	# print(dados)

	print(dados)
	print(dados.info())

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_AP.xlsx", index = False)




###################################  BA ###############################################

def dados_BA():

	cmn_arq = ".\Planilhas tribunais\TJBA_1.pdf"

	
	dados =[]
	with fitz.open(cmn_arq) as arquivo:
		for pagina in arquivo:
			blocks = pagina.get_text('dict')['blocks']
			for o in range(len(blocks)):
				try:
					lines = blocks[o]["lines"]
					txt_block = []
					for x in range(len(lines)):
						spans = lines[x]["spans"]
						for u in spans:
							txt_block.append(u['text'])
					if len(txt_block) > 3:
						dados.append(txt_block)
				except:
					pass

	del(dados[-2:])				

	df_ba = pd.DataFrame(columns = dados[0])
	df_ba_errados = pd.DataFrame(columns = dados[0])
	df_ba.drop(columns =["CLASSE","CODIGO_ASSUNTO","CODIGO_CLASSE", "CODIGO_MOVIMENTO"], inplace= True)	
	df_ba_errados.drop(columns =["CLASSE","CODIGO_ASSUNTO","CODIGO_CLASSE", "ASSUNTO", "CODIGO_MOVIMENTO"], inplace= True)


	# print(df_ba)
	# z = input("")


	del(dados[0])
	del(dados[2782])

	## tratar esses depois
	erros = [2809,2901,3142,3149,3200,3273,3553]
	for k in range(len(dados)):
		if len(dados[k]) == 7:
			df_ba.loc[k] = dados[k]
		else:
			if len(dados[k]) == 6 and k not in erros:
				df_ba_errados.loc[k] = dados[k]
			else:
				# print(k)
				# print(dados[k][0])
				cortados = re.split("VARA|1", dados[k][0])
				del dados[k][0]
				# print(cortados)
				if len(cortados) == 2:
					dados[k].insert(0,cortados[0])
					dados[k].insert(1,"VARA "+str(cortados[1]))
					# print(dados[k])
					df_ba.loc[k] = dados[k]
				if len(cortados) == 3:
					dados[k].insert(0,cortados[0])
					dados[k].insert(1,"1"+str(cortados[1])+"VARA"+str(cortados[2]))
					# print(dados[k])
					df_ba.loc[k] = dados[k]




	cortes = df_ba_errados ['NUM_PROCESSO_CNJ'].astype(str).str.split(")", n=2 , expand = True)
	df_ba_errados ['NUM_PROCESSO_CNJ'] = cortes[0]
	df_ba_errados ['ASSUNTO'] = cortes[1]



	df_ba = pd.concat([df_ba,df_ba_errados], ignore_index=True)
	cortes_2 = df_ba['NUM_PROCESSO_CNJ'].astype(str).str.split(" ", n=2 , expand = True)
	df_ba['NUM_PROCESSO_CNJ'] = cortes_2[0].astype(str).str.strip()


	df_ba['ANO'] = df_ba['ANO'].astype(str).str.replace(".","")
	df_ba['ANO'] = df_ba['ANO'].astype(int)

	df_ba['DATA_MOVIMENTO'] = df_ba['DATA_MOVIMENTO'].astype(str).str.split(" ", expand = True)[1]



	df_ba.rename(columns={'NUM_PROCESSO_CNJ': 'Número do Processo', 
		'DATA_MOVIMENTO': 'Data da Sentença', "COMARCA": "Comarca", "VARA": "Vara", 
		'ANO':'Ano'},
	 inplace = True)



	# ajuste no número do processo

	fim = df_ba['Número do Processo'].astype(str).str[-4:]
	est = df_ba['Número do Processo'].astype(str).str[-6:-4]
	just = df_ba['Número do Processo'].astype(str).str[-7]
	ano_aj = df_ba['Número do Processo'].astype(str).str[-11:-7]
	cod = df_ba['Número do Processo'].astype(str).str[-13:-11]
	rest = df_ba['Número do Processo'].astype(str).str[:-13]

	df_ba['Número do Processo'] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_dados = ano_aj.astype(int)
	df_ba["Ano"] = ano_dados
	df_filter = df_ba["Ano"] >= 2017
	df_ba = df_ba[df_filter]


	df_ba ["Estado"] = "BA"
	df_ba ["Origem"] = ""
	df_ba ["Competência"] = "Estadual"
	df_ba ["Planilha"] = 'TJBA_1'
	df_ba ["Data da Distribuição"] = None


	dados = df_ba


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]
	print(dados)
	print(dados.info())


	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_BA.xlsx", index = False)




######################################################################################################################

def dados_CE():

	dados_pdf =[]
	nome_planilha = []
	for k in range(1,10):
		cmn_arq = ".\Planilhas tribunais\TJCE_"+str(k)+".txt"
		arquivo = open(cmn_arq, encoding= "utf-8")
		texto = arquivo.readlines()
		for linha in texto:
			if len(linha) > 1:
				partes = linha.split("[")
				quebra = partes[1].split("]")
				num = quebra[0].strip()
				num = re.sub(r'\D',"",num)
				# print(num)
				dados_pdf.append(num)
				nome_planilha.append("TJCE_"+str(k))

	dados_1 = pd.DataFrame(columns =["Número do Processo","Planilha"])

	dados_1 ["Número do Processo"] = dados_pdf
	dados_1 ["Planilha"] = nome_planilha

	dados_1["Número do Processo"] = dados_1["Número do Processo"].astype(str).str.replace(".","")
	dados_1["Número do Processo"] = dados_1["Número do Processo"].astype(str).str.replace("-","")

	dados_1["Comarca"] = None
	dados_1["Vara"] = None
	dados_1["Data da Distribuição"] = None
	dados_1["Data da Sentença"] = None
	dados_1["Origem"] = 'SAJ'


	# print(dados_1)

	# print(dados_1["Número do Processo"])
	# z = input("")


	####################

	dados_pdf =[]
	nome_planilha= []
	for n in range(10,25):

		cmn_arq = ".\Planilhas tribunais\TJCE_"+str(n)+".pdf"
		# print(cmn_arq)

		with fitz.open(cmn_arq) as arquivo:
			for pagina in arquivo:
				blocks = pagina.get_text('dict')['blocks']
				for o in range(len(blocks)):
					txt_block = []
					try:
						lines = blocks[o]["lines"]
						for x in range(len(lines)):
							spans = lines[x]["spans"]
							for u in spans:
								if len(u['text']) > 5:
									if re.match(r'\d{5,7}.+',u['text'].strip()) or re.match(r'\d\.\d\..+',u['text'].strip()):
										# print("-------------")
										# print(u['text'].strip())
										txt_block.append(u['text'].strip())
										
									
									if len(txt_block) > 1:	
										num = str(txt_block[0]+txt_block[1])
										num = re.sub(r'\D',"",num)
										dados_pdf.append(num)
										nome_planilha.append("TJCE_"+str(n))		
					except:
						pass

	dados_2 = pd.DataFrame(columns =["Número do Processo","Planilha"])

	dados_2 ["Número do Processo"] = dados_pdf
	dados_2 ["Planilha"] = nome_planilha

	dados_2["Número do Processo"] = dados_2["Número do Processo"].astype(str).str.replace(".","")
	dados_2["Número do Processo"] = dados_2["Número do Processo"].astype(str).str.replace("-","")

	dados_2["Comarca"] = None
	dados_2["Vara"] = None
	dados_2["Data da Distribuição"] = None
	dados_2["Data da Sentença"] = None
	dados_2["Origem"] = 'SAJ'
			

	# print(dados_2)
	# print(dados_2["Número do Processo"])


	###############################

	dados_pdf =[]
	nome_planilha = []
	for j in range(200,208):
		cmn_arq = ".\Planilhas tribunais\TJCE_"+str(j)+".pdf"

		
		dados =[]
		with fitz.open(cmn_arq) as arquivo:
			for pagina in arquivo:
				blocks = pagina.get_text('dict')['blocks']
				for o in range(len(blocks)):
					# print("estamos no bloco", o)
					try:
						lines = blocks[o]["lines"]
						for x in range(len(lines)):
							spans = lines[x]["spans"]	
							for u in spans:
								if re.match(r'\d{5,7}.+',u['text'].strip()):
									# print(u['text'])
									# z = input("")
									num = u['text']
									num  = re.sub(r'\D',"",num)
									dados_pdf.append(num)
									nome_planilha.append("TJCE_"+str(j))
					except:
						pass


	dados_3 = pd.DataFrame(columns =["Número do Processo","Planilha"])

	dados_3 ["Número do Processo"] = dados_pdf
	dados_3 ["Planilha"] = nome_planilha

	idx = dados_3[dados_3 ["Número do Processo"] == '0001750'].index.to_list()

	# print("o index é", idx)

	dados_3.drop(idx, inplace= True)
	

	dados_3["Comarca"] = None
	dados_3["Vara"] = None
	dados_3["Data da Distribuição"] = None
	dados_3["Data da Sentença"] = None
	dados_3["Origem"] = 'SEEU'
			
	# print(dados_3)
	# dados_3.to_excel("dados_3.xlsx", index = False)

	##################
	planilha = pd.read_excel(".\Planilhas tribunais\TJCE_100.xlsx", engine ='openpyxl', dtype="object" )
	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJCE_101.xlsx", engine ='openpyxl', dtype="object" )
	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJCE_102.xlsx", engine ='openpyxl', dtype="object" )
	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJCE_103.xlsx", engine ='openpyxl', dtype="object" )
	planilha_4 = pd.read_excel(".\Planilhas tribunais\TJCE_104.xlsx", engine ='openpyxl', dtype="object" )
	
	p_100 = planilha[["Processo","Vara"]]
	p_100["Planilha"] = "TJCE_100"
	p_101 = planilha_1[["Processo","Vara"]]
	p_101["Planilha"] = "TJCE_101"
	p_102 = planilha_2[["Processo","Vara"]]
	p_102["Planilha"] = "TJCE_102"
	p_103 = planilha_3[["Processo","Vara"]]
	p_103["Planilha"] = "TJCE_103"
	p_104 = planilha_3[["Processo","Vara"]]
	p_104["Planilha"] = "TJCE_104"

	dados_4 = pd.concat([p_100,p_101,p_102,p_103,p_104])

	dados_4.rename(columns={"Processo":'Número do Processo'}, inplace = True)


	dados_4["Competência"] = "Estadual"

	dados_4["Comarca"] = None
	dados_4["Vara"] = None
	dados_4["Data da Distribuição"] = None
	dados_4["Data da Sentença"] = None
	dados_4["Origem"] = None


	# print(dados_4)


	#########################

	dados = pd.concat([dados_1, dados_2, dados_3, dados_4])

	# dados.to_excel("dados_teste.xlsx", index = False)

	# print(dados["Número do Processo"])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)


	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("","")

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "CE"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Competência"] = "Estadual"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.loc[dados.Planilha == "TJCE_203", "Origem"] = "SAJ"

	idx = dados.loc[dados.Ano == 8201].index

	dados.drop(idx, inplace= True)

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_CE.xlsx", index = False)
			



#################################                  ES               ##################################################

def dados_ES():

	dados = pd.read_excel(".\Planilhas tribunais\TJES_1.xlsx", engine ='openpyxl')


	dados.rename(columns={'DS_PROCES': 'Número do Processo', 
		'DT_JULGAMENTO': 'Data da Sentença', "COMARCA": "Comarca", "VARA": "Vara", 
		'ANO':'Ano', 'DT_DISTRIBUICAO': 'Data da Distribuição'},
	 inplace = True)

	dados['Vara'] = dados['Vara'].astype(str).str.split("-", expand = True)[1].str.strip()

	ano = dados['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	dados ["Ano"] = ano.astype(int)

	dados["Estado"] = "ES"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados ["Origem"] = None
	dados ["Competência"] = "Estadual"
	dados ["Planilha"] = 'TJES_1'


	dados["Comarca"] = dados["Comarca"].replace(to_replace = r"(?i)comarca da|(?i)comarca de", value = '', regex = True).str.strip()

	anos_distr = dados["Data da Distribuição"].str[-2:]

	dados['Data da Distribuição'] = (dados['Data da Distribuição'].str[:-2]+"20"+anos_distr).replace(to_replace = r"/", value = '-', regex = True)


	anos_sent = dados["Data da Sentença"].str[-2:]

	dados["Data da Sentença"] = (dados["Data da Sentença"].str[:-2]+"20"+anos_sent).replace(to_replace = r"/", value = '-', regex = True)


	# dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'], format = "%d-%m-%Y")
	# # dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	# dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	# dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]
	

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)
	
	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_ES.xlsx", index = False)



#################################                  GO              ##################################################


def dados_GO():


	planilha = pd.read_excel(".\Planilhas tribunais\TJGO_1.xlsx", engine ='openpyxl', dtype="object", sheet_name="ouvidoria227.162.100.962v2" )
	dados = planilha[["comarca","processo","data_distribuicao","serventia"]]


	dados.rename(columns={'comarca': 'Comarca', 'processo': 'Número do Processo', 'serventia':"Vara", 
		'data_distribuicao':'Data da Distribuição'},
	 inplace = True)


	dados["Planilha"] = "TJGO_1"


	dados["Origem"] = None


	dados["Competência"] = "Estadual"

	# print(dados['Data da Distribuição'])

	dados['Data da Sentença'] = None

	#################################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TJGO_1.xlsx", engine ='openpyxl', dtype="object", sheet_name="ouvidoria227.162.100.962" )
	dados_2 = planilha[["comarca","processo","data_distribuicao","serventia"]]


	dados_2.rename(columns={'comarca': 'Comarca', 'processo': 'Número do Processo', 'serventia':"Vara", 
		'data_distribuicao':'Data da Distribuição'},
	 inplace = True)


	dados_2["Planilha"] = "TJGO_1_2"


	dados_2["Origem"] = None


	dados_2["Competência"] = "Estadual"


	# print(dados['Data da Distribuição'])

	dados_2['Data da Sentença'] = None


	#######################################################################

	cmn_arq = ".\Planilhas tribunais\TJGO_2.pdf"

	
	dados_pdf =[]
	with fitz.open(cmn_arq) as arquivo:
		for pagina in arquivo:
			blocks = pagina.get_text('dict')['blocks']
			for o in range(len(blocks)):
				try:
					lines = blocks[o]["lines"]
					txt_block = []
					for x in range(len(lines)):
						spans = lines[x]["spans"]
						for u in spans:
							txt_block.append(u['text'])
					if len(txt_block) > 3:
						dados_pdf.append(txt_block)
				except:
					pass

	del(dados_pdf[-2:])	

	lista_num =[]
	for item in dados_pdf:
		part = item
		for num in part:
			lista_num.append(num)



	dados_3 = pd.DataFrame({"Número do Processo":lista_num})

	dados_3["Comarca"] = None
	dados_3["Vara"] = None
	dados_3["Data da Distribuição"] = None
	dados_3["Data da Sentença"] = None
	dados_3["Ano"] = None
	dados_3["Estado"] = 'GO'
	dados_3["Competência"] = 'Estadual'
	dados_3['Planilha'] = "TJGO_2"
	dados_3["Origem"] = None


	######################################################################
	dados =pd.concat([dados, dados_2, dados_3])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "GO"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")



	dados["Vara"] = dados["Vara"].replace(to_replace = r"(?i)Ju(í|i)zo d(a|o)|-.+", value = '', regex = True).str.strip()

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)
	

	print(dados)
	print(dados.info())



	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_GO.xlsx", index = False)





#################################                  4 - MA               ##################################################


def dados_MA():

	planilha = pd.read_excel(".\Planilhas tribunais\TJMA_1.xlsx", engine ='openpyxl')

	dados = planilha[["Sistema","Número Único","Comarca","Vara", "Data Abertura","Data do Movimento"]]

	# print(dados ["Data do Movimento"])

	# dados["Data Abertura"] = dados["Data Abertura"].astype(str).str.split(" ", n=1, expand = True)[0]
	# dados["Data do Movimento"] = dados["Data do Movimento"].astype(str).str.split(" ", n=1, expand = True)[0]
	ano = dados["Número Único"].astype(str).str.split(".", expand = True)[1]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MA"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados.rename(columns={'Número Único': 'Número do Processo','Sistema': 'Origem', 'Data do Movimento': 'Data da Sentença',
		'Data Abertura':'Data da Distribuição'}, 
		inplace = True)

	dados["Competência"] = "Estadual"

	dados["Planilha"] = "TJMA_1"



	###################################

	planilha = pd.read_excel(".\Planilhas tribunais\TJMA_2.xlsx", engine ='openpyxl', dtype="object" )

	
	dados_2 = planilha[["Sistema","Número Único","Comarca","Vara","Data do Movimento","Data Abertura"]]


	dados_2.rename(columns={"Número Único": 'Número do Processo', "Sistema":"Origem","Data do Movimento":"Data da Sentença",
		'Data Abertura':'Data da Distribuição'},
	 inplace = True)


	dados_2["Planilha"] = "TJMA_2"

	dados_2["Competência"] = "Estadual"




	#############################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TJMA_3.xlsx", engine ='openpyxl', dtype="object" )

	
	dados_3 = planilha[["Sistema","Número","Comarca","Vara","Data do movimento","Data de distribuição"]]


	dados_3.rename(columns={"Número": 'Número do Processo', "Sistema":"Origem","Data do movimento":"Data da Sentença",
		'Data de distribuição':'Data da Distribuição'},
	 inplace = True)


	dados_3["Planilha"] = "TJMA_3"

	dados_3["Competência"] = "Estadual"



	###############################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TJMA_4.xlsx", engine ='openpyxl', dtype="object" )

	
	dados_4 = planilha[["Sistema","Número","Comarca","Vara","Data do movimento","Data de distribuição"]]


	dados_4.rename(columns={"Número": 'Número do Processo', "Sistema":"Origem","Data do movimento":"Data da Sentença",
		'Data de distribuição':'Data da Distribuição'},
	 inplace = True)


	dados_4["Planilha"] = "TJMA_4"

	dados_4["Competência"] = "Estadual"




	#############################################################

	dados = pd.concat([dados,dados_2,dados_3, dados_4])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "MA"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Comarca"] = dados["Comarca"].replace(to_replace = r"(?i)Ju(í|i)zo d(a|o)|-.+", value = '', regex = True).str.strip()


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]


	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MA.xlsx", index = False)





#################################                 5 - MG               ##################################################


def dados_MG():

	planilha_1 = pd.read_excel(".\Planilhas tribunais\TJMG_1.xlsx", engine ='openpyxl')
	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJMG_2.xlsx", engine ='openpyxl')
	planilha_3 = pd.read_excel(".\Planilhas tribunais\TJMG_3.xlsx", engine ='openpyxl')

	dados_1 = planilha_1[["Nº do Feito Único","Comarca","Vara","Origem dos Dados","Data da Distribuição","Data Sentença"]]
	dados_1["Planilha"] = "TJMG_1"
	dados_2 = planilha_2[["Nº do Feito Único","Comarca","Vara","Origem dos Dados","Data da Distribuição","Data Sentença"]]
	dados_2["Planilha"] = "TJMG_2"
	dados_3 = planilha_3[["Nº do Feito Único","Comarca","Vara","Origem dos Dados","Data da Distribuição","Data Sentença"]]
	dados_3["Planilha"] = "TJMG_3"
	

	dados = pd.concat([dados_1,dados_2,dados_3])


	dados.rename(columns={'Nº do Feito Único': 'Número do Processo','Origem dos Dados': 'Origem', 'Data Sentença': 'Data da Sentença'}, 
		inplace = True)


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano = dados["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MG"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados["Competência"] = "Estadual"


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]


	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)
	
	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MG.xlsx", index = False)







#################################                 6 - MS              ##################################################




#Mandou só as quantidades, não mandou os dados


#################################                 7 - MT               ##################################################


def dados_MT():

	planilha = pd.read_excel(".\Planilhas tribunais\TJMT_1.xlsx", engine ='openpyxl')

	dados = planilha


	dados.rename(columns={'NumeroUnico': 'Número do Processo', 'DataDecisao': 'Data da Sentença','Lotacao':'Vara',
		'Data_Inicio_Tramite':'Data da Distribuição'}, 
		inplace = True)
	

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	ano = dados['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "MT"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	
	dados["Competência"] = "Estadual"
	


	dados["Planilha"] = 'TJMT_1'

	dados["Origem"] = None

	#################################################

	dados_2 = pd.read_excel(".\Planilhas tribunais\TJMT_2.xlsx", engine ='openpyxl')


	dados_2.rename(columns={'NumeroUnico': 'Número do Processo', 'DataExtincao': 'Data da Sentença','Lotacao':'Vara',
		'DataDistribuicao':'Data da Distribuição'}, 
		inplace = True)
	

	dados_2['Data da Distribuição'] = pd.to_datetime(dados_2['Data da Distribuição'])
	dados_2['Data da Distribuição'] = dados_2['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados_2["Data da Sentença"] = pd.to_datetime(dados_2["Data da Sentença"])
	dados_2["Data da Sentença"] = dados_2["Data da Sentença"].dt.strftime("%d-%m-%Y")


	ano_2 = dados_2['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	dados_2["Ano"] = ano_2.astype(int)
	dados_2["Estado"] = "MT"

	df_filter_2 = dados_2["Ano"] >= 2017
	dados_2 = dados_2[df_filter_2]

	
	dados_2["Competência"] = "Estadual"
	

	dados_2["Planilha"] = 'TJMT_2'

	dados_2["Origem"] = None


	##################################################

	dados = pd.concat([dados,dados_2])


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_MT.xlsx", index = False)





#################################                 8 - PA               ##################################################

def dados_PA():

	planilha = pd.read_excel(".\Planilhas tribunais\TJPA_1.xlsx", engine ='openpyxl', sheet_name = 'Select select')

	dados = planilha

	# print(dados)
	# z= input("")

	dados["DATA DISTRIBUIÇÃO"] = dados["DATA DISTRIBUIÇÃO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')
	dados["DATA EXTINÇÃO PUNIBILIDADE"] = dados["DATA EXTINÇÃO PUNIBILIDADE"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')


	dados.rename(columns={'PROCESSO': 'Número do Processo', 'DATA EXTINÇÃO PUNIBILIDADE': 'Data da Sentença','UNIDADE SENTENÇA':'Vara',
		'DATA DISTRIBUIÇÃO':'Data da Distribuição', 'COMARCA': 'Comarca'}, 
		inplace = True)


	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano = dados['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "PA"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	
	dados["Competência"] = "Estadual"

	dados["Planilha"] = "TJPA_1"

	dados["Origem"] = None


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	##################################################

	dados_2 = pd.read_excel(".\Planilhas tribunais\TJPA_2.xlsx", engine ='openpyxl')


	# print(dados)
	# z= input("")

	dados_2["DATA DISTRIBUIÇÃO"] = dados_2["DATA_DISTRIBUICAO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')
	dados_2["DATA_DECISAO"] = dados_2["DATA_DECISAO"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/",'-')


	dados_2.rename(columns={'PROCESSO': 'Número do Processo', 'DATA_DECISAO': 'Data da Sentença','UNIDADE':'Vara',
		'DATA DISTRIBUIÇÃO':'Data da Distribuição', 'COMARCA': 'Comarca'}, 
		inplace = True)


	fim = dados_2["Número do Processo"].astype(str).str[-4:]
	est = dados_2["Número do Processo"].astype(str).str[-6:-4]
	just = dados_2["Número do Processo"].astype(str).str[-7]
	ano_aj = dados_2["Número do Processo"].astype(str).str[-11:-7]
	cod = dados_2["Número do Processo"].astype(str).str[-13:-11]
	rest = dados_2["Número do Processo"].astype(str).str[:-13]

	dados_2["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_2 = dados_2['Número do Processo'].astype(str).str.split(".", expand = True)[1]

	dados_2["Ano"] = ano_2.astype(int)
	dados_2["Estado"] = "PA"

	df_filter_2 = dados_2 ["Ano"] >= 2017
	dados_2 = dados_2[df_filter_2]

	
	dados_2["Competência"] = "Estadual"

	dados_2["Planilha"] = "TJPA_2"

	dados_2["Origem"] = None


	dados_2['Data da Distribuição'] = pd.to_datetime(dados_2['Data da Distribuição'])
	dados_2['Data da Distribuição'] = dados_2['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados_2["Data da Sentença"] = pd.to_datetime(dados_2["Data da Sentença"])
	dados_2["Data da Sentença"] = dados_2["Data da Sentença"].dt.strftime("%d-%m-%Y")


	#################################################

	dados = pd.concat([dados,dados_2])


	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())
	

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PA.xlsx", index = False)





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

	dados["Origem"] = None

	dados["Data da Distribuição"] = None


	dados["Competência"] = "Estadual"
	dados["Estado"] = "PB"

	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.replace("/","-")


	dados["Planilha"] = "TJPB_1"

	ano = dados["Número do Processo"].astype(str).str.split(".", expand = True)[1]

	dados["Ano"] = ano.astype(int)

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PB.xlsx", index = False)




#################################                 10 - PE              ##################################################

def dados_PE():

	planilha = pd.read_excel(".\Planilhas tribunais\TJPE_1.xlsx", engine ='openpyxl')

	dados = planilha[['ORIGEM','UNIDADE JUDICIÁRIA','NPU','DATA DA DISTRIBUIÇÃO','DATA DO JULGAMENTO']]


	dados.rename(columns={'ORIGEM':'Origem','NPU': 'Número do Processo', 'DATA DO JULGAMENTO': 'Data da Sentença','UNIDADE JUDICIÁRIA':'Vara',
		'DATA DA DISTRIBUIÇÃO':'Data da Distribuição'}, 
		inplace = True)


	dados["Competência"] = "Estadual"

	dados["Estado"] = "PE"

	dados["Planilha"] = 'TJPE_1'


	dados["Comarca"] = dados["Vara"].astype(str).str.split("\sDA\s", expand = True)[1]


	dados.loc[dados.Comarca != "CAPITAL", "Comarca"] = dados["Vara"].astype(str).str.split("\sCOMARCA DE\s", expand = True)[1]

	# print(dados["Comarca"])
	
	ano_aj = dados ["Número do Processo"].astype(str).str.split(".",expand = True)[1].str.strip()

	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.replace("/","-")
	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.replace("/","-").str.split(" ", n=1, expand = True)[0]


	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)
	

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PE.xlsx", index = False)




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

	dados["Origem"] = None

	dados["Planilha"] = 'TJPI_1'

	dados.drop(columns =["Movimento"], inplace = True)

	dados["Competência"] = "Estadual"




		##########################

	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJPI_2.xlsx", engine ='openpyxl')

	dados_2 = planilha_2


	dados_2["Data distribuição"] = dados_2["Data distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados_2["Data movimentação"] = dados_2["Data movimentação"].astype(str).str.split(" ", n=1, expand = True)[0]
	
	dados_2["Ano"] = dados_2["Ano"].astype(int)
	dados_2["Estado"] = "PI"

	dados_2["Origem"] = None

	df_filter = dados_2["Ano"] >= 2017
	dados_2 = dados_2[df_filter]


	dados_2["Planilha"] = 'TJPI_2'


	dados_2.rename(columns={'Processo': 'Número do Processo', 'Data movimentação': 'Data da Sentença','Unidade':'Vara',
		'Data distribuição':'Data da Distribuição'}, 
		inplace = True)


	dados_2.drop(columns =["Movimento descrição"], inplace = True)

	dados_2["Competência"] = "Estadual"

	##########################################################################################

	planilha_3 = pd.read_csv(".\Planilhas tribunais\TJPI_3.csv", sep =";")

	dados_3 = planilha_3

	# print(dados_3)
	# z= input("")


	dados_3["data_movimentacao"] = dados_3["data_movimentacao"].astype(str).str.split(" ", n=1, expand = True)[0].replace("/","-")
	dados_3["data_distribuicao"] = dados_3["data_distribuicao"].astype(str).str.split(" ", n=1, expand = True)[0].replace("/","-")
	
	dados_3["Ano"] = dados_3["ano"].astype(int)
	dados_3["Estado"] = "PI"

	dados_3["Origem"] = None

	df_filter = dados_3["Ano"] >= 2017
	dados_3 = dados_3[df_filter]


	dados_3["Planilha"] = 'TJPI_3'


	dados_3.rename(columns={'numero_unico': 'Número do Processo', 'data_movimentacao': 'Data da Sentença','orgao_julgador_nome':'Vara',
		'data_distribuicao':'Data da Distribuição'}, 
		inplace = True)


	dados_3.drop(columns =["movimento_descricao","ano"], inplace = True)

	dados_3["Competência"] = "Estadual"



	############################################################################################



	dados = pd.concat([dados,dados_2,dados_3])

	dados ["Comarca"] = dados["Vara"].astype(str).str.split("DE|de",expand = True)[1].str.strip()


	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PI.xlsx", index = False)





#################################                 11 - PR              ##################################################


def dados_PR():

	dados = pd.read_excel(".\Planilhas tribunais\TJPR_1.xlsx", engine ='openpyxl')


	dados["Data de Distribuição"] = dados["Data de Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	dados["Data do Movimento 1042"] = dados["Data do Movimento 1042"].astype(str).str.split(" ", n=1, expand = True)[0]


	dados.rename(columns={'Número Único': 'Número do Processo', 'Data do Movimento 1042': 'Data da Sentença',
		'Data de Distribuição':'Data da Distribuição'}, 
		inplace = True)


	dados["Planilha"] = 'TJPR_1'


	#####################


	planilha = pd.read_excel(".\Planilhas tribunais\TJPR_2.xlsx", engine ='openpyxl')


	dados_2 = planilha [['Número Único','Comarca']]

	dados_2.rename(columns={'Número Único': 'Número do Processo'}, inplace = True)
	
	dados_2["Vara"] = None
	dados_2["Data da Distribuição"] = None
	dados_2["Data da Sentença"] = None
	dados_2["Origem"] = None

	dados_2["Planilha"] = 'TJPR_2'


	###################

	planilha = pd.read_excel(".\Planilhas tribunais\TJPR_3.xlsx", engine ='openpyxl')


	dados_3 = planilha [['Número Único','Comarca']]

	dados_3.rename(columns={'Número Único': 'Número do Processo'}, inplace = True)
	
	dados_3["Vara"] = None
	dados_3["Data da Distribuição"] = None
	dados_3["Data da Sentença"] = None
	dados_3["Origem"] = None

	dados_3["Planilha"] = 'TJPR_3'


	###################

	dados = pd.concat([dados,dados_2,dados_3])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano = dados["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "PR"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados["Origem"] = None


	dados["Competência"] = "Estadual"


	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")



	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)


	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_PR.xlsx", index = False)



#########################################    RN  #########################################################################


def dados_RN():
	
	dados = pd.read_excel(".\Planilhas tribunais\TJRN_1.xlsx", engine ='openpyxl')

	dados.rename(columns={"SISTEMA": "Origem", 'PROCESSO': 'Número do Processo', 'COMARCA':'Comarca', "UNIDADE":"Vara",
	'DATA DISTRIBUIÇÃO':'Data da Distribuição', 'MOVIMENTO EXTINÇÃO PUNIBILIDADE DATA':"Data da Sentença"}, 
	inplace = True)

	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")


	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano = dados["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados["Planilha"] = 'TJRN_1'

	dados["Ano"] = ano.astype(int)
	dados["Estado"] = "RN"

	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados["Competência"] = "Estadual"



	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]


	dados["Comarca"] = dados["Comarca"].replace(to_replace = r"TJRN - Comarca de|TJRN -  Comarca de", value = '', regex = True).str.strip()
	dados["Vara"] = dados["Vara"].replace(to_replace = r"TJRN -|-.+", value = '', regex = True).str.strip()

	
	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	print(dados)
	print(dados.info())



	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_RN.xlsx", index = False)




#################################                 12 - RJ             ##################################################

# não tem nada




#################################                 13 - RO             ##################################################

def dados_RO():

	''' dúvidas: Origem dos dados do RO? Quais são do SEEU? sabemos?? '''


	planilha = pd.read_excel(".\Planilhas tribunais\TJRO_1.xlsx", engine ='openpyxl')

	dados = planilha

	ano = dados["Número Processo"].astype(str).str.split(".", expand = True)[1]

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


	dados["Planilha"] = "TJRO_1"

	dados["Origem"] = None

	# print(dados)

	#########################################################################

	planilha_2 = pd.read_excel(".\Planilhas tribunais\TJRO_2.xlsx", engine ='openpyxl')

	dados_2 = planilha_2[['NR PROCESSO','COMARCA',"VARA",'DATA DISTRIBUICAO','DATA MOVIMENTO EXTINCAO']]

	dados_2.rename(columns={'NR PROCESSO': 'Número do Processo', 'COMARCA':'Comarca', "VARA":"Vara",
	'DATA DISTRIBUICAO':'Data da Distribuição', 'DATA MOVIMENTO EXTINCAO':"Data da Sentença"}, 
	inplace = True)

	

	indexes = dados_2[dados_2['Número do Processo'] == 'SEGREDO DE JUSTIÇA' ].index
	dados_2.drop(indexes, inplace=True)


	ano_2 = dados_2["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados_2["Planilha"] = 'TJRO_2'

	dados_2["Ano"] = ano_2.astype(int)
	dados_2["Estado"] = "RO"

	df_filter = dados_2["Ano"] >= 2017
	dados_2 = dados_2[df_filter]


	dados_2["Competência"] = "Estadual"


	dados_2["Origem"] = None

	#####################################################

	dados_3 = pd.read_excel(".\Planilhas tribunais\TJRO_3.xlsx", engine ='openpyxl')

	dados_3.rename(columns={'NR_PROCESSO': 'Número do Processo'}, inplace = True)


	ano_3 = dados_3["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados_3["Ano"] = ano_3.astype(int)

	df_filter = dados_3["Ano"] >= 2017
	dados_3 = dados_3[df_filter]

	dados_3["Comarca"] = None
	dados_3["Vara"] = None
	dados_3["Data da Distribuição"] = None
	dados_3["Data da Sentença"] = None
	dados_3["Estado"] = 'RO'
	dados_3["Competência"] = 'Estadual'
	dados_3['Planilha'] = "TJRO_3"
	dados_3["Origem"] = None


	##############################################
	

	dados = pd.concat([dados,dados_2,dados_3])


	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_RO.xlsx", index = False)




#################################                 14 - RR             ##################################################

def dados_RR():

#ver depois com a Naty...mandou de feminicídio??? Primeira leva


	dados_2 = pd.read_excel(".\Planilhas tribunais\TJRR_1.xlsx", engine ='openpyxl')


	dados_2.rename(columns={'PROCESSO': 'Número do Processo', 'COMARCA':'Comarca', "UNIDADE JUDICIAL":"Vara",
	'DISTRIBUIÇÃO':'Data da Distribuição', 'DATA DA SENTENÇA':"Data da Sentença", 'SISTEMA':"Origem"}, 
	inplace = True)



	ano_2 = dados_2["Número do Processo"].astype(str).str.split(".", expand = True)[1]


	dados_2["Planilha"] = 'TJRR_1'

	dados_2["Ano"] = ano_2.astype(int)
	dados_2["Estado"] = "RR"

	df_filter = dados_2["Ano"] >= 2017
	dados_2 = dados_2[df_filter]


	dados_2["Competência"] = "Estadual"



	dados = dados_2[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência", 'Planilha']]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	
	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_RR.xlsx", index = False)




#################################                 15 - RS             ##################################################

# não tem nada



#################################                 15 - SE             ##################################################

def dados_SE():
	cmn_arq = ".\Planilhas tribunais\TJSE_1.pdf"

	
	dados_pdf =[]
	with fitz.open(cmn_arq) as arquivo:
		for pagina in arquivo:
			blocks = pagina.get_text('dict')['blocks']
			for o in range(len(blocks)):
				try:
					lines = blocks[o]["lines"]
					txt_block = []
					for x in range(len(lines)):
						spans = lines[x]["spans"]
						for u in spans:
							txt_block.append(u['text'])
					if len(txt_block) > 3:
						dados_pdf.append(txt_block)
				except:
					pass


	del(dados_pdf[0])
		
	df_se = pd.DataFrame(columns =["Número do Processo","NADA",'NADA_2',"Data da Distribuição","Data da Sentença", "Ano", "Vara", "Comarca"])

	for k in range(len(dados_pdf)):
		partes = dados_pdf[k][6].split("-")

		if len(partes) == 3:
			del(dados_pdf[k][6])
			dados_pdf[k].insert(6,partes[1])
			dados_pdf[k].insert(7,"")
			df_se.loc[k] = dados_pdf[k]
		elif len(partes) == 2:
			del(dados_pdf[k][6])
			dados_pdf[k].insert(6,"")
			dados_pdf[k].insert(7,partes[1])
			df_se.loc[k] = dados_pdf[k]

	df_se.drop(columns=["NADA",'NADA_2'], inplace = True)


	df_se['Comarca'] = df_se['Comarca'].str.strip()

	df_se.loc[df_se['Comarca'].str.contains("Vara", case= False) == True , "Vara"] = df_se["Comarca"]
	df_se.loc[df_se['Comarca'].str.contains("Vara", case= False) == True , "Comarca"] = ''

	df_se.loc[(df_se['Vara'].str.contains("Vara de Execução", case= False) == False) &  (df_se['Comarca'] == ""), "Comarca"] = df_se["Vara"].astype(str).str.split("\sde\s",expand = True)[1]

	df_se["Vara"] = df_se["Vara"].astype(str).str.strip()

	df_se["Origem"] = "SEEU"
	df_se["Planilha"] = "TJSE_1"

	################################################################################################################

	cmn_arq = ".\Planilhas tribunais\TJSE_2.pdf" ## é igual a primeira!!!

	
	dados_pdf =[]
	with fitz.open(cmn_arq) as arquivo:
		for pagina in arquivo:
			blocks = pagina.get_text('dict')['blocks']
			for o in range(len(blocks)):
				try:
					lines = blocks[o]["lines"]
					txt_block = []
					for x in range(len(lines)):
						spans = lines[x]["spans"]
						for u in spans:
							txt_block.append(u['text'])
					if len(txt_block) > 3:
						dados_pdf.append(txt_block)
				except:
					pass

	del(dados_pdf[0])
		
	df_se_2 = pd.DataFrame(columns =["Número do Processo","NADA",'NADA_2',"Data da Distribuição","Data da Sentença", "Ano", "Vara", "Comarca"])

	for k in range(len(dados_pdf)):
		partes = dados_pdf[k][6].split("-")

		if len(partes) == 3:
			del(dados_pdf[k][6])
			dados_pdf[k].insert(6,partes[1])
			dados_pdf[k].insert(7,"")
			df_se_2.loc[k] = dados_pdf[k]
		elif len(partes) == 2:
			del(dados_pdf[k][6])
			dados_pdf[k].insert(6,"")
			dados_pdf[k].insert(7,partes[1])
			df_se_2.loc[k] = dados_pdf[k]

	df_se_2.drop(columns=["NADA",'NADA_2'], inplace = True)

	
	df_se_2["Origem"] = "SEEU"
	df_se_2["Planilha"] = "TJSE_2"

	#######################################

	dados = pd.concat([df_se, df_se_2])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "SE"
	dados["Competência"] = "Estadual"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset="Número do Processo", inplace= True)


	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	
	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_SE.xlsx", index = False)




#################################                 16 - SC             ##################################################

# não mandou os números dos processos




#################################                 17 - SP             ##################################################


def dados_SP():

	''' dúvidas: Origem dos dados do SP? Quais são do SEEU? sabemos?? AO que parece todos são do SAJ'''


	planilha = pd.read_excel(".\Planilhas tribunais\TJSP_1.xlsx", engine ='openpyxl')

	dados = planilha[["Número do Processo","Descrição do Foro","Descrição da Vara","Data Distribuição",
	"Data da Extinção da Punibilidade"]]


	# dados["Data Distribuição"] = dados["Data Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]
	# dados["Data da Extinção da Punibilidade"] = dados["Data da Extinção da Punibilidade"].astype(str).str.split(" ", n=1, expand = True)[0]
	

	# ano = dados["Número do Processo"].astype(str).str.split(".", expand = True)[1]

	# dados["Ano"] = ano.astype(int)
	# dados["Estado"] = "SP"

	# df_filter = dados ["Ano"] >= 2017
	# dados = dados[df_filter]

	# dados["Origem"] = "SAJ"


	dados.rename(columns={'Número do Processo': 'Número do Processo', 'Data da Extinção da Punibilidade': 'Data da Sentença','Descrição da Vara':'Vara',
		'Data Distribuição':'Data da Distribuição', 'Descrição do Foro': 'Comarca'}, 
		inplace = True)


	dados["Competência"] = "Estadual"


	dados["Planilha"] = "TJSP_1"

	################################################################


	planilha = pd.read_excel(".\Planilhas tribunais\TJSP_2.xlsx", engine ='openpyxl', dtype="object" )
	planilha_2 = planilha[["Descrição do Foro","Número do Processo","Data Distribuição",'Data da Extinção da Punibilidade',"Descrição da Vara"]]


	planilha_2.rename(columns={'Descrição do Foro': 'Comarca', 'Descrição da Vara':'Vara',
		'Data da Extinção da Punibilidade': 'Data da Sentença', 
		'Data Distribuição':'Data da Distribuição'},
	 inplace = True)

	planilha_2["Planilha"] = "TJSP_2"


	planilha_2["Origem"] = None


	planilha_2["Competência"] = "Estadual"


	planilha_2["Estado"] = 'SP'

	####################################


	planilha = pd.read_excel(".\Planilhas tribunais\TJSP_3.xlsx", engine ='openpyxl', dtype="object" )
	planilha_3 = planilha[["Descrição do Foro","Número do Processo","Data Distribuição",'Data da Extinção da Punibilidade',"Descrição da Vara"]]


	planilha_3.rename(columns={'Descrição do Foro': 'Comarca', 'Descrição da Vara':'Vara',
		'Data da Extinção da Punibilidade': 'Data da Sentença', 
		'Data Distribuição':'Data da Distribuição'},
	 inplace = True)

	planilha_3["Planilha"] = "TJSP_3"


	planilha_3["Origem"] = None


	planilha_3["Competência"] = "Estadual"


	planilha_3["Estado"] = 'SP'


	##############################################################################################

	dados = pd.concat([dados, planilha_2, planilha_3])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "SP"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Vara"] = dados["Vara"].replace(to_replace = r"(?i)Ju(í|i)zo d(a|o)|-.+", value = '', regex = True).str.strip()
	dados["Comarca"] = dados["Comarca"].replace(to_replace = r"(?i)foro d(e|a)", value = '', regex = True).str.strip()


	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado", "Competência","Planilha"]]



	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	
	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_SP.xlsx", index = False)





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


	planilha_1["Planilha"] = "TJTO_1"

	planilha_1["Estado"] = 'TO'

	planilha_1["Competência"] = 'Estadual'


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

	planilha_2["Planilha"] = "TJTO_2"

	planilha_2["Estado"] = 'TO'

	planilha_2["Competência"] = "Estadual"


	# x = planilha_2["Data da Sentença"]

	planilha_2["Data da Sentença"] = pd.to_datetime(planilha_2["Data da Sentença"])
	planilha_2["Data da Sentença"] = planilha_2["Data da Sentença"].dt.strftime("%d-%m-%Y")

	# y = planilha_2["Data da Sentença"]

	# g = x.astype(str).str[8:10]
	# i = y.astype(str).str[:2]

	# h = pd.concat([x,y,g,i], axis =1, keys=["x","y","g","i"])

	# h["Comparação"] = np.where(h['g'] == h['i'], "Igual","Diferente")

	# h = h.dropna()

	# print(h)
	# print(h["Comparação"].value_counts())

	# z = input("pronto!")

	

	########################


	planilha = pd.read_excel(".\Planilhas tribunais\TJTO_3.xlsx", engine ='openpyxl', sheet_name = 'E-proc', dtype="object" )
	planilha_3 = planilha[["Localidade","Processo","Data Distribuíção",'Data do Movimento',"Vara",'Ano']]


	planilha_3.rename(columns={'Localidade': 'Comarca', 'Processo': 'Número do Processo', 
		'Data do Movimento': 'Data da Sentença', 
		'Data Distribuíção':'Data da Distribuição'},
	 inplace = True)


	planilha_3["Data da Distribuição"] = planilha_3["Data da Distribuição"].astype(str).str.replace("/","-")
	planilha_3["Data da Sentença"] = planilha_3["Data da Sentença"].astype(str).str.replace("/","-")

	planilha_3["Planilha"] = "TJTO_3_1"


	planilha_3["Origem"] = "EPROC"


	planilha_3["Competência"] = "Estadual"


	planilha_3["Estado"] = 'TO'


	##############################

	planilha = pd.read_excel(".\Planilhas tribunais\TJTO_3.xlsx", engine ='openpyxl', sheet_name = 'SEEU', dtype="object" )
	planilha_4 = planilha[["Processo",'Ano']]


	planilha_4.rename(columns={'Processo': 'Número do Processo'},
	 inplace = True)



	planilha_4["Planilha"] = "TJTO_3_2"


	planilha_4["Origem"] = "SEEU"


	planilha_4["Competência"] = "Estadual"


	planilha_4["Comarca"] = None
	planilha_4["Vara"] = None
	planilha_4["Data da Distribuição"] = None
	planilha_4["Data da Sentença"] = None
	planilha_4["Estado"] = 'TO'




	#########################################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TJTO_4.xlsx", engine ='openpyxl', dtype="object" )
	planilha_5 = planilha[["Localidade","Processo","Data Distribuíção",'Data do Julgamento ',"Vara"]]


	planilha_5.rename(columns={'Localidade': 'Comarca', 'Processo': 'Número do Processo', 
		'Data do Julgamento ': 'Data da Sentença', 
		'Data Distribuíção':'Data da Distribuição'},
	 inplace = True)


	planilha_5["Data da Distribuição"] = planilha_5["Data da Distribuição"].astype(str).str.replace("/","-")
	planilha_5["Data da Sentença"] = planilha_5["Data da Sentença"].astype(str).str.replace("/","-")

	planilha_5["Planilha"] = "TJTO_4"


	planilha_5["Origem"] = "EPROC"


	planilha_5["Competência"] = "Estadual"

	
	planilha_5["Estado"] = 'TO'



	##################################



	dados = pd.concat([planilha_1, planilha_2, planilha_3, planilha_4, planilha_5])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	dados["Estado"] = "TO"
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Vara"] = dados["Vara"].replace(to_replace = r"(?i)Ju(í|i)zo d(a|o)|-.+", value = '', regex = True).str.strip()

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)


	############# ajuste nos pedaços

	parte_certa = dados.iloc[:1547,:]

	# print(parte_certa)

	# z= input("")

	### fazer o split pelo espaço na dt distr e dt sentença(fazer inversão)
	parte_ajus_dist_1 = dados.iloc[1547:1553,:]

	parte_ajus_dist_1["Data da Sentença"] = parte_ajus_dist_1["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]
	parte_ajus_dist_1["Data da Distribuição"] = parte_ajus_dist_1["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]  



	parte_ajus_dist_1["Data da Sentença"] = pd.to_datetime(parte_ajus_dist_1["Data da Sentença"])
	parte_ajus_dist_1["Data da Sentença"] = parte_ajus_dist_1["Data da Sentença"].dt.strftime("%d-%m-%Y") 



	## fazer o split e inverter ambas as datas
	parte_ajus_dist_2 = dados.iloc[1553:1559,:]


	parte_ajus_dist_2["Data da Sentença"] = parte_ajus_dist_2["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]
	parte_ajus_dist_2["Data da Distribuição"] = parte_ajus_dist_2["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]  


	parte_ajus_dist_2["Data da Sentença"] = pd.to_datetime(parte_ajus_dist_2["Data da Sentença"])
	parte_ajus_dist_2["Data da Sentença"] = parte_ajus_dist_2["Data da Sentença"].dt.strftime("%d-%m-%Y") 
	parte_ajus_dist_2["Data da Distribuição"] = pd.to_datetime(parte_ajus_dist_2["Data da Distribuição"])
	parte_ajus_dist_2["Data da Distribuição"] = parte_ajus_dist_2["Data da Distribuição"].dt.strftime("%d-%m-%Y") 


	## fazer o split pelo espaço na dt distr e dt sentença(fazer inversão)


	parte_ajus_dist_3 = dados.iloc[1569:1579,:]
	
	parte_ajus_dist_3["Data da Sentença"] = parte_ajus_dist_3["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]
	parte_ajus_dist_3["Data da Distribuição"] = parte_ajus_dist_3["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]  
	

	parte_ajus_dist_3["Data da Sentença"] = pd.to_datetime(parte_ajus_dist_3["Data da Sentença"])
	parte_ajus_dist_3["Data da Sentença"] = parte_ajus_dist_3["Data da Sentença"].dt.strftime("%d-%m-%Y")


	## fazer o split e inverter ambas as datas

	parte_ajus_dist_4 = dados.iloc[1579:,:]

	# print(parte_ajus_dist_4)

	# z= input("")
	parte_ajus_dist_4["Data da Sentença"] = parte_ajus_dist_4["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0]
	parte_ajus_dist_4["Data da Distribuição"] = parte_ajus_dist_4["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]  

	parte_ajus_dist_4["Data da Sentença"] = pd.to_datetime(parte_ajus_dist_4["Data da Sentença"])
	parte_ajus_dist_4["Data da Sentença"] = parte_ajus_dist_4["Data da Sentença"].dt.strftime("%d-%m-%Y") 
	parte_ajus_dist_4["Data da Distribuição"] = pd.to_datetime(parte_ajus_dist_4["Data da Distribuição"])
	parte_ajus_dist_4["Data da Distribuição"] = parte_ajus_dist_4["Data da Distribuição"].dt.strftime("%d-%m-%Y") 



	dados = pd.concat([parte_certa,parte_ajus_dist_1,parte_ajus_dist_2,parte_ajus_dist_3,parte_ajus_dist_4])

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TO.xlsx", index = False)








#################################                 19 - TRF 1            ##################################################

# não tem






###################################################################################################################################


def dados_TRF2():

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_2.xlsx", engine ='openpyxl')

	
	dados = planilha[["num_processo","secao","vara","data_distribuicao","data_sentenca"]]

	dados["Estado"] = dados["secao"].replace(to_replace = r"(?i)sj", value = '', regex = True).str.strip()

	dados.rename(columns={"num_processo": 'Número do Processo',"data_sentenca":"Data da Sentença",
		'vara':'Vara','data_distribuicao':'Data da Distribuição'},
	 inplace = True)


	#ajuste e corte da comarca

	dados["Comarca"] = dados["Vara"].astype(str).str.split("\sdo\s", expand = True)[1]

	dados.loc[dados.Comarca != "Rio de Janeiro", "Comarca"] = dados["Vara"].astype(str).str.split("\sde\s", expand = True)[1]


	######

	dados["Tribunal"] = "TRF2"

	dados["Planilha"] = "TRF_2"

	dados["Competência"] = "Federal"


	dados["Origem"] = None

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")

	
	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF2.xlsx", index = False)






#################################                 20 - TRF 3            ##################################################



def dados_TRF3():

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3.xlsx", engine ='openpyxl')

	planilha_1 = planilha[["SEÇÃO","SUBSEÇÃO","DATA DISTRIBUIÇÃO","DATA DA FASE","NUMERO DO PROCESSO"]]

	planilha_1["DATA DISTRIBUIÇÃO"] = planilha_1["DATA DISTRIBUIÇÃO"].astype(str).str.split(" ", n=1, expand = True)[0]
	planilha_1["DATA DA FASE"] = planilha_1["DATA DA FASE"].astype(str).str.split(" ", n=1, expand = True)[0]

	planilha_1["Origem"] = "DW"
	planilha_1["Planilha"] = "TRF_3_1"

	planilha_1["Competência"] = "Federal"


	planilha_1.rename(columns={'SEÇÃO':'Estado','NUMERO DO PROCESSO': 'Número do Processo', 
		'DATA DA FASE': 'Data da Sentença','SUBSEÇÃO': "Comarca", 'DATA DISTRIBUIÇÃO':'Data da Distribuição'}, 
		inplace = True)



	###################### Não temos a data de distribuição dos processos do SEEU #######################




	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3.xlsx", engine ='openpyxl', sheet_name='SEEU _ Morte Agente')

	planilha_2 = planilha[["Seção Judiciária","Subseção Judiciária","Data Fase","Processo"]]


	planilha_2["Data Fase"] = planilha_2["Data Fase"].astype(str).str.split(" ", n=1, expand = True)[0]

	planilha_2["Planilha"] = "TRF_3_1_1"	

	planilha_2["Origem"] = "SEEU"
	
	planilha_2.dropna(inplace = True)

	planilha_2.reset_index(inplace=True)

	planilha_2["Processo"] = planilha_2["Processo"].astype(str).str[:-3]
	

	planilha_2.rename(columns={'Seção Judiciária':'Estado','Processo': 'Número do Processo', 
		'Data Fase': 'Data da Sentença','Subseção Judiciária': "Comarca"}, 
		inplace = True)

	


	#################################################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3_1.xlsx", engine ='openpyxl', sheet_name = 'SEEU_Morte Agente', dtype="object" )
	
	planilha_3 = planilha[["Seção","Subseção","Número do Processo",'Data Fase']]


	planilha_3.rename(columns={'Seção':'Estado','Subseção': 'Comarca',
		'Data Fase': 'Data da Sentença'},
	 inplace = True)


	planilha_3["Planilha"] = "TRF_3_2"


	planilha_3["Origem"] = "SEEU"


	planilha_3["Competência"] = "Federal"



	planilha_3["Comarca"] = planilha_3["Comarca"].str.strip()

	


	##################################################################################

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_3_1.xlsx", engine ='openpyxl', sheet_name = 'DW_Morte Agente', dtype="object" )

	
	dados_4 = planilha[["SEÇÃO","SUBSEÇÃO","NUMERO DO PROCESSO",'DATA DISTRIBUIÇÃO','DATA DA FASE']]


	dados_4.rename(columns={'SEÇÃO':'Estado','SUBSEÇÃO': 'Comarca',
		'DATA DA FASE': 'Data da Sentença', "NUMERO DO PROCESSO": 'Número do Processo',
		'DATA DISTRIBUIÇÃO':'Data da Distribuição'}, inplace= True)


	dados_4["Comarca"] = dados_4["Comarca"].str.strip()

	dados_4["Planilha"] = "TRF_3_2_1"

	dados_4["Competência"] = "Federal"

	dados_4["Origem"] = "DW"



	########################################################################

	dados = pd.concat([planilha_1, planilha_2, planilha_3,dados_4])

	# print(dados)

	dados["Competência"] = "Federal"

	dados["Data da Distribuição"] = np.where(dados["Data da Distribuição"].astype(str).str.strip() == 'nan', "",dados["Data da Distribuição"])



	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	dados["Vara"] = None

	dados["Tribunal"] = "TRF3"	

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)


	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados["Data da Sentença"] = dados["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")


	parte_ajus_dist_1 = dados.iloc[:140,:]


	parte_ajus_dist_1["Data da Distribuição"] = pd.to_datetime(parte_ajus_dist_1["Data da Distribuição"])
	parte_ajus_dist_1["Data da Distribuição"] = parte_ajus_dist_1["Data da Distribuição"].dt.strftime("%d-%m-%Y")
	parte_ajus_dist_1["Data da Sentença"] = pd.to_datetime(parte_ajus_dist_1["Data da Sentença"])
	parte_ajus_dist_1["Data da Sentença"] = parte_ajus_dist_1["Data da Sentença"].dt.strftime("%d-%m-%Y") 
	


	parte_certa = dados.iloc[140:,:]

	dados = pd.concat([parte_ajus_dist_1,parte_certa])

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF3.xlsx", index = False)






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

	try:
		dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	except:
		pass
	try:
		dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")
	except:
		pass	

	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]


	dados["Tribunal"] = "TRF4"

	dados["Planilha"] = "TRF_4"

	dados = dados[["Número do Processo", "Comarca", "Vara", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Tribunal","Competência","Planilha"]]
	# print(dados)

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)



	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")
	dados["Data da Sentença"] = pd.to_datetime(dados["Data da Sentença"])
	dados["Data da Sentença"] = dados["Data da Sentença"].dt.strftime("%d-%m-%Y")


	print(dados)
	print(dados.info())

	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF4.xlsx", index = False)






####################################################################################################################################################

def dados_TRF5():

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_5.xlsx", engine ='openpyxl')

	
	dados = planilha[["Número Processo","Sistema","Serventia","Data 1ª Distribuição","Loc"]]

	dados.rename(columns={"Número Processo": 'Número do Processo',"Loc":"Estado",
		'Serventia':'Vara','Data 1ª Distribuição':'Data da Distribuição'},
	 inplace = True)


	######
	dados["Origem"] = None

	dados["Planilha"] = "TRF_5"

	dados["Competência"] = "Federal"

	dados['Data da Sentença'] = None
	
	dados['Comarca'] = None

	dados["Data da Distribuição"] = dados["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0]


	dados['Data da Distribuição'] = pd.to_datetime(dados['Data da Distribuição'])
	dados['Data da Distribuição'] = dados['Data da Distribuição'].dt.strftime("%d-%m-%Y")




	#################################################


	planilha = pd.read_excel(".\Planilhas tribunais\TRF_5_2.xlsx", engine ='openpyxl')

	
	dados_2 = planilha[["Número Processo","Serventia","Data 1ª Distribuição", "Data Sentença", "Estado"]]

	dados_2.rename(columns={"Número Processo": 'Número do Processo',
		'Serventia':'Vara','Data 1ª Distribuição':'Data da Distribuição', "Data Sentença": "Data da Sentença" },
	 inplace = True)


	######

	dados_2["Origem"] = None

	dados_2["Planilha"] = "TRF_5_2"

	dados_2["Competência"] = "Federal"

	
	dados_2['Comarca'] = None

	dados_2["Data da Distribuição"] = dados_2["Data da Distribuição"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")
	dados_2["Data da Sentença"] = dados_2["Data da Sentença"].astype(str).str.split(" ", n=1, expand = True)[0].str.replace("/","-")


	######################

	planilha = pd.read_excel(".\Planilhas tribunais\TRF_5_3.xlsx", engine ='openpyxl')

	
	dados_3 = planilha[["Número Processo","Serventia","Data 1ª Distribuição", "Data Sentença", "Estado"]]

	dados_3.rename(columns={"Número Processo": 'Número do Processo',
		'Serventia':'Vara','Data 1ª Distribuição':'Data da Distribuição', "Data Sentença": "Data da Sentença" },
	 inplace = True)


	######

	dados_3["Origem"] = None

	dados_3["Planilha"] = "TRF_5_3"

	dados_3["Competência"] = "Federal"

	
	dados_3['Comarca'] = None


	######################

	dados = pd.concat([dados,dados_2, dados_3])

	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace("-","")
	dados['Número do Processo'] = dados['Número do Processo'].astype(str).str.replace(".","")


	dados['Número do Processo'] = dados['Número do Processo'].astype(str)

	# ajuste no número do processo

	fim = dados["Número do Processo"].astype(str).str[-4:]
	est = dados["Número do Processo"].astype(str).str[-6:-4]
	just = dados["Número do Processo"].astype(str).str[-7]
	ano_aj = dados["Número do Processo"].astype(str).str[-11:-7]
	cod = dados["Número do Processo"].astype(str).str[-13:-11]
	rest = dados["Número do Processo"].astype(str).str[:-13]

	dados["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	dados["Ano"] = ano_dados
	df_filter = dados ["Ano"] >= 2017
	dados = dados[df_filter]

	

	dados = dados[["Número do Processo", "Comarca", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano", "Estado","Competência","Planilha"]]

	dados.drop_duplicates(subset = 'Número do Processo', inplace= True)

	dados["Tribunal"] = "TRF5"

	print(dados)
	print(dados.info())


	dir_path = str(os.path.dirname(os.path.realpath(__file__)))
	path = dir_path + f'\planilhas filtradas'
	Path(path).mkdir(parents=True, exist_ok=True)
	dados.to_excel(".\planilhas filtradas\Dados_TRF5.xlsx", index = False)





####################################################################################################################################################


def seleciona_amostra():

	planilha = pd.read_excel("Dados_compilados.xlsx", engine ='openpyxl')

	estados = pd.DataFrame(planilha.groupby(["Tribunal"])["Tribunal"].count())
	estados.columns = ["quantidade"]

	estados = estados.reset_index()
	# print(estados)


	selct = []
	for item in estados["Tribunal"]:
		if re.search('TJMMG|TJMRS|STJ|STM|TJMSP|TRE',item):
			pass
		else:
			selct.append(item)	

	# print(len(selct))

	amostras = pd.DataFrame()
	for trib in selct:
		df_filter = planilha["Tribunal"] == trib
		planilha_1 = planilha[df_filter]
		amostra_trib = planilha_1.sample(10)
		amostras = pd.concat([amostras,amostra_trib])


	
	# print(amostras)

	amostras.to_excel("Amostra_teste_2.xlsx", index = False)



	#################################################################################################################################################


def seleciona_amostra_quali():

	planilha = pd.read_csv("Dados_unificados_JSON_LAI_SEEU.csv",  dtype = 'object')

	# cruzar com os dados das demais planilhas
	lista_planilhas_a_ler = glob.glob("./sorteio_0/*.xlsx")

	dados_planilhas_lidas = []

	todos_dados = pd.DataFrame()
	for planilha_2 in lista_planilhas_a_ler:
	#	print("Nome da planilha a ler: ", planilha)
		dados_planilhas_lidas.append(pd.read_excel(planilha_2, dtype="object", engine ='openpyxl'))

	todos_dados = todos_dados.append(dados_planilhas_lidas, ignore_index=True, sort=False)

	todos_dados.drop_duplicates(subset = 'Número do Processo', inplace= True)
	print(todos_dados)
	# z = input("")	

	print(len(planilha))

	# dropar os dados das demais planilhas
	cont = 0
	lista_numeros = list(todos_dados["Número do Processo"])
	for h in range(len(planilha["Número do Processo"])):
		if planilha["Número do Processo"][h] not in lista_numeros:
			pass
		else:
			planilha.drop([h], inplace = True)
			cont = cont+1			

	print(cont)		
	print(len(planilha))
	# z = input("")		

	planilha = planilha.reset_index()


	# gerar a planilha já sem os sorteados anteriormente na variável planilha

	tribunais = pd.DataFrame(planilha.groupby(["Tribunal"])["Tribunal"].count())
	tribunais.columns = ["quantidade"]

	tribunais = tribunais.reset_index()
	# print(tribunais)
	# a= input("")


	selct = []
	for item in tribunais["Tribunal"]:
		if re.search('TJAC|TJAM|TJAP|TJBA|TJGO|TJPE|TJPR|TJRO|TJRR|TJSE|TJTO|TRF5',item):
			selct.append(item)
		else:
			pass


	manu = ['TJAC','TJAM','TJAP','TJBA']
	vivi = ['TJGO','TJPE','TJPR','TJRO']
	ana = ['TJRR','TJSE','TJTO','TRF5']			



	dfs_manu = []
	dfs_vivi = []
	dfs_ana = []
	for k in range(len(selct)):
		df_filter = planilha["Tribunal"] == selct[k]
		planilha_1 = planilha[df_filter]
		try:
			amostra_trib = planilha_1.sample(194)
		except:
			amostra_trib = planilha_1
		if selct[k] in manu:
			dfs_manu.append(amostra_trib)
			# print(amostra_trib)
		elif selct[k] in vivi:
			dfs_vivi.append(amostra_trib)
			# print(amostra_trib)
		elif selct[k] in ana:
			dfs_ana.append(amostra_trib)
			# print(amostra_trib)

	# a= input("")		


	dfs_manu_rw = []
	dfs_vivi_rw = []
	dfs_ana_rw = []		

	for n in range(len(dfs_manu)):
		# Ana recebe Manu

		amostra_trib = dfs_manu[n].sample(6)
		dfs_ana_rw.append(amostra_trib)

		## vivi recebe Ana

		amostra_trib = dfs_ana[n].sample(6)
		dfs_vivi_rw.append(amostra_trib)


		# manu recebe Vivi
		amostra_trib = dfs_vivi[n].sample(6)
		dfs_manu_rw.append(amostra_trib)



	for z in range(len(dfs_manu)):
		amostras = pd.concat([dfs_manu_rw[z],dfs_manu[z]])
		amostras.to_excel("sorteio_1_amostra_"+str(z+1)+"_Manu.xlsx", index = False)
		print("Manu")
		print(amostras)
		# print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)
		amostras = pd.concat([dfs_vivi_rw[z],dfs_vivi[z]])
		amostras.to_excel("sorteio_1_amostra_"+str(z+1)+"_Vivi.xlsx", index = False)
		print("Vivi")
		# print(amostras)
		print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)
		amostras = pd.concat([dfs_ana_rw[z],dfs_ana[z]])
		amostras.to_excel("sorteio_1_amostra_"+str(z+1)+"_Ana.xlsx", index = False)
		print("Ana")
		# print(amostras)
		print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)

		# a = input("")


#############################################################################################
				
def seleciona_amostra_quali_v_2():

	#### faltou amostrar TRF3 - fazer com a próxima leva

	planilha = pd.read_csv("Dados_unificados_JSON_LAI_SEEU_v2.csv",  dtype = 'object')

	tribunais = pd.DataFrame(planilha.groupby(["Tribunal"])["Tribunal"].count())
	tribunais.columns = ["quantidade"]

	tribunais = tribunais.reset_index()
	# print(tribunais)
	# a= input("")


	selct = []
	for item in tribunais["Tribunal"]:
		if re.search('MG|MA|DF|MS|MT|PA|PI|SP|TRF1',item):
			selct.append(item)
		else:
			pass


	manu = ['TJMG','TJMS','TJPI']
	vivi = ['TJMA','TJMT','TJSP']
	ana = ['TJDFT','TJPA','TRF1']		



	dfs_manu = []
	dfs_vivi = []
	dfs_ana = []
	for k in range(len(selct)):
		df_filter = planilha["Tribunal"] == selct[k]
		planilha_1 = planilha[df_filter]
		amostra_trib = planilha_1.sample(194)
		print(amostra_trib)
		z= input("")
		if selct[k] in manu:
			dfs_manu.append(amostra_trib)
			# print(amostra_trib)
		elif selct[k] in vivi:
			dfs_vivi.append(amostra_trib)
			# print(amostra_trib)
		elif selct[k] in ana:
			dfs_ana.append(amostra_trib)
			# print(amostra_trib)


	print(len(dfs_ana))
	print()
	print()
	print(len(dfs_manu))
	print()
	print()
	print(len(dfs_vivi))		
	a= input("")		


	dfs_manu_rw = []
	dfs_vivi_rw = []
	dfs_ana_rw = []		

	for n in range(len(dfs_manu)):
		# Ana recebe Manu

		amostra_trib = dfs_manu[n].sample(6)
		dfs_ana_rw.append(amostra_trib)

		## vivi recebe Ana

		amostra_trib = dfs_ana[n].sample(6)
		dfs_vivi_rw.append(amostra_trib)


		# manu recebe Vivi
		amostra_trib = dfs_vivi[n].sample(6)
		dfs_manu_rw.append(amostra_trib)



	for z in range(len(dfs_manu)):
		amostras = pd.concat([dfs_manu_rw[z],dfs_manu[z]])
		amostras.to_excel("sorteio_0_v2_amostra_"+str(z+1)+"_Manu.xlsx", index = False)
		print("Manu")
		print(amostras)
		# print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)
		amostras = pd.concat([dfs_vivi_rw[z],dfs_vivi[z]])
		amostras.to_excel("sorteio_0_v2_amostra_"+str(z+1)+"_Vivi.xlsx", index = False)
		print("Vivi")
		# print(amostras)
		print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)
		amostras = pd.concat([dfs_ana_rw[z],dfs_ana[z]])
		amostras.to_excel("sorteio_0_v2_amostra_"+str(z+1)+"_Ana.xlsx", index = False)
		print("Ana")
		# print(amostras)
		print(amostras.info())
		print(amostras.Tribunal.value_counts())
		print("\n ******"*5)


if __name__ == "__main__":

	# dados_AC()
	# dados_AL()
	# dados_AM()
	# dados_AP()
	# dados_BA()
	# dados_CE()
	# dados_ES()
	# dados_GO()
	# dados_MA()
	# dados_MG()
	# dados_MT()
	# dados_PA()
	# dados_PB()
	# dados_PE()
	# dados_PI()
	# dados_PR()
	# dados_RN()
	# dados_RO()
	# dados_RR()
	# dados_SE()
	# dados_SP()
	# dados_TO()
	# dados_TRF2()
	# dados_TRF3()
	# dados_TRF4()
	# dados_TRF5()
	# main()
	# seleciona_amostra()
	# seleciona_amostra_quali()
	seleciona_amostra_quali_v_2()