#!/usr/bin/env python3
"""
Script para gerar documentação MkDocs a partir dos workflows n8n
"""

import json
import os
from pathlib import Path
from collections import defaultdict

# Diretórios
BASE_DIR = Path(__file__).parent
REF_DIR = BASE_DIR / "Ref" / "2494913847"
DOCS_DIR = BASE_DIR / "n8np-docs" / "docs"
WORKFLOWS_DIR = DOCS_DIR / "workflows"
TOPICOS_DIR = DOCS_DIR / "topicos"

# Categorias de workflows
CATEGORIAS = {
    "AI Agents": ["agent", "rag", "chatbot", "ai", "gpt", "claude", "llm", "voice"],
    "Automações": ["workflow", "automation", "customer", "support", "invoice", "linkedin", "whatsapp"],
    "Integrações": ["google", "drive", "sheets", "gmail", "supabase", "postgres", "airtable",
                    "firecrawl", "apify", "openai", "perplexity", "piapi"],
    "HITL": ["hitl", "validação", "validacion", "human", "approval", "feedback"],
    "Arquitetura": ["orchestrator", "routing", "parallelization", "chaining", "brain", "error"],
}

def categorizar_workflow(nome):
    """Categoriza workflow baseado no nome"""
    nome_lower = nome.lower()
    categorias = []

    for categoria, keywords in CATEGORIAS.items():
        if any(keyword in nome_lower for keyword in keywords):
            categorias.append(categoria)

    if not categorias:
        categorias.append("Outros")

    return categorias

def processar_workflow(workflow_path):
    """Extrai informações de um workflow n8n"""
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        nome = data.get('name', 'Sem nome')
        nodes = data.get('nodes', [])

        # Extrair tipos de nodes únicos
        node_types = set()
        integracoes = set()

        for node in nodes:
            node_type = node.get('type', '')
            node_types.add(node_type)

            # Identificar integrações
            if 'google' in node_type.lower():
                integracoes.add('Google')
            if 'gmail' in node_type.lower():
                integracoes.add('Gmail')
            if 'airtable' in node_type.lower():
                integracoes.add('Airtable')
            if 'supabase' in node_type.lower():
                integracoes.add('Supabase')
            if 'openai' in node_type.lower() or 'langchain' in node_type.lower():
                integracoes.add('OpenAI/LangChain')

        return {
            'nome': nome,
            'nodes_count': len(nodes),
            'node_types': list(node_types),
            'integracoes': list(integracoes),
            'path': str(workflow_path.relative_to(BASE_DIR))
        }
    except Exception as e:
        print(f"Erro ao processar {workflow_path}: {e}")
        return None

def gerar_pagina_workflow(workflows, categoria, filename):
    """Gera página markdown para uma categoria de workflows"""

    md = f"# {categoria}\n\n"
    md += f"Total de workflows: **{len(workflows)}**\n\n"

    # Agrupar por tópico
    por_topico = defaultdict(list)
    for wf in workflows:
        topico = Path(wf['path']).parts[2]  # Ref/2494913847/[TOPICO]/...
        por_topico[topico].append(wf)

    for topico in sorted(por_topico.keys()):
        wfs = por_topico[topico]
        md += f"\n## Tópico {topico}\n\n"

        for wf in sorted(wfs, key=lambda x: x['nome']):
            md += f"### {wf['nome']}\n\n"
            md += f"- **Nodes:** {wf['nodes_count']}\n"

            if wf['integracoes']:
                md += f"- **Integrações:** {', '.join(sorted(wf['integracoes']))}\n"

            md += f"- **Arquivo:** `{wf['path']}`\n"
            md += f"\n??? info \"Detalhes Técnicos\"\n"
            md += f"    **Node types usados:**\n"
            for nt in sorted(wf['node_types'])[:10]:  # Limitar a 10
                md += f"    - `{nt}`\n"
            md += "\n"

    # Salvar arquivo
    output_path = WORKFLOWS_DIR / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✓ Gerado: {output_path}")

def gerar_indice_workflows(todos_workflows):
    """Gera página índice de workflows"""

    md = "# Visão Geral dos Workflows\n\n"
    md += f"Total de **{len(todos_workflows)} workflows** catalogados.\n\n"

    md += "## 📊 Por Categoria\n\n"
    md += "| Categoria | Quantidade |\n"
    md += "|-----------|------------|\n"

    # Contar por categoria
    contagem = defaultdict(int)
    for wf in todos_workflows:
        cats = categorizar_workflow(wf['nome'])
        for cat in cats:
            contagem[cat] += 1

    for cat in sorted(contagem.keys()):
        count = contagem[cat]
        link = cat.lower().replace(" ", "-")
        md += f"| [{cat}]({link}.md) | {count} |\n"

    md += "\n## 🔍 Busca Rápida\n\n"
    md += "Use a busca no topo da página ou navegue pelas categorias:\n\n"

    for cat in sorted(contagem.keys()):
        link = cat.lower().replace(" ", "-")
        md += f"- **[{cat}]({link}.md)** - {contagem[cat]} workflows\n"

    # Salvar
    output_path = WORKFLOWS_DIR / "index.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✓ Gerado: {output_path}")

