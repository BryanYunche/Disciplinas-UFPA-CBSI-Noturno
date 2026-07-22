## Problema 01: O que é um qubit do ponto de vista matemático da teoria da informação? Através de um exemplo simples, como podemos construir um qubit na prática?

Do ponto de vista matemático, ele é um vetor cuja existência é definida por um conjunto de regras que o condicionam a um_ **espaço vetorial complexo bidimensional**. Isto é, diferentemente de um bit clássico que é representado estritamente por 1 ou 0, o qubit é representado por uma combinação linear da base computacional. Geralmente para a realização dos cálculos é utilizada a **Notação de Dirac** _para representar esses vetores e outras operações. É importante entender que, por ser uma combinação linear dos estados de base_ ∣0⟩ _e_ ∣1⟩_, o qubit assume uma propriedade chamada sobreposição. Note que não estou dizendo que é um valor que muda constantemente de forma caótica; ele é regido por amplitudes exatas e, quando medido ou observado, ele_ **é obrigado a colapsar e assumir um valor clássico**_. Outro ponto relevante sobre o qubit é não confundir o estado de sobreposição com emaranhamento. Uma forma fácil de evitar confusão nos estudos iniciais é pensar que para existir sobreposição é necessário apenas um qubit, pois é uma característica individual, e **para o estado de emaranhamento é necessário um sistema composto de dois ou mais qubits**_.

Tendo definido o conceito acima, posso construir um qubit na prática utilizando sistemas físicos do mundo real que possuam a capacidade de sobreposição como característica. Isto é, sistemas que possam habitar um _continuum_ de estados entre dois níveis de energia ou propriedades físicas formalizáveis. Um exemplo clássico disso é utilizar **dois níveis de energia de um elétron em um átomo** ou a **polarização de uma partícula de luz (fóton)**. Enquanto não está sendo "observado" pelo ambiente, o sistema evolui em uma sobreposição desses dois estados (misturando, por exemplo, o nível de energia fundamental e o excitado). Mas, caso eu decida "observá-lo", ou melhor, "medi-lo" no final do cálculo, a sobreposição é interrompida e o qubit é obrigado a colapsar, me entregando como resultado um valor clássico bem definido e mutuamente exclusivo (0 ou 1).

---

## Problema 02: O que é uma porta quântica? Qual a diferença entre a porta clássica e a porta quântica? O que é a computação quântica?

Tendo conhecimento que a unidade fundamental de informação da computação quântica é um qubit que necessariamente é um **vetor**, precisamos de algo que possa manipula-los para que a informação não seja apenas algo estático sem valor ou "aleatório", para isso utilizamos as portas quânticas, que similar as portas clássicas tem como função manipular a unidade fundamental de informação e criar sistemas. Para manipular um vetor utilizamos uma matriz unitária, essa matriz pode manipular um ou mais qubits por vez, mas para ter melhor entendimento vamos imaginar que ela está manipulando apenas um qubit. Quando aplicado essa porta quântica obtemos uma combinação linear que modifica o estado do quibit.

A principal diferença entre as portas clássicas e quânticas é a propriedade de irreversibilidade, isto é, uma porta lógica clássica não pode ser reversível e ainda perde informações, é uma característica física do sistema e intrínseco da computação clássica. Para a computação quântica isso não ocorre, por **regra matemática** como as portas são representadas por uma matriz, quando aplicadas essas matriz sempre vão possuir uma inversa que possa retornar o estado anterior da porta.

Em resumo, a computação quântica pode ser considerado um outro paradigma que processa e interpreta a informação baseado na mecânica quântica, isto é, ele não utiliza as leis da física clássica. Isso ocorre pela dimensão microscópica que a computação quântica atua, a física clássica se utiliza do mundo macroscópico para poder interpretar e construir sistemas e circuitos que possam ser inferidos usando a física clássica.

---

## Problema 03: Seja um espaço vetorial complexo H com vetores de base |0⟩ e |1⟩ , e A um operador linear de *H* para *H*, tal que A|0⟩ = |1⟩ e A|1⟩ = |0⟩ . Forneça uma representação matricial para A nas bases de entrada e saída |0⟩ e |1⟩ . Existe alguma semelhança entre o operador A acima descrito e alguma porta lógica quântica? 

