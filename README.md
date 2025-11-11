# Microsserviço de Leilão de Carros Online

Este microsserviço simula uma parte de um sistema de leilão de carros online. Ele é responsável por receber lances de usuários, processá-los em uma fila e determinar o maior lance para cada carro.

## Funcionalidades

- **Recebimento de Lances:** Os usuários podem dar lances em carros. Cada lance é um evento que contém informações sobre o carro, o valor do lance e o comprador.
- **Fila de Lances:** Os lances recebidos são adicionados a uma fila para processamento assíncrono.
- **Processamento de Lances:** Um processo em segundo plano consome a fila de lances, determinando e atualizando o maior lance para cada carro.

## Arquitetura

O microsserviço é composto pelos seguintes componentes:

- **`LanceParaCarro.py`:** Contém a função `LanceParaCarro`, que é o ponto de entrada para novos lances. Ele recebe um lance e o adiciona à fila de lances.
- **`FilaLance.py`:** Define a fila `FilaLance`, que é usada para armazenar os lances pendentes de processamento.
- **`MaiorLance.py`:** Contém a função `MaiorLance`, que processa os lances da fila. Ele mantém um registro do maior lance para cada carro e o atualiza conforme novos lances maiores são recebidos.

## Como funciona

1. Um usuário envia um lance para um carro através de um evento.
2. A função `LanceParaCarro` recebe o evento e o adiciona à `FilaLance`.
3. O processo `MaiorLance` está em execução contínua, monitorando a `FilaLance`.
4. Quando um novo lance é adicionado à fila, o `MaiorLance` o retira e o processa.
5. O `MaiorLance` compara o valor do lance com o maior lance atual para o mesmo carro.
6. Se o novo lance for maior, ele é armazenado como o novo maior lance para aquele carro.
7. O resultado do maior lance para cada carro é exibido no console.
