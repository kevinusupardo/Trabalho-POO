#2° INFORMATICA MATUTINO
#Hayrine lima
#Kevin Gabriel 

import getpass
from datetime import datetime

#LISTAS
pontos = []

class Produto:
  def __init__(self,valorproduto,nomeproduto,qtd,tipo):
    self.valorproduto=valorproduto
    self.nomeproduto=nomeproduto
    self.qtd=qtd
    self.tipo=tipo
  
  def quantidade(self):
    self.qtd=int(input('quantos? '))

class Pedido:
  def __init__(self):
    self.cliente= []
    self.valorpart=[]
    self.itensproduto=[]
    self.valortotal= 0

  def addcarrinho(self,objproduto, objcliente):
    print(f'\n{objcliente.nome}, estes são os itens no seu carrinho...')
    self.itensproduto.append(objproduto)
    self.valorpart.append(objproduto.valorproduto)
    len(self.valorpart)
    self.valortotal=0
    for x in range(len(self.valorpart)):
      self.valortotal=self.valorpart[x] + self.valortotal
    for x in range (len(self.itensproduto)):
      print(f'\n{self.itensproduto[x].nomeproduto}, R${self.itensproduto[x].valorproduto}')
    print(f'\n VALOR TOTAL:{self.valortotal}')    

class Pagamento:
  def __init__(self):
    self.dinheirocliente = 0
    self.troco=0
  
  def calctroco(self,objpedido):
    while True:
      self.dinheirocliente = int(input('Troco pra quanto?'))
      len(objpedido.valorpart)
      objpedido.valortotal = 0
      for x in range(len(objpedido.valorpart)):
        objpedido.valortotal= self.valorpart[x] + self.valortotal
      self.troco = (self.dinheirocliente - objpedido.valortotal)
      if self.trococliente <= 0:
        print('Valor aceitável')
        continue
      else:
        print(f'Troco: R${self.troco}')
        break


class Endereco:
  def __init__(self, bairro, rua, numero):
    self.bairro=bairro
    self.rua=rua
    self.numero=numero

class Pessoa:
  def __init__(self, email, senha, nome, nascimento, cpf, telefone):
    self.listaemail=[]
    self.email=email
    self.listaemail.append(email)
    self.listasenha=[]
    self.senha=senha
    self.listasenha.append(senha)
    self.nome=nome
    self.nascimento=nascimento
    self.cpf=cpf
    self.telefone=telefone
    

  def fazerlogin(self):
    while True:
      print('\nFAÇA LOGIN')
      loginemail= input('email:')
      loginsenha=getpass.getpass('senha:')

      #login e senha incorreta
      if loginemail not in self.listaemail and loginsenha not in self.listasenha:
        print('\nLogin incorreto!')
        print('\nTente novamente...')
        continue
      
      #email correto, senha incorreta
      if loginemail in self.listaemail and loginsenha not in self.listasenha:
        print('\nSenha incorreta!')
        print('\nTente novamente...')
        continue
      
      #email incorreto, senha correta
      if loginemail not in self.listaemail and loginsenha in self.listasenha:
        print('\nInforme um email cadastrado!')
        print('\nTente novamente...')
        continue

      #email e senha corretos
      if loginemail in self.listaemail and loginsenha in self.listasenha:
        print(f'\nBEM VIND@ {self.nome}')
        break

