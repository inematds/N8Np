# Documentação - Fluxo ONG Castração Central (n8n v1.104.2)

## Visão Geral

Este fluxo n8n implementa um sistema de atendimento automatizado para uma ONG de castração de animais, utilizando inteligência artificial para classificar intenções e direcionar usuários para agentes especializados.

## Arquitetura do Sistema

### 🎯 Agente Orquestrador Principal
- **OrquestradorONG**: Recebe mensagens, identifica intenções e roteia para agentes especializados
- **Canais de entrada**: WhatsApp (EvolutionAPI) e E-mail (IMAP)
- **Classificação inteligente**: Usa OpenAI para identificar a intenção do usuário

### 🤖 Subagentes Especializados

#### 1. AgenteCastracao
- **Função**: Agendamento de castrações
- **Integrações**: 
  - Supabase (armazenamento de dados)
  - Google Calendar (agendamento)
- **Dados coletados**: Nome do tutor, animal, contato, data preferida, endereço

#### 2. AgenteAdocaoDoacao
- **Função**: Gerenciamento de adoções e doações
- **Integração**: Supabase
- **Dados coletados**: Tipo de solicitação, detalhes do animal, localização, contato

#### 3. AgenteAnimaisPerdidos
- **Função**: Registro de animais perdidos/encontrados
- **Integração**: Supabase com geolocalização
- **Dados coletados**: Características do animal, local, data, contato responsável

#### 4. AgenteDicas (RAG)
- **Função**: Resposta a dúvidas frequentes
- **Integração**: Base vetorial no Supabase
- **Funcionalidade**: Busca semântica e geração de respostas contextualizadas

## Fluxo de Dados

```
Entrada (WhatsApp/Email) 
    ↓
Set Initial Data 
    ↓
Switch Channel 
    ↓
OrquestradorONG (Classificação IA)
    ↓
Switch Intenção 
    ↓
Agentes Especializados
    ↓
Processamento e Armazenamento
    ↓
Log Sistema
    ↓
Preparar Resposta
    ↓
Switch Resposta
    ↓
Envio (WhatsApp/Email)
```

## Componentes Técnicos

### Triggers
- **WhatsApp Webhook**: Recebe mensagens via EvolutionAPI
- **Email IMAP Trigger**: Monitora caixa de entrada

### Processamento
- **Set Nodes**: Formatação e preparação de dados
- **Switch Nodes**: Roteamento condicional
- **Agent Nodes**: Processamento com IA (OpenAI)
- **HTTP Request Nodes**: Integrações com APIs externas

### Armazenamento e Logging
- **Supabase**: Banco de dados principal
- **Redis**: Cache e memória de curto prazo
- **Google Calendar**: Agendamentos
- **Logs Sistema**: Auditoria e monitoramento

### Respostas
- **Evolution API**: Envio de mensagens WhatsApp
- **SMTP**: Envio de e-mails

## Configurações Necessárias

### Variáveis de Ambiente
```
SUPABASE_URL=sua_url_supabase
EVOLUTION_API_URL=sua_url_evolution_api
EVOLUTION_INSTANCE=sua_instancia
EMAIL_ONG=email_da_ong@exemplo.com
```

### Credenciais Necessárias
- `openai-ong-credentials`: API OpenAI
- `supabase-ong-credentials`: API Supabase
- `google-calendar-ong-credentials`: Google Calendar OAuth2
- `evolution-api-credentials`: Evolution API Header Auth
- `smtp-ong-credentials`: SMTP para envio de e-mails
- `imap-ong-credentials`: IMAP para recebimento de e-mails

### Tabelas Supabase Necessárias

#### castracoes
```sql
CREATE TABLE castracoes (
  id SERIAL PRIMARY KEY,
  nome_tutor VARCHAR(255),
  tipo_animal VARCHAR(50),
  nome_animal VARCHAR(255),
  idade_animal VARCHAR(50),
  contato VARCHAR(255),
  data_preferida DATE,
  endereco TEXT,
  usuario_id VARCHAR(255),
  canal VARCHAR(50),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### adocoes_doacoes
```sql
CREATE TABLE adocoes_doacoes (
  id SERIAL PRIMARY KEY,
  tipo_solicitacao VARCHAR(50),
  nome_solicitante VARCHAR(255),
  contato_solicitante VARCHAR(255),
  localizacao VARCHAR(255),
  detalhes_animal TEXT,
  observacoes TEXT,
  usuario_id VARCHAR(255),
  canal VARCHAR(50),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### animais_perdidos
```sql
CREATE TABLE animais_perdidos (
  id SERIAL PRIMARY KEY,
  tipo_caso VARCHAR(50),
  nome_animal VARCHAR(255),
  caracteristicas TEXT,
  local_ocorrencia VARCHAR(255),
  data_ocorrencia DATE,
  contato_responsavel VARCHAR(255),
  observacoes_especiais TEXT,
  usuario_id VARCHAR(255),
  canal VARCHAR(50),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT NOW()
);
```

#### logs_sistema
```sql
CREATE TABLE logs_sistema (
  id SERIAL PRIMARY KEY,
  usuario_id VARCHAR(255),
  canal VARCHAR(50),
  agente_usado VARCHAR(255),
  input_texto TEXT,
  output_texto TEXT,
  status VARCHAR(50),
  timestamp TIMESTAMP DEFAULT NOW(),
  tokens_usados INTEGER,
  detalhes_erro TEXT
);
```

## Funcionalidades Principais

### ✅ Multicanal
- WhatsApp via EvolutionAPI
- E-mail via IMAP/SMTP

### ✅ IA Conversacional
- Classificação automática de intenções
- Agentes especializados por domínio
- Respostas contextualizadas

### ✅ Integrações Robustas
- Supabase para persistência
- Google Calendar para agendamentos
- RAG para base de conhecimento

### ✅ Monitoramento
- Logging completo de interações
- Tratamento de erros
- Métricas de uso de tokens

### ✅ Escalabilidade
- Arquitetura modular
- Fácil adição de novos agentes
- Configuração via variáveis de ambiente

## Próximos Passos

1. **Configurar credenciais** no n8n
2. **Criar tabelas** no Supabase
3. **Configurar webhooks** do WhatsApp
4. **Testar fluxo** com dados reais
5. **Ajustar prompts** dos agentes conforme necessário
6. **Implementar Redis** para cache (opcional)
7. **Configurar monitoramento** e alertas

## Versão
- **n8n**: v1.104.2
- **Fluxo**: v1.0.0
- **Data**: {{ $now }}

