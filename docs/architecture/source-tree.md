# Arvore de Diretorios - N8Np

## Estrutura Completa do Projeto

```
n8np-app/
│
├── app/                              # Next.js App Router
│   ├── layout.tsx                    # Layout raiz
│   ├── page.tsx                      # Home page (/)
│   ├── loading.tsx                   # Loading global
│   ├── error.tsx                     # Error boundary global
│   ├── not-found.tsx                 # Pagina 404
│   │
│   ├── workflows/                    # /workflows
│   │   ├── page.tsx                  # Listagem de workflows
│   │   ├── loading.tsx               # Loading da listagem
│   │   └── [slug]/                   # /workflows/[slug]
│   │       ├── page.tsx              # Detalhes do workflow
│   │       └── loading.tsx           # Loading dos detalhes
│   │
│   ├── categories/                   # /categories
│   │   └── [slug]/                   # /categories/[slug]
│   │       └── page.tsx              # Workflows por categoria
│   │
│   ├── search/                       # /search
│   │   └── page.tsx                  # Resultados de busca
│   │
│   ├── submit/                       # /submit
│   │   └── page.tsx                  # Formulario de cadastro
│   │
│   ├── curso/                        # /curso
│   │   ├── page.tsx                  # Lista de licoes
│   │   └── [lesson]/                 # /curso/[lesson]
│   │       └── page.tsx              # Detalhe da licao
│   │
│   ├── auth/                         # /auth
│   │   ├── login/
│   │   │   └── page.tsx              # Pagina de login
│   │   └── callback/
│   │       └── route.ts              # OAuth callback
│   │
│   └── api/                          # API Routes
│       ├── workflows/
│       │   ├── route.ts              # GET all, POST new
│       │   ├── [id]/
│       │   │   └── route.ts          # GET, PUT, DELETE one
│       │   └── download/
│       │       └── [id]/
│       │           └── route.ts      # Download JSON
│       │
│       ├── categories/
│       │   └── route.ts              # GET categorias
│       │
│       ├── search/
│       │   └── route.ts              # Busca full-text
│       │
│       ├── chat/
│       │   └── route.ts              # Chatbot endpoint
│       │
│       └── auth/
│           └── [...nextauth]/
│               └── route.ts          # NextAuth handlers
│
├── components/                       # Componentes React
│   │
│   ├── ui/                           # shadcn/ui (base)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   ├── select.tsx
│   │   ├── dialog.tsx
│   │   ├── dropdown-menu.tsx
│   │   ├── skeleton.tsx
│   │   ├── badge.tsx
│   │   ├── avatar.tsx
│   │   ├── toast.tsx
│   │   └── ...
│   │
│   ├── workflow/                     # Componentes de workflow
│   │   ├── workflow-card.tsx         # Card individual
│   │   ├── workflow-grid.tsx         # Grid de cards
│   │   ├── workflow-detail.tsx       # Pagina de detalhes
│   │   ├── workflow-nodes.tsx        # Lista de nodes
│   │   ├── workflow-integrations.tsx # Icones de integracoes
│   │   ├── workflow-difficulty.tsx   # Estrelas de dificuldade
│   │   ├── workflow-download.tsx     # Botao de download
│   │   └── workflow-related.tsx      # Workflows relacionados
│   │
│   ├── category/                     # Componentes de categoria
│   │   ├── category-card.tsx         # Card de categoria
│   │   ├── category-grid.tsx         # Grid de categorias
│   │   └── category-badge.tsx        # Badge de categoria
│   │
│   ├── search/                       # Componentes de busca
│   │   ├── search-bar.tsx            # Barra de busca
│   │   ├── search-filters.tsx        # Filtros avancados
│   │   ├── search-results.tsx        # Lista de resultados
│   │   └── search-suggestions.tsx    # Sugestoes de busca
│   │
│   ├── chat/                         # Componentes do chatbot
│   │   ├── chat-widget.tsx           # Widget flutuante
│   │   ├── chat-messages.tsx         # Lista de mensagens
│   │   ├── chat-input.tsx            # Input de mensagem
│   │   └── chat-suggestion.tsx       # Sugestao de workflow
│   │
│   ├── submit/                       # Componentes de cadastro
│   │   ├── submit-form.tsx           # Formulario completo
│   │   ├── submit-uploader.tsx       # Upload de JSON
│   │   ├── submit-preview.tsx        # Preview do workflow
│   │   └── submit-metadata.tsx       # Edicao de metadados
│   │
│   ├── curso/                        # Componentes do curso
│   │   ├── lesson-card.tsx           # Card de licao
│   │   ├── lesson-list.tsx           # Lista de licoes
│   │   └── lesson-progress.tsx       # Barra de progresso
│   │
│   ├── layout/                       # Componentes de layout
│   │   ├── header.tsx                # Cabecalho
│   │   ├── footer.tsx                # Rodape
│   │   ├── sidebar.tsx               # Menu lateral (mobile)
│   │   ├── nav-links.tsx             # Links de navegacao
│   │   └── theme-toggle.tsx          # Toggle claro/escuro
│   │
│   └── shared/                       # Componentes compartilhados
│       ├── loading-spinner.tsx       # Spinner de loading
│       ├── error-message.tsx         # Mensagem de erro
│       ├── empty-state.tsx           # Estado vazio
│       └── pagination.tsx            # Paginacao
│
├── lib/                              # Bibliotecas e utils
│   ├── supabase/
│   │   ├── client.ts                 # Cliente Supabase (browser)
│   │   ├── server.ts                 # Cliente Supabase (server)
│   │   └── admin.ts                  # Cliente admin
│   │
│   ├── openai.ts                     # Cliente OpenAI
│   ├── utils.ts                      # Funcoes utilitarias (cn, etc)
│   ├── workflow-parser.ts            # Parser de JSON n8n
│   ├── constants.ts                  # Constantes do app
│   └── validators.ts                 # Schemas Zod
│
├── hooks/                            # React Hooks customizados
│   ├── use-workflows.ts              # Buscar workflows
│   ├── use-workflow.ts               # Buscar um workflow
│   ├── use-categories.ts             # Buscar categorias
│   ├── use-search.ts                 # Busca com debounce
│   ├── use-chat.ts                   # Conversa com chatbot
│   ├── use-favorites.ts              # Favoritos do usuario
│   └── use-auth.ts                   # Estado de autenticacao
│
├── types/                            # TypeScript types
│   ├── workflow.ts                   # Tipos de workflow
│   ├── category.ts                   # Tipos de categoria
│   ├── user.ts                       # Tipos de usuario
│   ├── chat.ts                       # Tipos do chat
│   ├── api.ts                        # Tipos de resposta API
│   └── supabase.ts                   # Tipos gerados do Supabase
│
├── data/                             # Dados estaticos
│   ├── workflows/                    # JSONs de workflows
│   │   ├── ai-agents/
│   │   ├── automations/
│   │   └── integrations/
│   │
│   ├── categories.json               # Lista de categorias
│   └── integrations.json             # Lista de integracoes
│
├── public/                           # Arquivos publicos
│   ├── icons/                        # Icones de integracoes
│   │   ├── openai.svg
│   │   ├── supabase.svg
│   │   ├── google.svg
│   │   └── ...
│   │
│   ├── images/
│   │   ├── logo.svg
│   │   ├── hero.png
│   │   └── og-image.png
│   │
│   └── favicon.ico
│
├── styles/
│   └── globals.css                   # Estilos globais + Tailwind
│
├── __tests__/                        # Testes
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── e2e/
│
├── .env.local                        # Variaveis locais
├── .env.example                      # Exemplo de variaveis
├── .eslintrc.json                    # Config ESLint
├── .prettierrc                       # Config Prettier
├── tailwind.config.ts                # Config Tailwind
├── tsconfig.json                     # Config TypeScript
├── next.config.js                    # Config Next.js
├── package.json
└── README.md
```

## Convencoes de Nomenclatura

| Tipo | Convencao | Exemplo |
|------|-----------|---------|
| Pastas | kebab-case | `workflow-card/` |
| Componentes | kebab-case.tsx | `workflow-card.tsx` |
| Hooks | use-nome.ts | `use-workflows.ts` |
| Utils | nome.ts | `utils.ts` |
| Types | nome.ts | `workflow.ts` |
| Constantes | UPPER_SNAKE | `MAX_RESULTS` |

## Imports Aliases

```json
// tsconfig.json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"],
      "@/components/*": ["./components/*"],
      "@/lib/*": ["./lib/*"],
      "@/hooks/*": ["./hooks/*"],
      "@/types/*": ["./types/*"]
    }
  }
}
```

## Uso

```typescript
// Ao inves de
import { WorkflowCard } from '../../../components/workflow/workflow-card';

// Usar
import { WorkflowCard } from '@/components/workflow/workflow-card';
```