![[ava-01-prb-03.jpg]]

---
## Problema 04: Seja um espaço vetorial complexo H com vetores de base |0⟩ e |1⟩ , e B um operador linear de *H* para H, tal que B|0⟩ = |0⟩ e B|1⟩ = − |1⟩ . Forneça uma representação matricial para B nas bases de entrada e saída |0⟩ e |1⟩ . Existe alguma semelhança entre o operador B acima descrito e alguma porta lógica quântica?

![[ava-01-prb-04.jpg]]


---
## Problema 05: Seja um espaço vetorial complexo H com vetores de base |0⟩ e |1⟩ , e C um operador linear de H para H, tal que C|0 = (|0⟩ +|1⟩ )/ √2 e C|1 = (|0⟩ − |1⟩ )/ √2. Forneça uma representação matricial para C nas bases de entrada e saída |0⟩ e |1⟩ . Existe alguma semelhança entre o operador C acima descrito e alguma porta quântica?

![[ava-01-prb-05.jpg]]

---

## Problema 06: Mostre que, usando a porta quântica de 2-qubits CNOT (Not-Controlado), é possível usar circuitos quânticos para copiar informação clássica.

![[ava-01-prb-06.jpg]]

---

## Problema 07: Mostre que, usando a porta quântica de 2-qubits CNOT (Not-Controlado), é impossível fazer uma cópia de estado quântico desconhecido, ou seja, não podemos copiar qubits que são completamente desconhecidos.

![[ava-01-prb-07.jpg]]

---

## Problema 08: Mostre um passo-a-passo de um circuito quântico para criar estados de Bell de 2-qubits, maximamente emaranhado. Qual utilidade dos estados de Bell? Forneça exemplos. 

![[estado-emaranhado.png]]

Eu utilizo o compose para ficar claro de forma visual como foi monta os estádos de bell, iniciando os qubits com 0.

Em seguida aplico a porta hadamard nos qubits fazendo com que entrem em superposição ao jogar o qubit para o angulo de 45 º, obtendo um resultaod de 
$$|\psi_1\rangle = |0\rangle \otimes \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) = \frac{|00\rangle + |01\rangle}{\sqrt{2}}$$

Aplicando a CNOT chegamos a este estado bipartido: 
$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$
 Isto é, existe 50% de chance de o estado emaranhado ser 00 e 50% de chance de ser 11.
 
---
## Problema 09: Qual a finalidade do circuito de Teleportação Quântica? Adote o livro texto da disciplina como referência.

A teleportação quântica parece algo que não exige a necessidade de ser explicado a finalidade, informação é destruída de um lado e reconstruída do outro. Do ponto de vista teórico parece simplex, mas considerando a infraestrutura atual a qual prevalece a computação clássica e os meios de comunicação clássicos o envio de um quibit ou uma informação quântica tornasse um trabalho hérculeo. O teleporte quântico foi criado para sanar esse problema permitindo que seja trocada informação quântica entre dois pontos por meio dos estados emaranhados ou melhor os estados de bell. Partindo da premissa que duas parte possuem qubits complementares e emaranhados sendos estes obtidos previamente, imagine que essas partes se separam por uma distância X e que tem que trocar informação, essa distância não possue um meio de comunicação quântico e sim apenas clássico pela qual se correspondem, a comunicação pode ser realizada pelos meios clássicos quando um ponto envia um conjunto de instruções para o outro ponto sobre como aplicar um operador sobre o qubit que está em posse para concertar e reconstruir a informação, note que eu não copiei a informação de um qubit e sim utiliei o emaranhamento entre dois qubits para poder obter a informação de um.

A finalidade do circuito de Teleportação Quântica é fornecer uma técnica para transferir um estado quântico de um local para outro, mesmo na ausência de um canal de comunicação quântica direto. Do ponto de vista teórico parece simples, mas, considerando a infraestrutura atual na qual prevalece a comunicação clássica, o envio direto de um qubit torna-se um trabalho hercúleo.

