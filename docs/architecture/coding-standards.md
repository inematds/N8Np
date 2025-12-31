# Padroes de Codigo - N8Np

## 1. Estrutura de Arquivos

### Nomenclatura

```
Componentes:    kebab-case.tsx      (workflow-card.tsx)
Paginas:        page.tsx            (Next.js App Router)
Hooks:          use-nome.ts         (use-workflows.ts)
Utils:          nome.ts             (utils.ts)
Types:          nome.ts             (workflow.ts)
API Routes:     route.ts            (Next.js convention)
```

### Organizacao de Componentes

```typescript
// 1. Imports externos
import { useState } from 'react';
import { Button } from '@/components/ui/button';

// 2. Imports internos
import { Workflow } from '@/types/workflow';
import { cn } from '@/lib/utils';

// 3. Types/Interfaces
interface WorkflowCardProps {
  workflow: Workflow;
  onDownload?: (id: string) => void;
}

// 4. Componente
export function WorkflowCard({ workflow, onDownload }: WorkflowCardProps) {
  // 4.1 Hooks
  const [isLoading, setIsLoading] = useState(false);

  // 4.2 Handlers
  const handleDownload = async () => {
    setIsLoading(true);
    await onDownload?.(workflow.id);
    setIsLoading(false);
  };

  // 4.3 Render
  return (
    <div className="rounded-lg border p-4">
      <h3>{workflow.name}</h3>
      <Button onClick={handleDownload} disabled={isLoading}>
        {isLoading ? 'Baixando...' : 'Baixar'}
      </Button>
    </div>
  );
}
```

---

## 2. TypeScript

### Tipos Obrigatorios

```typescript
// Sempre tipar props
interface Props {
  title: string;
  count?: number;  // opcional
}

// Sempre tipar retornos de funcao async
async function fetchWorkflows(): Promise<Workflow[]> {
  // ...
}

// Usar tipos do Supabase
import { Database } from '@/types/supabase';
type WorkflowRow = Database['public']['Tables']['workflows']['Row'];
```

### Evitar

```typescript
// NAO usar any
const data: any = response;  // ❌

// Usar unknown e validar
const data: unknown = response;  // ✅
if (isWorkflow(data)) {
  // ...
}
```

---

## 3. React

### Componentes Funcionais

```typescript
// Sempre usar function declaration para componentes exportados
export function WorkflowCard({ workflow }: Props) {
  return <div>...</div>;
}

// Arrow functions para componentes internos
const CardHeader = () => <header>...</header>;
```

### Hooks Customizados

```typescript
// Sempre prefixar com 'use'
export function useWorkflows(categoryId?: string) {
  const { data, isLoading } = useQuery({
    queryKey: ['workflows', categoryId],
    queryFn: () => fetchWorkflows(categoryId),
  });

  return { workflows: data ?? [], isLoading };
}
```

### Evitar

```typescript
// NAO usar useEffect para fetch
useEffect(() => {
  fetch('/api/workflows').then(...);  // ❌
}, []);

// Usar React Query
const { data } = useQuery({...});  // ✅
```

---

## 4. Tailwind CSS

### Classes Ordenadas

```tsx
// Ordem: layout > display > spacing > sizing > colors > effects
<div className="
  flex flex-col          // layout
  items-center justify-center  // alignment
  gap-4 p-6              // spacing
  w-full max-w-md        // sizing
  bg-white text-gray-900 // colors
  rounded-lg shadow-md   // effects
">
```

### Usar cn() para condicional

```typescript
import { cn } from '@/lib/utils';

<button
  className={cn(
    'px-4 py-2 rounded',
    isActive && 'bg-blue-500 text-white',
    isDisabled && 'opacity-50 cursor-not-allowed'
  )}
>
```

---

## 5. API Routes

### Estrutura Padrao

```typescript
// app/api/workflows/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';

// Schema de validacao
const querySchema = z.object({
  page: z.coerce.number().default(1),
  limit: z.coerce.number().default(20),
});

export async function GET(request: NextRequest) {
  try {
    // 1. Validar input
    const { searchParams } = new URL(request.url);
    const query = querySchema.parse(Object.fromEntries(searchParams));

    // 2. Buscar dados
    const { data, error } = await supabase
      .from('workflows')
      .select('*')
      .range((query.page - 1) * query.limit, query.page * query.limit - 1);

    if (error) throw error;

    // 3. Retornar sucesso
    return NextResponse.json({ data, pagination: {...} });

  } catch (error) {
    // 4. Tratar erros
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Parametros invalidos', details: error.errors },
        { status: 400 }
      );
    }

    return NextResponse.json(
      { error: 'Erro interno' },
      { status: 500 }
    );
  }
}
```

---

## 6. Supabase

### Queries

```typescript
// Usar select especifico, nunca *
const { data } = await supabase
  .from('workflows')
  .select('id, name, description, category:categories(name)')  // ✅
  .eq('is_published', true);

// NAO usar
.select('*')  // ❌
```

### Tratamento de Erros

```typescript
const { data, error } = await supabase.from('workflows').select();

if (error) {
  console.error('Supabase error:', error.message);
  throw new Error('Falha ao buscar workflows');
}
```

---

## 7. Commits

### Formato

```
<tipo>: <descricao curta>

[corpo opcional]

[footer opcional]
```

### Tipos

| Tipo | Uso |
|------|-----|
| feat | Nova funcionalidade |
| fix | Correcao de bug |
| docs | Documentacao |
| style | Formatacao |
| refactor | Refatoracao |
| test | Testes |
| chore | Manutencao |

### Exemplos

```
feat: adiciona filtro por categoria na busca

fix: corrige download de JSON com caracteres especiais

docs: atualiza README com instrucoes de deploy
```

---

## 8. Testes

### Estrutura

```typescript
// __tests__/components/workflow-card.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { WorkflowCard } from '@/components/workflow/workflow-card';

describe('WorkflowCard', () => {
  const mockWorkflow = {
    id: '1',
    name: 'Test Workflow',
    description: 'Test description',
  };

  it('renders workflow name', () => {
    render(<WorkflowCard workflow={mockWorkflow} />);
    expect(screen.getByText('Test Workflow')).toBeInTheDocument();
  });

  it('calls onDownload when button clicked', () => {
    const onDownload = jest.fn();
    render(<WorkflowCard workflow={mockWorkflow} onDownload={onDownload} />);

    fireEvent.click(screen.getByRole('button', { name: /baixar/i }));

    expect(onDownload).toHaveBeenCalledWith('1');
  });
});
```

---

## 9. Acessibilidade

### Obrigatorio

```tsx
// Sempre usar alt em imagens
<Image src={icon} alt="Icone do OpenAI" />

// Sempre usar labels em inputs
<label htmlFor="search">Buscar</label>
<input id="search" type="text" />

// Sempre usar role quando necessario
<div role="list">
  <div role="listitem">Item 1</div>
</div>

// Sempre usar aria-label em botoes de icone
<button aria-label="Fechar modal">
  <X className="h-4 w-4" />
</button>
```

---

## 10. Performance

### Imports Dinamicos

```typescript
// Componentes pesados
const ChatWidget = dynamic(() => import('@/components/chat/chat-widget'), {
  loading: () => <Skeleton className="h-12 w-12 rounded-full" />,
  ssr: false,
});
```

### Memoizacao

```typescript
// Componentes que recebem muitas props
const WorkflowCard = memo(function WorkflowCard({ workflow }: Props) {
  return <div>...</div>;
});

// Callbacks em loops
const handleDownload = useCallback((id: string) => {
  // ...
}, []);
```
