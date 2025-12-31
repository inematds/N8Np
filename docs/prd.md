# PRD - Sistema de Gestao N8Np

## Documento de Requisitos do Produto

**Versao:** 1.0
**Data:** 31 de Dezembro de 2025
**Status:** Aprovado

---

## 1. Visao Geral

### 1.1 O que e o N8Np?

O **N8Np** e uma plataforma completa para gerenciar, buscar, classificar e cadastrar workflows n8n e AI Agents. A plataforma serve como uma biblioteca inteligente onde usuarios podem:

- **Encontrar** o workflow ideal para sua necessidade
- **Entender** o que cada workflow faz sem conhecimento tecnico
- **Baixar** arquivos JSON prontos para importar no n8n
- **Cadastrar** novos workflows para a comunidade
- **Aprender** atraves de tutoriais e o curso completo

### 1.2 Problema que Resolve

| Problema | Solucao N8Np |
|----------|--------------|
| "Nao sei qual workflow usar" | Sistema de busca inteligente com filtros |
| "Nao entendo o que esse workflow faz" | Descricoes claras e visuais |
| "Nao sei como comecar" | Tutoriais guiados e chatbot assistente |
| "Quero compartilhar meu workflow" | Sistema de cadastro simplificado |
| "Sao muitos workflows, me perdi" | Categorização automatica e tags |

### 1.3 Publico-Alvo

1. **Iniciantes em n8n** - Querem aprender e encontrar exemplos
2. **Desenvolvedores** - Buscam referencias e padroes
3. **Empresas** - Precisam de automacoes prontas
4. **Comunidade N8Np** - Querem compartilhar conhecimento

---

## 2. Estatisticas do Conteudo

| Metrica | Quantidade |
|---------|------------|
| Total de workflows | 532 |
| AI Agents | 198 |
| Automacoes | 66 |
| Integracoes | 36 |
| Arquitetura | 10 |
| HITL (Human-in-the-Loop) | 7 |
| Outros | 256 |
| Topicos da comunidade | 420 |
| Licoes do curso | 23 |

### 2.1 Categorias de Workflows

```
AI Agents (198)
├── RAG Pipelines & Chatbots
├── Agentes de Vendas
├── Agentes de Atendimento
├── Voice Agents
└── Multi-Agent Systems

Automacoes (66)
├── Customer Support
├── LinkedIn Automation
├── Invoice Processing
├── WhatsApp Automation
└── Email Automation

Integracoes (36)
├── Google (Drive, Sheets, Gmail)
├── Supabase / Postgres
├── OpenAI / Anthropic
├── Airtable
└── APIs diversas

Arquitetura (10)
├── Orchestrator Pattern
├── Prompt Chaining
├── Routing
├── Parallelization
└── Error Handling

HITL - Human in the Loop (7)
├── Email Validation
├── Sales Approval
└── Content Review
```

---

## 3. Requisitos Funcionais

### RF01 - Catalogo de Workflows

**O que faz:** Lista todos os workflows de forma organizada

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF01.1 | Listar workflows por categoria | Alta |
| RF01.2 | Mostrar card com nome, descricao, categoria | Alta |
| RF01.3 | Exibir quantidade de nodes | Media |
| RF01.4 | Mostrar integracoes usadas (icones) | Media |
| RF01.5 | Indicar nivel de dificuldade | Baixa |

**Como o usuario ve:**
```
┌─────────────────────────────────────────────────┐
│ [icon] RAG Pipeline & Chatbot                   │
│                                                 │
│ Cria um chatbot inteligente com RAG para       │
│ responder perguntas baseado em documentos.      │
│                                                 │
│ Categoria: AI Agents    Nodes: 15              │
│ Integracoes: [OpenAI] [Supabase] [Google]      │
│ Dificuldade: ★★★☆☆                             │
│                                                 │
│ [Ver Detalhes]  [Baixar JSON]                  │
└─────────────────────────────────────────────────┘
```

### RF02 - Sistema de Busca

