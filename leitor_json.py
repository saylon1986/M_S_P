import json
import pandas as pd



def ler_JSON():

	with open('processos_insper.json', 'r', encoding='utf8') as f:
		info = json.load(f)


	colunas = info[0].keys()
	# print(keys)


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


	print(df)
	df = df[['siglaTribunal','numero', "segmentoJustica",'mov_1st_1042_dataHora','dataAjuizamento','orgaoJulgador_codigoOrgao']]


	df.rename(columns={'siglaTribunal':'Tribunal','numero': 'Número do Processo', "segmentoJustica": "Competência",
			'mov_1st_1042_dataHora': 'Data da Sentença','dataAjuizamento':'Data da Distribuição', 'orgaoJulgador_codigoOrgao':'Vara'}, 
			inplace = True)


	# df['Estado'] = df['Estado'].str[2:].str.strip()
	df['Competência'] = df['Competência'].str.split(" ",n=1, expand = True)[1]




	df['Data da Sentença'] = df['Data da Sentença'].str[0:4]+"-"+df['Data da Sentença'].str[4:6]+'-'+df['Data da Sentença'].str[6:8]
	df['Data da Distribuição'] = df['Data da Distribuição'].str[0:4]+"-"+df['Data da Distribuição'].str[4:6]+'-'+df['Data da Distribuição'].str[6:8]


	df["Origem"] = "JSON_DATAJUD"
	df['Ano'] = df['Data da Distribuição'].str[0:4].astype(int)
	df['Vara'] = df['Vara'].astype(str)

	df_filter = df["Ano"] >= 2017
	df = df[df_filter]

	df = df[["Número do Processo", "Vara", "Origem", "Data da Distribuição","Data da Sentença", "Ano","Tribunal", "Competência"]]

	print(df) 

	df.to_excel("Dados_Json.xlsx", index = False)

# df.to_excel("Dados_Json_tudo.xlsx", index = False)
# ler_JSON()




def unificador():

	planilha = pd.read_excel("Dados_compilados.xlsx", engine ='openpyxl')


	planilha ["Número do Processo"] = planilha['Número do Processo'].str.replace(".","")
	planilha ["Número do Processo"] = planilha['Número do Processo'].str.replace("-","")

	# print(planilha)


	planilha_2 = pd.read_excel("Dados_Json.xlsx", engine ='openpyxl')

	planilha_2 ["Número do Processo"] = planilha_2['Número do Processo'].str.replace(".","")
	planilha_2 ["Número do Processo"] = planilha_2['Número do Processo'].str.replace("-","")


	planilha ["Número do Processo"] = planilha['Número do Processo'].astype(str)
	planilha_2 ["Número do Processo"] = planilha_2['Número do Processo'].astype(str)
	# print(planilha_2)


	# planilha_final = planilha_2.merge(planilha , on = ["Número do Processo","Origem","Data da Distribuição","Data da Sentença", "Ano","Competência","Tribunal"], 
	# 	how = "left") 

	planilha_final = pd.concat([planilha,planilha_2])

	planilha_final.drop_duplicates(subset="Número do Processo", inplace= True)

	print(planilha_final)

	planilha_final.to_excel("Dados_unificados_JSON_LAI.xlsx", index = False)

unificador()