# Manual Ilustrativo: Curso Básico de N8N

## Introdução ao N8N

O N8N é uma poderosa ferramenta de automação de fluxo de trabalho de código aberto e *fair-code*. Ele permite que você conecte diferentes aplicativos e serviços para automatizar tarefas repetitivas, sem a necessidade de escrever código complexo. Com uma interface visual baseada em nodes, o N8N capacita usuários a criar desde automações simples até fluxos de trabalho altamente sofisticados que podem incluir lógica condicional, processamento de dados e integração com inteligência artificial.

### Para que serve o N8N?

O N8N é utilizado para uma vasta gama de aplicações, incluindo:

- **Automação de Marketing:** Sincronizar dados entre CRMs, ferramentas de e-mail marketing e plataformas de mídia social.
- **Processos de Negócios:** Automatizar o faturamento, a geração de relatórios e a gestão de inventário.
- **Desenvolvimento e DevOps:** Criar pipelines de CI/CD, monitorar sistemas e automatizar backups.
- **Projetos Pessoais:** Integrar dispositivos de casa inteligente, gerenciar finanças pessoais e automatizar tarefas do dia a dia.

### Visão Geral da Interface

A interface do N8N é centrada no **Canvas**, uma área de trabalho visual onde você constrói seus workflows. Os principais componentes da interface são:

- **Canvas:** Onde você arrasta e conecta os nodes para criar seu fluxo de automação.
- **Painel de Nodes:** Localizado à esquerda, contém todos os nodes disponíveis, organizados por categoria.
- **Painel de Configurações:** Ao selecionar um node, este painel aparece à direita, permitindo que você configure seus parâmetros e credenciais.
- **Barra de Execução:** Na parte inferior, permite que você execute, teste e ative seus workflows.

![Visão geral da interface do N8N](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908686_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL1pGQzAyVk1VSkY5Qg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg2ODZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwxcEdRekF5VmsxVlNrWTVRZy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=EVXpCK1OVJdsMAdRMU9706O-JpQhQ9IMINM7ypW8~Pxf6JlqhS7XBXGHgPnOWISm8O59WCdcyDCHekwdp3rMpP0YzCzjZVRIm8TtLTbbhxm~h1eUbUiK3DEIoUIBCSYW6sQfYS4qJk2cwx~uDv0TNbaFlBGZwIZeUzbSR3MwW2-LXmtjWUbFHDJytN~cXXnhHuSkl2qwAHFph1V7bncsBMznriBazYZf2A9fJT2VAhP6xL5IQggW2vnu2TjkqtxHb~2CI~KszxT4bSzY6rK~LJLJNL-vSpxLRXrIB2vG2vMFtYr~MRZvWMZFHJhtjq7H8pkipitlbekUqq86mne0Ow__)

## 1. Conceitos Fundamentais da Automação

Para dominar o N8N, é essencial compreender seus três pilares: **Workflows**, **Nodes** e o **Fluxo de Dados**.

### Workflows

Um workflow (fluxo de trabalho) é a sequência de passos que define uma automação. Ele representa o processo completo, desde o evento inicial que o dispara até a conclusão da tarefa. No N8N, um workflow é uma coleção de nodes interconectados no Canvas.

![Exemplo de um workflow no N8N](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908689_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL2dzWlVtWjBnUU16Rg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg2ODlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwyZHpXbFZ0V2pCblVVMTZSZy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=omOU30tlpF7ZI64RHREyiagZtEwzQSKTOv~Ic2qHLmuuEMUbeXlXilfQuGIbvtjXd0kPWOf2KzbNO63PlHgmVUxSIUbp7bMCsmuvTkW7uWSD5qscdrInhjQy4707cYW9RXpvT3PkPrME43RjkfYz2g6BR2easY7JxluZhyyPuZ5pJ9JbA-wEzZzrJsm~aLDO4nBQcuYv-aEpPpLIBYzbc4-Bjm68MDVuTJ856-P4WOI-WNUzMsrpdGUCTDyJiYT1V1cVlL9bEnydKBbMUTh5Ici7alRn9zsWKbtj-vAuVc63t~5WgGBEGVr0kZAtuUcU64gTCQZljS0VuqPfUqaJ~Q__)

### Nodes

Os nodes são os blocos de construção de um workflow. Cada node representa uma ação ou um evento específico. Existem dois tipos principais de nodes:

