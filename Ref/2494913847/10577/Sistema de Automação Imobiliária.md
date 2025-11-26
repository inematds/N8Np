# Sistema de Automação Imobiliária

## 🏠 Visão Geral

Sistema completo de automação para imobiliárias usando n8n, integrando WhatsApp Business, E-mail e Telegram com backend Supabase. Oferece atendimento automatizado inteligente com supervisão humana (HITL - Human-in-the-Loop).

## ✨ Funcionalidades Principais

### 🤖 Agentes Inteligentes
- **Orquestrador Central**: Coordena todas as interações e roteia para agentes especializados
- **Atendimento Inicial**: Qualifica leads e identifica necessidades
- **Agendamento de Visitas**: Automatiza agendamentos com confirmações
- **Captação de Proprietários**: Processa cadastros de imóveis
- **Relacionamento**: Follow-up automático e newsletter personalizada

### 📱 Canais de Comunicação
- **WhatsApp Business API**: Atendimento via WhatsApp com respostas automáticas
- **E-mail IMAP/SMTP**: Processamento de e-mails com newsletter HTML
- **Telegram Bot**: Supervisão e controle via comandos

### 🎯 Sistema HITL
- Supervisão humana inteligente
- Notificações automáticas para casos complexos
- Dashboard de controle via Telegram
- Aprovação e resposta manual quando necessário

### 📊 Analytics e Relatórios
- Métricas em tempo real
- Relatórios diários e semanais
- Score de qualificação de clientes
- Monitoramento de performance

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   WhatsApp      │    │     E-mail      │    │   Telegram      │
│   Business API  │    │   IMAP/SMTP     │    │     Bot         │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴─────────────┐
                    │    Agente Orquestrador    │
                    │         (n8n)             │
                    └─────────────┬─────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
┌─────────┴───────┐    ┌─────────┴───────┐    ┌─────────┴───────┐
│   Atendimento   │    │   Agendamento   │    │   Captação      │
│    Inicial      │    │   de Visitas    │    │ Proprietários   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴─────────────┐
                    │      Supabase             │
                    │    (PostgreSQL)           │
                    └───────────────────────────┘
```

## 🚀 Instalação Rápida

### Pré-requisitos
- Conta Supabase
- Instância n8n (cloud ou self-hosted)
- WhatsApp Business API configurado
- Conta de e-mail com IMAP/SMTP
- Bot Telegram criado

### 1. Configurar Backend
```bash
# 1. Criar projeto no Supabase
# 2. Executar scripts SQL da pasta supabase/
# 3. Configurar políticas de segurança
```

### 2. Importar Workflows
```bash
# 1. Importar todos os arquivos .json da pasta n8n-workflows/
# 2. Configurar credenciais (Supabase, SMTP, IMAP, Telegram)
# 3. Configurar variáveis de ambiente
```

### 3. Configurar Integrações
```bash
# 1. Configurar webhook do WhatsApp
# 2. Configurar bot do Telegram
# 3. Testar conectividade
```

## 📁 Estrutura do Projeto

```
automacao-imobiliaria/
├── supabase/
│   ├── schema.sql              # Estrutura do banco de dados
│   └── security.sql            # Políticas de segurança RLS
├── n8n-workflows/
│   ├── 01-orquestrador-central.json
│   ├── 02-monitoramento-metricas.json
│   ├── 03-atendimento-inicial.json
│   ├── 04-agendamento-visitas.json
│   ├── 05-captacao-proprietarios.json
│   ├── 06-relacionamento-follow-up.json
│   ├── 07-integracao-whatsapp.json
│   ├── 08-integracao-email.json
│   └── 09-sistema-hitl-telegram.json
├── documentacao/
│   ├── arquitetura.md
│   ├── manual-instalacao.md
│   ├── guia-uso.md
│   ├── configuracao-variaveis.md
│   └── troubleshooting-faq.md
└── README.md
```

## 🔧 Configuração

### Variáveis de Ambiente Principais

```bash
# Supabase
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua_chave_aqui
SUPABASE_SERVICE_ROLE_KEY=sua_chave_service_role

