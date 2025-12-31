# Epic 5: Chatbot Assistente

## Descricao

Criar um chatbot inteligente que ajuda usuarios a encontrar workflows, responder duvidas e explicar como usar a plataforma.

## Objetivo

Ajudar usuarios que nao sabem o que procurar a encontrar o workflow ideal.

## Criterios de Aceite do Epic

- [ ] Usuario pode conversar em linguagem natural
- [ ] Bot sugere workflows baseado na conversa
- [ ] Bot explica o que cada workflow faz
- [ ] Bot responde duvidas sobre n8n
- [ ] Conversa persiste durante a sessao

---

## Stories

### Story 5.1: Widget de Chat Flutuante

**Como** usuario
**Quero** ter acesso rapido ao chat
**Para** pedir ajuda a qualquer momento

**Tarefas:**
- [ ] Criar componente ChatWidget
- [ ] Botao flutuante no canto inferior direito
- [ ] Animacao de abrir/fechar
- [ ] Badge de notificacao

**Componente:**
```tsx
// components/chat/chat-widget.tsx

// Fechado:
// ┌─────┐
// │ 💬  │  ← Botao flutuante
// └─────┘

// Aberto:
// ┌─────────────────────────────────┐
// │ 🤖 Assistente N8Np          [X] │
// ├─────────────────────────────────┤
// │                                 │
// │ [Mensagens do chat]             │
// │                                 │
// │                                 │
// ├─────────────────────────────────┤
// │ Digite sua mensagem...    [→]   │
// └─────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Widget aparece em todas as paginas
- [ ] Abre/fecha com animacao
- [ ] Responsivo em mobile
- [ ] Nao bloqueia conteudo

---

### Story 5.2: Interface de Mensagens

**Como** usuario
**Quero** ver historico de mensagens
**Para** acompanhar a conversa

**Tarefas:**
- [ ] Criar componente ChatMessages
- [ ] Diferenciar mensagens usuario/bot
- [ ] Auto-scroll para nova mensagem
- [ ] Loading indicator enquanto bot pensa

**Componente:**
```tsx
// components/chat/chat-messages.tsx

// ┌─────────────────────────────────┐
// │ 🤖 Ola! Como posso ajudar?      │
// │                                 │
// │          Quero automatizar ◀   │
// │          WhatsApp              │
// │                                 │
// │ 🤖 Encontrei 3 workflows para   │
// │    voce:                        │
// │    1. WhatsApp Agent            │
// │    2. WhatsApp + GPT            │
// │    3. Evolution API             │
// │                                 │
// │    ● ● ●  ← Loading             │
// └─────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Mensagens diferenciadas visualmente
- [ ] Auto-scroll funciona
- [ ] Loading enquanto processa
- [ ] Historico mantido na sessao

---

### Story 5.3: Input de Mensagem

**Como** usuario
**Quero** digitar mensagens
**Para** conversar com o bot

**Tarefas:**
- [ ] Criar componente ChatInput
- [ ] Enviar com Enter ou botao
- [ ] Limpar campo apos envio
- [ ] Desabilitar enquanto processa

