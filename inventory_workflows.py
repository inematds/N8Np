#!/usr/bin/env python3
"""
Inventario completo de workflows n8n do repositorio N8Np
Suporta multiplas fontes de workflows
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

# Diretorio base
BASE_DIR = Path("/home/nmaldaner/projetos/N8Np/doc")

# Fontes de workflows
SOURCES = {
    "n8np": {
        "name": "N8Np VIP",
        "path": "2494913847",
        "badge": "VIP",
        "color": "#f59e0b",
        "telegram": True,
        "github": None
    },
    "zengfr": {
        "name": "zengfr",
        "path": "zengfr",
        "badge": None,
        "color": "#3b82f6",
        "telegram": False,
        "github": "https://github.com/zengfr/n8n-workflow-all-templates"
    },
    "zie619": {
        "name": "zie619",
        "path": "zie619",
        "badge": None,
        "color": "#22c55e",
        "telegram": False,
        "github": "https://github.com/Zie619/n8n-workflows"
    },
    "danitilahun": {
        "name": "danitilahun",
        "path": "danitilahun",
        "badge": None,
        "color": "#a855f7",
        "telegram": False,
        "github": "https://github.com/Danitilahun/n8n-workflow-templates"
    },
    "wassupjay": {
        "name": "wassupjay",
        "path": "wassupjay",
        "badge": "AI",
        "color": "#ec4899",
        "telegram": False,
        "github": "https://github.com/wassupjay/n8n-free-templates"
    },
    "enescingoz": {
        "name": "enescingoz",
        "path": "enescingoz",
        "badge": "AI",
        "color": "#f97316",
        "telegram": False,
        "github": "https://github.com/enescingoz/awesome-n8n-templates"
    }
}

# Categorias baseadas em palavras-chave e nodes
CATEGORIES = {
    "AI Agents & RAG": [
        "agent", "rag", "llm", "openai", "claude", "anthropic", "gpt",
        "chatbot", "ai", "embedding", "vector", "langchain", "memory",
        "deepseek", "gemini", "perplexity", "groq"
    ],
    "WhatsApp & Telegram": [
        "whatsapp", "telegram", "evolution", "baileys", "waha", "z-api"
    ],
    "Email & Comunicacao": [
        "email", "gmail", "smtp", "imap", "outlook", "newsletter", "mail"
    ],
    "Planilhas & Dados": [
        "sheets", "excel", "airtable", "notion", "spreadsheet", "csv",
        "database", "supabase", "postgres", "mysql", "mongodb"
    ],
    "Video & Midia": [
        "video", "youtube", "vimeo", "ffmpeg", "media", "image", "audio",
        "tiktok", "reels", "shorts", "veo", "heygen", "runway"
    ],
    "Integracoes & APIs": [
        "api", "webhook", "http", "rest", "graphql", "integration"
    ],
    "Redes Sociais": [
        "instagram", "linkedin", "twitter", "facebook", "social", "bluesky",
        "x post", "tiktok"
    ],
    "Produtividade & Calendario": [
        "calendar", "calendly", "schedule", "task", "todo", "trello",
        "asana", "clickup", "notion"
    ],
    "Vendas & CRM": [
        "crm", "sales", "lead", "hubspot", "pipedrive", "customer",
        "client", "invoice", "payment"
    ],
    "Automacao & Utilidades": [
        "automation", "workflow", "trigger", "loop", "batch", "error",
        "backup", "sync", "monitor"
    ],
    "Web Scraping & Extracao": [
        "scrape", "scraping", "crawl", "extract", "firecrawl", "apify",
        "browser", "puppeteer", "playwright"
    ],
    "Documentos & Conteudo": [
        "document", "pdf", "doc", "content", "text", "write", "blog",
        "article", "post", "gamma"
    ]
}

# Arquivos a ignorar
IGNORE_FILES = {'messages.json', 'metadata.json', 'package.json', 'package-lock.json', 'tsconfig.json'}

def extract_workflow_info(json_path, source_id, source_info):
    """Extrai informacoes de um arquivo de workflow n8n"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Verificar se e um workflow n8n valido (tem nodes)
        nodes = data.get('nodes', [])
        if not nodes and not isinstance(data, dict):
            return None

        # Pegar nome do workflow
        name = data.get('name', json_path.stem)
        if not name or name == '':
            name = json_path.stem

        node_types = set()
        node_names = []

        for node in nodes:
            node_type = node.get('type', '')
            node_name = node.get('name', '')
            if node_type:
                node_types.add(node_type)
            if node_name:
                node_names.append(node_name)

        # Descricao se houver
        description = data.get('description', '') or ''

        # Tags se houver
        tags = data.get('tags', []) or []
        if isinstance(tags, list):
            clean_tags = []
            for t in tags:
                if isinstance(t, dict):
                    clean_tags.append(str(t.get('name', '')))
                elif isinstance(t, str):
                    clean_tags.append(t)
                else:
                    clean_tags.append(str(t))
            tags = [tag for tag in clean_tags if tag]

        # Buscar imagens na mesma pasta (so para n8np)
        images = []
        thumbnail = None
        if source_id == 'n8np':
            folder = json_path.parent
            for img in folder.glob("*.jpg"):
                rel_path = str(img).replace("/home/nmaldaner/projetos/N8Np/", "")
                images.append(rel_path)
            for img in folder.glob("*.png"):
                rel_path = str(img).replace("/home/nmaldaner/projetos/N8Np/", "")
                images.append(rel_path)
            images.sort()
            thumbnail = images[0] if images else None

        # Caminho relativo
        rel_path = str(json_path).replace("/home/nmaldaner/projetos/N8Np/", "")

        # Folder ID (para link do telegram)
        folder_id = json_path.parent.name

        return {
            'name': name,
            'file': json_path.name,
            'folder': folder_id,
            'path': str(json_path),
            'rel_path': rel_path,
            'source': source_id,
            'source_name': source_info['name'],
            'source_color': source_info['color'],
            'source_badge': source_info['badge'],
            'source_github': source_info['github'],
            'has_telegram': source_info['telegram'],
            'node_types': list(node_types),
            'node_names': node_names,
            'node_count': len(nodes),
            'description': description[:500] if description else '',
            'tags': tags,
            'images': images,
            'thumbnail': thumbnail
        }
    except Exception as e:
        return None

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
        categories.append("Outros")

    return categories

