#!/usr/bin/env python3
"""
Inventário completo de workflows n8n do repositório N8Np
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Diretório base
BASE_DIR = Path("/home/nmaldaner/projetos/N8Np/doc/2494913847")

# Categorias baseadas em palavras-chave e nodes
CATEGORIES = {
    "🤖 AI Agents & RAG": [
        "agent", "rag", "llm", "openai", "claude", "anthropic", "gpt",
        "chatbot", "ai", "embedding", "vector", "langchain", "memory",
        "deepseek", "gemini", "perplexity", "groq"
    ],
    "💬 WhatsApp & Telegram": [
        "whatsapp", "telegram", "evolution", "baileys", "waha", "z-api"
    ],
    "📧 Email & Comunicação": [
        "email", "gmail", "smtp", "imap", "outlook", "newsletter", "mail"
    ],
    "📊 Planilhas & Dados": [
        "sheets", "excel", "airtable", "notion", "spreadsheet", "csv",
        "database", "supabase", "postgres", "mysql", "mongodb"
    ],
    "🎬 Vídeo & Mídia": [
        "video", "youtube", "vimeo", "ffmpeg", "media", "image", "audio",
        "tiktok", "reels", "shorts", "veo", "heygen", "runway"
    ],
    "🔗 Integrações & APIs": [
        "api", "webhook", "http", "rest", "graphql", "integration"
    ],
    "📱 Redes Sociais": [
        "instagram", "linkedin", "twitter", "facebook", "social", "bluesky",
        "x post", "tiktok"
    ],
    "📅 Produtividade & Calendário": [
        "calendar", "calendly", "schedule", "task", "todo", "trello",
        "asana", "clickup", "notion"
    ],
    "💰 Vendas & CRM": [
        "crm", "sales", "lead", "hubspot", "pipedrive", "customer",
        "client", "invoice", "payment"
    ],
    "🔄 Automação & Utilidades": [
        "automation", "workflow", "trigger", "loop", "batch", "error",
        "backup", "sync", "monitor"
    ],
    "🌐 Web Scraping & Extração": [
        "scrape", "scraping", "crawl", "extract", "firecrawl", "apify",
        "browser", "puppeteer", "playwright"
    ],
    "📝 Documentos & Conteúdo": [
        "document", "pdf", "doc", "content", "text", "write", "blog",
        "article", "post", "gamma"
    ]
}

def extract_workflow_info(json_path):
    """Extrai informações de um arquivo de workflow n8n"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Pegar nome do workflow
        name = data.get('name', json_path.stem)

        # Pegar nodes
        nodes = data.get('nodes', [])
        node_types = set()
        node_names = []

        for node in nodes:
            node_type = node.get('type', '')
            node_name = node.get('name', '')
            node_types.add(node_type)
            node_names.append(node_name)

        # Descrição se houver
        description = data.get('description', '')

        # Tags se houver
        tags = data.get('tags', [])
        if isinstance(tags, list):
            tags = [t.get('name', t) if isinstance(t, dict) else t for t in tags]

        # Buscar imagens na mesma pasta
        images = []
        folder = json_path.parent
        for img in folder.glob("*.jpg"):
            # Caminho relativo para GitHub Pages
            rel_path = str(img).replace("/home/nmaldaner/projetos/N8Np/", "")
            images.append(rel_path)
        for img in folder.glob("*.png"):
            rel_path = str(img).replace("/home/nmaldaner/projetos/N8Np/", "")
            images.append(rel_path)

        # Ordenar e pegar a primeira imagem como thumbnail
        images.sort()
        thumbnail = images[0] if images else None

        return {
            'name': name,
            'file': json_path.name,
            'folder': json_path.parent.name,
            'path': str(json_path),
            'node_types': list(node_types),
            'node_names': node_names,
            'node_count': len(nodes),
            'description': description,
            'tags': tags,
            'images': images,
            'thumbnail': thumbnail
        }
    except Exception as e:
        return {
            'name': json_path.stem,
            'file': json_path.name,
            'folder': json_path.parent.name,
            'path': str(json_path),
            'error': str(e)
        }

