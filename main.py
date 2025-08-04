from time import sleep
import os
import random

#--------------------Funções úteis----------------------
def apagar_tela():
    os.system('cls')

s_cor = '\033[m'    

#classe base
class Player:
    def __init__(self, nome, poçao=2, hp = 100):
        self.nome = nome
        self.poçao = poçao
        self.hp = hp
    
    def falar(self):
        print(f'{self.nome} argumentou...')
    
    def recuperar_hp(self):
        if self.poçao != 0:
            print(f'{self.nome} tomou uma poção.')
            self.poçao -= 1
            self.hp += 50
            if self.hp > 100:
                self.hp = 100  
        
        else:
            print(f'{self.nome} achou que tinha uma poção...')                   

#subclasse 1    
class Guerreiro(Player):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.arma = arma
    
    def ataque(self, inimigo):
        print(f'{self.nome} atacou com sua {self.arma}')
        print(f'{inimigo.nome} -10')
        inimigo.hp -= 10
    
    def especial(self, inimigo):
        print(f'{self.nome} girou sua {self.arma} com toda sua força!')
        print(f'{inimigo.nome} -30')
        inimigo.hp -= 30    
            
#subclasse 2    
class Mago(Player):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.arma = arma
    
    def ataque(self,inimigo):
        print(f'{self.nome} lançou magia com seu {self.arma}.')
        print(f'{inimigo.nome} -10')
        inimigo.hp -= 10            

    def especial(self, inimigo):
        print(f'{self.nome} conjurou uma enorme Bola de Fogo!')
        print(f'{inimigo.nome} -30')
        inimigo.hp -= 30            

#subclasse 3 (Minha favorita)
class Samurai(Player):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.arma = arma

    def ataque(self,inimigo):
        if self.arma == 'Katana':
            print(f'{self.nome} atacou com sua {self.arma}.')
            print(f'{inimigo.nome} -10')
            inimigo.hp -= 10            
        else:
            print(f'{self.nome} atirou com sua {self.arma}.')
            print(f'{inimigo.nome} -10')
            inimigo.hp -= 10
    
    def especial(self,inimigo):
        print(f'{self.nome} usou o hack de SUPERAQUECER o inimigo!')
        print(f'{inimigo.nome} -30')
        inimigo.hp -= 30                    


#Inimigo
class Enemy(Player):
    def __init__(self, nome, poçao=2, hp=100):
        super().__init__(nome, poçao, hp)
        
    def ataque(self, jogador):
        print(f'{self.nome} usou seu Tridente para atacar!')
        print(f'{jogador.nome} -12')
        jogador.hp -= 12
    
    def especial(self, jogador):
        print(f'{self.nome} invocou uma grande onda de Peixes Yokais!')
        print(f'{jogador.nome} -35')
        jogador.hp -= 35 
    
           

# INICIO
prologo = '''
Durante séculos, o Lago do Silêncio permaneceu intocado.
Suas águas escondem um segredo: um ser ancestral, guardião dos peixes e mestre dos yokais aquáticos...
'''

prologo2 = '''Mas a paz acabou.
A vila de Mizukai começou a pescar mais do que devia.
E agora, furioso, o Fishmancer ameaça submergir toda a vila em um tsunami de escamas e tentáculos.
Você é o único que pode detê-lo.
Escolha seu destino: Guerreiro, Mago ou Samurai.
Pegue uma arma. Prepare suas poções. E enfrente a fúria do invocador de peixes.
O futuro da vila está nas suas mãos.'''

'''
for letra in prologo:
    print(letra, end='', flush=True)
    sleep(0.1)
sleep(1)
print('FISHMANCER!')
sleep(1)    
for l in prologo2:
    print(l, end='', flush=True)
    sleep(0.05)
sleep(1)
print('\nMEU DEUS, QUE FEDOR DE PEIXE!')
'''

#CRIADOR DE PERSONAGEM
input('Pressione [ENTER] para continuar. ')
apagar_tela()

nome = str(input('Qual é o seu nome? '))
print('''Escolha o seu caminho!
[1] Guerreiro
[2] Mago
[3] Samurai''')

while True:
    try:
        classe = int(input('Classe: '))
        if classe < 1 or classe > 3:
            print('ERRO. Tente novamente!')
        else:
            if classe == 1:
                cor = '\033[32m'
                classe = 'Guerreiro'
            elif classe == 2:
                cor = '\033[36m'
                classe = 'Mago' 
            elif classe == 3:
                cor = '\033[31m'
                classe = 'Samurai'                               
            break                 
    except Exception as e:
        print('ERRO. Tente novamente!', e)    

