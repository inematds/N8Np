# Tech Stack - N8Np

## Tecnologias Escolhidas

### Frontend

| Tecnologia | Versao | Uso |
|------------|--------|-----|
| **Next.js** | 14.x | Framework React com App Router |
| **React** | 18.x | Biblioteca UI |
| **TypeScript** | 5.x | Tipagem estatica |
| **Tailwind CSS** | 3.x | Estilizacao |
| **shadcn/ui** | latest | Componentes UI |
| **Lucide React** | latest | Icones |
| **React Query** | 5.x | Gerenciamento de estado servidor |
| **Zustand** | 4.x | Estado global cliente |

### Backend

| Tecnologia | Versao | Uso |
|------------|--------|-----|
| **Next.js API Routes** | 14.x | Endpoints REST |
| **Supabase** | latest | Database + Auth + Storage |
| **OpenAI SDK** | 4.x | Integracao com GPT-4 |
| **Zod** | 3.x | Validacao de schemas |

### Infraestrutura

| Tecnologia | Uso |
|------------|-----|
| **Vercel** | Hosting e Deploy |
| **Supabase Cloud** | Database PostgreSQL |
| **GitHub** | Repositorio e CI/CD |

### Desenvolvimento

| Ferramenta | Uso |
|------------|-----|
| **ESLint** | Linting |
| **Prettier** | Formatacao |
| **Husky** | Git hooks |
| **Jest** | Testes unitarios |
| **Playwright** | Testes E2E |

---

## Dependencias do package.json

```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@supabase/supabase-js": "^2.39.0",
    "@supabase/auth-helpers-nextjs": "^0.8.0",
    "openai": "^4.20.0",
    "@tanstack/react-query": "^5.0.0",
    "zustand": "^4.4.0",
    "zod": "^3.22.0",
    "lucide-react": "^0.294.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0",
    "eslint": "^8.55.0",
    "eslint-config-next": "^14.0.0",
    "prettier": "^3.1.0",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.1.0"
  }
}
```

---

## Variaveis de Ambiente

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx
SUPABASE_SERVICE_ROLE_KEY=xxx

# OpenAI
OPENAI_API_KEY=sk-xxx

# Auth
NEXTAUTH_SECRET=xxx
NEXTAUTH_URL=http://localhost:3000

# Google OAuth (opcional)
GOOGLE_CLIENT_ID=xxx
GOOGLE_CLIENT_SECRET=xxx
```

---

## Comandos

```bash
# Desenvolvimento
npm run dev          # Inicia servidor dev
npm run build        # Build de producao
npm run start        # Inicia servidor producao
npm run lint         # Executa linter
npm run test         # Executa testes
npm run db:migrate   # Migracoes Supabase
npm run db:seed      # Popula banco com dados iniciais
```