class Cliente(Pessoa):
  def __init__(self, email, senha, nome, nascimento, cpf, telefone, objendereco):
    super().__init__(email, senha, nome, nascimento, cpf, telefone)
    self.endereco = objendereco

  def fazercadastro(self,objendereco):
    while True:
      print('\nCADASTRE-SE\n')

      while True: 
        try:
          self.nome = input('Nome: ')
          if self.nome =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos")
        else:
          break

      while True: 
        try:
          self.email = input('Email: ')
          if self.email =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos")
        else:
          break

      while True: 
        try:
          senha=getpass.getpass('Digite sua senha: ')
          self.senha=senha
          if self.senha =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos.")
        else:
          break
      
      senha2 = getpass.getpass ('Digite sua senha novamente:')
      
      while True: 
        try:
          self.nascimento=input('Data de nascimento:')
          if self.nascimento =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos.")
        else:
          break
   
      while True: 
        try:
          self.cpf=input('CPF:')
          if self.cpf =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos.")
        else:
          break
        
      while True: 
        try:
          self.telefone=input('Telefone:')
          if self.telefone =="":
              raise ValueError
        except ValueError:
          print ("Preencha todos os campos.")
        else:
          break
      
      print('\nInforme seu endereço...')
      objendereco.rua=input('Rua: ')
      objendereco.numero=input('Nº:')
      objendereco.bairro=input('Bairro: ')
      if senha == senha2:
        self.listaemail.append(self.email)
        self.listasenha.append(senha)
        print(f'\nSeu cadastro está pronto {self.nome}!\nFaça seu login:\n\n......CONVENIÊNCIA.HAYVIN......\n')
        break
      else:
        print('\nATENÇÃO! As senhas não estão iguais! ')
        print('\nFaça seu cadastro novamente!')
        continue
    
  def alterardados(self):
    while True:
      print("_________________________\n Qual dado deseja alterar?\n1-Email\n2-Senha\n3-Endereço\n4-Telefone")
      dados = input('\nDigite o numero da operação: ')
      
      if dados not in ['1', '2', '3', '4']:
         print('\nopção inválida!\n')
         continue
      if dados == '1':
        self.listaemail.remove
        (self.email)
        novoemail=input('\nDigite seu novo email: ')
        self.listaemail.append(novoemail)
        print('\nALTERAÇÃO REALIZADA COM SUCESSO')
        break

      if dados == '2':
       
        senhaantiga=getpass.getpass('Digite sua senha antiga: ')
        if senhaantiga not in self.listasenha:
          print('\nSENHA INCORRETA\n')
          continue
        else:
          print('\nSENHA VÁLIDA!\n')
          self.listasenha.remove
          (self.senha)
          novasenha=getpass.getpass('Digite sua nova senha: ')
          novasenha2=getpass.getpass('Digite sua nova senha novamente: ')
          if novasenha==novasenha2:
            Cliente.senha=novasenha
            self.listasenha.append(novasenha)
            print('ALTERAÇÃO REALIZADA COM SUCESSO\n ')
            break
          else:
            print('Senha inválida\n')
            continue  
        break
      if dados == '3':
        print('INSIRA SUAS NOVAS INFORMAÇÕES')
        endereco1.bairro = input('Bairro: ')
        endereco1.rua = input('Rua: ')
        endereco1.numero = input('Nº: ')
        break 
      
      if dados=='4':
        novotelefone=input('Digite o novo Telefone: ')
        Cliente.telefone = novotelefone
        print('ALTERAÇÃO FEITA COM SUCESSO!')
        break

class Funcionario(Pessoa):
  def __init__(self,email, senha, nome, nascimento, cpf, telefone):
    super().__init__(email, senha, nome, nascimento, cpf, telefone)

  def verPedidos(self):
    pass
  def baterponto1(self):
    while True:
      ponto1 =input('digite 1 para bater ponto de início')
      if ponto1=='1':
        hora = datetime.now()
        hora2 = hora.strftime('Entrada: %d/%m/%Y %H:%M:%S')
        pontos.append(hora2)
        print(hora2)
        break
  def baterponto2(self):
    while True:
      ponto1 =input('digite 2 para bater ponto de início')
      if ponto1=='2':
        hora = datetime.now()
        hora2 = hora.strftime('Entrada: %d/%m/%Y %H:%M:%S')
        pontos.append(hora2)
        print(hora2)
        break

#PESSOAS
endereco1 = Endereco(' ',' ',' ') 
cliente1 = Cliente(' ',' ',' ',' ',' ',' ', endereco1)
#Funcionario
funcionario1 = Funcionario('func1@gmail.com', '123', 'Joelson', '06/10/1995', '522.467.510-00', '0000000000')
codfuncionario1 = '1234'
funcionario2 = Funcionario('func2@gmail.com', '123', 'Juresca', '09/04/2000', '421.536.854-00', '1111111111')
codfuncionario2 = '4321'

#PRODUTOS
brigadeiro = Produto(4.00, 'Brigadeirinho',1,'doce')
bolo = Produto(5.00,'Bolo de pote', 1, 'doce')
salgado = Produto(20.00,'Salgadinho',1,'salgado frito')

refrigerante = Produto(10.00,'Refrigerante',1,'bebida')
sucodetox = Produto(15.00,'Suco natural detox',1,'bebida')
suco = Produto(12.00,'Suco natural',1,'bebida')

pedido1 = Pedido()
pagamento1 = Pagamento()


#INICIO
print('......CONVENIÊNCIA.HAYVIN......')
print("........🅑 🅔 🅜  🅥 🅘 🅝 🅓 🅔.......")