def categorize_workflow(workflow_info):
    """Categoriza um workflow baseado em nome, nodes e tags"""
    categories = []

    # Texto para buscar palavras-chave
    search_text = " ".join([
        workflow_info.get('name', ''),
        workflow_info.get('description', ''),
        " ".join(workflow_info.get('node_types', [])),
        " ".join(workflow_info.get('node_names', [])),
        " ".join(workflow_info.get('tags', []))
    ]).lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in search_text:
                categories.append(category)
                break

    if not categories:
        categories.append("📦 Outros")

    return categories

def main():
    print("=" * 80)
    print("📊 INVENTÁRIO COMPLETO DE WORKFLOWS N8N")
    print("=" * 80)
    print()

    # Encontrar todos os JSONs (excluindo messages.json e metadata.json)
    json_files = []
    for json_path in BASE_DIR.rglob("*.json"):
        if json_path.name not in ['messages.json', 'metadata.json']:
            json_files.append(json_path)

    print(f"📁 Total de arquivos JSON encontrados: {len(json_files)}")
    print()

    # Processar cada workflow
    workflows = []
    errors = []

    for json_path in json_files:
        info = extract_workflow_info(json_path)
        if 'error' in info:
            errors.append(info)
        else:
            info['categories'] = categorize_workflow(info)
            workflows.append(info)

    print(f"✅ Workflows processados com sucesso: {len(workflows)}")
    print(f"❌ Arquivos com erro: {len(errors)}")
    print()

    # Agrupar por categoria
    by_category = defaultdict(list)
    for wf in workflows:
        for cat in wf['categories']:
            by_category[cat].append(wf)

    # Ordenar categorias por quantidade
    sorted_categories = sorted(by_category.items(), key=lambda x: -len(x[1]))

    print("=" * 80)
    print("📂 WORKFLOWS POR CATEGORIA")
    print("=" * 80)
    print()

    for category, wfs in sorted_categories:
        print(f"\n{'='*60}")
        print(f"{category} ({len(wfs)} workflows)")
        print("=" * 60)

        # Ordenar por nome
        wfs_sorted = sorted(wfs, key=lambda x: x['name'].lower())

        for wf in wfs_sorted:
            nodes_preview = ", ".join(wf.get('node_types', [])[:3])
            if len(wf.get('node_types', [])) > 3:
                nodes_preview += "..."
            print(f"  • {wf['name']}")
            print(f"    📁 Pasta: {wf['folder']} | 🔧 Nodes: {wf['node_count']}")
            if wf.get('description'):
                desc = wf['description'][:100] + "..." if len(wf.get('description', '')) > 100 else wf['description']
                print(f"    📝 {desc}")
            print()

    # Resumo estatístico
    print("\n" + "=" * 80)
    print("📈 RESUMO ESTATÍSTICO")
    print("=" * 80)
    print()

    # Contagem por categoria
    print("Workflows por categoria:")
    for category, wfs in sorted_categories:
        print(f"  {category}: {len(wfs)}")

    # Nodes mais usados
    print("\n\nNodes mais utilizados:")
    node_counter = defaultdict(int)
    for wf in workflows:
        for node_type in wf.get('node_types', []):
            node_counter[node_type] += 1

    top_nodes = sorted(node_counter.items(), key=lambda x: -x[1])[:20]
    for node, count in top_nodes:
        # Simplificar nome do node
        simple_name = node.replace('n8n-nodes-base.', '').replace('@n8n/n8n-nodes-langchain.', 'LC:')
        print(f"  {simple_name}: {count}")

    # Salvar dados completos em JSON
    output_data = {
        'total_workflows': len(workflows),
        'total_errors': len(errors),
        'categories': {cat: len(wfs) for cat, wfs in sorted_categories},
        'top_nodes': dict(top_nodes),
        'workflows': workflows,
        'errors': errors
    }

    output_path = Path("/home/nmaldaner/projetos/N8Np/workflow_inventory.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n\n💾 Dados completos salvos em: {output_path}")

if __name__ == "__main__":
    main()