- **Triggers (Gatilhos):** São os nodes que iniciam um workflow. Eles 

são acionados por eventos específicos, como a chegada de um e-mail, um horário agendado ou uma chamada de webhook. Todo workflow deve começar com um trigger.

- **Actions (Ações):** São os nodes que executam tarefas dentro do workflow, como ler um arquivo, enviar uma mensagem, atualizar um banco de dados ou aplicar lógica condicional.

![Tipos de Triggers no N8N](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908691_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL3hBcHJ5UXRpd1A0Sg.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg2OTFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwzaEJjSEo1VVhScGQxQTBTZy5qcGciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=gnaR5Ek-eBa28IOC-RWe54L9jsLohyA4SbltE3iyQlfjKllQmgFtjwIREXC6Q2lV7hquJwFlngoFnm0fpQeGAOO6bEbdRbiXapqFZTKLiYqXl8p4UobfgdIyWshAA1B5hAjSdP~3GYC-7iPIHAfRch1R1BLUWfYqrd0SOd9GR~QR~wZoLbFQssDXn9JpiPzGjVWKYdQlUQaKmsjF8PMnslW6uBJj0I8TXN4-6k-zNMWQOg562cgHcHqd26KzqD0E15OpCzBTJxWFe3RFZFP4oVKrhOTmK8HXhQFmPpGbLYrSqnWk-yWwxbv5Z4TjZ62ivIoZtKas-9G5UUL~rZDpLw__)

### Fluxo de Dados

O coração do N8N é a forma como os dados fluem entre os nodes. Cada node que é executado produz um conjunto de dados (geralmente em formato JSON). Esses dados são então passados para o próximo node na conexão, que pode usá-los para executar sua própria tarefa. Compreender como manipular e transformar esses dados usando expressões é fundamental para construir automações complexas.

## 2. APIs e Webhooks: Conectando o N8N ao Mundo

APIs (Interfaces de Programação de Aplicativos) e Webhooks são os principais mecanismos que o N8N utiliza para se comunicar com serviços externos.

### O Node HTTP Request

O node **HTTP Request** é um dos mais versáteis do N8N. Ele permite que você se comunique com qualquer serviço que tenha uma API REST, mesmo que não exista um node dedicado para ele. Com este node, você pode:

- **GET:** Obter dados de um serviço.
- **POST:** Enviar novos dados para serem criados.
- **PUT/PATCH:** Atualizar dados existentes.
- **DELETE:** Remover dados.

Para configurar o node, você precisa especificar a URL do endpoint da API, o método HTTP e, se necessário, as credenciais de autenticação e o corpo da requisição (payload).

![Exemplo de configuração do node HTTP Request](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908696_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL3kxNGtGWWVSZ0JuZQ.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg2OTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwza3hOR3RHV1dWU1owSnVaUS5qcGciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=v6ppcfEScX7lQkIvDfuRCTqYUd-Fsckkv0XL~3bCdCWUJqqRbi6Lb-Q4aOyg7S7SaXgOIF50a39uJYWc6l1Cj6tuA58yKwQen2tvB91dSt1q2pvlncoYtaYkZ9v~lwoD92DLG0dqiB7Yi-IuXH3xrIwT6QcRunuLSBhCudlFHtsl~hAiX-QMyvOUjeAJrrabdtxmwUzZ3p6uoPMrAXnKSjQrwP6nDLKrZJsgA9c~kVxuIPMZ4Wqyc8sbomjA0FWVl7NttYrbaSAwjzkEInnoIwwrMXSo~IvMczDzPst80Nb-LuOVfsMRDZ0j0HStRO9RIK52lFg7MoToIeGprO~TVw__)

### Webhooks: A Porta de Entrada para o N8N

O node **Webhook** atua como um trigger que gera uma URL única. Quando um serviço externo envia uma requisição (geralmente um POST) para essa URL, o workflow é iniciado. Isso é extremamente útil para receber notificações em tempo real de sistemas como gateways de pagamento, plataformas de e-commerce ou sistemas de gerenciamento de conteúdo.

**Como funciona:**

1.  **Criação:** Você adiciona um node Webhook ao seu workflow, e ele gera uma URL de teste e uma de produção.
2.  **Configuração:** Você copia a URL do webhook e a insere nas configurações do serviço externo que enviará os dados.
3.  **Execução:** Quando o evento ocorre no serviço externo, ele envia os dados para a URL do N8N, que por sua vez dispara o workflow.

