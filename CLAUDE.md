# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a reference repository containing n8n workflow examples, documentation, and course materials. The repository is organized as an archive of Telegram conversations and shared n8n workflows focused on AI agents, automation, and workflow patterns.

## Repository Structure

```
N8Np/
└── Ref/
    └── 2494913847/
        ├── [topic_id]/
        │   ├── content.txt          # Telegram conversation export
        │   ├── messages.json        # Structured message data
        │   ├── metadata.json        # Topic metadata
        │   ├── *.json              # n8n workflow files
        │   ├── *.pdf               # Documentation and course materials
        │   └── *.jpg               # Screenshots and diagrams
```

Each numbered subdirectory (e.g., `8187`, `4581`, `2851`) represents a Telegram topic/conversation containing:
- **n8n workflow files** (`.json`): Importable workflow definitions
- **content.txt**: Human-readable conversation transcript
- **messages.json**: Structured message data
- **metadata.json**: Topic information (title, creation date, message count)
- **Supporting materials**: PDFs, images, and other resources

## n8n Workflow Files

The repository contains 1000+ n8n workflow examples covering:

### Core Workflow Patterns
- RAG (Retrieval Augmented Generation) pipelines and chatbots
- Customer support automation
- LinkedIn automation workflows
- Invoice processing workflows
- API integration patterns

### AI Agent Architectures
- First AI agents setup
- RAG workflows vs RAG agents
- Technical analyst agents vs workflows
- Orchestrator architecture patterns
- Prompt chaining techniques
- Routing and parallelization strategies

### Human-in-the-Loop (HITL)
- Email validation with human approval (`Agente_de_emails_con_validaci_n_humana.json`)
- Sales agent workflows with human review
- Feedback loop implementation patterns

### Advanced Patterns
- Error logging systems
- Dynamic brain architecture
- Evaluator and optimizer patterns
- Voice email agents

### Integrations
- Google Drive triggers and uploads
- Supabase/Postgres integration
- Firecrawl extraction templates
- Apify web scraping
- OpenAI image generation
- Perplexity API usage
- PiAPI music generation

## Working with n8n Workflow Files

### Understanding Workflow Structure
n8n workflow files are JSON documents with the following key sections:
- **name**: Workflow name/title
- **nodes**: Array of workflow nodes (triggers, actions, logic)
- **connections**: Node connection mappings
- **settings**: Workflow-level configuration

Each node contains:
- **parameters**: Node-specific configuration
- **type**: Node type (e.g., `n8n-nodes-base.googleDriveTrigger`)
- **position**: Canvas coordinates `[x, y]`
- **credentials**: Reference to credential IDs

### Common Node Types
- **Triggers**: `googleDriveTrigger`, `webhook`, `schedule`
- **AI/LLM**: OpenAI nodes, Claude nodes, text classifiers
- **Data**: Airtable, Supabase, database operations
- **Logic**: IF conditions, switches, loops, code nodes
- **Communication**: Gmail, email, notifications

### Credentials in Workflows
Workflow files contain credential references but NOT actual credentials:
```json
"credentials": {
  "googleDriveOAuth2Api": {
    "id": "V2ewjiHO0o6xhQ2R",
    "name": "Google Drive account"
  }
}
```
When importing workflows, users must reconfigure credentials in their n8n instance.

## Content Files

### content.txt Format
Each `content.txt` follows this structure:
```
TOPICO [id]
==================================================

Titulo: [topic title]
Criado em: [timestamp]

Total de mensagens: [count]
Midias baixadas: [count]

--------------------------------------------------

MENSAGEM [number]
Autor: [author name]
Data: [ISO timestamp]
Texto:
[message content]
Midia: [media type] -> [filename]

------------------------------
```

### Common Authors
- **INEMA**: Primary content contributor (workflows, courses, documentation)
- Various community members sharing use cases and questions

## Course Materials

The repository includes "The Ultimate n8n Course" materials covering:
1. RAG Pipeline & Chatbot
2. Customer Support Workflow
3. LinkedIn Workflow
4. Invoice Workflow
5. API Calls in n8n
6. Perplexity integration
7. Firecrawl Extract Template
8. Apify web scraping
9. OpenAI Image Generation
10. Product Videos automation
11-23. Advanced agent patterns and architectures

## Language

Content is primarily in **Portuguese (Brazilian)**, with some English technical terms and workflow names.

## Working with This Repository

### Finding Workflows
Use topic numbers or workflow names to locate specific examples:
```bash
# Find workflows by name pattern
find Ref/ -name "*RAG*.json"

# Find specific topic
ls Ref/2494913847/8187/

# Search conversation content
grep -r "specific topic" Ref/*/content.txt
```

### Extracting Workflow Information
To understand a workflow's purpose:
1. Read the corresponding `content.txt` for context
2. Look for workflow name in messages
3. Check for related images/screenshots
4. Examine the JSON structure for node types and connections

### Common Operations
- **Listing all workflows in a topic**: `ls Ref/2494913847/[topic_id]/*.json`
- **Reading conversation context**: `cat Ref/2494913847/[topic_id]/content.txt`
- **Checking metadata**: `cat Ref/2494913847/[topic_id]/metadata.json`

## Notes

- This is a **reference/archive repository**, not an active n8n installation
- Workflows cannot be executed directly; they must be imported into an n8n instance
- All credentials must be reconfigured after importing
- The repository structure is organized by Telegram conversation exports
- Topic IDs are numeric and represent individual conversation threads
