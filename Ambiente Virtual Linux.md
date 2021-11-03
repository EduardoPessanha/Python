<CENTER>

# CRIANDO AMBIENTE VIRTUAL NO LINUX  

</CENTER>

##  Sintaxe  

Criando o ambiente virtual --> python3 -m venv /path/to/new/virtual/"venv"  

*   Onde '/path/to/new/virtual/"venv"' é o caminho/nome da pasta do ambiente virtual

Ativando o ambiente virtual --> source "venv"/bin/activate

*   Onde "venv" é o nome do seu ambiente virtual.


Exemplo  

```py

python3 -m venv "venv"

source "venv"/bin/activate

```  
  
## Outra forma de criar o ambiente virtual é usar o virtualenv:  


### \* Instalação:  

pip instal virtualenv  

### \* Inicialização de um novo ambiente virtual:  

* python3 -m virtualenv /path/to/new/virtual/<nome_da_pasta>

### \* Ativação do novo ambiente virtual:  

* \<nome_da_pasta>/script/activate (Windows)  
  
* source \<nome_da_pasta>/bin/activate (Linux)  

<!-- ### \* Desativação do novo ambiente virtual:  

* \<nome_da_pasta>/script/deactivate -->