**Componente:**
```tsx
// components/chat/chat-input.tsx
interface ChatInputProps {
  onSend: (message: string) => void;
  isLoading: boolean;
}

// ┌─────────────────────────────────┐
// │ Digite sua mensagem...    [→]   │
// └─────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Enter envia mensagem
- [ ] Botao envia mensagem
- [ ] Campo limpa apos envio
- [ ] Desabilita durante loading

---

### Story 5.4: API do Chatbot com OpenAI

**Como** desenvolvedor
**Quero** integrar com OpenAI
**Para** gerar respostas inteligentes

**Tarefas:**
- [ ] Criar API route POST /api/chat
- [ ] Configurar cliente OpenAI
- [ ] Criar system prompt
- [ ] Buscar workflows relevantes
- [ ] Retornar resposta + sugestoes

**System Prompt:**
```typescript
const SYSTEM_PROMPT = `Voce e o assistente da plataforma N8Np, uma biblioteca de workflows n8n.

Seu objetivo e ajudar usuarios a:
1. Encontrar workflows adequados para suas necessidades
2. Explicar o que cada workflow faz
3. Responder duvidas sobre n8n e automacao

Regras:
- Seja amigavel e prestativo
- Faca perguntas para entender a necessidade
- Sugira workflows especificos da biblioteca
- Explique em linguagem simples
- Se nao souber, diga que nao sabe

Workflows disponiveis (resumo):
- AI Agents: 198 workflows de agentes com IA
- Automacoes: 66 workflows de automacao
- Integracoes: 36 workflows de integracao
- E mais...

Quando sugerir workflows, retorne no formato:
WORKFLOWS: [slug1, slug2, slug3]
`;
```

**API Route:**
```typescript
// app/api/chat/route.ts
export async function POST(request: Request) {
  const { message, history } = await request.json();

  // 1. Buscar workflows relacionados (semantic search)
  const relevantWorkflows = await searchWorkflows(message);

  // 2. Montar contexto
  const context = `
    Workflows relacionados a "${message}":
    ${relevantWorkflows.map(w => `- ${w.name}: ${w.description}`).join('\n')}
  `;

  // 3. Chamar OpenAI
  const completion = await openai.chat.completions.create({
    model: 'gpt-4-turbo-preview',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT + '\n\n' + context },
      ...history,
      { role: 'user', content: message },
    ],
  });

  // 4. Extrair workflows sugeridos
  const response = completion.choices[0].message.content;
  const suggestedSlugs = extractWorkflowSlugs(response);

  return NextResponse.json({
    response,
    suggestions: suggestedSlugs,
  });
}
```

**Criterios de Aceite:**
- [ ] Responde em < 5 segundos
- [ ] Respostas relevantes
- [ ] Sugere workflows reais
- [ ] Mantem contexto da conversa

---

### Story 5.5: Sugestoes de Workflows no Chat

**Como** usuario
**Quero** ver cards de workflows sugeridos
**Para** clicar e ver detalhes

**Tarefas:**
- [ ] Criar componente ChatSuggestion
- [ ] Renderizar mini-cards no chat
- [ ] Clicar abre pagina do workflow
- [ ] Mostrar ate 3 sugestoes

**Componente:**
```tsx
// components/chat/chat-suggestion.tsx

// ┌─────────────────────────────────┐
// │ 🤖 Encontrei esses workflows:   │
// │                                 │
// │ ┌─────────────────────────────┐ │
// │ │ WhatsApp Agent              │ │
// │ │ Atendimento automatico...   │ │
// │ │ [Ver detalhes]              │ │
// │ └─────────────────────────────┘ │
// │                                 │
// │ ┌─────────────────────────────┐ │
// │ │ WhatsApp + GPT              │ │
// │ │ Respostas com IA...         │ │
// │ │ [Ver detalhes]              │ │
// │ └─────────────────────────────┘ │
// └─────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Mostra mini-cards clicaveis
- [ ] Maximo 3 sugestoes por mensagem
- [ ] Clicar abre workflow
- [ ] Layout responsivo no chat

---

### Story 5.6: Mensagem de Boas-Vindas

**Como** usuario
**Quero** ver mensagem inicial
**Para** entender como usar o chat

**Tarefas:**
- [ ] Criar mensagem de boas-vindas
- [ ] Sugerir perguntas iniciais
- [ ] Mostrar ao abrir chat vazio

**Mensagem:**
```
🤖 Ola! Sou o assistente do N8Np.

Posso ajudar voce a:
• Encontrar o workflow ideal
• Explicar como usar um workflow
• Tirar duvidas sobre n8n

Experimente perguntar:
┌────────────────────────────────┐
│ "Quero automatizar WhatsApp"   │
└────────────────────────────────┘
┌────────────────────────────────┐
│ "O que e RAG?"                 │
└────────────────────────────────┘
┌────────────────────────────────┐
│ "Workflows para iniciantes"    │
└────────────────────────────────┘
```