def gerar_paginas_topicos():
    """Gera páginas para tópicos individuais"""

    # Índice de tópicos
    md = "# Tópicos da Comunidade\n\n"
    md += "Conversas do Telegram organizadas por tópico.\n\n"
    md += "| Tópico | Mensagens | Data |\n"
    md += "|--------|-----------|------|\n"

    topicos = []

    for topico_dir in sorted(REF_DIR.iterdir()):
        if not topico_dir.is_dir():
            continue

        metadata_file = topico_dir / "metadata.json"
        if metadata_file.exists():
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    meta = json.load(f)

                topico_id = meta.get('topic_id')
                total_msgs = meta.get('total_messages', 0)
                data = meta.get('topic_creation_date', 'N/A')[:10]

                md += f"| [{topico_id}]({topico_id}.md) | {total_msgs} | {data} |\n"
                topicos.append(meta)
            except:
                pass

    # Salvar índice
    output_path = TOPICOS_DIR / "index.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✓ Gerado: {output_path}")

def gerar_pagina_curso():
    """Gera página do curso"""

    md = "# The Ultimate n8n Course\n\n"
    md += "Curso completo com 23 lições progressivas sobre n8n, AI agents e automações.\n\n"

    licoes = [
        "RAG Pipeline & Chatbot",
        "Customer Support Workflow",
        "LinkedIn Workflow",
        "Invoice Workflow",
        "API Calls in n8n",
        "Perplexity",
        "Firecrawl Extract Template",
        "Apify",
        "OpenAI Image Gen",
        "Product Videos",
        "RAG Workflow vs RAG Agent",
        "Technical Analyst Agent vs Workflow",
        "First AI Agent",
        "Supabase Postgres",
        "Orchestrator Architecture",
        "Prompt Chaining",
        "Routing",
        "Parallelization",
        "Evaluator Optimizer",
        "HITL Example Flows",
        "Error Logger",
        "Dynamic Brain",
        "Voice Email Agent"
    ]

    md += "## 📚 Lições\n\n"

    for i, licao in enumerate(licoes, 1):
        # Tentar encontrar o workflow correspondente
        workflow_file = f"{i}) {licao}.json"

        md += f"### {i}. {licao}\n\n"
        md += f"!!! abstract \"Lição {i}\"\n"
        md += f"    {licao}\n\n"

        # Buscar no tópico 8187 (onde está o curso)
        curso_path = REF_DIR / "8187" / workflow_file
        if curso_path.exists():
            rel_path = curso_path.relative_to(BASE_DIR)
            md += f"    **Arquivo:** `{rel_path}`\n\n"

    md += "\n## 📖 Materiais Adicionais\n\n"
    md += "- The Ultimate n8n Starter Kit (PDF)\n"
    md += "- AI Works Guide (PDF)\n"
    md += "- Mastering Reactive Prompting for AI Agents (PDF)\n"

    # Salvar
    output_path = DOCS_DIR / "curso" / "index.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✓ Gerado: {output_path}")

def gerar_about():
    """Gera página sobre"""

    md = "# Sobre o N8Np\n\n"
    md += "## 📦 O que é este repositório?\n\n"
    md += "O N8Np é uma coleção completa de workflows n8n, AI agents e automações "
    md += "coletados da comunidade Telegram.\n\n"

    md += "## 📊 Estatísticas\n\n"
    md += "- **535** workflows n8n\n"
    md += "- **420** tópicos/conversas\n"
    md += "- **1.1 GB** de conteúdo\n"
    md += "- **70** PDFs educacionais\n"
    md += "- **1000+** imagens e screenshots\n\n"

    md += "## 🤝 Como Contribuir\n\n"
    md += "Este é um arquivo da comunidade. Para adicionar seus workflows:\n\n"
    md += "1. Compartilhe no grupo Telegram\n"
    md += "2. Ou faça um PR no repositório GitHub\n\n"

    md += "## ⚠️ Aviso Legal\n\n"
    md += "- Todos os workflows são compartilhados pela comunidade\n"
    md += "- Credenciais devem ser reconfiguradas ao importar\n"
    md += "- Use por sua conta e risco\n"
    md += "- Sempre revise os workflows antes de usar em produção\n"

    # Salvar
    output_path = DOCS_DIR / "about.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"✓ Gerado: {output_path}")

def main():
    print("🚀 Gerando documentação N8Np...\n")

    # Criar diretórios
    WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
    TOPICOS_DIR.mkdir(parents=True, exist_ok=True)

    # Coletar todos os workflows
    print("📂 Coletando workflows...")
    todos_workflows = []

    for topico_dir in REF_DIR.iterdir():
        if not topico_dir.is_dir():
            continue

        for json_file in topico_dir.glob("*.json"):
            # Ignorar metadata e messages
            if json_file.name in ['metadata.json', 'messages.json']:
                continue

            wf = processar_workflow(json_file)
            if wf:
                todos_workflows.append(wf)

    print(f"   Encontrados {len(todos_workflows)} workflows\n")

    # Organizar por categoria
    print("🏷️  Categorizando workflows...")
    por_categoria = defaultdict(list)

    for wf in todos_workflows:
        categorias = categorizar_workflow(wf['nome'])
        for cat in categorias:
            por_categoria[cat].append(wf)

    # Gerar páginas por categoria
    print("\n📝 Gerando páginas de categorias...")
    for categoria, workflows in por_categoria.items():
        filename = f"{categoria.lower().replace(' ', '-')}.md"
        gerar_pagina_workflow(workflows, categoria, filename)

    # Gerar índice
    print("\n📋 Gerando índices...")
    gerar_indice_workflows(todos_workflows)
    gerar_paginas_topicos()
    gerar_pagina_curso()
    gerar_about()

    print("\n✅ Documentação gerada com sucesso!")
    print(f"\n📂 Arquivos em: {DOCS_DIR}")
    print("\n🌐 Para visualizar:")
    print("   cd n8np-docs")
    print("   mkdocs serve")

if __name__ == "__main__":
    main()