![Workflow utilizando um Webhook como trigger](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908699_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL1VuSzlJQUVtU08wcQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg2OTlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwxVnVTemxKUVVWdFUwOHdjUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=c45-u2OJbxOJpk1nP2xMXBrlGrMEU1CZ5uun9wEpMbq5gRlmFahAV2dusahTK04YkFJPUJKnuZn1yiu0ruEzNdMFDj1cVz1HPRyK24b1DkKDAskiJ~MGFxHLKAAKi8DQ-L31LfvM-DC7mtlOrnkXu9MaH6ET6tYHoDtupr0rs3ABr8bdWrUGBK2VsgfWXnULlwlt9rAgSeCklchjgoncsKw7mpMpdAHjRg9JmVANrno9sQAnutU0Q9G2baR6SNd9~Dpet4c5rl-s9FQOjGj2oHjkupK6veGZoCcYYt9ccyI6zKadGgeBKpoOsiy6rPoNaKjcSKYf8IFI8FelQUctLA__)

## 3. Ambiente Técnico e Instalação

O N8N oferece flexibilidade na forma como é hospedado. Você pode optar pela nuvem do N8N (N8N Cloud) ou auto-hospedar (self-hosted) em sua própria infraestrutura.

### N8N Cloud vs. Self-Hosted

| Característica | N8N Cloud | Self-Hosted |
| :--- | :--- | :--- |
| **Configuração** | Imediata, sem necessidade de instalação. | Requer instalação e configuração em um servidor. |
| **Manutenção** | Gerenciada pela equipe do N8N. | Responsabilidade do usuário (atualizações, segurança). |
| **Custo** | Planos de assinatura baseados no uso. | Custo do servidor (VPS, etc.), mas o software é gratuito. |
| **Flexibilidade** | Limitada às configurações da plataforma. | Controle total sobre o ambiente, sem limites de execução. |

### Instalação com Docker (Self-Hosted)

Docker é o método recomendado para auto-hospedar o N8N, pois simplifica a instalação e o gerenciamento. Para começar, você precisa de um servidor (como uma VPS) com Docker e Docker Compose instalados.

O comando básico para iniciar o N8N com Docker é:

```bash
docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
```

Este comando inicia o N8N e o torna acessível em `http://localhost:5678`.

![Instalando N8N com Docker](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908713_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL0R1MnRlbUpOOHhwVw.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg3MTNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwwUjFNblJsYlVwT09IaHdWdy5qcGciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=czdLp4Pflij~dZ6kLX50T349eWp-ANoUlC1Q3Gq-e41QW4rdvrkXoxSp2R33NL4QiRFIlQMoH7-GVnjR-XSzUFsbofQHziotYuw02ukUf1h~J1FTR1FE65gEo10C1CwAkaiVfhQq4XGMOcVY5QoR9jFVqTuC7Zd3VW2PmZwZ-IIYMSEKPf0tugJSxubwatx2TGHRAzDGB2uZaLMoVB~Ql9F74BJE8D0vRZf8VrA7ISTVTfzY9WQJvgiP0vJGyTLJsMtZBGleP1GANQ0M1VFCFs8oVAGVxZe5qwQOmOW~M7lReKQp-4AMOl4kKCCvLfnSAi1R0nmRez2P6W-Zq9uB4g__)

