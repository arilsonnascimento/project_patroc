## project_patroc

project_patroc é um projeto desenvolvido para a disciplina de Linhas de Transmissão e Ondas do curso de Engenharia Elétrica da UFRN. O nome “project_patroc” é uma homenagem ao professor José Patrocínio, carinhosamente apelidado de "Patroc" pelos alunos. O próprio professor se refere a si mesmo dessa forma, o que tornou o apelido uma marca da disciplina.

Embora não tenha sido exigido formalmente pelo professor, resolvi me desafiar a desenvolver este código e torná-lo acessível publicamente. O objetivo inicial é implementar o código em Python, disponibilizá-lo no GitHub e hospedá-lo de forma gratuita no Vercel, com uma interface acessível por meio de uma página HTML.


## Abordagem


Os tópicos tratados aqui são Propagação de Ondas Eletromagnéticas e Linhas de Transmissão, capítulos 10 e 11, respectivamente, do Sadiku (Elementos de eletromagnetismo I Matthcw N. O. Sadiku - 3ª ed).

# Propagação de Ondas Eletromagnéticas

Os tópicos dessa seção podem ser traduzidos em cálculos envolvendo a propagação de ondas em diferentes meios, análise de perdas e características de transmissão.

 * Ondas em dielétricos com perdas: Aqui, fórmulas que envolvem a tangente de perdas podem ser aplicadas para diferentes materiais, como feito no exemplo que já foi convertido para Python.
 * Ondas planas no espaço livre e em condutores: O desenvolvimento de expressões para o comportamento de ondas, levando em consideração permissividade e condutividade de diferentes meios, pode ser tratado em funções específicas.
 * Vetores de Poynting e potência: Pode-se desenvolver uma função que calcule a densidade de potência transportada por uma onda eletromagnética, usando os campos elétricos e magnéticos.
 * Reflexão e incidência de ondas planas: Desenvolver expressões para os coeficientes de reflexão e transmissão de ondas pode ser outra função importante, permitindo que o usuário insira ângulos de incidência e propriedades dos meios.

# Linhas de Transmissão

Nesta seção, o projeto deve contemplar a formulação matemática e implementação das equações características de linhas de transmissão. Alguns pontos a considerar:

* Parâmetros das linhas de transmissão: Implementar cálculos dos parâmetros R, L, G e C, utilizando diferentes frequências e materiais.
* Equações das linhas de transmissão: Abordar as equações telegráficas, que são centrais no estudo de linhas de transmissão, e representá-las em termos de tensões e correntes ao longo da linha.
* Impedância de entrada e ROE: Um módulo para cálculo de impedância de entrada em função da distância da carga, permitindo simular linhas de transmissão com diferentes terminações e calcular a relação de onda estacionária (ROE).
* Carta de Smith: Aqui pode-se considerar o desenvolvimento de uma interface gráfica que represente as impedâncias e admitâncias ao longo da linha, algo que pode ser feito em Python usando bibliotecas de visualização como matplotlib.
* Transientes e linhas de microfita: Finalmente, transientes e microfitas podem ser implementados em cálculos que lidem com fenômenos de reflexão e de propagação de sinais em meios não ideais.
