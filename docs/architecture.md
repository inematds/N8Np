# Arquitetura do Sistema N8Np

## Documento de Arquitetura Tecnica

**Versao:** 1.0
**Data:** 31 de Dezembro de 2025

---

## 1. Visao Geral da Arquitetura

### 1.1 Diagrama de Alto Nivel

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Next.js 14 (App Router)               │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │    │
│  │  │  Home    │ │ Catalogo │ │ Detalhes │ │ Cadastro │   │    │
│  │  │  Page    │ │  Page    │ │   Page   │ │   Page   │   │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │    │
│  │                                                          │    │
│  │  ┌──────────────────────────────────────────────────┐   │    │
│  │  │              Componentes Compartilhados           │   │    │
│  │  │  SearchBar | WorkflowCard | Filters | ChatWidget │   │    │
│  │  └──────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ API Routes / Server Actions
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    API Routes (Next.js)                  │    │
│  │  /api/workflows     - CRUD de workflows                  │    │
│  │  /api/search        - Busca full-text                    │    │
│  │  /api/categories    - Listagem de categorias             │    │
│  │  /api/chat          - Endpoint do chatbot                │    │
│  │  /api/auth          - Autenticacao                       │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATABASE                                  │
│  ┌──────────────────────┐  ┌──────────────────────┐            │
│  │      Supabase        │  │    Vector Store      │            │
│  │  - workflows         │  │  (embeddings para    │            │
│  │  - categories        │  │   busca semantica)   │            │
│  │  - users             │  │                      │            │
│  │  - favorites         │  │                      │            │
│  └──────────────────────┘  └──────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SERVICOS EXTERNOS                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   OpenAI     │  │    GitHub    │  │   Vercel     │          │
│  │  (Chatbot)   │  │   (Storage)  │  │  (Deploy)    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Decisoes Arquiteturais

| Decisao | Escolha | Justificativa |
|---------|---------|---------------|
| Framework | Next.js 14 | SSR, API Routes, App Router, otimo DX |
| Estilizacao | Tailwind CSS | Rapido, consistente, responsivo |
| Componentes | shadcn/ui | Acessiveis, customizaveis, bonitos |
| Database | Supabase | PostgreSQL + Auth + Storage gratuito |
| Deploy | Vercel | Integracao nativa com Next.js |
| Chatbot | OpenAI API | GPT-4 para assistente inteligente |

---

## 2. Estrutura do Projeto

```
n8np-app/
├── app/                          # App Router (Next.js 14)
│   ├── layout.tsx                # Layout principal
│   ├── page.tsx                  # Home page
│   ├── workflows/
│   │   ├── page.tsx              # Listagem de workflows
│   │   └── [id]/
│   │       └── page.tsx          # Detalhes do workflow
│   ├── categories/
│   │   └── [slug]/
│   │       └── page.tsx          # Workflows por categoria
│   ├── submit/
│   │   └── page.tsx              # Cadastro de workflow
│   ├── curso/
│   │   └── page.tsx              # Area de aprendizado
│   └── api/
│       ├── workflows/
│       │   ├── route.ts          # GET all, POST new
│       │   └── [id]/
│       │       └── route.ts      # GET one, PUT, DELETE
│       ├── search/
│       │   └── route.ts          # Busca full-text
│       ├── chat/
│       │   └── route.ts          # Chatbot endpoint
│       └── auth/
│           └── [...nextauth]/
│               └── route.ts      # NextAuth.js
│
├── components/
│   ├── ui/                       # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   └── ...
│   ├── workflow/
│   │   ├── workflow-card.tsx     # Card de workflow
│   │   ├── workflow-grid.tsx     # Grid de cards
│   │   ├── workflow-filters.tsx  # Filtros
│   │   └── workflow-detail.tsx   # Detalhes completos
│   ├── search/
│   │   ├── search-bar.tsx        # Barra de busca
│   │   └── search-results.tsx    # Resultados
│   ├── chat/
│   │   ├── chat-widget.tsx       # Widget flutuante
│   │   └── chat-messages.tsx     # Mensagens
│   └── layout/
│       ├── header.tsx            # Cabecalho
│       ├── footer.tsx            # Rodape
│       └── sidebar.tsx           # Menu lateral
│
├── lib/
│   ├── supabase.ts               # Cliente Supabase
│   ├── openai.ts                 # Cliente OpenAI
│   ├── utils.ts                  # Funcoes utilitarias
│   └── workflow-parser.ts        # Parser de JSON n8n
│
├── types/
│   ├── workflow.ts               # Tipos de workflow
│   ├── category.ts               # Tipos de categoria
│   └── user.ts                   # Tipos de usuario
│
├── hooks/
│   ├── use-workflows.ts          # Hook para workflows
│   ├── use-search.ts             # Hook para busca
│   └── use-chat.ts               # Hook para chat
│
├── data/
│   └── workflows/                # JSONs dos workflows (estatico)
│
├── public/
│   └── icons/                    # Icones de integracoes
│
├── styles/
│   └── globals.css               # Estilos globais
│
├── tailwind.config.ts
├── next.config.js
├── package.json
└── README.md
```

