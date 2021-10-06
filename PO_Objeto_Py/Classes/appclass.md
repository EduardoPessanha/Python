```py
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
```  

## A programação orientada a objetos (**POO**) é um paradigma de programação baseado no conceito de **objetos**, que podem conter dados e código:  

*  ## **dados** na forma de campos (geralmente conhecidos como atributos ou propriedades)
*  ## **código**, na forma de procedimentos (freqüentemente conhecido como métodos).
<br>  

### Uma característica dos objetos é que os próprios procedimentos de um objeto podem acessar e, muitas vezes, modificar os campos de dados de si mesmo (os objetos têm uma noção de **this** ou **self**) Na **POO**, os programas de computador são projetados a partir de objetos que interagem uns com os outros. As linguagens **POO** são diversas, mas as mais populares são baseadas em **classes** , o que significa que os objetos são instâncias de **classes** , que também determinam seus tipos.<br><br> 

### Na programação orientada à objetos o foco é na criação de objetos que contem tanto os dados quanto as funcionalidades.<br><br>

### Em Python, todo valor é na verdade um objeto. Seja uma string, uma lista, ou mesmo um inteiro, todos são objetos. Programas manipulam esses objetos realizando computações diretamente com eles ou chamando os seus métodos (ou seja, pedindo que esses objetos executem seus métodos).<br><br>
### Para ser mais específico, nós dizemos que um objeto possui um 'estado' e uma coleção de métodos que ele pode executar. O 'estado' de um objeto representa as coisas que o objeto sabe sobre si mesmo. Por exemplo, um objeto tartaruga, possui um estado que representa a sua posição, sua cor, sua direção, etc. Cada tartaruga também tem a capacidade de se mover para a frente, para trás, ou virar para a direita ou esquerda. Cada tartaruga é diferente pois, embora sejam todas tartarugas, cada uma tem um estado diferente (como posições diferentes, ou orientações, etc)<br><br>  

### As definições de classes podem aparecer em qualquer lugar em um programa, mas são geralmente perto do início (após os comandos import). As regras de sintaxe para a definição de uma classe são as mesmas de outros comandos compostos. Há um cabeçalho que começa com a palavra-chave 'class', seguido pelo nome da classe e terminando com dois pontos.<br><br>

### Toda classe deve ter um método com o nome especial **\__init__**. Este método de inicialização, muitas vezes referido como o '**construtor**', é chamado automaticamente sempre que uma nova instância da Classe é criada. Ela dá ao programador a oportunidade de configurar os atributos necessários dentro da nova instância, dando-lhes seus estados/valores iniciais. O parâmetro **self** (qe poderia ser qualquer outro nome, mas ninguém nunca faz!) é definido automaticamente para referenciar o objeto recém-criado que precisa ser inicializado.<br><br>

```py
class Ponto:
    """
    Criando a minha primeira Class!!!!!
    Classe para representar e/ou manipular coordenadas x, y
    """
    def __init__(self) -> None:   # *Construtor
        """
        ->Cria um novo ponto na origem
        """
        self.initx = 0
        self.inity = 0


p = Ponto()  # *instancie um objeto do tipo Ponto (Instanciar=criar um objeto)
q = Ponto()  # *e faça um segundo ponto

print("\nNada parece ter acontecido com os pontos\n")
print(p, 'id:', id(p), '\n')
print(q, 'id:', id(q), '\n')
print(p is q)
```
<br>

### Durante a inicialização dos objetos, criamos dois atributos chamados x e y
para cada um, e ambos com o valor 0.
Podemos observar que quando executamos o programa, nada acontece.
Felizmente este não é bem o caso. De fato, dois Pontos foram criados, cada um
com coordenadas x e y com valor 0. No entanto, como nós não pedimos aos pontos
para fazerem alguma coisa, não vemos resultado algum.

As variáveis p e q recebem referências a dois novos objetos Ponto. Uma função
Ponto() que cria uma nova instância do objeto é chamado de construtor, e cada
classe fornece automaticamente uma função construtora que tem o mesmo nome da
classe.
"""


# _Melhorando o Nosso Construtor:
"""
Até agora o nosso construtor só pode criar pontos na posição (0,0). Para criar um ponto na posição (7, 6) é preciso fornecer alguma capacidade adicional para passar informações para o construtor. Como os construtores são simplesmente funções com nomes especiais, podemos usar parâmetros para fornecer as informações específicas.

Nós podemos tornar o construtor da nossa classe mais geral, colocando parâmetros extras no método \__init__.<br><br>

```py
class Ponto:
    """
    Criando a minha primeira Class!!!!!
    Classe para representar e/ou manipular coordenadas x, y
    """
    def __init__(self, initx, inity) -> None:   # *Construtor
        self.initx = initx
        self.inity = inity


p = Ponto(6, 7)
```
# _Agora quando nós criamos novos pontos, podemos simplesmente fornecer os valores de x e y como argumentos. Quando o ponto é criado, os valores de 'initX' e 'initY' são atribuidos ao 'estado' do objeto.

# _Adicionando Outros Métodos à Nossa Classe:

"""
A principal vantagem de usar uma classe como Ponto em vez de algo como uma simples tupla (7, 6) agora se torna aparente. Podemos acrescentar 'métodos' para a classe Ponto que são operações úteis para trabalhar com pontos.
Se tivéssemos optado por usar uma simples tupla para representar o ponto, não teríamos essa capacidade. Criar uma classe como Ponto traz um “poder organizacional” excepcional para nossos programas e para o nosso pensamento. Podemos agrupar as operações que fazem sentido, e os tipos de dados a que pertencem, e cada instância da classe pode ter seu próprio estado.

Um 'método' se comporta como uma função, mas ele é chamado de uma instância específica. Os 'métodos' são acessados usando a notação de 'ponto'.
"""