**Criterios de Aceite:**
- [ ] Mensagem aparece ao abrir
- [ ] Sugestoes sao clicaveis
- [ ] Clicar envia pergunta
- [ ] Desaparece apos primeira mensagem

---

### Story 5.7: Busca Semantica para Contexto

**Como** sistema
**Quero** buscar workflows semanticamente
**Para** dar contexto ao chatbot

**Tarefas:**
- [ ] Configurar embeddings no Supabase
- [ ] Gerar embeddings para workflows
- [ ] Criar funcao de busca semantica
- [ ] Integrar com API do chat

**Embeddings:**
```typescript
// lib/embeddings.ts
import { OpenAI } from 'openai';

export async function generateEmbedding(text: string) {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: text,
  });
  return response.data[0].embedding;
}

export async function semanticSearch(query: string, limit = 5) {
  const queryEmbedding = await generateEmbedding(query);

  const { data } = await supabase.rpc('match_workflows', {
    query_embedding: queryEmbedding,
    match_threshold: 0.7,
    match_count: limit,
  });

  return data;
}
```

**Funcao SQL:**
```sql
CREATE OR REPLACE FUNCTION match_workflows(
  query_embedding vector(1536),
  match_threshold float,
  match_count int
)
RETURNS TABLE (
  id uuid,
  name text,
  description text,
  slug text,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    w.id,
    w.name,
    w.description,
    w.slug,
    1 - (w.embedding <=> query_embedding) AS similarity
  FROM workflows w
  WHERE 1 - (w.embedding <=> query_embedding) > match_threshold
  ORDER BY similarity DESC
  LIMIT match_count;
END;
$$;
```

**Criterios de Aceite:**
- [ ] Embeddings gerados para todos workflows
- [ ] Busca retorna resultados relevantes
- [ ] Performance < 500ms
- [ ] Threshold ajustavel

---

### Story 5.8: Respostas sobre n8n

**Como** usuario
**Quero** perguntar sobre n8n em geral
**Para** aprender mais sobre a ferramenta

**Tarefas:**
- [ ] Expandir system prompt com conhecimento n8n
- [ ] Adicionar exemplos de perguntas
- [ ] Testar respostas de qualidade

**Conhecimento adicional:**
```
- O que e n8n: Ferramenta open-source de automacao
- Como instalar: Docker, npm, cloud
- Conceitos: workflows, nodes, triggers, credentials
- Integracoes principais: 400+ nodes
- Comunidade: forum, discord, github
```

**Criterios de Aceite:**
- [ ] Responde "O que e n8n?"
- [ ] Responde "Como instalar?"
- [ ] Responde sobre nodes especificos
- [ ] Admite quando nao sabe

---

## Definicao de Pronto (DoD)

- [ ] Respostas relevantes em 90% dos casos
- [ ] Latencia < 5 segundos
- [ ] Funciona em mobile
- [ ] Nao expoe API keys

---

## Estimativa

| Story | Complexidade | Pontos |
|-------|--------------|--------|
| 5.1 Widget | Media | 3 |
| 5.2 Mensagens | Media | 3 |
| 5.3 Input | Baixa | 2 |
| 5.4 API OpenAI | Alta | 8 |
| 5.5 Sugestoes | Media | 3 |
| 5.6 Boas-vindas | Baixa | 1 |
| 5.7 Busca Semantica | Alta | 8 |
| 5.8 Respostas n8n | Media | 3 |
| **Total** | | **31** |

---

## Dependencias

- Requer Epic 1 (Catalogo) completo
- Requer Epic 2 (Busca) para busca semantica
- Requer chave de API OpenAI
- Requer pgvector no Supabase
