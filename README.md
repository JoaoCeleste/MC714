# MC714


1. Instalar o Docker e garantir que ele esteja rodando
2. Abrir um terminal no diretorio em que os arquivos estão
3. Escrever a seguinte linha de comando: docker-compose -f docker-compose-script.yml up --build (Substituindo script por lamport,mutex ou leader)
4. Para limpar os conteiners criados depois do teste docker-compose -f docker-compose-script.yml down
5. Caso queira testar os outros algoritimos repita do passo 2

Obs: Até o momento não consegui ajustar o algoritimo de lamport para encerrar automaticamente, após execução pode para a execução utilizando Ctrl+C