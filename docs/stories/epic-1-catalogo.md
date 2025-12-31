# Epic 1: Catalogo de Workflows

## Descricao

Criar o catalogo principal onde usuarios podem navegar por todos os 532 workflows organizados por categoria, ver detalhes e baixar arquivos JSON.

## Objetivo

Permitir que usuarios encontrem e baixem workflows de forma facil e organizada.

## Criterios de Aceite do Epic

- [ ] Usuario pode ver lista de todas as categorias na home
- [ ] Usuario pode clicar em categoria e ver workflows dela
- [ ] Usuario pode ver card com informacoes basicas do workflow
- [ ] Usuario pode clicar em workflow e ver pagina de detalhes
- [ ] Usuario pode baixar o arquivo JSON do workflow

---

## Stories

### Story 1.1: Setup do Projeto

**Como** desenvolvedor
**Quero** ter o projeto Next.js configurado
**Para** comecar o desenvolvimento

**Tarefas:**
- [ ] Criar projeto Next.js 14 com TypeScript
- [ ] Configurar Tailwind CSS
- [ ] Instalar shadcn/ui
- [ ] Configurar ESLint e Prettier
- [ ] Criar estrutura de pastas
- [ ] Configurar variaveis de ambiente

**Arquivos a criar:**
```
n8np-app/
├── app/layout.tsx
├── app/page.tsx
├── tailwind.config.ts
├── .env.local
└── package.json
```

**Criterios de Aceite:**
- [ ] `npm run dev` inicia servidor sem erros
- [ ] Pagina inicial renderiza com Tailwind
- [ ] TypeScript funcionando

---

### Story 1.2: Configurar Supabase

**Como** desenvolvedor
**Quero** ter o banco de dados configurado
**Para** armazenar workflows e categorias

**Tarefas:**
- [ ] Criar projeto no Supabase
- [ ] Criar tabela `categories`
- [ ] Criar tabela `workflows`
- [ ] Criar tabela `workflow_nodes`
- [ ] Configurar indices
- [ ] Criar cliente Supabase no projeto

**SQL a executar:**
```sql
-- Ver docs/architecture.md secao 3.2
```

**Arquivos a criar:**
```
lib/supabase/client.ts
lib/supabase/server.ts
types/supabase.ts
```

**Criterios de Aceite:**
- [ ] Conexao com Supabase funcionando
- [ ] Tabelas criadas com schema correto
- [ ] Cliente tipado com TypeScript

---

### Story 1.3: Seed de Dados Iniciais

**Como** desenvolvedor
**Quero** popular o banco com os 532 workflows
**Para** ter dados reais para testar

**Tarefas:**
- [ ] Criar script de seed
- [ ] Parsear JSONs dos workflows
- [ ] Extrair metadados (nome, nodes, integracoes)
- [ ] Inserir categorias
- [ ] Inserir workflows
- [ ] Inserir nodes de cada workflow

**Script:**
```typescript
// scripts/seed.ts
// Le arquivos de data/workflows/
// Extrai informacoes
// Insere no Supabase
```

**Criterios de Aceite:**
- [ ] 6 categorias inseridas
- [ ] 532 workflows inseridos
- [ ] Todos os nodes mapeados

---

### Story 1.4: Pagina Home com Categorias

**Como** usuario
**Quero** ver as categorias na pagina inicial
**Para** escolher qual tipo de workflow procurar

**Tarefas:**
- [ ] Criar componente CategoryCard
- [ ] Criar componente CategoryGrid
- [ ] Criar API route GET /api/categories
- [ ] Criar hook useCategories
- [ ] Implementar pagina Home

**Componentes:**
```tsx
// components/category/category-card.tsx
interface CategoryCardProps {
  category: {
    id: string;
    name: string;
    slug: string;
    icon: string;
    workflow_count: number;
  };
}

// Mostra: icone, nome, quantidade
```

**Layout da Home:**
```
[Header]

[SearchBar]

CATEGORIAS
[AI Agents (198)] [Automacoes (66)] [Integracoes (36)]
[Arquitetura (10)] [HITL (7)] [Outros (256)]

WORKFLOWS POPULARES
[Card] [Card] [Card] [Card]

[Footer]
```

**Criterios de Aceite:**
- [ ] 6 cards de categoria renderizam
- [ ] Cada card mostra icone, nome e quantidade
- [ ] Cards sao clicaveis e navegam para /categories/[slug]