# WhatsApp Business API
WHATSAPP_ACCESS_TOKEN=seu_token_aqui
WHATSAPP_PHONE_NUMBER_ID=seu_phone_id
WHATSAPP_VERIFY_TOKEN=seu_verify_token

# E-mail
SMTP_HOST=smtp.gmail.com
SMTP_USER=seu_email@gmail.com
SMTP_PASS=sua_senha_app

# Telegram
TELEGRAM_BOT_TOKEN=seu_bot_token
TELEGRAM_ALLOWED_USERS=123456789,987654321

# n8n
N8N_WEBHOOK_BASE_URL=https://seu-n8n.com
INTERNAL_API_KEY=sua_chave_interna
```

## 📊 Métricas e KPIs

### Principais Indicadores
- **Tempo de Resposta**: < 60 segundos
- **Taxa de Resolução Automática**: > 85%
- **Satisfação do Cliente**: > 4.5/5
- **Taxa de Conversão**: > 15%
- **Uptime do Sistema**: > 99.5%

### Dashboard Telegram
- Status do sistema em tempo real
- Clientes ativos e score de qualificação
- Visitas agendadas para o dia
- Solicitações HITL pendentes
- Relatórios automáticos

## 🎯 Casos de Uso

### Para Imobiliárias
- Atendimento 24/7 automatizado
- Qualificação inteligente de leads
- Agendamento automático de visitas
- Follow-up personalizado
- Captação de novos imóveis

### Para Corretores
- Dashboard de controle via Telegram
- Notificações de leads qualificados
- Agenda automatizada
- Relatórios de performance
- Supervisão de IA quando necessário

### Para Clientes
- Atendimento instantâneo
- Respostas personalizadas
- Agendamento fácil de visitas
- Newsletter com novidades
- Múltiplos canais de contato

## 🔒 Segurança

- **Row Level Security (RLS)** no Supabase
- **Autenticação por tokens** em todas as APIs
- **Criptografia TLS** em todas as comunicações
- **Logs auditáveis** de todas as operações
- **Controle de acesso** granular por usuário

## 📈 Escalabilidade

- **Arquitetura modular** permite expansão fácil
- **Webhooks assíncronos** para alta performance
- **Cache inteligente** para otimização
- **Rate limiting** para proteção de APIs
- **Monitoramento** proativo de recursos

## 🛠️ Tecnologias Utilizadas

- **n8n**: Automação e workflows
- **Supabase**: Backend e banco de dados PostgreSQL
- **WhatsApp Business API**: Comunicação via WhatsApp
- **Telegram Bot API**: Interface de supervisão
- **SMTP/IMAP**: Processamento de e-mails
- **JavaScript/Node.js**: Lógica de negócio
- **SQL**: Consultas e relatórios

## 📚 Documentação

- [Manual de Instalação](documentacao/manual-instalacao.md)
- [Guia de Uso](documentacao/guia-uso.md)
- [Configuração de Variáveis](documentacao/configuracao-variaveis.md)
- [Troubleshooting e FAQ](documentacao/troubleshooting-faq.md)
- [Arquitetura do Sistema](documentacao/arquitetura.md)

## 🤝 Suporte

### Canais de Suporte
- **E-mail**: suporte@imobiliaria.com
- **Telegram**: @suporte_imobiliaria
- **Documentação**: [Wiki do projeto]

### SLA
- **Crítico**: 4 horas
- **Alto**: 24 horas
- **Médio**: 48 horas
- **Baixo**: 1 semana

## 📄 Licença

Este projeto é proprietário. Todos os direitos reservados.

## 🎉 Contribuições

Para contribuir com o projeto:
1. Faça fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📞 Contato

- **Desenvolvedor**: [Seu nome]
- **E-mail**: dev@imobiliaria.com
- **LinkedIn**: [Seu perfil]
- **GitHub**: [Seu perfil]

---

**Versão**: 1.0.0  
**Última atualização**: 26/06/2025  
**Status**: Produção

> 💡 **Dica**: Comece pelo [Manual de Instalação](documentacao/manual-instalacao.md) para configurar o sistema passo a passo.

