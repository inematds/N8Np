# Arquitetura

Total de workflows: **10**


## Tópico 11146

### Parallelization

- **Nodes:** 12
- **Integrações:** Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/11146/Parallelization (1).json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
    - `@n8n/n8n-nodes-langchain.outputParserStructured`
    - `n8n-nodes-base.googleSheets`
    - `n8n-nodes-base.manualTrigger`
    - `n8n-nodes-base.perplexity`
    - `n8n-nodes-base.stickyNote`


## Tópico 12382

### 5 Error Handling Techniques

- **Nodes:** 45
- **Integrações:** Airtable, Gmail, Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/12382/5 Error Handling Techniques.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.chatTrigger`
    - `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
    - `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
    - `@tavily/n8n-nodes-tavily.tavily`
    - `n8n-nodes-base.airtableTool`
    - `n8n-nodes-base.code`
    - `n8n-nodes-base.errorTrigger`
    - `n8n-nodes-base.gmail`
    - `n8n-nodes-base.googleSheets`


## Tópico 2360

### Parallelization

- **Nodes:** 13
- **Integrações:** Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/2360/Parallelization.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.chatTrigger`
    - `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `n8n-nodes-base.aggregate`
    - `n8n-nodes-base.googleDocs`
    - `n8n-nodes-base.merge`
    - `n8n-nodes-base.stickyNote`

### Prompt Chaining

- **Nodes:** 10
- **Integrações:** Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/2360/Prompt_Chaining.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.chatTrigger`
    - `@n8n/n8n-nodes-langchain.lmChatAnthropic`
    - `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
    - `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `n8n-nodes-base.googleDocs`
    - `n8n-nodes-base.stickyNote`

### Routing

- **Nodes:** 14
- **Integrações:** Gmail, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/2360/Routing.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `@n8n/n8n-nodes-langchain.textClassifier`
    - `n8n-nodes-base.gmail`
    - `n8n-nodes-base.gmailTool`
    - `n8n-nodes-base.gmailTrigger`
    - `n8n-nodes-base.stickyNote`
    - `n8n-nodes-base.telegramTool`


## Tópico 6189

### Error Logger

- **Nodes:** 5
- **Integrações:** Google
- **Arquivo:** `Ref/2494913847/6189/Error_Logger.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `n8n-nodes-base.errorTrigger`
    - `n8n-nodes-base.googleSheets`
    - `n8n-nodes-base.slack`
    - `n8n-nodes-base.stickyNote`


## Tópico 8187

### Error Logger

- **Nodes:** 5
- **Integrações:** Google
- **Arquivo:** `Ref/2494913847/8187/21) Error Logger.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `n8n-nodes-base.errorTrigger`
    - `n8n-nodes-base.googleSheets`
    - `n8n-nodes-base.slack`
    - `n8n-nodes-base.stickyNote`

### Parallelization

- **Nodes:** 13
- **Integrações:** Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/8187/18) Parallelization.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.chatTrigger`
    - `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `n8n-nodes-base.aggregate`
    - `n8n-nodes-base.googleDocs`
    - `n8n-nodes-base.merge`
    - `n8n-nodes-base.stickyNote`

### Prompt Chaining

- **Nodes:** 10
- **Integrações:** Google, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/8187/16) Prompt Chaining.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.chatTrigger`
    - `@n8n/n8n-nodes-langchain.lmChatAnthropic`
    - `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
    - `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `n8n-nodes-base.googleDocs`
    - `n8n-nodes-base.stickyNote`

### Routing

- **Nodes:** 14
- **Integrações:** Gmail, OpenAI/LangChain
- **Arquivo:** `Ref/2494913847/8187/17) Routing.json`

??? info "Detalhes Técnicos"
    **Node types usados:**
    - `@n8n/n8n-nodes-langchain.agent`
    - `@n8n/n8n-nodes-langchain.lmChatOpenAi`
    - `@n8n/n8n-nodes-langchain.textClassifier`
    - `n8n-nodes-base.gmail`
    - `n8n-nodes-base.gmailTool`
    - `n8n-nodes-base.gmailTrigger`
    - `n8n-nodes-base.stickyNote`
    - `n8n-nodes-base.telegramTool`