**O que faz:** Permite encontrar workflows rapidamente

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF02.1 | Busca por texto livre | Alta |
| RF02.2 | Filtro por categoria | Alta |
| RF02.3 | Filtro por integracao | Alta |
| RF02.4 | Filtro por dificuldade | Media |
| RF02.5 | Ordenacao (popularidade, data, nome) | Media |
| RF02.6 | Busca por tags | Media |

**Exemplos de busca:**
- "chatbot com RAG" → Mostra todos RAG chatbots
- Filtro: AI Agents + OpenAI → Agentes que usam OpenAI
- "vendas email" → Workflows de vendas com email

### RF03 - Pagina de Detalhes do Workflow

**O que faz:** Mostra tudo sobre um workflow especifico

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF03.1 | Nome e descricao completa | Alta |
| RF03.2 | Lista de nodes usados | Alta |
| RF03.3 | Integracoes necessarias | Alta |
| RF03.4 | Botao de download JSON | Alta |
| RF03.5 | Instrucoes de uso | Alta |
| RF03.6 | Screenshots/diagramas | Media |
| RF03.7 | Workflows relacionados | Media |
| RF03.8 | Comentarios da comunidade | Baixa |

**Layout da pagina:**
```
═══════════════════════════════════════════════════════
  RAG Pipeline & Chatbot
═══════════════════════════════════════════════════════

📝 DESCRICAO
Este workflow cria um chatbot inteligente usando RAG
(Retrieval Augmented Generation). Ele indexa documentos
do Google Drive e permite fazer perguntas sobre eles.

🔧 O QUE VOCE PRECISA
- Conta Google (Drive)
- Chave API OpenAI ou OpenRouter
- Banco Supabase (para vetores)

📋 NODES USADOS (15)
┌──────────────────────────────────────┐
│ • Google Drive Trigger               │
│ • Document Loader                    │
│ • Text Splitter                      │
│ • OpenAI Embeddings                  │
│ • Supabase Vector Store              │
│ • Chat Trigger                       │
│ • AI Agent                           │
│ • ...                                │
└──────────────────────────────────────┘

📥 COMO USAR
1. Baixe o arquivo JSON
2. Importe no seu n8n (Workflows > Import)
3. Configure as credenciais marcadas em vermelho
4. Ative o workflow

[████ BAIXAR JSON ████]

🔗 WORKFLOWS RELACIONADOS
• Dynamic RAG Pipeline
• RAG con imagenes
• RAG Reranking
═══════════════════════════════════════════════════════
```

### RF04 - Cadastro de Workflows

**O que faz:** Permite adicionar novos workflows

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF04.1 | Upload de arquivo JSON | Alta |
| RF04.2 | Extracao automatica de metadados | Alta |
| RF04.3 | Formulario para descricao | Alta |
| RF04.4 | Selecao de categoria | Alta |
| RF04.5 | Adicao de tags | Media |
| RF04.6 | Preview antes de publicar | Media |
| RF04.7 | Moderacao antes de publicar | Baixa |

**Fluxo de cadastro:**
```
1. Upload JSON
      ↓
2. Sistema extrai: nome, nodes, integracoes
      ↓
3. Usuario adiciona: descricao, categoria, tags
      ↓
4. Preview do card
      ↓
5. Publicar (vai para moderacao ou direto)
```

### RF05 - Sistema de Usuarios

**O que faz:** Gerencia contas e preferencias

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF05.1 | Cadastro com email | Media |
| RF05.2 | Login com Google | Media |
| RF05.3 | Favoritar workflows | Media |
| RF05.4 | Historico de downloads | Baixa |
| RF05.5 | Perfil com workflows enviados | Baixa |

### RF06 - Chatbot Assistente

**O que faz:** Ajuda usuarios a encontrar workflows

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF06.1 | Chat em linguagem natural | Alta |
| RF06.2 | Sugerir workflows baseado na conversa | Alta |
| RF06.3 | Responder duvidas sobre n8n | Media |
| RF06.4 | Explicar workflows especificos | Media |

