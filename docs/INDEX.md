# Documentacao do Sistema N8Np

## Indice de Documentos

Este diretorio contem toda a documentacao tecnica e de produto do sistema N8Np - Biblioteca de Workflows n8n.

---

## Documentos Principais

### Produto

| Documento | Descricao |
|-----------|-----------|
| [PRD](prd.md) | Documento de Requisitos do Produto - visao geral, funcionalidades, wireframes |
| [ROADMAP](ROADMAP.md) | Plano de implementacao por fases |

### Arquitetura

| Documento | Descricao |
|-----------|-----------|
| [Arquitetura](architecture.md) | Visao geral da arquitetura, modelo de dados, APIs |
| [Tech Stack](architecture/tech-stack.md) | Tecnologias utilizadas e dependencias |
| [Coding Standards](architecture/coding-standards.md) | Padroes de codigo e boas praticas |
| [Source Tree](architecture/source-tree.md) | Estrutura de diretorios do projeto |

### Stories (Epics)

| Epic | Descricao | Pontos |
|------|-----------|--------|
| [Epic 1: Catalogo](stories/epic-1-catalogo.md) | Setup, catalogo, detalhes, download | 23 |
| [Epic 2: Busca](stories/epic-2-busca.md) | Full-text search, filtros, tags | 23 |
| [Epic 3: Cadastro](stories/epic-3-cadastro.md) | Upload, parser, formulario, publicacao | 28 |
| [Epic 4: Usuarios](stories/epic-4-usuarios.md) | Auth, login, favoritos, perfil | 24 |
| [Epic 5: Chatbot](stories/epic-5-chatbot.md) | Widget, OpenAI, busca semantica | 31 |

---

## Estrutura de Pastas

```
docs/
├── INDEX.md                 # Este arquivo
├── prd.md                   # Requisitos do produto
├── architecture.md          # Arquitetura geral
├── ROADMAP.md               # Plano de fases
│
├── architecture/            # Detalhes tecnicos
│   ├── tech-stack.md        # Tecnologias
│   ├── coding-standards.md  # Padroes de codigo
│   └── source-tree.md       # Estrutura do projeto
│
├── stories/                 # Epics e user stories
│   ├── epic-1-catalogo.md
│   ├── epic-2-busca.md
│   ├── epic-3-cadastro.md
│   ├── epic-4-usuarios.md
│   └── epic-5-chatbot.md
│
├── prd/                     # PRD fragmentado (futuro)
│
└── qa/                      # Documentos de QA (futuro)
```

---

## Como Usar Esta Documentacao

### Para Entender o Projeto
1. Comece pelo [PRD](prd.md) para entender o que e o sistema
2. Veja o [ROADMAP](ROADMAP.md) para entender as fases

### Para Desenvolver
1. Leia a [Arquitetura](architecture.md) para visao tecnica
2. Configure o ambiente seguindo [Tech Stack](architecture/tech-stack.md)
3. Siga os [Coding Standards](architecture/coding-standards.md)
4. Implemente as stories de cada Epic

### Para Contribuir
1. Escolha um Epic para trabalhar
2. Pegue uma Story especifica
3. Siga os criterios de aceite
4. Faca PR seguindo padroes

---

## Status do Projeto

| Fase | Status | Progresso |
|------|--------|-----------|
| Documentacao | ✅ Completa | 100% |
| Fase 1: MVP | ⬜ Nao iniciada | 0% |
| Fase 2: Busca | ⬜ Nao iniciada | 0% |
| Fase 3: Usuarios | ⬜ Nao iniciada | 0% |
| Fase 4: Cadastro | ⬜ Nao iniciada | 0% |
| Fase 5: Chatbot | ⬜ Nao iniciada | 0% |

---

## Contato

- **Repositorio:** https://github.com/inematds/N8Np
- **Site atual:** https://inematds.github.io/N8Np/
- **Comunidade:** https://t.me/n8np

---

*Documentacao gerada em 31/12/2025*
