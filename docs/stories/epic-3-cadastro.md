# Epic 3: Cadastro de Workflows

## Descricao

Permitir que usuarios cadastrem novos workflows na plataforma, fazendo upload do JSON e adicionando metadados.

## Objetivo

Expandir a biblioteca com contribuicoes da comunidade de forma organizada.

## Criterios de Aceite do Epic

- [ ] Usuario pode fazer upload de arquivo JSON
- [ ] Sistema extrai metadados automaticamente
- [ ] Usuario pode editar descricao e categoria
- [ ] Usuario pode adicionar tags
- [ ] Workflow e publicado no catalogo

---

## Stories

### Story 3.1: Pagina de Cadastro

**Como** usuario
**Quero** acessar formulario de cadastro
**Para** enviar meu workflow

**Tarefas:**
- [ ] Criar pagina /submit
- [ ] Criar layout do formulario
- [ ] Adicionar navegacao no header
- [ ] Verificar se usuario esta logado

**Layout:**
```
[Header]

═══════════════════════════════════════
  Adicionar Novo Workflow
═══════════════════════════════════════

Compartilhe seu workflow com a comunidade!

[Passo 1: Upload] → [Passo 2: Detalhes] → [Passo 3: Revisar]

┌─────────────────────────────────────┐
│                                     │
│    📁 Arraste o arquivo JSON aqui   │
│                                     │
│         ou clique para buscar       │
│                                     │
└─────────────────────────────────────┘

[Footer]
```

**Criterios de Aceite:**
- [ ] Pagina acessivel via menu
- [ ] Layout responsivo
- [ ] Usuario nao logado ve mensagem para logar

---

### Story 3.2: Upload e Parsing de JSON

**Como** usuario
**Quero** fazer upload do arquivo JSON
**Para** que o sistema extraia informacoes

**Tarefas:**
- [ ] Criar componente FileUploader
- [ ] Validar se arquivo e JSON valido
- [ ] Validar se e workflow n8n valido
- [ ] Parsear e extrair metadados
- [ ] Mostrar preview das informacoes

**Parser de Workflow:**
```typescript
// lib/workflow-parser.ts
interface ParsedWorkflow {
  name: string;
  nodes: Array<{
    type: string;
    name: string;
  }>;
  nodesCount: number;
  integrations: string[];
  isValid: boolean;
  errors?: string[];
}

function parseN8nWorkflow(json: unknown): ParsedWorkflow {
  // 1. Validar estrutura basica
  // 2. Extrair nome
  // 3. Extrair nodes
  // 4. Identificar integracoes pelos node types
  // 5. Retornar objeto parseado
}
```

**Integracoes Auto-Detectadas:**
```typescript
const INTEGRATION_MAP: Record<string, string> = {
  'n8n-nodes-base.googleDrive': 'google',
  'n8n-nodes-base.gmail': 'google',
  '@n8n/n8n-nodes-langchain.lmChatOpenAi': 'openai',
  'n8n-nodes-base.supabase': 'supabase',
  // ...
};
```

**Criterios de Aceite:**
- [ ] Aceita apenas arquivos .json
- [ ] Valida estrutura de workflow n8n
- [ ] Extrai nome corretamente
- [ ] Conta nodes corretamente
- [ ] Identifica integracoes automaticamente
- [ ] Mostra erros claros se invalido

---

### Story 3.3: Formulario de Metadados

**Como** usuario
**Quero** adicionar descricao e categoria
**Para** que outros entendam meu workflow

**Tarefas:**
- [ ] Criar formulario de metadados
- [ ] Campo de descricao (textarea)
- [ ] Selecao de categoria (dropdown)
- [ ] Selecao de dificuldade (1-5)
- [ ] Adicao de tags (input com chips)
- [ ] Validacao de campos obrigatorios

**Layout:**
```
Passo 2: Detalhes

Nome do Workflow: [RAG Pipeline & Chatbot    ]
(extraido do JSON, editavel)

Descricao: *
┌─────────────────────────────────────────────┐
│ Descreva o que seu workflow faz, para que   │
│ serve e o que o usuario precisa configurar. │
│                                             │
│ Minimo 50 caracteres.                       │
└─────────────────────────────────────────────┘

Categoria: * [AI Agents ▼]

Dificuldade: ★★★☆☆

Tags: [rag] [chatbot] [ia] [+ adicionar]

[← Voltar]                           [Proximo →]
```

**Validacoes:**
```typescript
const submitSchema = z.object({
  name: z.string().min(3).max(100),
  description: z.string().min(50).max(2000),
  categoryId: z.string().uuid(),
  difficulty: z.number().min(1).max(5),
  tags: z.array(z.string()).max(10),
});
```

