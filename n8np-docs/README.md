# 📚 N8Np Documentation Site

Site de documentação gerado automaticamente com **MkDocs Material** para a biblioteca de workflows n8n.

## 🚀 Como Usar

### Visualizar Localmente

```bash
cd n8np-docs
mkdocs serve
```

Acesse: http://127.0.0.1:8000

### Gerar Site Estático

```bash
cd n8np-docs
mkdocs build
```

Os arquivos HTML serão gerados em `site/`

## 📤 Deploy

### GitHub Pages

```bash
cd n8np-docs
mkdocs gh-deploy
```

Isso irá:
1. Fazer build do site
2. Criar/atualizar branch `gh-pages`
3. Fazer push para GitHub
4. Site disponível em: `https://[seu-usuario].github.io/N8Np/`

### Netlify

1. Conecte seu repositório ao Netlify
2. Configurações de build:
   - **Build command:** `cd n8np-docs && mkdocs build`
   - **Publish directory:** `n8np-docs/site`

### Vercel

1. Conecte seu repositório ao Vercel
2. Configurações de build:
   - **Build command:** `cd n8np-docs && pip install mkdocs mkdocs-material && mkdocs build`
   - **Output directory:** `n8np-docs/site`

## 🔄 Atualizar Conteúdo

Se novos workflows forem adicionados em `Ref/`, execute:

```bash
python3 generate_docs.py
```

Isso irá:
- Escanear todos os workflows
- Categorizar automaticamente
- Gerar páginas markdown atualizadas
- Atualizar índices

## 📁 Estrutura

```
n8np-docs/
├── mkdocs.yml          # Configuração do MkDocs
├── docs/               # Conteúdo markdown
│   ├── index.md       # Página inicial
│   ├── workflows/     # Categorias de workflows
│   ├── curso/         # The Ultimate n8n Course
│   ├── topicos/       # Conversas da comunidade
│   └── about.md       # Sobre
└── site/              # Site gerado (após build)
```

## ⚙️ Personalização

### Alterar Tema

Edite `mkdocs.yml`:

```yaml
theme:
  palette:
    primary: blue  # Cores: red, pink, purple, indigo, blue, etc
    accent: cyan
```

### Adicionar Páginas

1. Crie arquivo `.md` em `docs/`
2. Adicione à navegação em `mkdocs.yml`:

```yaml
nav:
  - Nova Página: nova-pagina.md
```

## 🔍 Busca

A busca funciona automaticamente em:
- Português
- Inglês
- Conteúdo de todos os arquivos markdown

## 📊 Estatísticas

- **532 workflows** catalogados
- **198 AI Agents**
- **6 categorias** automáticas
- **420 tópicos** da comunidade
- **23 lições** do curso

## 🛠️ Tecnologias

- [MkDocs](https://www.mkdocs.org/) - Gerador de sites
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - Tema profissional
- Python 3.13+ - Script de geração

## 📝 License

Conteúdo compartilhado pela comunidade N8Np.