if classe == 'Guerreiro':
    print('''Escolha sua arma!
[1] Espada
[2] Clava
''')
elif classe == 'Mago':
    print('''Escolha sua arma!
[1] Cajado
[2] Livro de Magias
''')
elif classe == 'Samurai':
    print('''Escolha sua arma!
[1] Katana
[2] Escopeta
''')        

while True:
    try:
        arma = int(input('Arma: '))
        if arma < 1 or arma > 3:
            print('ERRO. Tente novamente!')
        else:
            
            if arma == 1:
                if classe == 'Guerreiro':
                    arma = 'Espada'
                elif classe == 'Mago':
                    arma = 'Cajado'
                elif classe == 'Samurai':
                    arma = 'Katana'        
            
            elif arma == 2:
                if classe == 'Guerreiro':
                    arma = 'Clava'
                elif classe == 'Mago':
                    arma = 'Livro de Magias'
                elif classe == 'Samurai':
                    arma = 'Escopeta'                             
            break                 
    except Exception as e:
        print('ERRO. Tente novamente!', e)      

if classe == 'Guerreiro':
    jogador = Guerreiro(nome,arma)
elif classe == 'Mago':
    jogador = Mago(nome,arma)
elif classe == 'Samurai':
    jogador = Samurai(nome,arma)

inimigo = Enemy('FishMancer',3,100)               

sleep(0.8)
apagar_tela()

pos_criador = f'{cor}{nome}{s_cor} está pronto pra batalha contra o FishMancer! seguiu o caminho de {cor}{classe}{s_cor} e pegou {cor}{arma}{s_cor}. O mestre da vila lhe deu duas poções, use com sabedoria...'
'''
for l in pos_criador:
    print(l, end='', flush=True)
    sleep(0.1)
'''
    
print(f'''{cor}
------------------------------------------------------------
Nome: {nome} | HP: 100
------------------------------------------------------------
Classe: {classe} | Arma: {arma} |
------------------------------------------------------------
Itens: {2} - Poção (Recupera 50hp) |

{s_cor}''')

input('Pressione [ENTER] para continuar. ')
apagar_tela()    

#----------BATALHA FINAL!----------
contador = 0
contador_inimigo = 0
#Toda a batalha vai acontecer dentro desse while
while True:
    
    print(
f'''{jogador.nome} HP: {cor}{'/' * jogador.hp}{s_cor}
{inimigo.nome} HP: {'/' * inimigo.hp}
''')
    
    if contador < 3:
        print(
    f'''{cor}[1] ATACAR
[2] FALAR
[3] TOMAR POÇÃO{s_cor}''')
        
        try:
            escolha = int(input(f'{jogador.nome}: '))
            if escolha < 1 or escolha > 3:
                print('ERRO. Tente novamente!')
            else:
                if escolha == 1:
                    jogador.ataque(inimigo)
                elif escolha == 2:
                    jogador.falar()
                elif escolha == 3:
                    jogador.recuperar_hp()                                                  
        except Exception as e:
            print('ERRO. Tente novamente!', e)
        contador += 1           
    
    elif contador >= 3:
        print(
    f'''{cor}[1] ATACAR
[2] FALAR
[3] TOMAR POÇÃO
[4] ESPECIAL!{s_cor}''')
        
        try:
            escolha = int(input(f'{jogador.nome}: '))
            if escolha < 1 or escolha > 4:
                print('ERRO. Tente novamente!')
            else:
                if escolha == 1:
                    jogador.ataque(inimigo)
                elif escolha == 2:
                    jogador.falar()
                    print(f'{inimigo.nome} não deu ouvidos...')
                elif escolha == 3:
                    jogador.recuperar_hp()
                elif escolha == 4:
                    jogador.especial(inimigo)
                    contador = 0                                                      
        except Exception as e:
            print('ERRO. Tente novamente!', e)
    
    if inimigo.hp <= 0 or jogador.hp <= 0:
        break     
    
    if contador_inimigo < 3:
        menu_inimigo = [1,2,3]
        contador_inimigo += 1
    elif contador_inimigo >= 3:
        menu_inimigo = [1,2,3,4]
     
    
    escolha_inimigo = random.choice(menu_inimigo)
    if escolha_inimigo == 4:
        contador_inimigo = 0
    print(escolha_inimigo)         
    
    
    if inimigo.hp <= 0 or jogador.hp <= 0:
        break                
        
        
    
