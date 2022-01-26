from PyQt5 import uic, QtWidgets, QtCore
from time import sleep
# import pandas as pd

# Iniciando a aplicação
app = QtWidgets.QApplication([])

# Carregando as interfaces
primeira_tela = uic.loadUi('home.ui')
segunda_tela = uic.loadUi('cadastro.ui')
terceira_tela = uic.loadUi('email.ui')

# Retirando a borda da interface
primeira_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
primeira_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)
segunda_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
segunda_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)
terceira_tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
terceira_tela.setAttribute(QtCore.Qt.WA_TranslucentBackground)


# Mostrando a primeira tela
primeira_tela.show()

# Fechando a pagina Home e mostrando a pagina de cadastro
def home():
    primeira_tela.close()
    segunda_tela.show()

# Variaveis do certificado
def cadastro():
    for c in range(101):
        sleep(0.02)
        segunda_tela.progressBar.setValue(c)
        evento = str(segunda_tela.lineEdit.text())
        horario = str(segunda_tela.lineEdit_2.text())
        carga_horaria = str(segunda_tela.lineEdit_3.text())
    segunda_tela.close()
    terceira_tela.show()    


# Enviando certificado para o email
def email():
    for c in range(101):
        sleep(0.02)
        terceira_tela.progressBar_2.setValue(c)
    terceira_tela.label.setText('Certificado enviado com sucesso!')

# Chamando as funções
primeira_tela.pushButton_2.clicked.connect(home)
segunda_tela.pushButton.clicked.connect(cadastro)
terceira_tela.pushButton_2.clicked.connect(email)

# Executando a aplicação
app.exec()