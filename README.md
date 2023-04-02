# _BowlingScoreKeeper_
Repositório base para experimento de TCC II relacionado a TDD.

## Instruções

O objetivo é desenvolver uma aplicação que consegue calcular o placar de um jogo de boliche completo (de apenas um jogador). Não há uma interface gráfica. Você pode trabalhar apenas com classes/objetos e com testes unitários utilizando o pacote `unittest` (pacote da biblioteca padrão Python). Você não precisa criar uma função `main`.

O **game** (jogo em português) consiste de 10 **frames** (quadros em português) como mostrado mais abaixo. Em cada quadro/frame, o jogador tem duas oportunidades para derrubar 10 pinos. O **score** (placar em português) de cada quadro/frame é o total de número de pinos derrubados, mais a soma de bônus no caso de strikes e spares.

Um **spare** é quando um jogador derruba todos os 10 pinos em duas tentativas. O bônus para esse quadro/frame é do número de pinos derrubados na próxima tetativa. Então, no terceiro quandro/frame abaixo, o placar/score é de 10 (o número total de pinos derrubados) mais um bônus de 5 (o número de pinos derrubados na próxima tentativa).

Um **strike** é quando um jogador derruba todos os 10 pinos em sua primeira tentativa. O bônus para esse quadro/frame é o valor das próximas duas tentativas.

No décimo quadro/frame, se um jogador fizer um spare ou um strike, ele deve jogar as tentativas a mais para calcular o score/placar total do quadro/frame. Entretando, não mais que 3 tentativas podem ser feitas no último quadro/frame.

![image](https://user-images.githubusercontent.com/43941670/221432081-17c0625a-0f1a-4254-8a24-e5577ec83ca0.png)
