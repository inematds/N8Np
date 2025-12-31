# Epic 4: Sistema de Usuarios

## Descricao

Implementar autenticacao e sistema de usuarios para permitir cadastro de workflows, favoritos e personalizacao.

## Objetivo

Permitir que usuarios tenham conta para interagir com a plataforma.

## Criterios de Aceite do Epic

- [ ] Usuario pode criar conta com email
- [ ] Usuario pode logar com Google
- [ ] Usuario pode favoritar workflows
- [ ] Usuario pode ver seus favoritos
- [ ] Usuario pode ver seus workflows enviados

---

## Stories

### Story 4.1: Setup de Autenticacao

**Como** desenvolvedor
**Quero** configurar sistema de autenticacao
**Para** usuarios poderem criar conta

**Tarefas:**
- [ ] Configurar Supabase Auth
- [ ] Criar cliente de autenticacao
- [ ] Criar hook useAuth
- [ ] Criar contexto de autenticacao
- [ ] Configurar middleware de rotas protegidas

**Arquivos:**
```
lib/supabase/auth.ts
hooks/use-auth.ts
app/auth/callback/route.ts
middleware.ts
```

**Configuracao Supabase:**
```typescript
// lib/supabase/auth.ts
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs';

export const supabase = createClientComponentClient();

export async function signInWithGoogle() {
  return supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: `${window.location.origin}/auth/callback`,
    },
  });
}

export async function signInWithEmail(email: string, password: string) {
  return supabase.auth.signInWithPassword({ email, password });
}

export async function signUp(email: string, password: string) {
  return supabase.auth.signUp({ email, password });
}

export async function signOut() {
  return supabase.auth.signOut();
}
```

**Criterios de Aceite:**
- [ ] Supabase Auth configurado
- [ ] Google OAuth funcionando
- [ ] Email/senha funcionando
- [ ] Callback de autenticacao funciona

---

### Story 4.2: Pagina de Login

**Como** usuario
**Quero** fazer login na plataforma
**Para** acessar recursos exclusivos

**Tarefas:**
- [ ] Criar pagina /auth/login
- [ ] Criar formulario de login
- [ ] Adicionar botao Google
- [ ] Adicionar link para cadastro
- [ ] Mostrar erros de autenticacao

**Layout:**
```
┌─────────────────────────────────────────────┐
│                                             │
│              N8Np                           │
│                                             │
│         Entrar na sua conta                 │
│                                             │
│  [  🔵  Continuar com Google  ]             │
│                                             │
│  ────────── ou ──────────                   │
│                                             │
│  Email                                      │
│  ┌───────────────────────────────────┐      │
│  │ seu@email.com                     │      │
│  └───────────────────────────────────┘      │
│                                             │
│  Senha                                      │
│  ┌───────────────────────────────────┐      │
│  │ ••••••••                          │      │
│  └───────────────────────────────────┘      │
│                                             │
│  [        Entrar        ]                   │
│                                             │
│  Nao tem conta? Criar conta                 │
│                                             │
└─────────────────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Login com Google funciona
- [ ] Login com email funciona
- [ ] Erros mostrados claramente
- [ ] Redireciona apos login

---

### Story 4.3: Pagina de Cadastro

**Como** visitante
**Quero** criar uma conta
**Para** usar recursos da plataforma

**Tarefas:**
- [ ] Criar pagina /auth/signup
- [ ] Criar formulario de cadastro
- [ ] Validar email e senha
- [ ] Enviar email de confirmacao
- [ ] Mostrar mensagem de sucesso

**Validacoes:**
```typescript
const signupSchema = z.object({
  email: z.string().email('Email invalido'),
  password: z.string()
    .min(8, 'Minimo 8 caracteres')
    .regex(/[A-Z]/, 'Precisa ter maiuscula')
    .regex(/[0-9]/, 'Precisa ter numero'),
  confirmPassword: z.string(),
}).refine(data => data.password === data.confirmPassword, {
  message: 'Senhas nao conferem',
  path: ['confirmPassword'],
});
```

**Criterios de Aceite:**
- [ ] Validacao de email
- [ ] Validacao de senha forte
- [ ] Email de confirmacao enviado
- [ ] Mensagem clara de proximo passo

---

### Story 4.4: Header com Estado de Login

**Como** usuario logado
**Quero** ver meu status no header
**Para** saber que estou logado

**Tarefas:**
- [ ] Criar componente UserMenu
- [ ] Mostrar avatar/nome quando logado
- [ ] Dropdown com opcoes
- [ ] Botao de login quando deslogado

**Componente:**
```tsx
// components/layout/user-menu.tsx
// Quando logado:
// ┌────────────────────────┐
// │  [Avatar] Joao ▼       │
// │  ┌──────────────────┐  │
// │  │ Meu Perfil       │  │
// │  │ Meus Workflows   │  │
// │  │ Favoritos        │  │
// │  │ ────────────     │  │
// │  │ Sair             │  │
// │  └──────────────────┘  │
// └────────────────────────┘

