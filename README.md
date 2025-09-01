## Trabalho de Inteligência Artificial – UFPA

### Descrição

Este repositório contém o projeto da disciplina de Inteligência Artificial da UFPA, desenvolvido por **Andrey Santos**, **Bryan Young** e **Mayara Lima**. Apresenta uma solução integrando frontend, bot no Telegram e infraestrutura Docker para facilitar a execução.

### Tecnologias

- **Docker Compose**: para orquestração dos serviços.
    
- **Frontend**: aplicação web rodando em `localhost:80`.
    
- **Bot Telegram**: integração automática e comunicação via Telegram.
    
- **Jupyter Notebook**, **Vue.js**, **Python**, **CSS**: linguagens e ferramentas usadas no desenvolvimento ([GitHub](https://github.com/andrsantos/TrabalhoDeInteligenciaArtificial/tree/main "GitHub - andrsantos/TrabalhoDeInteligenciaArtificial: Trabalho da disciplina de inteligência artificial da UFPA feito por Andrey Santos, Bryan Young e Mayara Lima.")).
    

### Pré-requisitos

- Ter o **Docker Desktop** instalado no seu computador.
    

### Como executar

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/andrsantos/TrabalhoDeInteligenciaArtificial.git
    cd TrabalhoDeInteligenciaArtificial
    ```
    
2. Inicie todos os serviços com Docker Compose:
    
    ```bash
    docker-compose up
    ```
    
3. Após a inicialização:
    
    - O **frontend** estará disponível em `http://localhost:80`.
        
    - O **bot Telegram** será iniciado automaticamente e ficará disponível conforme configuração.
        

### Estrutura do Repositório

- `docker-compose.yml`: configura os containers para frontend e bot Telegram.
    
- `Nosso Notebook`: notebooks Jupyter com experimentos e análises.
    
- `Nosso Workflow no n8n`: automações implementadas com n8n.
    
- `ProjetoKdd`: projeto de KDD relacionado ao tema.
    
- `Telegram-bot`: código fonte do bot integrado ao Telegram. ([GitHub](https://github.com/andrsantos/TrabalhoDeInteligenciaArtificial/tree/main "GitHub - andrsantos/TrabalhoDeInteligenciaArtificial: Trabalho da disciplina de inteligência artificial da UFPA feito por Andrey Santos, Bryan Young e Mayara Lima."))
    

### Colaboração

- **Pull Requests** são bem-vindos! Sinta-se à vontade para propor melhorias.
    
- **Issues** podem ser abertas para bugs, sugestões ou dúvidas.
    
- Para discussões colaborativas, podemos usar **Issues** ou **Discussions**.
    

### Licença

Este projeto está sob uma licença aberta.

---
### Tutorial Rápido

|Etapa|O que fazer|
|---|---|
|Setup|`docker-compose up`|
|Frontend|`http://localhost:80`|
|Bot Telegram|Executa automaticamente|
|Estrutura|Contém notebooks, automações, projeto KDD e bot|
