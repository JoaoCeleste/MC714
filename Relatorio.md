Esse relatório relata a implementação dos seguintes algoritmos: 

-Relógio Logico de Lamport 

-Exclusão Mútua 

-Eleição do Lider 

Todos esses algoritmos foram implementados em python usando troca de mensagens com MPI e usam o ambiente Docker para serem executados. Mais detalhes sobre como executar os códigos estão no arquivo README 

  

-Relógio Logico de Lamport 

Inicialmente importamos a biblioteca do MPI. Também iniciamos o comunicador global e cada um dos programas vai adquirir seu rank, pegar o número de processos no comunicador e iniciar o clock. 

Definimos então as funções para mandar e receber as mensagens contendo o clock. Enviamos usamos o comunicador e enviamos o clock, imprimindo qual dos programas está fazendo a operação, assim como o clock que enviou e para quem.  Ao receber, armazenamos o clock recebido e usamos a função max para escolher o maior dentre o clock local e o clock recebido. Ao fazer a escolha, esse valor é acrescido de 1 e se torna o novo clock local, imprimimos quem recebeu a mensagem, o clock recebido e quem o envio. 

Iniciamos o código principal com um condicional para garantir que temos pelo menos 3 processos e colocamos uma barreira para que os 3 sincronizem antes de iniciar uma simulação de troca de mensagens. Então temos um script que simula para cada processos o avanço do clock local deles assim como envio e recebimento de mensagens entre eles. Por fim todos temos uma última barreira que espera todos os processos acabarem e finalizamos o algoritmo. 

 

-Exclusão Multipla(Mutex) 

Inicialmente importamos a biblioteca do MPI. Também iniciamos o comunicador global e cada um dos programas vai adquirir seu rank, pegar o número de processos no comunicador. 

Então temos as funções responsáveis por requisitar e liberar os acessos a regiões críticas.  A primeira delas tem o processo que quer requisitar o acesso como argumento, este que envia a requisição para todos os outros processos e espera a permissão deles para acessar a seção crítica. Já a segunda envia a mensagem da liberação da seção crítica para todos os outros processos. 

Então temos o corpo main, onde primariamente usamos o rank de cada processo para chamar um sleep para garantir que as requisições de acesso não sejam simultâneas. Então cada um dos processos faz a requisição da seção crítica com a função já descrita, e quando o recebe temos um print para denotar o mesmo e um sleep que simula o que seria o uso da seção pelo programa. Por fim ele chama a função para liberar o acesso. 

 

-Eleição do Líder 

Inicialmente importamos a biblioteca do MPI e random. Também iniciamos o comunicador global e cada um dos programas vai adquirir seu rank, pegar o número de processos no comunicador. 

Temos então a função responsável pela eleição do líder, que inicia imprimindo qual processo iniciou a eleição e colocando ele como líder provisório inicial. Então ele envia mensagens para todos os outros processos e espera a resposta. Se o rank do processo que respondeu a mensagem for maior do que o que está armazenado como líder provisório então esse processo é armazenado como novo líder provisório. Então depois de receber todas as mensagens de resposta a função retorna o líder, que é o processo com maior rank dentre todos os ativos. 

Na main usamos a função random seed para escolher um único processo que chama a eleição, e depois que ela ocorre fazemos a impressão do processo que chamou a eleição e do que foi escolhido como líder. 

 

 

 

 
