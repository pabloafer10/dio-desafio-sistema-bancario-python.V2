# 🏦 <u>Projeto Bootcamp DIO - Sistema Bancário - V2</u>

### <u>Objetivo geral</u>
##### **Manter toda regra de negócio já existente na V1, e implementar as novas regras para V2. Para V2 iremos separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.**

### <u>Desafio</u>
##### **Nosso desafio consiste em deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).**

### <u>Separação em Funções</u>
##### **Devemos criar funções para todas as operações do sistema, cada função vai ter uma regra na passagem de argumentos.** 

## <u>Explicando o projeto</u>
##### **Este projeto é a versão 2 de um sistema bancário simples desenvolvido em Python, com funcionalidades básicas de operações financeiras como:**  
✔ **Existentes da V1:**  
✅ Depósito de valores  
✅ Saque de dinheiro  
✅ Consulta de Extrato  

✔✔ **Implementação da V2**  
✅✅ **Criação de usuário**       
✅✅ **Criação de conta corrente**  

📌 <u>**Regras de Negócio:**</u>  
🔹 <u>**Depósitos:**</u>  
✔ V1 - Apenas valores positivos são permitidos.  
✔ V1 - Em caso de valor inválido deve ser exibido a mensagem: "Valor inválido, tente novamente."  
✔ V1 - Todos os depósitos devem ser armazenados e exibidos na consulta de extrato.  
✔✔ _**Para V2 incluiremos:**_  
✔✔ - **A função depósito deve receber os argumentos apenas por posição (positional only).**  
✔✔ **V2 - Sugestão de argumentos: saldo, valor, extrato.**  
✔✔ **V2 - Sugestão de retorno: saldo e extrato.**  

🔹 <u>**Saques:**</u>  
✔ V1 - Limite diário de 3 saques.  
✔ V1 - Caso o limite diário de saque seja maior do que permitido, deve ser exibido a mensagem: "Limite de saques diário excedido! Por favor, tente novamente."  
✔ V1 - Valor máximo de R$ 500,00 por saque.  
✔ V1 - Caso o saldo seja insuficiente, deve ser exibido a mensagem: "Saldo insuficiente! Por favor, tente novamente."  
✔ V1 - Caso o valor do saque seja inválido, deve ser exibido a mensagem: "Valor informado inválido, tente novamente."  
✔ V1 - Todos os saques devem ser armazenados e exibidos na consulta de extrato.         
✔✔ _**Para V2 incluiremos:**_  
✔✔ **V2 - A função saque deve receber os argumentos apenas por nome (keyword only).**  
✔✔ **V2 - Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.**  
✔✔ **V2 - Sugestão de retorno: saldo e extrato.**  

🔹 <u>**Extrato:** </u>  
✔ V1 - Deve listar todos os depósitos e saques realizados.  
✔ V1 - No final, exibe o saldo disponível no formato: R$ xxx.xx.                    
✔✔ _**Para V2 incluiremos:**_  
✔✔ **V2 - A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).**  
✔✔ **V2 - Argumentos posicionais: saldo.**  
✔✔ **V2 - Argumentos nomeados: extrato.**  

🔹 <u>**Novas funções:**</u>  
✔✔ **V2 - Criar novos usuários:**  
✔✔ **V2 - Armazenar os usuários em uma lista.**  
✔✔ **V2 - Um usuário é composto por: nome, data de nascimento, cpf e endereço.**  
✔✔ **V2 - O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.**  
✔✔ **V2 - Deve ser armazenado somente os números do CPF.**  
✔✔ **V2 - Não podemos cadastrar 2 usuários com o mesmo CPF.**  

✔✔ **V2 - Criar conta corrente:**  
✔✔ **V2 - Deve armazenar contas em uma lista.**  
✔✔ **V2 - Uma conta é composta por: agência, número da conta e usuário.**  
✔✔ **V2 - O número da conta é sequencial, iniciando em 1.**  
✔✔ **V2 - O número da agência é fixo: "0001".**  
✔✔ **V2 - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.**  

🔹 <u>**Outras regras:**</u>  
✔ V1 - O usuário pode optar por sair do sistema a qualquer momento.  
✔ V1 - Se a entrada do usuário for inválida (não estiver no menu de opções), deve ser exibido a mensagem: "Opção inválida, por favor seleciona novamente a operação desejada."  

🔹 <u>**V2 - Dica do professor**</u>  
✔✔ **V2 - Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.**