Tendo isso em vista o teleporte quântico foi criado para resolver esse problema. Partindo da premissa de que duas partes possuem qubits complementares e emaranhados ou estados de Bell, distribuídos previamente, imagine que essas partes estejam separadas por uma distância X e possuam apenas um meio de comunicação clássico. O emissor faz o qubit da mensagem interagir com a sua metade do par emaranhado e realiza uma medição. Essa medição gera bits clássicos que são enviados como um conjunto de instruções para o receptor. Com essas instruções clássicas, o receptor aplica um operador no qubit que está em sua posse para consertar a fase e reconstruir a informação original. É importante notar que não ocorre a cópia da informação, pois a informação original é destruída na medição do lado do emissor.

Em resumo um circuito de teleporte quântico tem a finalidade de servir como uma ferramenta essencial para comunicação quântica em redes ruidosas e para a construção de portas lógicas tolerantes a falhas.

---

## Problema 10: Demonstre matematicamente, usando as bases de qubits (vetores de base |0⟩ e |1⟩ ), o circuito de teleporte quântico.

Obs: Não entendi como faz ainda a teleportação quantica:

---

## Problema 11: O que é o paralelismo quântico? Forneça um circuito quântico que demonstra claramente esse conceito. Existe diferença entre o paralelismo clássico e quântico?

Obs: Não entendi como funciona o Paralelismo

---

## Problema 12: Verifique que |w⟩ = (1, 1) e |v⟩ = (1, -1) são ortogonais. Quais são as formas normalizadas desses vetores?

![[ava-01-prb-12.jpg]]

---

## Problema 13: As matrizes de Pauli (figura 2.2, pag. 65 do livro texto) podem ser consideradas como operadores com relação as bases ortonormais |0⟩ e |1⟩, no espaço de Hilbert bidimensional. Expresse cada um desses operadores na notação de produto externo.

![[ava-01-prb-13.jpg]]

---

## Problema 14: Determine os autovetores, autovalores e as representações diagonal das portas quânticas X, Y e Z ( ou matrizes de Pauli na Mecânica Quântica).

![[ava-01-prb-14-01.jpg]]
![[ava-01-prb-14-02.jpg]]
![[ava-01-prb-14-03.jpg]]

---
## Problema 15: Segundo o livro texto da disciplina, forneça os postulados da mecânica quântica, com pelo menos, um exemplo prático de cada postulado.

Postulado 01: Um sistema físico isolado tem associado a ele um espaço vetorial complexo com produto interno, conhecido como o **espaço de estados** do sistema. O sistema é completamente descrito pelo seu vetor de estado, que é um vetor unitário habitando esse espaço de estados.

Exemplo Prático P1: Um qubit, como visto na questão 01 para a construção disso temos que considerar sistemas físicos do mundo real que possuam a capacidade de sobreposição como característica. Utilizando o exemplo dado na questão 01, devemos *utilizar **dois níveis de energia de um elétron em um átomo** ou a **polarização de uma partícula de luz (fóton)**. Enquanto não está sendo "observado" pelo ambiente, o sistema evolui em uma sobreposição desses dois estados (misturando, por exemplo, o nível de energia fundamental e o excitado). Mas, caso eu decida "observá-lo", ou melhor, "medi-lo" no final do cálculo, a sobreposição é interrompida e o qubit é obrigado a colapsar, me entregando como resultado um valor clássico bem definido e mutuamente exclusivo (0 ou 1).*


Postulado 2: A evolução de um sistema quântico fechado ao longo do tempo é descrita por uma **transformação unitária**. Isso significa que o estado ∣ψ⟩ do sistema em um momento t1​ está relacionado ao estado ∣ψ′⟩ em um momento t2​ por meio de um operador unitário U, seguindo a equação ∣ψ′⟩=U∣ψ⟩. 

Exemplo Prático P2: Podemos demonstrar a aplicação de uma porta quântica durante a execução de um algoritmo. Dado que um computador quântico possui um qubit no estado inicial ∣0⟩, ao aplicar uma porta lógica NOT ou Pauli-X  é a evolução temporal que força o sistema a transitar para o estado de saída ∣1⟩. 

