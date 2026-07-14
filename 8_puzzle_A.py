import copy


class bloco :
    def __init__(self, estado, movimento, g, h, pai):
        self.estado = estado
        self.movimento = movimento
        self.g = g
        self.h = h
        self.f = g + h
        self.pai = pai
        self.filhos = []
    
    def add_filho(self, estado, movimento, g, h, pai):
        filho = bloco(estado, movimento, g, h, pai)
        filho.pai = self
        filho.movimento = movimento
        filho.g = self.g + 1
        filho.h = h
        filho.f = g + h
        self.filhos.append(filho)
        filho.filhos = []
        return filho

    def escolhe_melhor_filho(self):
        melhor_filho = self.filhos[0]
        for filho in self.filhos:
            if filho.f < melhor_filho.f:
                melhor_filho = filho
        return melhor_filho


numero_de_movimentos = 0
quantidade_estados_expandidos = 0
TOTAL_COLUNAS = 3
TOTAL_LINHAS = 3
estado_inicial = [[1,2,3],
                  [4,0,6],
                  [7,5,8]]
estado_final = [[1,2,3],
                [4,5,6],
                [7,8,0]]


def ta_dentro_do_tabuleiro(linha, coluna):
    return linha >= 0 and linha <= TOTAL_LINHAS - 1 and coluna >= 0 and coluna <= TOTAL_COLUNAS - 1

def chegou_no_estado_final(estado): 
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if estado[linha][coluna] != estado_final[linha][coluna]:
                return False
    return True

def move_pra_baixo(estado):
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if estado[linha][coluna] == 0:
                if ta_dentro_do_tabuleiro(linha + 1, coluna):
                    novo_estado = copy.deepcopy(estado)
                    temp = novo_estado[linha][coluna]
                    novo_estado[linha][coluna] = novo_estado[linha + 1][coluna]
                    novo_estado[linha + 1][coluna] = temp
                    return novo_estado
    return None

def move_pra_cima(estado):
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if estado[linha][coluna] == 0:
                if ta_dentro_do_tabuleiro(linha - 1, coluna):
                    novo_estado = copy.deepcopy(estado)
                    temp = novo_estado[linha][coluna]
                    novo_estado[linha][coluna] = novo_estado[linha - 1][coluna]
                    novo_estado[linha - 1][coluna] = temp
                    return novo_estado
    return None

def move_pra_direita(estado):
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if estado[linha][coluna] == 0:
                if ta_dentro_do_tabuleiro(linha, coluna + 1):
                    novo_estado = copy.deepcopy(estado)
                    temp = novo_estado[linha][coluna]
                    novo_estado[linha][coluna] = novo_estado[linha][coluna + 1]
                    novo_estado[linha][coluna + 1] = temp
                    return novo_estado
    return None
            
def move_pra_esquerda(estado):
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if estado[linha][coluna] == 0:
                if ta_dentro_do_tabuleiro(linha, coluna - 1):
                    novo_estado = copy.deepcopy(estado)
                    temp = novo_estado[linha][coluna]
                    novo_estado[linha][coluna] = novo_estado[linha][coluna - 1]
                    novo_estado[linha][coluna - 1] = temp
                    return novo_estado
    return None
        
def calcula_h_manhattan(estado):
    h = 0
    for linha in range(TOTAL_LINHAS):
        for coluna in range(TOTAL_COLUNAS):
            if (estado[linha][coluna] != estado_final[linha][coluna]) and estado[linha][coluna] != 0: # se o bloco não tá na posição certa
               
                for linha_final in range(TOTAL_LINHAS):
                    for coluna_final in range(TOTAL_COLUNAS):
                        if estado[linha][coluna] == estado_final[linha_final][coluna_final]: # encontra a posição certa e calcula a distância de manhattan entre elas
                            h += abs(linha - linha_final) + abs(coluna - coluna_final)
    return h




inicio = bloco(estado_inicial, "", 0, calcula_h_manhattan(estado_inicial), None)
if move_pra_esquerda(inicio.estado) != None:
  filho_esquerda = inicio.add_filho(move_pra_esquerda(inicio.estado), "Esquerda", 0, calcula_h_manhattan(move_pra_esquerda(inicio.estado)), inicio)
  quantidade_estados_expandidos += 1
if move_pra_direita(inicio.estado) != None:
  filho_direita = inicio.add_filho(move_pra_direita(inicio.estado), "Direita", 0, calcula_h_manhattan(move_pra_direita(inicio.estado)), inicio)
  quantidade_estados_expandidos += 1
if move_pra_cima(inicio.estado) != None:
  filho_cima = inicio.add_filho(move_pra_cima(inicio.estado), "Cima", 0, calcula_h_manhattan(move_pra_cima(inicio.estado)), inicio)
  quantidade_estados_expandidos += 1
if move_pra_baixo(inicio.estado) != None:
  filho_baixo = inicio.add_filho(move_pra_baixo(inicio.estado), "Baixo", 0, calcula_h_manhattan(move_pra_baixo(inicio.estado)), inicio)
  quantidade_estados_expandidos += 1


while not chegou_no_estado_final(inicio.estado):
    numero_de_movimentos += 1
    if move_pra_esquerda(inicio.estado) != None:
      filho_esquerda = inicio.add_filho(move_pra_esquerda(inicio.estado), "Esquerda", 0, calcula_h_manhattan(move_pra_esquerda(inicio.estado)), inicio)
    if move_pra_direita(inicio.estado) != None:
      filho_direita = inicio.add_filho(move_pra_direita(inicio.estado), "Direita", 0, calcula_h_manhattan(move_pra_direita(inicio.estado)), inicio)
    if move_pra_cima(inicio.estado) != None:
      filho_cima = inicio.add_filho(move_pra_cima(inicio.estado), "Cima", 0, calcula_h_manhattan(move_pra_cima(inicio.estado)), inicio)
    if move_pra_baixo(inicio.estado) != None:
      filho_baixo = inicio.add_filho(move_pra_baixo(inicio.estado), "Baixo", 0, calcula_h_manhattan(move_pra_baixo(inicio.estado)), inicio)
    inicio = inicio.escolhe_melhor_filho()

print(f"Número total de movimentos: {numero_de_movimentos}")
print(f"Número total de estados expandidos: {quantidade_estados_expandidos}")

while True:
  if inicio.pai == None:
    break

  inicio = inicio.pai


print("Caminho percorrido:")
while inicio.filhos != []:
  for linha in inicio.estado:
    print(linha)
  inicio = inicio.escolhe_melhor_filho()
  print(inicio.movimento)
for linha in inicio.estado:
    print(linha)