**Exemplo de conversa:**
```
Usuario: Preciso automatizar atendimento no WhatsApp
Bot: Encontrei 3 workflows para voce:
     1. WhatsApp Agent - Atendimento completo com IA
     2. WhatsApp + GPT - Respostas automaticas simples
     3. WhatsApp Evolution - Integracao com Evolution API
     Qual deles quer ver em detalhes?

Usuario: O primeiro
Bot: [Mostra card do WhatsApp Agent]
     Este workflow usa AI Agent para atender clientes...
```

### RF07 - Area de Aprendizado

**O que faz:** Tutoriais e curso completo

| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF07.1 | Listagem das 23 licoes do curso | Media |
| RF07.2 | Ordem sugerida de aprendizado | Media |
| RF07.3 | Marcar licoes concluidas | Baixa |
| RF07.4 | Guias por categoria | Baixa |

---

## 4. Requisitos Nao-Funcionais

### RNF01 - Desempenho
- Busca retorna em menos de 500ms
- Pagina carrega em menos de 2 segundos
- Suporta 1000 usuarios simultaneos

### RNF02 - Usabilidade
- Interface responsiva (mobile/desktop)
- Navegacao por no maximo 3 cliques
- Textos claros para nao-tecnicos
- Modo claro e escuro

### RNF03 - Disponibilidade
- 99% de uptime
- Deploy automatico via GitHub Pages ou Vercel

### RNF04 - Seguranca
- Autenticacao segura (JWT ou OAuth)
- Sanitizacao de inputs
- Rate limiting na API

---

## 5. Jornadas do Usuario

### Jornada 1: Buscar Workflow

```
[Usuario chega no site]
        ↓
[Ve categorias na home]
        ↓
[Clica em "AI Agents"]
        ↓
[Ve lista de 198 workflows]
        ↓
[Usa filtro: "RAG"]
        ↓
[Encontra 15 resultados]
        ↓
[Clica em "RAG Pipeline"]
        ↓
[Le descricao e instrucoes]
        ↓
[Clica em "Baixar JSON"]
        ↓
[Importa no n8n]
        ↓
[SUCESSO!]
```

### Jornada 2: Pedir Ajuda ao Chatbot

```
[Usuario nao sabe o que procurar]
        ↓
[Clica no icone de chat]
        ↓
[Digita: "quero automatizar postagens no Instagram"]
        ↓
[Bot sugere 3 workflows]
        ↓
[Usuario escolhe um]
        ↓
[Bot explica como usar]
        ↓
[Usuario baixa e implementa]
```

### Jornada 3: Cadastrar Workflow

```
[Usuario tem workflow proprio]
        ↓
[Clica em "Adicionar Workflow"]
        ↓
[Faz upload do JSON]
        ↓
[Sistema extrai informacoes]
        ↓
[Usuario completa descricao]
        ↓
[Seleciona categoria e tags]
        ↓
[Clica em "Publicar"]
        ↓
[Workflow aparece no catalogo]
```

---

## 6. Wireframes Conceituais

### 6.1 Home Page

```
╔═══════════════════════════════════════════════════════════════╗
║  N8Np - Biblioteca de Workflows n8n                    [Login]║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  🔍 Buscar workflows...                    [Pesquisar]  │  ║
║  └─────────────────────────────────────────────────────────┘  ║
║                                                               ║
║  ══════════════ CATEGORIAS ══════════════                     ║
║                                                               ║
║  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐         ║
║  │ 🤖       │ │ ⚡       │ │ 🔗       │ │ 🏗️       │         ║
║  │ AI       │ │ Auto-    │ │ Inte-    │ │ Arqui-   │         ║
║  │ Agents   │ │ macoes   │ │ gracoes  │ │ tetura   │         ║
║  │ (198)    │ │ (66)     │ │ (36)     │ │ (10)     │         ║
║  └──────────┘ └──────────┘ └──────────┘ └──────────┘         ║
║                                                               ║
║  ══════════════ POPULARES ══════════════                      ║
║                                                               ║
║  [Card 1] [Card 2] [Card 3] [Card 4]                         ║
║                                                               ║
║  ══════════════ RECENTES ══════════════                       ║
║                                                               ║
║  [Card 5] [Card 6] [Card 7] [Card 8]                         ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  [💬 Precisa de ajuda? Clique aqui]                          ║
╚═══════════════════════════════════════════════════════════════╝
```