Postulado 3: As medições em sistemas quânticos são descritas por uma coleção de **operadores de medição** {Mm​}, onde o índice m representa os resultados possíveis. Se o estado do sistema for ∣ψ⟩ antes da medição, a probabilidade de ocorrer o resultado exato m é de p(m)=⟨ψ∣Mm†​Mm​∣ψ⟩. Quando medido, o estado superposto é destruído e colapsa para o estado pós-medição.

Exemplo Prático P3: A **leitura final de um qubit na base computacional** no término de um algoritmo como o de teleporte quântico. Imagine um qubit em superposição no estado inicial (∣0⟩+∣1⟩​)/2. Ao aplicarmos os operadores de medição, a matemática deste postulado nos diz que, na prática do laboratório, observaremos o resultado lógico "0" em 50% das vezes , ou o resultado "1" nas outras 50% das vezes. Isso ocorre pois o vetor unitário que representa o qubit encontrasse em um angulo de 45º em relação as suas bases ortogonais ∣0⟩ e∣1⟩

Postulado 4: O espaço de estados de um sistema físico composto é o **produto tensorial** dos espaços de estados dos sistemas físicos que o compõem. Além disso, se os sistemas individuais (numerados de 1 a n) forem preparados em seus respectivos estados ∣ψi​⟩, o estado global conjunto de toda a máquina será descrito por ∣ψ1​⟩⊗∣ψ2​⟩⊗⋯⊗∣ψn​⟩.

Exemplo Prático P4: Um dos exemplos mais interessantes e amplamente debatidos na computação quântica é o emaranhamento, o emaranhamento é um exemplo excelente para perceber como o produto tensorial dos espaços complexos descritos podem ter um comportamento singular. Para isso é importante falar sobre os Estados de Bell. Quando queremos que dois qubits trabalhem juntos, e que possam se comunicar por meio de teleporte ou protocolo de comunicação superdensa, unimos no mesmo espaço de estados através do produto tensorial. O exemplo máximo disso é o par EPR, ​∣00⟩+∣11⟩/2​. Este estado demonstra um sistema composto indivisível onde a informação reside no vínculo entre os qubits, separá-los novamente como o simples produto de dois qubits isolados. Quando digo separa-los quero dizer "desemaranhar" eles possuem um comportamento único, o que é fundamental para outras aplicações como visto nos problemas de teleportação e protocolo de codificação superdensa.

---
## Problema 16: O que é o protocolo de codificação superdensa? Quais postulados quânticos são utilizados neste protocolo?

Semelhante ao protocolo de Teleportação, a codificação superdensa utiliza os Estados de Bell. O processo parte da premissa de que duas partes (A e B), separadas por uma distância X e conectadas por um canal quântico, (diferente do teleporte quântico), compartilham previamente um par de qubits emaranhados. Dependendo da informação clássica de 2 bits que o ponto A quer enviar (00, 01, 10 ou 11), o ponto A aplica portas lógicas específicas (Identidade, X, Z ou ZX) apenas na sua metade do par emaranhado. Em seguida, é enviado esse único qubit pelo canal quântico para o ponto B. Ao receber esse qubit, o ponto B realiza operações conjuntas (portas CNOT e Hadamard) utilizando o qubit recebido e o que ele já possuía. Após essas operações, ele mede o sistema e consegue extrair os exatos 2 bits clássicos originais.

Em resumo o protocolo de codificação superdensa realiza algo impossível para a computação clássica, **enviar dois bits clássicos de informação utilizando a transmissão física de apenas um único qubit**.

É envolvido nesse processo todos os quatro postulados da Computação quântica, o postulado 01 é visto quando definido o espaço de vetorial complexo dos dois qubits em sobreposição, que serão emaranhados por meio do produto tensorial visto no postulado 04, as aplicações dos operadores unitários no par emaranhado que envia a informação é resultado do estudo do postulado 02 que define os operadores unitários e por fim o postulado 03 é visto quando o sistema é medido e colapsa para extrair os 2 bit clássicos enviados pelo qubit.

