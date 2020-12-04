#   PROGRMAÇÃO ORIENTADA A OBJETOS - POO

## CONCEITOS BÁSICOS

### **_ORIENTAÇÃO A OBJETOS - OO_**
        
- Programação Orientada a Objetos - POO:  método de programação que
  usa tipos de dados personalizados.
- Em vez de operar apenas com tipos de dados primitivos, podemos
  cosntruir novos tipos de dados.
- Baseia-se fundamentalmente no conceito de Objetos.

### **_VANTAGENS DA OO_**
      
  **COMERN**ada:
  
  - **C**onfiável    - o isolamento entre as partes gera software seguro,
                       ao alterar uma parte, nenhuma outra será afetada.
                       Fornece uma estrutura nodular para a construção de 
                       programas.
  - **O**portuno     - um software criado nos princípios de orientação a
                       objeto é oportuno, isto é ao se dividir tudo em 
                       partes, várias delas podem ser desenvolvidas em 
                       paralelo.
  - **M**anutenível  - a manutenção / modificação de um software se torna 
                       mais fácil e acaba beneficiando todas as partes 
                       que usarem o objeto.  O software se torna mais 
                       fácil de manter.
  - **E**xtensível   - o software não se torna estático, ele pode crescer 
                       para se manter útil.
  - **R**eutilizável - os objetos criados para um sistema podem ser utilizados
                       em outros projetos distintos, o que torna o 
                       desenvolvimento mais rápido.
  - **N**atural      - todo software orientado a objeto tem que ser natural,
                       isto é, uma coisa que é natural é mais fácil de 
                       entender, porque se foca mais nas funcionalidades do 
                       que nos detalhes de implemetação. Não é necessário 
                       conhecer a implemetacao interna de um objeto para 
                       poder usá-lo.             

### **_ABSTRAÇÃO_**

 _A orientação a objetos é baseada no conceito de abstração._
 
- Abstrair é selecionar apectos específicos de um problema a ser 
  analisado, deixando de lado outros aspectos.  Representar uma 
  entidado do mundo real em formas de idéias.
- Entidades abstraídas podem se comunicar entre si, por meio de
  troca de mensagens.
  
  De acordo como o autor Correia (2006):
  
    _**"Pelo princípio da abstração, isolamos os objetos que
        queremos representar do ambiente complexo em que se 
        situam, e nesses objetos representamos somente as 
        características que são relevantes para o problema 
        em questão."**_
    
  https://www.youtube.com/watch?v=dG7LlYne2VA

### **_OBJETO_*

  - Objeto: é uma coisa material ou abstrata que pode ser 
            percebida pelos sentidos e descrito por meio de 
            suas características, comportamento e estado atual.

  Todo objeto tem: ATRIBUTOS, MÉTODO E ESTADO (STATUS)

  Todo objeto vem a partir de uma classe (um molde)

  Classe -> é um "molde" que foi utilizado para gerar um objeto.

  Para se criar um objeto é necessário que se defina antes um Classe.

  Exemplo:

  Classe caneta:

    - Atributos:
      - modelo -> Caractere
      - cor -> Caractere
      - ponta -> Real
      - carga -> Inteiro
      - tampada -> Lógico

    - Métodos:
      - Método rabiscar()
          Se (tampada) então
            Escreva("Erro")
          senão
            Escreva("Rabisco")
          FimSe
        FimMétodo
      - Método tampar()
          tampada = verdadeiro
        FimMétodo
      - Método escrever()
        FimMétodo
      - Método pintar()
        FimMétodo

  FimClasse

![ClasseCaneta](https://user-images.githubusercontent.com/68357896/101168939-fdcc3400-361a-11eb-8ed6-acadd959c6bc.png)


[CanetaClasse01](https://user-images.githubusercontent.com/68357896/101169900-636cf000-361c-11eb-9058-595abf1e6152.png)

![ClasseCaneta02](https://user-images.githubusercontent.com/68357896/101171820-15a5b700-361f-11eb-926d-cea36e70b9ff.png)

  - Classe -> Define os atributos e métodos comuns que serão 
              compartilhados por um objeto.

  - Objeto -> É a instância de uma Classe.