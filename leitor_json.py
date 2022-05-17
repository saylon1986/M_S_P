import json
import pandas as pd
from array_Estados import Comarcas
from tqdm import tqdm
import numpy as np


def ler_JSON():

	with open('processos_insper.json', 'r', encoding='utf8') as f:
		info = json.load(f)


	colunas = info[0].keys()
	# print(colunas)


	linhas = []
	for n in range(len(info)):
		caso = info[n]
		# print(caso)
		# print("-------------")
		linha=[]
		for item in caso:
			# print(item,":",caso[item])
			linha.append(caso[item])
		linhas.append(linha)
		# print(linha)
		# print("--------------")



	df = pd.DataFrame(linhas, columns=colunas).astype(str)


	# print(df.head())
	# z = input("")
	df = df[['siglaTribunal','numero', "segmentoJustica",'mov_1st_1042_dataHora','dataAjuizamento','orgaoJulgador_codigoOrgao']]


	df.rename(columns={'siglaTribunal':'Tribunal','numero': 'Número do Processo', "segmentoJustica": "Competência",
			'mov_1st_1042_dataHora': 'Data da Sentença','dataAjuizamento':'Data da Distribuição', 'orgaoJulgador_codigoOrgao':'Vara'}, 
			inplace = True)


	# df['Estado'] = df['Estado'].str[2:].str.strip()
	df['Competência'] = df['Competência'].str.split(" ",n=1, expand = True)[1]


	# print(df["Data da Sentença"].head(10))


	df['Data da Sentença'] = df['Data da Sentença'].str[0:4]+"-"+df['Data da Sentença'].str[4:6]+'-'+df['Data da Sentença'].str[6:8]
	df['Data da Distribuição'] = df['Data da Distribuição'].str[0:4]+"-"+df['Data da Distribuição'].str[4:6]+'-'+df['Data da Distribuição'].str[6:8]

	df.loc[df["Data da Distribuição"] == "2020-06-31", "Data da Distribuição"] = "2020-06-30"

	# print(df["Data da Sentença"].head(10))

	df['Data da Sentença'] = pd.to_datetime(df['Data da Sentença'])

	df['Data da Sentença'] = df['Data da Sentença'].dt.strftime('%d-%m-%Y')

	df['Data da Distribuição'] = pd.to_datetime(df['Data da Distribuição'])

	df['Data da Distribuição'] = df['Data da Distribuição'].dt.strftime('%d-%m-%Y')


	# print(df["Data da Sentença"].head(10))
	

	# z= input("")


	df["Origem"] = "JSON_DATAJUD"

	df["Origem_dados"] = "JSON"

	df["Vara"] = None


	df['Número do Processo'] = df['Número do Processo'].astype(str).str.replace("-","")
	df['Número do Processo'] = df['Número do Processo'].astype(str).str.replace(".","")


	df['Número do Processo'] = df['Número do Processo'].astype(str)

	# ajuste no número do processo

	fim = df["Número do Processo"].astype(str).str[-4:]
	est = df["Número do Processo"].astype(str).str[-6:-4]
	just = df["Número do Processo"].astype(str).str[-7]
	ano_aj = df["Número do Processo"].astype(str).str[-11:-7]
	cod = df["Número do Processo"].astype(str).str[-13:-11]
	rest = df["Número do Processo"].astype(str).str[:-13]

	df["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim
	
	ano_dados = ano_aj.astype(int)
	df["Ano"] = ano_dados
	df_filter = df["Ano"] >= 2017
	df = df[df_filter]
	
	df["Estado"] = None
	

	df = df[["Número do Processo", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano","Tribunal", "Competência", "Origem_dados","Estado"]]

	# print(df) 

	df.to_excel("Dados_Json.xlsx", index = False)


# ler_JSON()




def unificador():

	planilha = pd.read_excel("Dados_compilados_2.xlsx", engine ='openpyxl')

	planilha_2 = pd.read_excel("Dados_Json.xlsx", engine ='openpyxl', dtype ="object")

	planilha.drop_duplicates(subset="Número do Processo", inplace= True)

	planilha_2.drop_duplicates(subset="Número do Processo", inplace= True)


	planilha_final = planilha.merge(planilha_2 , on = "Número do Processo", how = "left") 

	# planilha_final.drop_duplicates(subset="Número do Processo", inplace= True)

	# planilha_final.to_excel("Dados_unificados_JSON_LAI.xlsx", index = False)



	planilha_final['Data da Distribuição_x'] = planilha_final['Data da Distribuição_x'].fillna(planilha_final['Data da Distribuição_y'])
	planilha_final['Data da Sentença_x'] = planilha_final['Data da Sentença_x'].fillna(planilha_final['Data da Sentença_y'])
	# planilha_final['Origem_dados_x'] = planilha_final['Origem_dados_x'].fillna(planilha_final['Origem_dados_y'])


	############## preciso dropar todas as colunas Y antes de fazer isso aqui  ####################
	planilha_final.drop(columns=["Vara_y", "Origem_y","Data da Distribuição_y","Data da Sentença_y","Ano_y","Tribunal_y","Competência_y","Origem_dados_y","Estado_y"], inplace= True)


	planilha_final.rename(columns={'Vara_x':'Vara','Data da Distribuição_x': "Data da Distribuição", "Data da Sentença_x": "Data da Sentença",
			'Ano_x': 'Ano','Estado_x':'Estado', 'Competência_x':'Competência','Origem_x':'Origem','Tribunal_x':'Tribunal','Origem_dados_x':'Origem_dados'}, 
			inplace = True)


	print(planilha_final)

	planilha_final = pd.concat([planilha_final,planilha_2])
	
	planilha_final.drop_duplicates(subset="Número do Processo", inplace= True)
	

	planilha_final['Planilha'] = planilha_final['Planilha'].fillna(planilha_2['Origem_dados'])
	
	print(planilha_final)

	# planilha_final.to_excel("Dados_unificados_JSON_LAI.xlsx", index = False)
	# z= input("")


	codigo = planilha_final["Número do Processo"].astype(str).str[-4:].to_list()
	estado = planilha_final["Estado"].to_list()



	comarcas = []
	for cod, est in tqdm(zip(codigo,estado)):
		try:
			array_estado = Comarcas(est) 
			for k in range(len(array_estado)):
				comarca = None
				if array_estado[k][0] == cod:
					comarca = array_estado[k][2]
					break
			comarcas.append(comarca)
		except:
			comarcas.append(None)


	planilha_final["Comarcas_aux"] = comarcas

	planilha_final['Comarca'] = planilha_final['Comarca'].fillna(planilha_final['Comarcas_aux'])

	planilha_final['Comarca'] = planilha_final['Comarca'].str.lower().str.strip()

	planilha_final['Vara'] = planilha_final['Vara'].str.lower().str.strip()

	planilha_final['Estado'] = planilha_final['Estado'].fillna(planilha_final['Tribunal'])

	planilha_final["Estado"] = planilha_final["Estado"].replace(to_replace = r"STJ|TJ|TRF.+|TRE-|T5|STM", value = '', regex = True).str.strip()

	planilha_final["Estado"] = planilha_final["Estado"].replace(to_replace = r"TJDFT|DFT", value = 'DF', regex = True).str.strip()

	planilha_final["Estado"] = planilha_final["Estado"].str[-2:]

	planilha_final.loc[planilha_final.Competência == "Tribunal de Justiça", "Competência"] = "Estadual"

	

	# ajustes 
	idx = planilha_final.loc[planilha_final.Competência == "Militar Estadual"].index
	planilha_final.drop(idx, inplace= True)


	idx = planilha_final.loc[planilha_final.Competência == "Eleitoral"].index
	planilha_final.drop(idx, inplace= True)


	idx = planilha_final.loc[planilha_final.Competência == "Militar da União"].index
	planilha_final.drop(idx, inplace= True)


	
	df_filter = planilha_final["Ano"] < 2022
	planilha_final = planilha_final[df_filter]
	
	planilha_final.drop(columns=["Comarcas_aux"], inplace= True)

	print(planilha_final)

	planilha_final.to_excel("Dados_unificados_JSON_LAI.xlsx", index = False)

# unificador()



def unificador_SEEU():


	planilha = pd.read_excel("Dados_unificados_JSON_LAI.xlsx", engine ='openpyxl')

	planilha_2 = pd.read_excel("Dados_SEEU.xlsx", engine ='openpyxl', sheet_name = 'PROCESSOS_UNICOS', dtype='object')


	planilha_2.rename(columns={'tribunal':'Tribunal','processo': 'Número do Processo', "comarca": "Comarca"}, 
			inplace = True)
	
	# print(planilha_2['Comarca'])

	planilha_2["Origem"] = "SEEU"
	planilha_2["Planilha"] = "SEEU"

	planilha_2["Origem_dados"] = "SEEU_EXTERNO"


	planilha_2["Tribunal"] = planilha_2["Tribunal"].astype(str).str.strip()
	planilha_2["Estado"] = planilha_2["Tribunal"].astype(str).str[-2:]


	planilha_2['Comarca'] = planilha_2['Comarca'].replace(to_replace = r".+- ", value = '', regex = True).str.strip()

	planilha_2["Competência"] = np.where(planilha_2['Estado'].isnull() == True, "Federal","Estadual")



	# ajuste no número do processo

	fim = planilha_2["Número do Processo"].astype(str).str[-4:]
	est = planilha_2["Número do Processo"].astype(str).str[-6:-4]
	just = planilha_2["Número do Processo"].astype(str).str[-7]
	ano_aj = planilha_2["Número do Processo"].astype(str).str[-11:-7]
	cod = planilha_2["Número do Processo"].astype(str).str[-13:-11]
	rest = planilha_2["Número do Processo"].astype(str).str[:-13]

	planilha_2["Número do Processo"] = rest+"-"+cod+"."+ano_aj+"."+just+"."+est+"."+fim

	ano_dados = ano_aj.astype(int)
	planilha_2["Ano"] = ano_dados
	df_filter = planilha_2["Ano"] >= 2017 
	planilha_2 = planilha_2[df_filter]


	planilha_final = planilha.merge(planilha_2 , on = "Número do Processo", how = "left")


	planilha_final['Comarca_x'] = planilha_final['Comarca_x'].fillna(planilha_final['Comarca_y'])
	planilha_final['Estado_x'] = planilha_final['Estado_x'].fillna(planilha_final['Estado_y'])
	planilha_final['Tribunal_x'] = planilha_final['Tribunal_x'].fillna(planilha_final['Tribunal_y'])


	planilha_final.drop(columns=["Comarca_y", "Tribunal_y","Origem_y","Origem_dados_y","Estado_y","Ano_y","Competência_y","Planilha_y"], inplace= True)



	dados_nasc = planilha_final['dt_nasc'].astype(str).str[-2:]+"-"+planilha_final['dt_nasc'].astype(str).str[-5:-3]+"-"+planilha_final['dt_nasc'].astype(str).str[:4]

	planilha_final["dt_nasc"] = np.where(planilha_final['dt_nasc'].isnull() == False, dados_nasc,'')
	

	planilha_final.rename(columns={'Planilha_x':'Planilha','Vara_x':'Vara','Data da Distribuição_x': "Data da Distribuição", "Data da Sentença_x": "Data da Sentença",
			'Ano_x': 'Ano','Estado_x':'Estado', 'Competência_x':'Competência','Origem_x':'Origem','Tribunal_x':'Tribunal','Origem_dados_x':'Origem_dados',"Comarca_x":"Comarca"}, 
			inplace = True)


	planilha_final = pd.concat([planilha_final,planilha_2])

	planilha_final["Estado"] = planilha_final["Estado"].replace(to_replace = r"FT", value = 'DF', regex = True).str.strip()

	planilha_final["Estado"] = planilha_final["Estado"].replace(to_replace = r"F3|F2|F5|F1", value = '', regex = True).str.strip()

	planilha_final['Comarca'] = planilha_final['Comarca'].str.lower().str.strip()

	planilha_final.drop_duplicates(subset="Número do Processo", inplace= True)

	df_filter = planilha_final["Ano"] < 2022
	planilha_final = planilha_final[df_filter]


	indexes = planilha_final[planilha_final['Tribunal'] == 'STJ' ].index
	planilha_final.drop(indexes, inplace=True)


	indexes = planilha_final[planilha_final['Tribunal'] == 'STJ' ].index
	planilha_final.drop(indexes, inplace=True)

	indexes = planilha_final[planilha_final['Tribunal'] == 'TRE-SP' ].index
	planilha_final.drop(indexes, inplace=True)

	indexes = planilha_final[planilha_final['Tribunal'] == 'TRE-PR' ].index
	planilha_final.drop(indexes, inplace=True)

	indexes = planilha_final[planilha_final['Tribunal'] == 'TJMRS' ].index
	planilha_final.drop(indexes, inplace=True)

	indexes = planilha_final[planilha_final['Tribunal'] == 'TJMMG' ].index
	planilha_final.drop(indexes, inplace=True)


	planilha_final['Comarca'] = planilha_final['Comarca'].replace(to_replace = r"comarca de|comarca da", value = '', regex = True).str.strip()

	print(planilha_final)

	planilha_final.to_excel("Dados_unificados_JSON_LAI_SEEU.xlsx", index = False)


unificador_SEEU()