**Criterios de Aceite:**
- [ ] Todos campos funcionam
- [ ] Validacao em tempo real
- [ ] Mensagens de erro claras
- [ ] Pode voltar sem perder dados

---

### Story 3.4: Preview e Confirmacao

**Como** usuario
**Quero** revisar antes de publicar
**Para** garantir que esta correto

**Tarefas:**
- [ ] Criar componente WorkflowPreview
- [ ] Mostrar card como aparecera
- [ ] Mostrar detalhes completos
- [ ] Botao de confirmar/editar

**Layout:**
```
Passo 3: Revisar

Seu workflow aparecera assim:

┌─────────────────────────────────────────────┐
│ [Preview do WorkflowCard]                   │
│                                             │
│ RAG Pipeline & Chatbot                      │
│ Cria um chatbot inteligente com RAG...      │
│ AI Agents | 15 nodes | ★★★☆☆               │
│ [OpenAI] [Supabase] [Google]                │
└─────────────────────────────────────────────┘

Nodes detectados:
• Google Drive Trigger
• Document Loader
• AI Agent
• ...

Integracoes: OpenAI, Supabase, Google
Tags: #rag #chatbot #ia

[ ] Confirmo que este workflow e meu ou tenho permissao
[ ] Confirmo que nao contem credenciais ou dados sensiveis

[← Editar]                           [Publicar ✓]
```

**Criterios de Aceite:**
- [ ] Preview identico ao card final
- [ ] Mostra todos dados inseridos
- [ ] Checkboxes de confirmacao obrigatorios
- [ ] Pode voltar para editar

---

### Story 3.5: Publicacao do Workflow

**Como** sistema
**Quero** salvar o workflow no banco
**Para** que apareca no catalogo

**Tarefas:**
- [ ] Criar API route POST /api/workflows
- [ ] Validar dados no servidor
- [ ] Salvar workflow no Supabase
- [ ] Salvar nodes relacionados
- [ ] Atualizar contador da categoria
- [ ] Redirecionar para pagina do workflow

**API:**
```typescript
// POST /api/workflows
{
  name: string;
  description: string;
  jsonContent: object;
  categoryId: string;
  difficulty: number;
  tags: string[];
}

// Response
{
  id: string;
  slug: string;
  message: "Workflow publicado com sucesso"
}
```

**Criterios de Aceite:**
- [ ] Workflow salvo corretamente
- [ ] Nodes salvos na tabela auxiliar
- [ ] Slug gerado automaticamente
- [ ] Redireciona para /workflows/[slug]
- [ ] Aparece imediatamente no catalogo

---

### Story 3.6: Edicao de Workflow Proprio

**Como** usuario logado
**Quero** editar meu workflow publicado
**Para** corrigir informacoes

**Tarefas:**
- [ ] Adicionar botao "Editar" se for o autor
- [ ] Criar pagina /workflows/[slug]/edit
- [ ] Reutilizar formulario de metadados
- [ ] Criar API route PUT /api/workflows/[id]

**Criterios de Aceite:**
- [ ] Apenas autor pode editar
- [ ] Formulario pre-preenchido
- [ ] Alteracoes salvas corretamente

---

### Story 3.7: Delecao de Workflow Proprio

**Como** usuario logado
**Quero** deletar meu workflow
**Para** remover do catalogo

**Tarefas:**
- [ ] Adicionar botao "Excluir" se for o autor
- [ ] Criar modal de confirmacao
- [ ] Criar API route DELETE /api/workflows/[id]
- [ ] Atualizar contador da categoria

**Criterios de Aceite:**
- [ ] Apenas autor pode deletar
- [ ] Confirmacao obrigatoria
- [ ] Workflow removido do catalogo
- [ ] Redireciona para home

---

## Definicao de Pronto (DoD)

- [ ] Validacoes funcionando
- [ ] Erros tratados graciosamente
- [ ] Testes de upload com varios JSONs
- [ ] Sem vulnerabilidades de upload

---

## Estimativa

| Story | Complexidade | Pontos |
|-------|--------------|--------|
| 3.1 Pagina Cadastro | Baixa | 2 |
| 3.2 Upload JSON | Alta | 8 |
| 3.3 Formulario | Media | 5 |
| 3.4 Preview | Media | 3 |
| 3.5 Publicacao | Media | 5 |
| 3.6 Edicao | Media | 3 |
| 3.7 Delecao | Baixa | 2 |
| **Total** | | **28** |

---

## Dependencias

- Requer Epic 1 (Catalogo) completo
- Requer Epic 4 (Usuarios) para autenticacao
