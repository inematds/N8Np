# N8Np - Sistema Multi-Fonte de Workflows n8n

## Visao Geral

O N8Np agrega workflows n8n de multiplas fontes em um unico sistema de busca e navegacao.

## Fontes de Workflows

| Fonte | Repositorio | Workflows | Tipo |
|-------|-------------|-----------|------|
| **N8Np VIP** | Local (Telegram) | 519 | Exclusivo/Curado |
| **zengfr** | github.com/zengfr/n8n-workflow-all-templates | 7.299 | Maior colecao |
| **zie619** | github.com/Zie619/n8n-workflows | 2.064 | Colecao ampla |
| **danitilahun** | github.com/Danitilahun/n8n-workflow-templates | 2.043 | Organizado |
| **wassupjay** | github.com/wassupjay/n8n-free-templates | 202 | Foco em AI/RAG |
| **enescingoz** | github.com/enescingoz/awesome-n8n-templates | 280 | AI-powered |

**Total: 12.407 workflows**

## Estrutura de Diretorios

```
N8Np/
├── doc/
│   ├── 2494913847/          # N8Np VIP (Telegram)
│   ├── zengfr/              # zengfr collection
│   ├── zie619/              # zie619 collection
│   ├── danitilahun/         # danitilahun collection
│   ├── wassupjay/           # wassupjay collection
│   └── enescingoz/          # enescingoz collection
├── index.html               # UI principal com menu de fontes
├── inventory_workflows.py   # Script de inventario multi-fonte
├── workflow_inventory.json  # Indice unificado de todos workflows
├── SOURCES.md              # Este arquivo
└── CLAUDE.md               # Instrucoes do projeto
```

## Arquitetura do Sistema

### 1. Coleta de Dados
- Cada fonte eh clonada/baixada para `doc/[fonte]/`
- Workflows sao arquivos JSON do n8n
- Mantemos copia local para garantir disponibilidade

### 2. Processamento
- `inventory_workflows.py` processa todas as fontes
- Extrai: nome, nodes, categorias, tags, imagens
- Gera `workflow_inventory.json` unificado

### 3. Interface (index.html)
- Menu de fontes (tabs ou dropdown)
- Filtro por categoria
- Filtro por modulos/nodes
- Busca textual
- Cards com thumbnails
- Modal com detalhes e galeria

### 4. Diferenciais por Fonte

| Fonte | Badge | Cor | Link Externo |
|-------|-------|-----|--------------|
| N8Np VIP | VIP | Dourado | Telegram |
| zengfr | - | Azul | GitHub |
| zie619 | - | Verde | GitHub |
| danitilahun | - | Roxo | GitHub |
| wassupjay | AI | Rosa | GitHub |
| enescingoz | AI | Laranja | GitHub |

## Atualizacao

Para atualizar as fontes:

```bash
# Atualizar repos externos
cd doc/zengfr && git pull
cd doc/zie619 && git pull
cd doc/danitilahun && git pull
cd doc/wassupjay && git pull
cd doc/enescingoz && git pull

# Regenerar inventario
python3 inventory_workflows.py
```

## Licencas

- N8Np VIP: Proprietario (acesso via Telegram)
- zengfr: Verificar repositorio original
- zie619: MIT License
- danitilahun: Verificar repositorio original
- wassupjay: Verificar repositorio original
- enescingoz: Verificar repositorio original

## Links

- GitHub N8Np: https://github.com/inematds/N8Np
- GitHub Pages: https://inematds.github.io/N8Np/
- Telegram VIP: https://t.me/c/2494913847/