class Ponto:
    """
    Criando a minha primeira Class!!!!!

    Classe para representar e/ou manipular coordenadas x, y
    """

    def __init__(self, initx, inity) -> None:   # *Construtor

        self.initx = initx
        self.inity = inity

    def getx(self):         # *Método
        return self.initx

# _Uma coisa a notar é que mesmo que o método getX não precise de qualquer outra informação como parâmetro para fazer o seu trabalho, ainda há um parâmetro formal, 'self'.
# _Todo método definido em uma classe que opere em objetos dessa classe terá 'self' como seu primeiro parâmetro. Mais uma vez, este serve como referência para o objeto em si, que por sua vez permite o acesso aos dados de estado no interior do objeto.

    def gety(self):         # *Método
        return self.inity

    def coordenada(self):         # *Método
        x = self.initx
        y = self.inity
        return print(f'\nAs cordenadas do ponto são: x = {x} e y = {y}\n')

    def dist_origem(self):
        """
        Calcula a distância do ponto até a origem
        """
        dist = (self.initx**2 + self.inity**2)**0.5
        return dist

        # _Nota-se que o chamador 'dist_origem()' não fornece nenhum argumento para suprir o valor do parâmetro self. Isso é verdade também para todas as chamadas de 'métodos'. A definição sempre terá um parâmetro adicional (self) quando comparado a chamada.


p = Ponto(7, 6)

print('\nx = ', p.getx())
print('\ny = ', p.gety())
p.coordenada()
print(f'\nA distância do ponto até a origem é {p.dist_origem()}\n')


# _Objetos Como Argumentos e Parâmetros:

# _Podemos passar um objeto como um argumento da forma habitual para uma função, para que esta possa controlar e usar qualquer instância do objeto que lhe seja passado.

def distancia(ponto1, ponto2):
    """
    Calcula a distância entre dois pontos
    """
    xdif = ponto2.getx() - ponto1.getx()
    ydif = ponto2.gety() - ponto1.gety()

    dif = (xdif**2 + ydif**2)**0.5

    return dif


p = Ponto(3, 4)
q = Ponto(0, 0)

print('\n', distancia(p, q))

# _Conversão de um Objeto para um String:
"""

_A maioria dos programadores de orientação à objetos não fariam o que acabamos de fazer em print_point. Quando trabalhamos com classes e objetos, uma alternativa é incluir um novo método na classe, mas não gostamos de métodos tagarelas que chamam print. A melhor alternativa é ter um método para que toda instância possa produzir um string que o represente. Vamos inicialmente chamar esse método de 'to_string':
"""

print(p)        # --> <__main__.Ponto object at 0x7fcade5e3f70>

# _A função print mostrada acima produz um string que representa o Ponto p. O padrão fornecido pelo Python diz que p é um objeto do tipo Ponto. No entanto, ele não diz nada sobre o estado específico do ponto.

# _Podemos melhorar esta representação se incluirmos um método especial chamado '__str__'.
# _Observe que este método usa a mesma convenção de nomes como o construtor, que é dois sublinhados antes e depois do nome.
# _É comum no Python utilizar essa técnica para dar nomes aos métodos especiais.

# _O método '__str__' é responsável por retornar uma representação na forma de um string, tal como definido pelo criador da classe.
# _Em outras palavras, você, como programador, deve escolher como um ponto deve ser impresso. Neste caso, podemos decidir que a representação em string irá incluir os valores de x e y, bem como algum texto de identificação. É necessário que o método '__str__' crie e retorne um string.


class Ponto:
    """
    Classe para representar e/ou manipular coordenadas x, y
    """

    def __init__(self, initx, inity) -> None:   # *Construtor

        self.initx = initx
        self.inity = inity

    def __str__(self):      # *to_string
        return f"x = {self.initx}, y = {self.inity}"

    def getx(self):         # *Método
        return self.initx

    def gety(self):         # *Método
        return self.inity

    def coordenada(self):         # *Método
        # x = self.initx
        # y = self.inity
        # return print(f'\nAs cordenadas do ponto são: x = {x} e y = {y}\n')
        return print(f'\nAs cordenadas do ponto são: x = {self.initx} e y = {self.inity}\n')

    def dist_origem(self):
        """
        Calcula a distância do ponto até a origem
        """
        dist = (self.initx**2 + self.inity**2)**0.5
        return dist


p = Ponto(5, 6)

print(p)        # --> x = 5, y = 6

# _Ao executar o programa acima, podemos ver que a função print agora mostra o string na forma que escolhemos.
# _Quando um programador muda o significado de um método especial dizemos que substituimos o método. 
# _Note também que a função 'str' para conversão de tipo usa o método '__str__' que nós fornecemos.

# _Instâncias e Valores de Retorno:
"""
Funções e métodos podem retornar objetos. Esta é, na verdade, nada de novo, já que tudo em Python é um objeto e temos retornado valores por algum tempo. A diferença aqui, é que nós queremos que o método crie um objeto usando o construtor e depois que retorne um novo objeto como o valor do método.

Suponha que você tenha um objeto ponto e deseja encontrar o ponto médio entre ele e algum outro ponto alvo. 
Gostaríamos de escrever um método, chamado de "caminho_médio" que recebe outro Pinto() como parâmetro e retorne o Ponto() que está a meio caminho entre o ponto e o alvo.
"""







# _Referências:
# *https://www.youtube.com/watch?v=RhtsCbKyYoA&t=1110s
# *https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html
