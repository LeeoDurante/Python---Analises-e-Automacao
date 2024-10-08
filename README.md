# Projeto: Análise de Ações Automatizada

Este projeto automatiza a obtenção e o envio de análises de ações utilizando a biblioteca `yfinance` para coletar dados de mercado, e as bibliotecas `pyautogui` e `pyperclip` para automatizar o envio de e-mails com as análises.

## Funcionalidades

- Coleta dados históricos de uma ação financeira específica com base no código da ação (ticker) fornecido pelo usuário.
- Calcula e exibe a cotação máxima, mínima e o valor médio da ação dentro do período especificado.
- Automatiza o envio de um e-mail contendo a análise solicitada, com detalhes sobre a cotação da ação.

## Tecnologias Utilizadas

- **Python 3**
- **yfinance**: Para obter dados financeiros históricos.
- **pyautogui**: Para automatizar a interação com a interface gráfica.
- **pyperclip**: Para copiar o conteúdo para a área de transferência.
- **webbrowser**: Para abrir o navegador e iniciar o processo de envio de e-mails.

## Pré-requisitos

Para executar este projeto, você precisará ter as seguintes bibliotecas Python instaladas:

```bash
pip install yfinance pyautogui pyperclip