---

### Story 1.5: Pagina de Categoria com Lista de Workflows

**Como** usuario
**Quero** ver todos os workflows de uma categoria
**Para** encontrar o que preciso

**Tarefas:**
- [ ] Criar componente WorkflowCard
- [ ] Criar componente WorkflowGrid
- [ ] Criar API route GET /api/workflows?category=slug
- [ ] Criar hook useWorkflows
- [ ] Implementar pagina /categories/[slug]
- [ ] Adicionar paginacao

**Componente WorkflowCard:**
```tsx
// components/workflow/workflow-card.tsx
// Mostra:
// - Nome
// - Descricao (truncada 100 chars)
// - Categoria badge
// - Quantidade de nodes
// - Icones de integracoes
// - Dificuldade (estrelas)
// - Botoes: Ver Detalhes, Baixar
```

**Layout:**
```
[Header]

AI Agents (198 workflows)

[Card] [Card] [Card]
[Card] [Card] [Card]
[Card] [Card] [Card]

[1] [2] [3] ... [20] >

[Footer]
```

**Criterios de Aceite:**
- [ ] Lista workflows da categoria correta
- [ ] Cards mostram todas informacoes
- [ ] Paginacao funciona (20 por pagina)
- [ ] Loading state enquanto carrega

---

### Story 1.6: Pagina de Detalhes do Workflow

**Como** usuario
**Quero** ver todas informacoes de um workflow
**Para** entender se ele resolve meu problema

**Tarefas:**
- [ ] Criar componente WorkflowDetail
- [ ] Criar componente WorkflowNodes
- [ ] Criar componente WorkflowIntegrations
- [ ] Criar API route GET /api/workflows/[id]
- [ ] Criar hook useWorkflow
- [ ] Implementar pagina /workflows/[slug]

**Layout:**
```
[Header]

═══════════════════════════════════════
  RAG Pipeline & Chatbot
═══════════════════════════════════════

DESCRICAO
Este workflow cria um chatbot...

O QUE VOCE PRECISA
- Conta Google
- Chave API OpenAI
- Banco Supabase

NODES USADOS (15)
• Google Drive Trigger
• Document Loader
• AI Agent
...

INTEGRACOES
[OpenAI] [Supabase] [Google]

[████ BAIXAR JSON ████]

WORKFLOWS RELACIONADOS
[Card] [Card] [Card]

[Footer]
```

**Criterios de Aceite:**
- [ ] Mostra todas informacoes do workflow
- [ ] Lista todos os nodes
- [ ] Mostra integracoes com icones
- [ ] Sugere workflows relacionados

---

### Story 1.7: Download de JSON

**Como** usuario
**Quero** baixar o arquivo JSON do workflow
**Para** importar no meu n8n

**Tarefas:**
- [ ] Criar API route GET /api/workflows/download/[id]
- [ ] Incrementar contador de downloads
- [ ] Gerar arquivo com nome correto
- [ ] Implementar botao de download

**Fluxo:**
```
Usuario clica "Baixar JSON"
         ↓
Fetch /api/workflows/download/{id}
         ↓
API incrementa downloads
         ↓
API retorna JSON com headers corretos
         ↓
Browser baixa arquivo "{nome}.json"
```

**Criterios de Aceite:**
- [ ] Arquivo baixa com nome correto
- [ ] Contador de downloads incrementa
- [ ] JSON e valido para importar no n8n

---

## Definicao de Pronto (DoD)

- [ ] Codigo revisado
- [ ] Testes unitarios passando
- [ ] Sem erros de TypeScript
- [ ] Responsivo (mobile/desktop)
- [ ] Acessivel (a11y basico)
- [ ] Documentado

---

## Estimativa

| Story | Complexidade | Pontos |
|-------|--------------|--------|
| 1.1 Setup | Baixa | 2 |
| 1.2 Supabase | Media | 3 |
| 1.3 Seed | Media | 3 |
| 1.4 Home | Media | 3 |
| 1.5 Lista | Media | 5 |
| 1.6 Detalhes | Alta | 5 |
| 1.7 Download | Baixa | 2 |
| **Total** | | **23** |

---

## Dependencias

- Nenhuma dependencia externa
- Este epic deve ser completado primeiro