def main():
    print("=" * 80)
    print("INVENTARIO MULTI-FONTE DE WORKFLOWS N8N")
    print("=" * 80)
    print()

    all_workflows = []
    errors = []
    source_stats = {}

    # Processar cada fonte
    for source_id, source_info in SOURCES.items():
        source_path = BASE_DIR / source_info['path']

        if not source_path.exists():
            print(f"[SKIP] {source_info['name']}: diretorio nao encontrado")
            continue

        print(f"\n[PROCESSANDO] {source_info['name']} ({source_path})")

        # Encontrar todos os JSONs
        json_files = []
        for json_path in source_path.rglob("*.json"):
            if json_path.name not in IGNORE_FILES:
                # Ignorar arquivos em .git
                if '.git' not in str(json_path):
                    json_files.append(json_path)

        print(f"  Arquivos JSON encontrados: {len(json_files)}")

        source_workflows = 0
        source_errors = 0

        for json_path in json_files:
            info = extract_workflow_info(json_path, source_id, source_info)
            if info and info.get('node_count', 0) > 0:
                info['categories'] = categorize_workflow(info)
                all_workflows.append(info)
                source_workflows += 1
            elif info is None:
                source_errors += 1

        source_stats[source_id] = {
            'name': source_info['name'],
            'total': source_workflows,
            'errors': source_errors,
            'color': source_info['color'],
            'badge': source_info['badge']
        }

        print(f"  Workflows validos: {source_workflows}")
        print(f"  Erros/ignorados: {source_errors}")

    print("\n" + "=" * 80)
    print(f"TOTAL: {len(all_workflows)} workflows processados")
    print("=" * 80)

    # Agrupar por categoria
    by_category = defaultdict(int)
    for wf in all_workflows:
        for cat in wf['categories']:
            by_category[cat] += 1

    # Nodes mais usados
    node_counter = defaultdict(int)
    for wf in all_workflows:
        for node_type in wf.get('node_types', []):
            node_counter[node_type] += 1

    top_nodes = dict(sorted(node_counter.items(), key=lambda x: -x[1])[:50])

    # Salvar dados completos em JSON
    output_data = {
        'total_workflows': len(all_workflows),
        'sources': source_stats,
        'categories': dict(sorted(by_category.items(), key=lambda x: -x[1])),
        'top_nodes': top_nodes,
        'workflows': all_workflows
    }

    output_path = Path("/home/nmaldaner/projetos/N8Np/workflow_inventory.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nDados salvos em: {output_path}")

    # Resumo por fonte
    print("\n" + "=" * 80)
    print("RESUMO POR FONTE")
    print("=" * 80)
    for source_id, stats in source_stats.items():
        print(f"  {stats['name']}: {stats['total']} workflows")

    # Resumo por categoria
    print("\n" + "=" * 80)
    print("RESUMO POR CATEGORIA")
    print("=" * 80)
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")

if __name__ == "__main__":
    main()