---

## 3. Modelo de Dados

### 3.1 Diagrama ER

```
┌────────────────────┐       ┌────────────────────┐
│     workflows      │       │    categories      │
├────────────────────┤       ├────────────────────┤
│ id (PK)            │───┐   │ id (PK)            │
│ name               │   │   │ name               │
│ slug               │   │   │ slug               │
│ description        │   │   │ icon               │
│ json_content       │   │   │ description        │
│ category_id (FK)───│───┼──>│ workflow_count     │
│ nodes_count        │   │   │ created_at         │
│ integrations[]     │   │   └────────────────────┘
│ difficulty         │   │
│ tags[]             │   │   ┌────────────────────┐
│ author_id (FK)─────│───┼──>│      users         │
│ downloads          │   │   ├────────────────────┤
│ created_at         │   │   │ id (PK)            │
│ updated_at         │   │   │ email              │
└────────────────────┘   │   │ name               │
         │               │   │ avatar_url         │
         │               │   │ provider           │
         ▼               │   │ created_at         │
┌────────────────────┐   │   └────────────────────┘
│   workflow_nodes   │   │            │
├────────────────────┤   │            │
│ id (PK)            │   │            │
│ workflow_id (FK)───│───┘            │
│ node_type          │                │
│ node_name          │                ▼
│ position           │   ┌────────────────────┐
└────────────────────┘   │    favorites       │
                         ├────────────────────┤
                         │ id (PK)            │
                         │ user_id (FK)       │
                         │ workflow_id (FK)   │
                         │ created_at         │
                         └────────────────────┘
```

### 3.2 Schema SQL (Supabase)

```sql
-- Categorias
CREATE TABLE categories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  slug VARCHAR(100) UNIQUE NOT NULL,
  icon VARCHAR(50),
  description TEXT,
  workflow_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Workflows
CREATE TABLE workflows (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  json_content JSONB NOT NULL,
  category_id UUID REFERENCES categories(id),
  nodes_count INTEGER DEFAULT 0,
  integrations TEXT[] DEFAULT '{}',
  difficulty INTEGER DEFAULT 1 CHECK (difficulty >= 1 AND difficulty <= 5),
  tags TEXT[] DEFAULT '{}',
  author_id UUID REFERENCES auth.users(id),
  downloads INTEGER DEFAULT 0,
  is_published BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Nodes de workflows (para busca detalhada)
CREATE TABLE workflow_nodes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_id UUID REFERENCES workflows(id) ON DELETE CASCADE,
  node_type VARCHAR(255) NOT NULL,
  node_name VARCHAR(255),
  position JSONB
);

-- Favoritos
CREATE TABLE favorites (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  workflow_id UUID REFERENCES workflows(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, workflow_id)
);

-- Indices para busca
CREATE INDEX idx_workflows_category ON workflows(category_id);
CREATE INDEX idx_workflows_tags ON workflows USING GIN(tags);
CREATE INDEX idx_workflows_integrations ON workflows USING GIN(integrations);
CREATE INDEX idx_workflow_nodes_type ON workflow_nodes(node_type);

-- Full-text search
ALTER TABLE workflows ADD COLUMN fts tsvector
  GENERATED ALWAYS AS (
    setweight(to_tsvector('portuguese', coalesce(name, '')), 'A') ||
    setweight(to_tsvector('portuguese', coalesce(description, '')), 'B') ||
    setweight(to_tsvector('english', array_to_string(tags, ' ')), 'C')
  ) STORED;

CREATE INDEX idx_workflows_fts ON workflows USING GIN(fts);
```