### 6.2 Pagina de Categoria

```
╔═══════════════════════════════════════════════════════════════╗
║  N8Np > AI Agents                                      [Login]║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🤖 AI Agents (198 workflows)                                 ║
║                                                               ║
║  ┌─ FILTROS ─────────────────────────────────────────────┐   ║
║  │ Integracao: [Todas ▼] [OpenAI] [Supabase] [Google]    │   ║
║  │ Dificuldade: [○ Facil] [○ Medio] [○ Avancado]         │   ║
║  │ Tags: [RAG] [Chatbot] [Vendas] [+]                     │   ║
║  └───────────────────────────────────────────────────────┘   ║
║                                                               ║
║  Ordenar por: [Relevancia ▼]                                 ║
║                                                               ║
║  ┌────────────────────────┐ ┌────────────────────────┐       ║
║  │ RAG Pipeline & Chatbot │ │ n8n Developer Agent    │       ║
║  │ Chatbot com RAG...     │ │ Agente desenvolvedor...│       ║
║  │ ★★★☆☆ | 15 nodes       │ │ ★★★★☆ | 17 nodes      │       ║
║  │ [OpenAI][Supabase]     │ │ [Anthropic][Google]    │       ║
║  └────────────────────────┘ └────────────────────────┘       ║
║                                                               ║
║  ┌────────────────────────┐ ┌────────────────────────┐       ║
║  │ WhatsApp Agent         │ │ Voice Email Agent      │       ║
║  │ Atendimento WhatsApp...│ │ Agente de voz para...  │       ║
║  │ ★★★★☆ | 45 nodes       │ │ ★★★★★ | 32 nodes      │       ║
║  │ [Evolution][OpenAI]    │ │ [OpenAI][Gmail]        │       ║
║  └────────────────────────┘ └────────────────────────┘       ║
║                                                               ║
║  [1] [2] [3] ... [20] Proxima >                              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 7. Metricas de Sucesso

| Metrica | Meta | Como Medir |
|---------|------|------------|
| Downloads de workflows | 1000/mes | Analytics |
| Tempo medio de busca | < 30 segundos | Logs |
| Novos cadastros | 50/mes | Database |
| Satisfacao do usuario | > 4/5 | Pesquisa |
| Uso do chatbot | 500 conversas/mes | Logs |

---

## 8. Fases de Implementacao

### Fase 1 - MVP (Minimo Viavel)
- [x] Catalogo de workflows
- [x] Sistema de busca basico
- [x] Pagina de detalhes
- [x] Download de JSON
- [ ] Deploy inicial

### Fase 2 - Busca Avancada
- [ ] Filtros por categoria
- [ ] Filtros por integracao
- [ ] Tags e ordenacao
- [ ] Busca full-text

### Fase 3 - Interacao
- [ ] Sistema de usuarios
- [ ] Favoritos
- [ ] Cadastro de workflows
- [ ] Comentarios

### Fase 4 - Inteligencia
- [ ] Chatbot assistente
- [ ] Recomendacoes
- [ ] Analytics

---

## 9. Glossario

| Termo | Definicao |
|-------|-----------|
| **Workflow** | Automacao criada no n8n, salva como arquivo JSON |
| **Node** | Bloco individual de um workflow (trigger, acao, logica) |
| **n8n** | Plataforma open-source de automacao de workflows |
| **RAG** | Retrieval Augmented Generation - tecnica de IA |
| **HITL** | Human-in-the-Loop - validacao humana em automacoes |
| **AI Agent** | Agente inteligente que usa LLMs para tomar decisoes |

---

## 10. Referencias

- Site atual: https://inematds.github.io/N8Np/
- Repositorio: https://github.com/inematds/N8Np
- Comunidade: https://t.me/n8np
- n8n Docs: https://docs.n8n.io/

---

**Aprovado por:** Sistema Automatizado
**Data:** 31/12/2025
