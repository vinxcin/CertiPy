![h1  CertiPy h1](https://user-images.githubusercontent.com/87454265/150715276-d1ac1e33-f2a3-4472-8c38-40ffccc8544a.png)

<h1 align="center">Gerador de Certificados <i>&</i> E-mail Automático <br></h1>


## 💚 Sobre o Projeto
<p>O projeto <b>CertiPy</b> visa integrar e automatizar dois processos repetitivos, bem como a geração de certificados e envio de e-mail, através da implementação de um algoritmo desenvolvido na linguagem de programação Python. Para isso, o algoritmo como um todo foi divido em três partes, que serão discorridos detalhadamente nos tópicos a seguir:</p>

- <b> 1º - </b> Nesta etapa, foi importado um dataset com extensão <b>.csv</b> com os dados populados atráves do google forms com as seguintes colunas: E-mail e Nome. A partir disso, os dados do dataset foram armazenados em um dicionário, sendo atribuidos aos "values" os dados da coluna "Nome" e como "keys" foram atribuidos os dados da coluna "E-mail."

- <b> 2º  - </b> Continuando, nesta etapa, foi criado um loop de repetição dentro de uma função para percorrer todos os valores dos dicionários com os nomes junto com a lib de manipulação de imagem gerando todos os certificados.


- <b> 3º  - </b> Após a geração de todos os certificados com sucesso, foi criada uma função para que os certificados fossem enviados aos seus respectivos proprietários. Para isso, foram passados alguns parâmetros e credenciais para acesso ao gmail.

<br>

## 📟 Video Demonstração

<a href="https://youtu.be/xtLaCaP0S0I"> ![image](https://user-images.githubusercontent.com/87454265/151272628-8a936003-fdb1-4690-9df2-e93133994691.png) </a>

<p align="center">Para assistir clique acima</p>


<br>

## 🔧 Desenvolvedor 
<table style="width:80%">
   <tr align="center">
    <td>📷</td>
    <td>Nome</td>
    <td>Cargo</td>
  </tr>
  <tr>
    <td><img src="https://media-exp1.licdn.com/dms/image/C4E03AQGbWtaRMqRQbg/profile-displayphoto-shrink_400_400/0/1642540012466?e=1648684800&v=beta&t=6LmQQrmmETIzg1p36AdsqaHUi_vo7opLpg5oROwyNgs" width="120">
</td>
    <td><a href="https://www.linkedin.com/in/vinicius-carvalho-rosa/" target="_blank">Vinicius Carvalho Rosa</a></td>
    <td>Data & IoT Engineer at BlueShift</td>
  </tr>
</table>

<br>

## 🐍 Ferramentas Utilizadas

<img align="center" alt="Vini-Python" height="20" width="30" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> Python <br><br>
<img align="center" alt="Vini-Python" height="20" width="30" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg"> Jupyter Lab <br><br>
<img align="center" alt="Vini-Python" height="20" width="30" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/qt/qt-original.svg"> Qt Designer <br><br>
<img align="center" alt="Vini-Python" height="20" width="30" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/canva/canva-original.svg"> Canva 

<br>

## 👽 Dependências 
- pip install PyQt5Designer 
- pip install email
- pip install mime
- pip install email-to
