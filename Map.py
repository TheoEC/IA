NN = []
NN.append("Acre: Amazonas, Rondonia")
NN.append("Amazonas: Acre, Rondonia, Roraima, Pará")
NN.append("Rondonia: Amazonas, Acre")
NN.append("Roraima: Pará, Amazonas")
NN.append("Pará: Tocantins, Maranhão, Amapá, Amazonas")
NN.append("Amapá: Pará")
NN.append("Tocantins: Piauí, Maranhão, Pará, Bahia")
NN.append("Piauí: Maranhão, Bahia, Ceará, Pernambuco, Tocantins")
NN.append("Maranhão:  Piauí, Tocantins, Pará")
NN.append("Ceará: RN, Paraíba, Pernambuco, Piauí")
NN.append("Paraíba: Ceará, RN, Pernambuco")
NN.append("RN: Paraíba, Ceará")
NN.append("Pernambuco: Paraíba, Ceará, Piauí, Bahia, Alagoas")
NN.append("Alagoas: Sergipe, Pernambuco, Bahia")
NN.append("Bahia: Alagoas, Sergipe, Pernambuco, Piauí, Tocantins")
NN.append("Sergipe: Bahia, Alagoas")

Cores = ["Azul", "Verde", "Vermelho"]
Estados = []

def get(nome):
  n = -2
  for i in range(len(Estados)):
    if Estados[i].Nome == nome:
      #print("Nome:", Estados[i].Nome, "\nVizinhos:", Estados[i].Vizinhos, "\nPossibilidades:", Estados[i].Possibilidades)
      n = i
      return n

def info(nome):
  retorno = ""
  for i in range(len(Estados)):
    if Estados[i].Nome == nome:
      print("Nome:", Estados[i].Nome, "\nVizinhos:", Estados[i].Vizinhos, "\nPossibilidades:", Estados[i].Possibilidades)
      retorno = Estados[i].Vizinhos
  
  return retorno

def Set_Cor(nome, cor):
  Estados[get(nome)].Set_cor(cor)
  Estados[get(nome)].Possibilidades.remove(cor)

class State:
  estados = []
  Nome = ""
  Cor = ""
  Possibilidades = []
  Vizinhos = []

  def __init__(self, nome):
    self.Nome = nome
    self.Possibilidades = ["Azul", "Verde", "Vermelho"]

  def Set_cor(self, cor):
    print(self.Nome, "-->", cor)
    self.Cor = cor

    for i in self.Vizinhos:
      print("i:",i,get(i))
      if (cor in Estados[get(i)].Possibilidades) == True:
        Estados[get(i)].Possibilidades.remove(cor)
      
      info(Estados[get(i)].Nome)
      print("------------------>")

  def Reseta(self):
    self.Cor = ""
    Possibilidades = ["Azul", "Verde", "Vermelho"]

for i in NN: #Adicionando os objetos State a lista Estados
  nome = i.split(":")[0]
  V = i.split(":")[1].replace(" ","").split(",")
  Novo_Estado = State(nome)
  Novo_Estado.Vizinhos = V
  Estados.append(Novo_Estado)

qm_e = ""
menos_vizinhos = 100
for i in Estados: #Procurando estado com menos vizinhos
  if len(i.Vizinhos) < menos_vizinhos and i.Cor == "":
    qm_e = i.Nome
    menos_vizinhos = len(i.Vizinhos)


def Tafaltando(est): #Saber se tem estado sem cor ainda
  for i in est:
    if i.Cor == "":
      return True
  return False


while(Tafaltando(Estados)):
  #print("Estado:", info("Paraíba")) 
  if len(Estados[get(qm_e)].Possibilidades) > 0:
    Set_Cor(qm_e, Estados[get(qm_e)].Possibilidades[0])
  else:
    print("Começou a treta")
    try:
      info(Estados[get(Estados[get(qm_e)].Vizinhos[0])].Nome)
      Set_Cor(Estados[get(Estados[get(qm_e)].Vizinhos[0])].Nome, Estados[get(Estados[get(qm_e)].Vizinhos[0])].Possibilidades[0])
    except:
      try:
        info(Estados[get(Estados[get(qm_e)].Vizinhos[1])].Nome)
        Set_Cor(Estados[get(Estados[get(qm_e)].Vizinhos[1])].Nome, Estados[get(Estados[get(qm_e)].Vizinhos[1])].Possibilidades[0])
      except:
        try:
          info(Estados[get(Estados[get(qm_e)].Vizinhos[2])].Nome)
          Set_Cor(Estados[get(Estados[get(qm_e)].Vizinhos[2])].Nome, Estados[get(Estados[get(qm_e)].Vizinhos[2])].Possibilidades[0])
        except:
          print("Ja era pcr\n\n\n")
          break

    deu = ["Azul", "Verde", "Vermelho"]
    for i in Estados[get(qm_e)].Vizinhos:
      if (Estados[get(i)].Cor in deu) == True:
        deu.remove(Estados[get(i)].Cor)
    if len(deu) > 0:
      Estados[get(qm_e)].Possibilidades = deu

      Set_Cor(qm_e, deu[0])
  #print("---------------------------------------\n\n")
  next = Estados[get(qm_e)].Vizinhos
  qm_e = ""
  for i in next:
    if Estados[get(i)].Cor == "":
      qm_e = Estados[get(i)].Nome
  if qm_e == "":
    menos_vizinhos = 100
    for i in Estados: #Procurando estado com menos vizinhos
      if len(i.Vizinhos) < menos_vizinhos and i.Cor == "":
        qm_e = i.Nome
        menos_vizinhos = len(i.Vizinhos)

  j = input("Proximo:"+qm_e)
  if j == "1":
    for i in Estados:
      if i.Cor != "":
        print(i.Nome, i.Cor)
    input()
  print("---------------------------------------------------\n\n")


for i in Estados:
    if i.Cor != "":
      print(i.Nome, i.Cor)
