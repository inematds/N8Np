# Epic 2: Sistema de Busca

## Descricao

Implementar sistema de busca completo que permite usuarios encontrar workflows por texto livre, filtros de categoria, integracao e dificuldade.

## Objetivo

Permitir que usuarios encontrem rapidamente o workflow ideal para sua necessidade.

## Criterios de Aceite do Epic

- [ ] Usuario pode buscar por texto livre
- [ ] Usuario pode filtrar por categoria
- [ ] Usuario pode filtrar por integracao
- [ ] Usuario pode filtrar por dificuldade
- [ ] Resultados sao relevantes e ordenados
- [ ] Busca retorna em menos de 500ms

---

## Stories

### Story 2.1: Barra de Busca Basica

**Como** usuario
**Quero** digitar texto na barra de busca
**Para** encontrar workflows por nome ou descricao

**Tarefas:**
- [ ] Criar componente SearchBar
- [ ] Implementar debounce (300ms)
- [ ] Criar API route GET /api/search?q=texto
- [ ] Implementar full-text search no Supabase
- [ ] Mostrar resultados em tempo real

**Componente:**
```tsx
// components/search/search-bar.tsx
interface SearchBarProps {
  onSearch: (query: string) => void;
  placeholder?: string;
}

// Features:
// - Input com icone de lupa
// - Debounce de 300ms
// - Botao X para limpar
// - Loading indicator
```

**Query Supabase:**
```sql
SELECT * FROM workflows
WHERE fts @@ plainto_tsquery('portuguese', $query)
ORDER BY ts_rank(fts, plainto_tsquery('portuguese', $query)) DESC
LIMIT 20;
```

**Criterios de Aceite:**
- [ ] Busca por nome funciona
- [ ] Busca por descricao funciona
- [ ] Debounce evita requisicoes excessivas
- [ ] Loading indicator durante busca
- [ ] Resultados ordenados por relevancia

---

### Story 2.2: Filtros por Categoria

**Como** usuario
**Quero** filtrar workflows por categoria
**Para** ver apenas o tipo que me interessa

**Tarefas:**
- [ ] Criar componente CategoryFilter
- [ ] Adicionar dropdown/chips de categorias
- [ ] Combinar filtro com busca textual
- [ ] Atualizar URL com parametros

**Componente:**
```tsx
// components/search/search-filters.tsx
interface FilterProps {
  categories: Category[];
  selectedCategory?: string;
  onCategoryChange: (slug: string | null) => void;
}

// Opcoes:
// - Dropdown select
// - Chips clicaveis
// - Multi-select (futuro)
```

**URL Pattern:**
```
/search?q=chatbot&category=ai-agents
```

**Criterios de Aceite:**
- [ ] Usuario pode selecionar categoria
- [ ] Filtro combina com busca textual
- [ ] URL reflete filtros aplicados
- [ ] Compartilhar URL mantem filtros

---

### Story 2.3: Filtros por Integracao

**Como** usuario
**Quero** filtrar por integracao (OpenAI, Google, etc)
**Para** ver apenas workflows compativeis com minhas ferramentas

**Tarefas:**
- [ ] Criar lista de integracoes disponiveis
- [ ] Adicionar icones para cada integracao
- [ ] Criar filtro multi-select
- [ ] Combinar com outros filtros

**Integracoes Principais:**
```typescript
const INTEGRATIONS = [
  { id: 'openai', name: 'OpenAI', icon: 'openai.svg' },
  { id: 'google', name: 'Google', icon: 'google.svg' },
  { id: 'supabase', name: 'Supabase', icon: 'supabase.svg' },
  { id: 'airtable', name: 'Airtable', icon: 'airtable.svg' },
  { id: 'gmail', name: 'Gmail', icon: 'gmail.svg' },
  { id: 'whatsapp', name: 'WhatsApp', icon: 'whatsapp.svg' },
  // ...
];
```

**Query:**
```sql
SELECT * FROM workflows
WHERE integrations @> ARRAY['openai']
```

**Criterios de Aceite:**
- [ ] Lista todas integracoes com icones
- [ ] Multi-select funciona
- [ ] Combina com outros filtros
- [ ] Mostra quantidade por integracao

---

### Story 2.4: Filtro por Dificuldade

**Como** usuario
**Quero** filtrar por nivel de dificuldade
**Para** encontrar workflows adequados ao meu nivel

**Tarefas:**
- [ ] Criar componente DifficultyFilter
- [ ] Implementar slider ou radio buttons
- [ ] Definir niveis (1-5 estrelas)
- [ ] Adicionar ao sistema de filtros

**Componente:**
```tsx
// Opcoes de UI:
// 1. Slider: 1 ──●── 5
// 2. Radio: ○ Facil ○ Medio ○ Avancado ○ Todos
// 3. Estrelas clicaveis: ★★★☆☆

// Mapeamento:
// Facil: 1-2
// Medio: 3
// Avancado: 4-5
```

**Criterios de Aceite:**
- [ ] Usuario pode selecionar dificuldade
- [ ] Filtro funciona corretamente
- [ ] Combina com outros filtros

---

### Story 2.5: Pagina de Resultados de Busca

**Como** usuario
**Quero** ver resultados de busca em pagina dedicada
**Para** ter mais espaco para explorar

**Tarefas:**
- [ ] Criar pagina /search
- [ ] Combinar todos os filtros
- [ ] Mostrar quantidade de resultados
- [ ] Adicionar ordenacao
- [ ] Implementar paginacao

**Layout:**
```
[Header]

🔍 Resultados para "chatbot rag"
Encontrados: 15 workflows

[Filtros]
Categoria: [AI Agents ▼]
Integracao: [OpenAI] [Supabase]
Dificuldade: [★★★☆☆]

Ordenar por: [Relevancia ▼]

[Card] [Card] [Card]
[Card] [Card] [Card]

[1] [2] [3] >

[Footer]
```

**Criterios de Aceite:**
- [ ] Mostra quantidade de resultados
- [ ] Todos filtros funcionam juntos
- [ ] Ordenacao funciona
- [ ] Paginacao funciona
- [ ] Estado vazio quando sem resultados

---

### Story 2.6: Sugestoes de Busca

**Como** usuario
**Quero** ver sugestoes enquanto digito
**Para** encontrar mais rapido

**Tarefas:**
- [ ] Criar componente SearchSuggestions
- [ ] Buscar sugestoes em tempo real
- [ ] Mostrar dropdown com resultados
- [ ] Navegar com teclado (setas)

**Componente:**
```tsx
// Mostra enquanto usuario digita:
// ┌────────────────────────────────┐
// │ 🔍 chatb                        │
// ├────────────────────────────────┤
// │ 📄 Chatbot Evolution Instagram  │
// │ 📄 Chatbot RAG Pipeline         │
// │ 📄 Chatbot WhatsApp Agent       │
// │                                 │
// │ Ver todos resultados para "chatb"│
// └────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Sugestoes aparecem apos 2 caracteres
- [ ] Maximo 5 sugestoes
- [ ] Clicar navega para workflow
- [ ] Setas do teclado funcionam
- [ ] Enter busca termo completo

---

### Story 2.7: Tags e Busca por Tags

**Como** usuario
**Quero** clicar em tags para buscar
**Para** explorar workflows similares

**Tarefas:**
- [ ] Adicionar tags aos workflows
- [ ] Criar componente TagBadge clicavel
- [ ] Filtrar por tag quando clicado
- [ ] Mostrar tags populares

**Tags Comuns:**
```
#rag #chatbot #vendas #atendimento #email
#whatsapp #linkedin #invoice #scraping
#voice #hitl #orchestrator #automation
```

**Criterios de Aceite:**
- [ ] Tags aparecem nos cards
- [ ] Clicar na tag filtra resultados
- [ ] Pagina mostra tags populares

---

## Definicao de Pronto (DoD)

- [ ] Busca retorna em < 500ms
- [ ] Funciona em mobile
- [ ] Testes de integracao passando
- [ ] Acessivel com teclado

---

## Estimativa

| Story | Complexidade | Pontos |
|-------|--------------|--------|
| 2.1 Busca Basica | Media | 5 |
| 2.2 Filtro Categoria | Baixa | 2 |
| 2.3 Filtro Integracao | Media | 3 |
| 2.4 Filtro Dificuldade | Baixa | 2 |
| 2.5 Pagina Resultados | Media | 3 |
| 2.6 Sugestoes | Alta | 5 |
| 2.7 Tags | Media | 3 |
| **Total** | | **23** |

---

## Dependencias

- Requer Epic 1 (Catalogo) completo
- Requer full-text search configurado no Supabase
