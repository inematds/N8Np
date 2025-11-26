# 🚀 N8Np - Biblioteca de Workflows n8n & AI Agents

[![MkDocs](https://img.shields.io/badge/docs-mkdocs-blue)](https://inematds.github.io/N8Np/)
[![Material for MkDocs](https://img.shields.io/badge/theme-material-00C7B7)](https://squidfunk.github.io/mkdocs-material/)
[![Workflows](https://img.shields.io/badge/workflows-532-success)](https://inematds.github.io/N8Np/workflows/)
[![License](https://img.shields.io/badge/license-Community-orange)](LICENSE)

> Biblioteca completa de workflows n8n, AI agents e automações da comunidade N8Np

## 📊 Estatísticas

- **532 workflows** catalogados
- **198 AI Agents**
- **420 tópicos** da comunidade
- **23 lições** do curso completo
- **1.1 GB** de conteúdo educacional

## 🌐 Acesse o Site

👉 **[https://inematds.github.io/N8Np/](https://inematds.github.io/N8Np/)**

Site de documentação completo com:
- 🔍 Busca inteligente
- 📁 Categorização automática
- 🎨 Tema moderno Material Design
- 🌗 Modo claro/escuro
- 📱 Responsivo

## 🎯 Categorias

### 🤖 [AI Agents](https://inematds.github.io/N8Np/workflows/ai-agents/)
Agentes inteligentes com LLMs (GPT-4, Claude, etc), RAG pipelines, chatbots e sistemas HITL

**Destaques:**
- Agente de vendas com validação humana
- First AI Agent com Google Sheets
- RAG Workflow vs RAG Agent
- Voice Email Agent

### 🔄 [Automações](https://inematds.github.io/N8Np/workflows/automations/)
Workflows para automatizar processos empresariais

**Destaques:**
- Customer Support Workflow
- LinkedIn Automation
- Invoice Processing
- WhatsApp Agent

### 🛠️ [Integrações](https://inematds.github.io/N8Np/workflows/integrations/)
Conectores com serviços populares

**Disponíveis:**
- Google Drive, Sheets, Gmail
- Supabase / Postgres
- OpenAI, Perplexity
- Airtable, Firecrawl, Apify

### 📚 [Curso Completo](https://inematds.github.io/N8Np/curso/)
"The Ultimate n8n Course" com 23 lições progressivas

## 🚀 Como Usar

### Acessar Online
Visite: [https://inematds.github.io/N8Np/](https://inematds.github.io/N8Np/)

### Rodar Localmente
```bash
# Clonar repositório
git clone https://github.com/inematds/N8Np.git
cd N8Np

# Instalar dependências
pip install mkdocs mkdocs-material

# Rodar site
cd n8np-docs
mkdocs serve
```

Acesse: http://127.0.0.1:8000

### Importar Workflows
1. Navegue pelo site e encontre o workflow desejado
2. Copie o caminho do arquivo (ex: `Ref/2494913847/8187/1) RAG Pipeline & Chatbot.json`)
3. Importe no seu n8n
4. Reconfigure as credenciais

## 📂 Estrutura do Repositório

```
N8Np/
├── Ref/                          # 532 workflows organizados por tópico
│   └── 2494913847/              # Grupo do Telegram
│       ├── [topic_id]/          # Tópico individual
│       │   ├── *.json          # Workflows n8n
│       │   ├── content.txt     # Conversa da comunidade
│       │   ├── metadata.json   # Metadados
│       │   └── *.pdf           # Documentação
│       └── ...
├── n8np-docs/                   # Site de documentação
│   ├── mkdocs.yml              # Configuração
│   ├── docs/                   # Conteúdo markdown
│   └── site/                   # HTML gerado
├── generate_docs.py             # Script de geração
├── CLAUDE.md                    # Guia para Claude Code
├── RELATORIO_ANALISE.md        # Análise do repositório
└── README.md                   # Este arquivo
```

## 🔄 Atualizar Documentação

Se novos workflows forem adicionados:

```bash
# Regenerar documentação
python3 generate_docs.py

# Deploy
cd n8np-docs
mkdocs gh-deploy
```

## 🤝 Contribuir

Contribuições são bem-vindas! Para adicionar workflows:

1. Adicione os arquivos `.json` em `Ref/2494913847/[novo_topico]/`
2. Execute `python3 generate_docs.py`
3. Faça um Pull Request

## 📖 Documentação

- [CLAUDE.md](CLAUDE.md) - Guia para Claude Code trabalhar no repo
- [RELATORIO_ANALISE.md](RELATORIO_ANALISE.md) - Análise completa do conteúdo
- [IMPLEMENTACAO_COMPLETA.md](IMPLEMENTACAO_COMPLETA.md) - Detalhes da implementação
- [n8np-docs/README.md](n8np-docs/README.md) - Documentação do site

## ⚠️ Importante

- Todos os workflows precisam de **credenciais reconfiguradas** após importação
- Este é um **repositório de referência**, não uma instalação n8n ativa
- Sempre revise os workflows antes de usar em produção

## 🌟 Destaques da Comunidade

### Workflow Mais Popular
**Agente de Vendas com Validação Humana**

Sistema completo de sales automation com loop de feedback humano usando Gmail "Send and Wait" + Text Classifier.

### Caso de Uso Real
**Geração de Músicas Automática**

Workflow que gera músicas com PiAPI e envia para Google Drive automaticamente.

## 📞 Comunidade

- 💬 [Telegram](https://t.me/n8np) - Comunidade N8Np
- 🌐 [Site](https://inematds.github.io/N8Np/) - Documentação oficial
- 📧 Email: inematds@gmail.com

## 📄 License

Conteúdo compartilhado pela comunidade N8Np para uso educacional.

---

<p align="center">
  <strong>✨ Criado pela comunidade N8Np</strong><br>
  <em>1.1 GB de conteúdo educacional | 532 workflows | 420 tópicos</em>
</p>

<p align="center">
  <a href="https://inematds.github.io/N8Np/">🌐 Visite o Site</a> •
  <a href="https://inematds.github.io/N8Np/workflows/">📁 Ver Workflows</a> •
  <a href="https://inematds.github.io/N8Np/curso/">📚 Fazer Curso</a>
</p>