Para uma configuração de produção, é altamente recomendável usar Docker Compose e configurar um proxy reverso (como Nginx) com SSL (Let's Encrypt) para garantir a segurança e o acesso via HTTPS.



## 4. Lógica e Variáveis: Tomando Decisões no Workflow

À medida que seus workflows se tornam mais complexos, você precisará controlar o fluxo de execução com base em condições específicas. O N8N oferece nodes de lógica para isso, principalmente o **IF** e o **Switch**.

### O Node IF

O node **IF** é o mais simples para controle de fluxo. Ele avalia uma ou mais condições e divide o workflow em dois caminhos: `true` (verdadeiro) e `false` (falso). Se a condição for atendida, os dados seguirão pelo caminho `true`; caso contrário, seguirão pelo `false`.

**Exemplo de uso:**

- Verificar se um pedido de e-commerce tem um valor superior a R$100.
- Checar se um e-mail contém a palavra "urgente" no assunto.
- Validar se um campo obrigatório de um formulário foi preenchido.

![Exemplo de uso do node IF para lógica condicional](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908768_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL1JScmR1UkpWdGZVbA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg3NjhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwxSlNjbVIxVWtwV2RHWlZiQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=uHnTVU~plj2e-n~4n~WylnbSkdZGACDJ4C4YLGbTXlW98rqe2JPhF9r8sEPEdFeO8Wn9NHc2hAXt0Nuz5wHHHZnSDmzLMYjGt0rXuTAZnA-KB63vlckhPFvYi6JvPzBOu8JCTpWNvmSiVkQNv~5T05EW~fXELKc-UEXJKVcQZBqFY8YNPpfkf90fdkrIjLESbwDpEVgRNekUvz5h911c3XmycILiNs7EPAv-pYw1dbjE4DRtdEaTV17PQEtiWQgWh0F5zSV0pExwAJOScRaWvHkU4h4Wdge5vxC8olELcmFJUmFLO-8lfSO8mTZKnc-VacmmjLDPXwcKJ6F081AuxA__)

### O Node Switch

O node **Switch** é uma versão mais poderosa do IF. Em vez de apenas dois caminhos, ele permite que você crie múltiplos caminhos (rotas) com base no valor de um único campo. É ideal para quando você tem várias saídas possíveis para uma mesma entrada.

**Exemplo de uso:**

- Direcionar um ticket de suporte para diferentes departamentos com base na categoria (Vendas, Técnico, Financeiro).
- Processar um pedido de forma diferente dependendo do status (Pago, Pendente, Cancelado).

![Exemplo de uso do node Switch para múltiplas rotas](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908769_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL2dpNUM2Yk1CNHNCWQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg3NjlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwyZHBOVU0yWWsxQ05ITkNXUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=RNxepgCYxFAF~rilMdAkNa07is9HL6AHbq-8vvRkXoZCAdoVqhYpqIh6G9dubTleJIjJf7RDlbT4M48hBpNaSrgMgt0YaegJqhgoH7v84hcKCP0TXEMa0m-g9tXnu6lKS4Fa8XOAygdqPy8cEX5z~NcZwHMZ8BqWire64byzyayk0xlGi-58p6TuZfroHpzPW3BOG-ZgC6GywOtItfeyXdVW5f3eZQIu2AdUdwYM5-eXHpRHM~GYvBEWGqOjsIZraR3usmSmegPK8-FuazX3gnJ86iqlccKcWiDpV9z5JTGg0ckNmsbJ2KxxMLX8tJjbPPZoYXzQBwDeKBXnrBZr-g__)

### Variáveis e Expressões

As expressões são a maneira de acessar e manipular dados dinamicamente dentro dos nodes. O N8N utiliza uma sintaxe que permite referenciar dados de nodes anteriores. Por exemplo, `{{$json["body"]["name"]}}` acessaria o campo `name` do corpo (body) de um webhook.

As variáveis permitem que você armazene e reutilize valores ao longo do seu workflow, tornando-os mais limpos e fáceis de manter.

## 5. Integrações com IA e Dados

O N8N se destaca por sua capacidade de integrar modelos de inteligência artificial e manipular estruturas de dados complexas, como JSON.

### Integração com OpenAI e Modelos de IA

Com os nodes de IA do N8N, você pode conectar seus workflows a modelos de linguagem como o GPT da OpenAI. Isso abre um leque de possibilidades:

- **Criação de Agentes Inteligentes:** Construir chatbots que podem responder a perguntas de clientes, usando ferramentas e dados internos.
- **Processamento de Linguagem Natural:** Analisar o sentimento de e-mails, resumir textos longos ou traduzir conteúdo.
- **Geração de Conteúdo:** Criar automaticamente posts para redes sociais, descrições de produtos ou respostas a e-mails.

![Workflow de um agente de IA com N8N e OpenAI](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908771_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzL25BbEJOYm9kTlVwWQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg3NzFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekwyNUJiRUpPWW05a1RsVndXUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=BExkXr6XtvKOBE~bOsvz6PAaWu2YTFCN4SFt6yg2ShYm~SUyJOq6Qa19w8X6UeX3048yt52sjUm1mz6jAJxAD-5mBK6LsuPS8tO~eAU-2hGPiaxeJctpvBZGBfJResQozsOnpkKpifiYwvwVR7~GsWjmE5my2L5F~2FANrPfjTMkSLypKrDOFDexl~xCYYcU3JMGRjed2yqVlxwVtYDKe~FhSH4zSdgbX53~Hw5OC6dU1DLDI~YsXG5mZdGg~gVibzT0IM1-KjD~cRpVpLcJK4w44o4gAwekU1XHepSdG0BpRyepxdgpXXdzNWk-FsUyrTJ-59XK2hlvZ3UyRhcd1g__)

### Manipulação de JSON

JSON (JavaScript Object Notation) é o formato de dados padrão na web e no N8N. Quase todos os dados que fluem entre os nodes estão em JSON. É crucial entender sua estrutura de objetos (pares de chave-valor) e arrays (listas) para:

- **Extrair informações específicas:** Usar expressões para pegar exatamente o dado que você precisa.
- **Transformar dados:** Mapear e reestruturar os dados de um formato para outro usando nodes como o **Set** e o **Code**.
- **Iterar sobre listas:** Usar nodes como o **Split in Batches** para processar cada item de um array individualmente.

## 6. Complementos que Ampliam o Potencial

Embora o N8N seja uma ferramenta *low-code*, ter conhecimentos básicos de programação pode levar suas automações a um novo patamar.

### JavaScript e o Node Code

O **Node Code** permite que você escreva código JavaScript diretamente em seu workflow. Isso é útil para:

- **Lógica Complexa:** Implementar algoritmos que seriam difíceis de construir apenas com nodes visuais.
- **Transformações de Dados Avançadas:** Realizar manipulações de dados que não são possíveis com expressões padrão.
- **Contornar Limitações:** Quando não há um node que faça exatamente o que você precisa, o Node Code oferece uma saída.

### SQL e Bancos de Dados

O N8N possui nodes para se conectar a uma variedade de bancos de dados, como PostgreSQL, MySQL, e SQL Server. Com conhecimento em SQL, você pode:

- Executar consultas complexas para buscar e filtrar dados.
- Inserir, atualizar e deletar registros diretamente do seu workflow.
- Criar automações que sincronizam dados entre seu banco de dados e outros aplicativos.

![Exemplo de integração de banco de dados no N8N](https://private-us-east-1.manuscdn.com/sessionFile/EFW7FbnSEbWbuCeshoYqsE/sandbox/DCPxLKcvKDIx1t6aw2L3SG-images_1761362908773_na1fn_L2hvbWUvdWJ1bnR1L244bl9tYW51YWxfaW1hZ2VzLzlyMWJoUmxGcWpYTA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvRUZXN0ZiblNFYldidUNlc2hvWXFzRS9zYW5kYm94L0RDUHhMS2N2S0RJeDF0NmF3MkwzU0ctaW1hZ2VzXzE3NjEzNjI5MDg3NzNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyNDRibDl0WVc1MVlXeGZhVzFoWjJWekx6bHlNV0pvVW14R2NXcFlUQS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=L7hr9ii85Xq2r9a~OaK~Ca9uEp-PRtYsET4ureMoldJNRe8zpiePjQdQqybwDYsHMXpYJtHoAoen~QVzKeQTOpyTStWhRLTu~FKVUHf7Sw~s547LiavEY9V5c2Al4D~sWX7m0CZ5KVk3RG132sgUXROrOJC8hQFxdkUpqb3PW8GlcQjv8NxADAhlRaTPlf-KmeRsjynN3vJxBajaGhyBCccyXtJ0a~62JOMH2-rdGAduTqCoigD8C-iW9HFxu7e~o7RoO0xPF-V36gOJ~dFIKTaDnRAMjM81O5pG6Tp8laec2TnuNHiYv03KJ28Yj7St6h~qAYMql2Q4Z9V2nE~k6Q__)

## Conclusão

Este manual cobriu os fundamentos essenciais para começar sua jornada com o N8N. Exploramos desde os conceitos básicos de workflows e nodes, passando pela comunicação com APIs e webhooks, até o uso de lógica condicional e integrações avançadas com IA. Com a prática e a exploração contínua da vasta biblioteca de nodes e da comunidade ativa, você estará bem equipado para automatizar praticamente qualquer processo digital.

---

### Referências

- [Documentação Oficial do N8N](https://docs.n8n.io)
- [Curso N8N Gratuito 2025 – NoCode StartUp](https://www.youtube.com/watch?v=-Ka4YKW7RwM)
- [Comunidade N8N no Reddit](https://www.reddit.com/r/n8n/)

