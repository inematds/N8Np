# Guia de Inicio Rapido - N8Np

## Para Comecar a Desenvolver

### 1. Pre-requisitos

```bash
# Node.js 18+
node --version  # v18.x ou superior

# npm ou yarn
npm --version   # 9.x ou superior

# Git
git --version
```

### 2. Criar Projeto

```bash
# Criar Next.js com TypeScript
npx create-next-app@latest n8np-app --typescript --tailwind --eslint --app --src-dir=false --import-alias="@/*"

cd n8np-app

# Instalar dependencias
npm install @supabase/supabase-js @supabase/auth-helpers-nextjs
npm install @tanstack/react-query zustand zod lucide-react
npm install class-variance-authority clsx tailwind-merge

# Instalar shadcn/ui
npx shadcn@latest init
npx shadcn@latest add button card input select dialog dropdown-menu skeleton badge avatar
```

### 3. Configurar Variaveis de Ambiente

```bash
# Criar arquivo .env.local
cp .env.example .env.local
```

```env
# .env.local
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx
SUPABASE_SERVICE_ROLE_KEY=xxx
OPENAI_API_KEY=sk-xxx  # Para o chatbot (Fase 5)
```

### 4. Configurar Supabase

1. Criar projeto em https://supabase.com
2. Ir em SQL Editor
3. Executar schema do arquivo `docs/architecture.md` secao 3.2
4. Copiar URL e chaves para .env.local

### 5. Criar Estrutura Basica

```bash
# Criar pastas
mkdir -p components/{ui,workflow,category,search,chat,layout,shared}
mkdir -p lib/supabase hooks types data/workflows
```

### 6. Rodar Projeto

```bash
npm run dev
```

Acesse http://localhost:3000

---

## Ordem de Implementacao Recomendada

### Semana 1: Setup + Catalogo

```
Dia 1-2: Setup
├── Projeto Next.js ✓
├── Supabase configurado
├── Estrutura de pastas
└── Variaveis de ambiente

Dia 3-4: Database
├── Tabelas criadas
├── Seed de categorias
├── Seed de workflows (pode ser parcial)
└── Cliente Supabase funcionando

Dia 5: Home Page
├── Layout basico
├── Header + Footer
├── Grid de categorias
└── Cards funcionais
```

### Semana 2: Catalogo + Busca Basica

```
Dia 1-2: Lista de Workflows
├── Pagina /categories/[slug]
├── WorkflowCard component
├── WorkflowGrid component
└── Paginacao

Dia 3-4: Detalhes
├── Pagina /workflows/[slug]
├── WorkflowDetail component
├── Lista de nodes
├── Download JSON

Dia 5: Busca Basica
├── SearchBar component
├── API /api/search
├── Full-text search funcionando
└── Resultados basicos
```

### Semana 3: Refinamento + Deploy

```
Dia 1-2: Filtros
├── Filtro por categoria
├── Filtro por integracao
├── Combinar filtros

Dia 3: Responsivo
├── Mobile menu
├── Cards responsivos
├── Testes em dispositivos

Dia 4-5: Deploy
├── Vercel setup
├── Variaveis de producao
├── Testes finais
├── Deploy MVP!
```

---

## Comandos Uteis

```bash
# Desenvolvimento
npm run dev           # Inicia servidor local

# Build
npm run build         # Build de producao
npm run start         # Inicia build local

# Qualidade
npm run lint          # Verifica erros
npm run lint:fix      # Corrige erros automaticamente

# Supabase
npx supabase gen types typescript --project-id <id> > types/supabase.ts

# Deploy
vercel                # Deploy preview
vercel --prod         # Deploy producao
```

---

## Arquivos Iniciais

### lib/supabase/client.ts

```typescript
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';
import { Database } from '@/types/supabase';

export const supabase = createClientComponentClient<Database>();
```

### lib/utils.ts

```typescript
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

### types/workflow.ts

```typescript
export interface Workflow {
  id: string;
  name: string;
  slug: string;
  description: string;
  category_id: string;
  nodes_count: number;
  integrations: string[];
  difficulty: number;
  tags: string[];
  downloads: number;
  created_at: string;
}

export interface Category {
  id: string;
  name: string;
  slug: string;
  icon: string;
  workflow_count: number;
}
```

---

## Proximos Passos

1. **Agora:** Criar projeto Next.js
2. **Depois:** Configurar Supabase
3. **Entao:** Implementar Epic 1, Story 1.1

Consulte os documentos em `docs/stories/` para detalhes de cada story.

---

## Ajuda

- **Documentacao:** Pasta `docs/`
- **PRD:** `docs/prd.md`
- **Arquitetura:** `docs/architecture.md`
- **Stories:** `docs/stories/`

Duvidas? Abra uma issue no repositorio!
