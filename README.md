# MC714


1. Instalar o Docker e garantir que ele esteja rodando
2. Mudar na linha 21 da Dockerfile o ultimo argumento com qual dos algoritimos você quer rodar : "lamport_clock.py", "leader_election.py", "mutex.py"
3. Abrir um terminal no diretorio em que os arquivos estão
4. Escrever a seguinte linha de comando: docker-compose up --build
5. Caso queira ver somente os resultados: docker-compose logs -f
6. Limpe os containers com: docker-compose down 
7. Caso queira testar os outros algoritimos repita do passo 2