Video referência: https://www.youtube.com/watch?v=-a6UOyv0548

---
## Problema 17: Utilizando a plataforma IBM Quantum via interface gráfica (Compose), explique a conexão entre os gráficos (3 gráficos) disponibilizados por essa interface e os postulados da Mecânica Quântica. Demonstre explicando cada passo através prints screen de cada gráfico e sua relação com dado postulado da Mecânica Quântica.

#### Interface Statevactor
![[statevector.png]]

O statevector mede a amplitude do sistema, ele é um complementar dos gráfico de probabilidade só que mais podereso pois pode mostrar probabilidade negaticas e até mesmo complexas, possibilidando assim poder entender melhor como mexer no estado de interferência do sistema para chegar ao resultado esperado.

---

#### Q-Sphere
![[q-sphere.png]]

Pode se confundir essa Q-Sphere com a esfera de bloch, as a principal difereça é que a esfera de bloch mostra um unico qubit. Essa esfera da IBM tem três parametros fundamentais, além de mostrar mais de um qubit ela mostra o resultado possivel. O primeiro parâmetro importante é o tamanho da bolinha que representa a probabilidade do estado; O segundo parâmetro é a cor da bilinha que mostra qual fase ela está e por ultimo a direção de onde está a pontado a seta.

---
#### Probabilidades
![[probabilidades.png]]
 
 O gráfico de probabilidade mostra qual a probabilidade dos resultados em bits clássicos ao medir o sistema que está sendo feito no compose naquele momento, por isso ele fica mudando pois a cada porta e modificação no circuito você mexe nas probabilidades ao colapsar.

---
Em resumo, o gráfico de probabilidades serve para mostrar as chances reais de medição ao final do sistema em porcentagens de 0 a 100% dado a combinação de quibits utilizada; Statevactor mostra o gráfico das amplitudes do sistema, diferente do gráfico de probabilidades o Statevector pode ser negativo e complexo, sendo uma ferramenta muito poderosa para analisar a interferência antes da medição final do sistema; Por fim a Q-Sphere mostra em um globo as amplitudes, probabilidades e fases de forma visual a fim de deixar claro como os qubits interagem entre si.

---
## Problema 18: Utilizando a plataforma IBM Quantum via interface gráfica (Compose), realize o protocolo de Codificação Superdensa. Demonstre explicando cada passo através prints screen.

- Utilizando o exemplo dos slides de codificação superdensa primeiro precisamos emaranhar os estados utilizando a porta hadamard e uma CNOT.
![[ava-01-prb-18-01.png]]
- Como eu quero passar a informação 01 eu mando os bitis 11, para mandar 11 apliquei duas portas NOT nos qubits e colapsei ele e enviei pelo canal Clássico.
![[ava-01-prb-18-02.png]]
- Aplicamos uma Porta NOT e uma Z com os condicionais neles caso seja 1 o bit clássico enviado.
![[ava-01-prb-18-03.png]]
- Agora ainda no canal quantico após a devida aplicação das portas necessárias para a decodificação aplicamos uma CNOT e uma Hadamard e medimos enfim a informação clássica de 2 bits utilizando apenas um qubit enviado.

Obs: Utilizei uma sequência de barreiras para destacar o canal quantico que foi enviado o qubit.

![[ava-01-prb-18-04.png]]

---
## Problema 19: Utilizando a plataforma IBM Quantum via interface gráfica (Compose), realize o protocolo de Teleportação Quântica. Demonstre explicando cada passo do circuito através prints screen. Explique o seu resultado com relação ao qubit teleportado.

Obs: Não entendi como faz ainda a teleportação quantica:

---
## Problema 20: Utilizando a plataforma IBM Quantum via interface gráfica (Compose), demonstre que o protocolo de Teleportação Quântica não funciona se a informação clássica não for transmitida para o receptor, no caso, o Bob. Demonstre explicando cada passo através prints screen. Qual é o qubit ou estado quântico que Bob tem se a informação clássica não for transmitida. Demonstre usando os gráficos do Compose.

Obs: Não entendi como faz ainda a teleportação quantica: