# Roadmap - Sistema N8Np

## Visao Geral das Fases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                ROADMAP N8Np                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FASE 1: MVP                    FASE 2: BUSCA                               │
│  ┌─────────────────────┐        ┌─────────────────────┐                     │
│  │ • Setup projeto     │        │ • Full-text search  │                     │
│  │ • Catalogo          │───────>│ • Filtros           │                     │
│  │ • Detalhes          │        │ • Tags              │                     │
│  │ • Download          │        │ • Sugestoes         │                     │
│  └─────────────────────┘        └─────────────────────┘                     │
│           │                              │                                  │
│           │                              │                                  │
│           ▼                              ▼                                  │
│  FASE 3: USUARIOS               FASE 4: CADASTRO                            │
│  ┌─────────────────────┐        ┌─────────────────────┐                     │
│  │ • Autenticacao      │        │ • Upload JSON       │                     │
│  │ • Login Google      │───────>│ • Parser automatico │                     │
│  │ • Favoritos         │        │ • Formulario        │                     │
│  │ • Perfil            │        │ • Publicacao        │                     │
│  └─────────────────────┘        └─────────────────────┘                     │
│                                          │                                  │
│                                          │                                  │
│                                          ▼                                  │
│                                 FASE 5: CHATBOT                             │
│                                 ┌─────────────────────┐                     │
│                                 │ • Widget chat       │                     │
│                                 │ • OpenAI GPT-4      │                     │
│                                 │ • Busca semantica   │                     │
│                                 │ • Sugestoes IA      │                     │
│                                 └─────────────────────┘                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Fase 1: MVP (Minimo Viavel)

**Objetivo:** Ter o catalogo basico funcionando

### Entregas

| Item | Descricao | Status |
|------|-----------|--------|
| Setup | Next.js + Tailwind + shadcn | ⬜ |
| Database | Supabase com schema | ⬜ |
| Seed | 532 workflows importados | ⬜ |
| Home | Categorias + populares | ⬜ |
| Lista | Grid de workflows | ⬜ |
| Detalhes | Pagina completa | ⬜ |
| Download | Baixar JSON | ⬜ |

### Pontos: 23
### Prioridade: CRITICA

---

## Fase 2: Sistema de Busca

**Objetivo:** Usuarios podem encontrar workflows rapidamente

### Entregas

| Item | Descricao | Status |
|------|-----------|--------|
| Busca texto | Full-text PostgreSQL | ⬜ |
| Filtro categoria | Dropdown | ⬜ |
| Filtro integracao | Multi-select | ⬜ |
| Filtro dificuldade | Slider/radio | ⬜ |
| Resultados | Pagina dedicada | ⬜ |
| Sugestoes | Autocomplete | ⬜ |
| Tags | Clicaveis | ⬜ |

### Pontos: 23
### Prioridade: ALTA

---

## Fase 3: Sistema de Usuarios

**Objetivo:** Usuarios podem ter conta e favoritar

### Entregas

| Item | Descricao | Status |
|------|-----------|--------|
| Auth setup | Supabase Auth | ⬜ |
| Login | Email + Google | ⬜ |
| Cadastro | Com validacao | ⬜ |
| Header | Menu usuario | ⬜ |
| Favoritos | Sistema completo | ⬜ |
| Pagina favoritos | Lista pessoal | ⬜ |
| Perfil | Dados + stats | ⬜ |

### Pontos: 24
### Prioridade: MEDIA

---

## Fase 4: Cadastro de Workflows

**Objetivo:** Comunidade pode contribuir

### Entregas

| Item | Descricao | Status |
|------|-----------|--------|
| Pagina submit | Layout wizard | ⬜ |
| Upload JSON | Com validacao | ⬜ |
| Parser | Extracao automatica | ⬜ |
| Formulario | Metadados | ⬜ |
| Preview | Antes de publicar | ⬜ |
| Publicacao | Salvar no banco | ⬜ |
| Edicao | Workflow proprio | ⬜ |
| Delecao | Com confirmacao | ⬜ |

### Pontos: 28
### Prioridade: MEDIA

---

## Fase 5: Chatbot Assistente

**Objetivo:** IA ajuda usuarios a encontrar workflows

### Entregas

| Item | Descricao | Status |
|------|-----------|--------|
| Widget | Chat flutuante | ⬜ |
| Mensagens | Interface completa | ⬜ |
| Input | Envio de mensagens | ⬜ |
| API OpenAI | Integracao GPT-4 | ⬜ |
| Sugestoes | Cards no chat | ⬜ |
| Boas-vindas | Mensagem inicial | ⬜ |
| Semantic search | Embeddings | ⬜ |
| Conhecimento n8n | Respostas gerais | ⬜ |

### Pontos: 31
### Prioridade: BAIXA (nice-to-have)

---

## Resumo de Pontos

| Fase | Pontos | % do Total |
|------|--------|------------|
| Fase 1: MVP | 23 | 18% |
| Fase 2: Busca | 23 | 18% |
| Fase 3: Usuarios | 24 | 19% |
| Fase 4: Cadastro | 28 | 22% |
| Fase 5: Chatbot | 31 | 24% |
| **Total** | **129** | 100% |

---

## Ordem de Implementacao Recomendada

```
1. Epic 1 (MVP)
   └── Prerequisito para todos os outros

2. Epic 2 (Busca)
   └── Melhora UX significativamente

3. Epic 4 (Usuarios)
   └── Necessario para cadastro

4. Epic 3 (Cadastro)
   └── Depende de usuarios

5. Epic 5 (Chatbot)
   └── Feature avancada, pode ser feita depois
```

---

## Metricas de Sucesso por Fase

### Fase 1
- [ ] Site no ar e acessivel
- [ ] Todos 532 workflows visiveis
- [ ] Downloads funcionando

### Fase 2
- [ ] Busca retorna em < 500ms
- [ ] 80% dos usuarios encontram workflow em < 30s

### Fase 3
- [ ] 50+ usuarios cadastrados no primeiro mes
- [ ] 80% retention rate

### Fase 4
- [ ] 10+ workflows da comunidade no primeiro mes
- [ ] < 5% de workflows rejeitados

### Fase 5
- [ ] 500+ conversas/mes
- [ ] 70% de satisfacao com respostas

---

## Riscos e Mitigacoes

| Risco | Impacto | Mitigacao |
|-------|---------|-----------|
| OpenAI cara | Alto | Usar modelo mais barato, cache |
| Supabase limite | Medio | Monitorar uso, upgrade se necessario |
| Spam cadastros | Medio | Moderacao, rate limiting |
| Performance busca | Alto | Indices, cache, paginacao |

---

## Proximos Passos

1. **Imediato:** Iniciar Fase 1 (MVP)
2. **Semana 1-2:** Setup + Catalogo basico
3. **Semana 3:** Busca basica
4. **Semana 4:** Deploy MVP
5. **Iteracao:** Coletar feedback e ajustar
