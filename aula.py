import pandas as pd

praga = "PERCEVEJO"
dataset = pd.read_csv('dicionario.csv')

qtdePresencas = [idx for idx, i in enumerate(dataset[praga]) if dataset[praga][idx] > 0]
qtdeAusencias = [idx for idx, i in enumerate(dataset[praga]) if dataset[praga][idx] == 0]

print("Total de presenças:", len(qtdePresencas))
print("Total de ausências:", len(qtdeAusencias))

dadosPresenca = dataset.filter(items = qtdePresencas, axis = 0)
dadosAusencia = dataset.filter(items = qtdeAusencias, axis = 0)

print("\nQuantidade Dataset Presenças: ", len(dadosPresenca))
print("Quantidade Dataset Ausências: ", len(dadosAusencia))

print("\nQuantidade Total de Pontos: ", len(dataset))

print("\nValores presentes nas Presenças: ")
print(dadosPresenca[praga].value_counts())

testDatasetPresenca = dadosPresenca.sample(n=5)
testDatasetAusencia = dadosAusencia.sample(n=5)
testDatasetCompleto = pd.concat([testDatasetPresenca, testDatasetAusencia])

dadosPresenca.drop(testDatasetPresenca.index, inplace=True)
dadosAusencia.drop(testDatasetAusencia.index, inplace=True)

print("\nQuantidade a ser movida Dataset Presenças: ", len(testDatasetPresenca))
print("Quantidade a ser movida Dataset Ausências: ", len(testDatasetAusencia))
print("Quantidade completa do dataset de test: ", len(testDatasetCompleto))

dataset = pd.concat([dadosAusencia, dadosPresenca])

print("\nNova quantidade no dataset de treinamento: ", len(dataset))
print("Nova quantidade Presença: ", len(dadosPresenca))
print("Nova quantidade Ausência: ", len(dadosAusencia))

diferenca = len(dadosAusencia) - len(dadosPresenca)
if diferenca > 0:
  dadosAusencia = dadosAusencia.drop(dadosAusencia.index[range(diferenca)])
else:
  dadosPresenca = dadosPresenca.drop(dadosPresenca.index[range(diferenca)])
dataset = pd.concat([dadosAusencia, dadosPresenca])

print("\nQuantidade no dataset Balanceado: ", len(dataset))
print("Quantidade dados Presença Balanceado: ", len(dadosPresenca))
print("Quantidade dados Ausência Balanceado: ", len(dadosAusencia))

print("\nValores presentes nas Presenças: ")
print(dadosPresenca[praga].value_counts())