---

## 4. APIs

### 4.1 Endpoints

#### GET /api/workflows
Lista todos os workflows com paginacao e filtros.

```typescript
// Request
GET /api/workflows?page=1&limit=20&category=ai-agents&integration=openai

// Response
{
  "data": [
    {
      "id": "uuid",
      "name": "RAG Pipeline & Chatbot",
      "slug": "rag-pipeline-chatbot",
      "description": "Chatbot com RAG...",
      "category": {
        "id": "uuid",
        "name": "AI Agents",
        "slug": "ai-agents"
      },
      "nodes_count": 15,
      "integrations": ["openai", "supabase", "google"],
      "difficulty": 3,
      "tags": ["rag", "chatbot", "ia"],
      "downloads": 150
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 198,
    "pages": 10
  }
}
```

#### GET /api/workflows/[id]
Retorna detalhes de um workflow especifico.

```typescript
// Response
{
  "id": "uuid",
  "name": "RAG Pipeline & Chatbot",
  "description": "Este workflow cria um chatbot...",
  "json_content": { /* n8n workflow JSON */ },
  "category": { "id": "uuid", "name": "AI Agents" },
  "nodes": [
    { "type": "n8n-nodes-base.googleDriveTrigger", "name": "Drive Trigger" },
    { "type": "@n8n/n8n-nodes-langchain.agent", "name": "AI Agent" }
  ],
  "integrations": ["openai", "supabase", "google"],
  "difficulty": 3,
  "tags": ["rag", "chatbot"],
  "downloads": 150,
  "related_workflows": [...]
}
```

#### POST /api/workflows
Cadastra novo workflow.

```typescript
// Request
{
  "json_file": "base64 encoded JSON",
  "description": "Descricao do workflow",
  "category_id": "uuid",
  "tags": ["tag1", "tag2"]
}

// Response
{
  "id": "uuid",
  "name": "Extracted from JSON",
  "slug": "extracted-from-json",
  "message": "Workflow cadastrado com sucesso"
}
```

#### GET /api/search
Busca full-text em workflows.

```typescript
// Request
GET /api/search?q=chatbot%20rag&category=ai-agents

// Response
{
  "results": [...],
  "total": 15,
  "query": "chatbot rag"
}
```

#### POST /api/chat
Conversa com o chatbot assistente.

```typescript
// Request
{
  "message": "Preciso automatizar WhatsApp",
  "history": [...]
}

// Response
{
  "response": "Encontrei 3 workflows para voce...",
  "suggestions": [
    { "id": "uuid", "name": "WhatsApp Agent" },
    { "id": "uuid", "name": "WhatsApp + GPT" }
  ]
}
```

---

## 5. Componentes Principais

### 5.1 WorkflowCard

```tsx
interface WorkflowCardProps {
  workflow: {
    id: string;
    name: string;
    description: string;
    category: Category;
    nodes_count: number;
    integrations: string[];
    difficulty: number;
  };
}

// Renderiza:
// - Nome do workflow
// - Descricao truncada (100 chars)
// - Categoria com icone
// - Quantidade de nodes
// - Icones das integracoes
// - Estrelas de dificuldade
// - Botoes: Ver Detalhes, Baixar JSON
```

### 5.2 SearchBar

```tsx
interface SearchBarProps {
  onSearch: (query: string) => void;
  filters: {
    category?: string;
    integration?: string;
    difficulty?: number;
  };
  onFilterChange: (filters: Filters) => void;
}

// Renderiza:
// - Input de busca com debounce
// - Dropdown de categorias
// - Dropdown de integracoes
// - Slider de dificuldade
// - Botao de buscar
```

### 5.3 ChatWidget

```tsx
// Widget flutuante no canto inferior direito
// - Botao para abrir/fechar
// - Area de mensagens com scroll
// - Input para digitar
// - Sugestoes de workflows inline
// - Historico da conversa
```

---

## 6. Fluxo de Dados

### 6.1 Busca de Workflow