// Quando deslogado:
// [ Entrar ]
```

**Criterios de Aceite:**
- [ ] Mostra avatar quando logado
- [ ] Dropdown com opcoes
- [ ] Botao "Entrar" quando deslogado
- [ ] Logout funciona

---

### Story 4.5: Sistema de Favoritos

**Como** usuario logado
**Quero** favoritar workflows
**Para** acessar rapidamente depois

**Tarefas:**
- [ ] Criar tabela favorites no Supabase
- [ ] Criar API POST/DELETE /api/favorites
- [ ] Adicionar botao de favorito nos cards
- [ ] Criar hook useFavorites
- [ ] Mostrar estado de favoritado

**Componente:**
```tsx
// components/workflow/favorite-button.tsx
interface FavoriteButtonProps {
  workflowId: string;
  isFavorited: boolean;
  onToggle: () => void;
}

// ♡ quando nao favoritado
// ♥ quando favoritado
// Animacao ao clicar
```

**Criterios de Aceite:**
- [ ] Botao aparece em todos os cards
- [ ] So funciona quando logado
- [ ] Estado persiste no banco
- [ ] Animacao de feedback

---

### Story 4.6: Pagina de Favoritos

**Como** usuario logado
**Quero** ver meus workflows favoritos
**Para** acessar rapidamente

**Tarefas:**
- [ ] Criar pagina /favoritos
- [ ] Buscar favoritos do usuario
- [ ] Mostrar grid de cards
- [ ] Permitir remover favorito

**Layout:**
```
[Header]

Meus Favoritos (12 workflows)

[Card ♥] [Card ♥] [Card ♥]
[Card ♥] [Card ♥] [Card ♥]

[Footer]
```

**Criterios de Aceite:**
- [ ] Lista todos favoritos
- [ ] Pode remover da lista
- [ ] Estado vazio quando sem favoritos
- [ ] Requer login para acessar

---

### Story 4.7: Pagina de Perfil

**Como** usuario logado
**Quero** ver meu perfil
**Para** gerenciar minha conta

**Tarefas:**
- [ ] Criar pagina /perfil
- [ ] Mostrar informacoes da conta
- [ ] Listar workflows enviados
- [ ] Estatisticas (downloads totais)

**Layout:**
```
[Header]

┌─────────────────────────────────────────────┐
│  [Avatar Grande]                            │
│  Joao Silva                                 │
│  joao@email.com                             │
│  Membro desde: Jan 2025                     │
│                                             │
│  📊 Estatisticas                            │
│  • 5 workflows enviados                     │
│  • 150 downloads totais                     │
│  • 12 favoritos                             │
└─────────────────────────────────────────────┘

Meus Workflows
[Card] [Card] [Card]

[Footer]
```

**Criterios de Aceite:**
- [ ] Mostra dados do usuario
- [ ] Lista workflows enviados
- [ ] Mostra estatisticas
- [ ] Pode editar informacoes basicas

---

## Definicao de Pronto (DoD)

- [ ] Autenticacao segura
- [ ] Sessoes funcionando
- [ ] Rotas protegidas
- [ ] Testes de fluxo completo

---

## Estimativa

| Story | Complexidade | Pontos |
|-------|--------------|--------|
| 4.1 Setup Auth | Alta | 5 |
| 4.2 Login | Media | 3 |
| 4.3 Cadastro | Media | 3 |
| 4.4 Header | Media | 3 |
| 4.5 Favoritos | Media | 5 |
| 4.6 Pagina Favoritos | Baixa | 2 |
| 4.7 Perfil | Media | 3 |
| **Total** | | **24** |

---

## Dependencias

- Requer Epic 1 (Catalogo) completo
- Configuracao do Google OAuth no console