#MENU INICIO
while True:
  menuinicio = input("    '1' - logar\n    '2' - cadastrar |")
  if menuinicio not in ['1', '2']:
    print('\nopção inválida!\ntente novamente\n')
    continue
  if menuinicio == '2':
    cliente1.fazercadastro(endereco1)
    continue

  #MENU CADASTRO  
  if menuinicio == '1':
    while True:
      menucadastro = input("\nDIGITE A OPÇÃO CORRESPONDENTE: c ou f \n\n   'c' - Cliente \n   'f' - Funcionário |")
      if menucadastro not in ['c', 'f']:
        print('opção inválida')
        continue
      if menucadastro == 'c': #MENU CLIENTE
        cliente1.fazerlogin()
        while True:
          menucliente = input('\n________CONVENIÊNCIA.HAYVIN_________\n 1 - alterar dados\n 2 - fazer pedido\n 3 - sair\n->')
          if menucliente not in ['1', '2','3']:
            print('opção inválida!\ntente novamente\n')
            continue
          if menucliente == '1':
              cliente1.alterardados()
              continue
          if menucliente == '3':
            break
          if menucliente == '2':
            while True:
              menucardapio=input(f'\n____________CARDÁPIO___________\nDigite o código do produto que deseja adquirir...\n______________________________\n1-{brigadeiro.nomeproduto}: R${brigadeiro.valorproduto}(unidade)\n2-{bolo.nomeproduto}: R${bolo.valorproduto}(unidade)\n3-{salgado.nomeproduto}: R${salgado.valorproduto}(cento)\n4-{refrigerante.nomeproduto}: R${refrigerante.valorproduto}(2L)\n5-{sucodetox.nomeproduto}: R${sucodetox.valorproduto}(1L)\n6-{suco.nomeproduto}: R${suco.valorproduto}(1L)\n______________________________\nPara FINALIZAR, digite 7\nPara CANCELAR, digite 8\n')
              if menucardapio not in ['1','2','3','4','5','6','7','8']:
                print('operação inválida')
              if menucardapio == '1':
                pedido1.addcarrinho(brigadeiro,cliente1)
              if menucardapio == '2':
                pedido1.addcarrinho(bolo,cliente1)
              if menucardapio == '3':
                pedido1.addcarrinho(salgado,cliente1)
              if menucardapio == '4':
                pedido1.addcarrinho(refrigerante,cliente1)
              if menucardapio == '5':
                pedido1.addcarrinho(sucodetox,cliente1)
              if menucardapio == '6':
                pedido1.addcarrinho(suco,cliente1)
              if menucardapio == '7':
                print('PEDIDO FINALIZADO COM SUCESSO! \nSEU PEDIDO SERÁ ENVIADO ATÉ O ENDEREÇO INFORMADO.')
                for x in range(len(pedido1.itensproduto)):
                  print(f'{pedido1.itensproduto[x].nomeproduto}, R${pedido1.itensproduto [x].valorproduto}')
                print (f'R${pedido1.valortotal}')
                break 
              if menucardapio == '8':
                pedido1.itensproduto =[]
                pedido1.valorpart=[]
      #MENU FUNCIONÁRIO
      if menucadastro == 'f':
        for x in range (4):
          cod = input('\n digite o código de funcionário: ')
          if cod == codfuncionario1:
            funcionario1.fazerlogin()
            while True:
              menufuncionario = input("""\n'1 - bater ponto inicial\n'2' - bater ponto final\n'3' - ver pontos\n'4' - sair |""")
              if menufuncionario not in ['1','2','3', '4']:
                print('opção inválida!')
                continue
              if menufuncionario =='1':
                funcionario1.baterponto1()
              if menufuncionario =='2':
                funcionario1.baterponto2()
              if menufuncionario =='3':
                print(pontos)
              if menufuncionario =='1':
                break
            break
          elif cod == codfuncionario2:
            funcionario2.fazerlogin()
            while True:
              menufuncionario = input("""\n'1 - bater ponto inicial\n'2' - bater ponto final\n'3' - ver pontos\n'4' - sair |""")
              if menufuncionario not in ['1','2','3', '4']:
                print('opção inválida!')
                continue
              if menufuncionario =='1':
                funcionario1.baterponto1()
              if menufuncionario =='2':
                funcionario1.baterponto2()
              if menufuncionario =='3':
                print(pontos)
              if menufuncionario =='1':
                break
            break
          else:
            print('       código inválido')
            print(f'\nvocê tem mais {3-x} tentativas')
            x-1
      break
    break