```
Usuario digita "chatbot rag"
         │
         ▼
SearchBar.onChange (debounce 300ms)
         │
         ▼
useSearch hook → fetch('/api/search?q=chatbot%20rag')
         │
         ▼
API Route → Supabase full-text search
         │
         ▼
Retorna resultados ordenados por relevancia
         │
         ▼
SearchResults.tsx renderiza cards
```

### 6.2 Download de Workflow

```
Usuario clica em "Baixar JSON"
         │
         ▼
workflow-detail.tsx → downloadWorkflow(id)
         │
         ▼
fetch('/api/workflows/${id}')
         │
         ▼
API incrementa contador de downloads
         │
         ▼
Retorna json_content
         │
         ▼
Cria Blob e dispara download
         │
         ▼
Arquivo "${name}.json" baixado
```

### 6.3 Conversa com Chatbot

```
Usuario: "quero automatizar instagram"
         │
         ▼
ChatWidget → POST /api/chat
         │
         ▼
API Route:
  1. Busca workflows relacionados (semantic search)
  2. Envia contexto + pergunta para OpenAI
  3. GPT gera resposta com sugestoes
         │
         ▼
Retorna resposta + workflow suggestions
         │
         ▼
ChatWidget renderiza resposta + cards clicaveis
```

---

## 7. Seguranca

### 7.1 Autenticacao

- NextAuth.js com providers: Google, GitHub, Email
- JWT tokens com refresh
- Sessoes armazenadas no Supabase

### 7.2 Autorizacao

| Acao | Publico | Logado | Admin |
|------|---------|--------|-------|
| Ver workflows | ✅ | ✅ | ✅ |
| Baixar JSON | ✅ | ✅ | ✅ |
| Favoritar | ❌ | ✅ | ✅ |
| Cadastrar workflow | ❌ | ✅ | ✅ |
| Editar workflow | ❌ | Proprio | ✅ |
| Deletar workflow | ❌ | Proprio | ✅ |
| Moderar | ❌ | ❌ | ✅ |

### 7.3 Validacoes

- Sanitizacao de inputs (XSS)
- Validacao de JSON uploadado
- Rate limiting: 100 req/min por IP
- CORS configurado

---

## 8. Performance

### 8.1 Estrategias

| Tecnica | Onde | Beneficio |
|---------|------|-----------|
| SSG | Home, Categorias | Paginas estaticas, rapidas |
| ISR | Detalhes workflow | Revalidacao a cada 1h |
| CDN | Assets estaticos | Distribuicao global |
| Lazy loading | Imagens, cards | Carregamento sob demanda |
| Debounce | Busca | Menos requisicoes |

### 8.2 Metricas Alvo

- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1

---

## 9. Monitoramento

### 9.1 Ferramentas

- **Vercel Analytics**: Metricas de performance
- **Supabase Dashboard**: Queries, uso do banco
- **Sentry**: Erros e excecoes
- **PostHog**: Analytics de produto

### 9.2 Alertas

- Erro rate > 1%
- Latencia API > 500ms
- Uso de banco > 80%

---

## 10. Deploy

### 10.1 Pipeline

```
git push main
     │
     ▼
GitHub Actions:
  - Lint (ESLint)
  - Type check (TypeScript)
  - Tests (Jest)
     │
     ▼
Vercel Build:
  - Next.js build
  - Geracao de paginas estaticas
     │
     ▼
Vercel Deploy:
  - Preview (PR)
  - Production (main)
     │
     ▼
Site live em n8np.vercel.app
```

### 10.2 Ambientes

| Ambiente | URL | Branch |
|----------|-----|--------|
| Development | localhost:3000 | feature/* |
| Preview | n8np-xxx.vercel.app | PR |
| Production | n8np.vercel.app | main |

---

## 11. Escalabilidade

### 11.1 Atual (MVP)

- Supabase Free tier (500MB, 50k req/mes)
- Vercel Hobby (100GB bandwidth)
- Suficiente para ~1000 usuarios/mes

### 11.2 Futuro

- Supabase Pro para mais storage
- Vercel Pro para mais bandwidth
- Redis para cache de buscas
- CDN proprio para JSONs

---

**Documento mantido por:** Equipe N8Np
**Ultima atualizacao:** 31/12/2025
