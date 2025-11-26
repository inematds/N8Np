# 🏥 Guia de Instalação - Sistema de Automação para Farmácia de Manipulação

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Requisitos](#requisitos)
3. [Instalação Rápida](#instalação-rápida)
4. [Configuração Detalhada](#configuração-detalhada)
5. [Importação dos Workflows](#importação-dos-workflows)
6. [Configuração de Integrações](#configuração-de-integrações)
7. [Testes e Validação](#testes-e-validação)
8. [Troubleshooting](#troubleshooting)
9. [Manutenção](#manutenção)
10. [Segurança](#segurança)

---

## 🎯 Visão Geral

Este sistema automatiza completamente o processo de recebimento e processamento de receitas médicas para farmácias de manipulação, incluindo:

- ✅ Recepção multi-canal (WhatsApp, Email, Web)
- ✅ OCR e extração inteligente de medicamentos
- ✅ Cálculo automático de orçamentos
- ✅ Envio de propostas com botões interativos
- ✅ Gestão de produção integrada
- ✅ Relatórios e monitoramento em tempo real

### Arquitetura do Sistema

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   WhatsApp      │     │     Email       │     │   Web Form      │
│  (Evolution)    │     │    (IMAP)       │     │   (Webhook)     │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                         │
         └───────────────────────┴─────────────────────────┘
                                 │
                        ┌────────▼────────┐
                        │   n8n Engine    │
                        │  (Workflows)    │
                        └────────┬────────┘
                                 │
         ┌───────────────────────┴─────────────────────────┐
         │                       │                         │
┌────────▼────────┐     ┌────────▼────────┐     ┌────────▼────────┐
│   PostgreSQL    │     │     Redis       │     │   Storage       │
│   (Database)    │     │    (Cache)      │     │  (Files/S3)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## 💻 Requisitos

### Hardware Mínimo (Desenvolvimento)
- **CPU**: 2 cores
- **RAM**: 4GB
- **Disco**: 20GB SSD
- **Rede**: 10 Mbps

### Hardware Recomendado (Produção)
- **CPU**: 4+ cores
- **RAM**: 8GB+
- **Disco**: 100GB SSD
- **Rede**: 100 Mbps

### Software
- **Docker**: 20.10+
- **Docker Compose**: 2.0+
- **Node.js**: 18+ (se instalação manual)
- **PostgreSQL**: 14+
- **Redis**: 7+

### Contas e APIs Necessárias
- ✅ Evolution API (WhatsApp)
- ✅ Conta Google (Gmail + Vision API)
- ✅ AWS (Textract - opcional)
- ✅ OpenAI API
- ✅ Slack (notificações)
- ✅ Trello ou Notion (gestão)

---

## 🚀 Instalação Rápida

### Opção 1: Docker Compose (Recomendado)

1. **Clone o repositório**
```bash
git clone https://github.com/sua-farmacia/automacao.git
cd automacao
```

2. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
nano .env
```

3. **Inicie os containers**
```bash
docker-compose up -d
```

4. **Aguarde a inicialização**
```bash
docker-compose logs -f n8n
```

5. **Acesse o n8n**
```
http://localhost:5678
Usuário: admin
Senha: farmacia2024
```

### Opção 2: Instalação Manual

1. **Instale o PostgreSQL**
```bash
sudo apt update
sudo apt install postgresql-14 postgresql-contrib
sudo -u postgres createuser farmacia_user
sudo -u postgres createdb farmacia_db -O farmacia_user
```

2. **Instale o Redis**
```bash
sudo apt install redis-server
sudo systemctl enable redis-server
```

3. **Instale o n8n**
```bash
npm install -g n8n
```

4. **Configure o banco de dados**
```bash
psql -U farmacia_user -d farmacia_db -f farmacia_database_schema.sql
```

5. **Configure as variáveis de ambiente**
```bash
export DB_TYPE=postgresdb
export DB_POSTGRESDB_HOST=localhost
export DB_POSTGRESDB_DATABASE=n8n_farmacia
# ... outras variáveis
```

6. **Inicie o n8n**
```bash
n8n start
```

---

## ⚙️ Configuração Detalhada

### 1. Banco de Dados PostgreSQL

1. **Execute o schema**
```sql
psql -U farmacia_user -d farmacia_db < farmacia_database_schema.sql
```

2. **Verifique as tabelas**
```sql
\dt
```

3. **Configure backup automático**
```bash
# Crie o script de backup
cat > /opt/farmacia/backup.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U farmacia_user farmacia_db > /backup/farmacia_$DATE.sql
find /backup -name "*.sql" -mtime +30 -delete
EOF

chmod +x /opt/farmacia/backup.sh

# Adicione ao crontab
crontab -e
0 2 * * * /opt/farmacia/backup.sh
```

### 2. Evolution API (WhatsApp)

1. **Configure a instância**
```bash
curl -X POST https://api.evolution.com/instance/create \
  -H "apikey: sua-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "instanceName": "farmacia-instance",
    "qrcode": true,
    "webhook": {
      "url": "https://n8n.farmacia.com/webhook/farmacia-receitas",
      "events": ["messages.upsert", "connection.update"]
    }
  }'
```

2. **Conecte o WhatsApp**
- Acesse o painel Evolution
- Escaneie o QR Code
- Verifique a conexão

### 3. Configuração de Email

1. **Gmail - Gere senha de app**
- Acesse: https://myaccount.google.com/apppasswords
- Crie uma senha específica
- Use no SMTP/IMAP

2. **Configure pastas IMAP**
```javascript
// No Gmail, crie as labels:
- Receitas
- Processadas
- Erro
```

### 4. APIs de OCR

#### Google Vision
1. Crie um projeto no Google Cloud
2. Ative a Vision API
3. Crie uma conta de serviço
4. Baixe o JSON de credenciais
5. Configure o caminho no n8n

#### AWS Textract
1. Crie um usuário IAM
2. Anexe a política `AmazonTextractFullAccess`
3. Gere access key e secret
4. Configure no n8n

---

## 📥 Importação dos Workflows

### 1. Prepare o n8n

1. **Acesse o n8n**
```
http://localhost:5678
```

2. **Configure as credenciais**
- Vá em Settings > Credentials
- Adicione todas as credenciais do arquivo `farmacia_credentials.json`

### 2. Importe os Workflows

1. **Workflow Principal**
- Clique em "Import from File"
- Selecione `farmacia_workflow_principal.json`
- Revise e ative

2. **Workflow de Resposta**
- Importe `farmacia_workflow_resposta.json`
- Configure o webhook URL
- Ative o workflow

3. **Workflow de Relatórios**
- Importe `farmacia_workflow_relatorios.json`
- Ajuste os horários se necessário
- Ative o workflow

4. **Workflow de Monitoramento**
- Importe `farmacia_workflow_monitoramento.json`
- Configure os alertas
- Ative o workflow

### 3. Configure os Webhooks

1. **Evolution API**
```bash
curl -X PUT https://api.evolution.com/webhook/set \
  -H "apikey: sua-api-key" \
  -d '{
    "url": "https://n8n.farmacia.com/webhook/farmacia-receitas",
    "webhook_by_events": true,
    "events": [
      "messages.upsert",
      "messages.update",
      "connection.update"
    ]
  }'
```

2. **Frontend/Formulário Web**
```javascript
// Configure seu formulário para POST em:
https://n8n.farmacia.com/webhook/farmacia-receitas

// Formato esperado:
{
  "source": "web",
  "client": {
    "name": "Nome do Cliente",
    "email": "email@cliente.com",
    "phone": "11999999999"
  },
  "files": ["base64_da_imagem"],
  "message": "Mensagem adicional"
}
```

---

## 🔌 Configuração de Integrações

### Slack

1. **Crie um App Slack**
- Acesse: https://api.slack.com/apps
- Crie novo app
- Adicione OAuth scopes: `chat:write`, `files:write`
- Instale no workspace

2. **Configure os canais**
```
#farmacia-notificacoes - Notificações gerais
#farmacia-alertas - Alertas do sistema
#farmacia-operacoes - Filas e pedidos
#farmacia-relatorios - Relatórios diários
#farmacia-metricas - KPIs e métricas
```

### Trello

1. **Crie o board**
- Nome: "Produção Farmácia"
- Listas: Pendente, Em Produção, Pronto, Entregue

2. **Configure automações**
```javascript
// Power-Ups recomendados:
- Butler (automações)
- Calendar (prazos)
- Custom Fields (dados extras)
```

### Notion

1. **Crie o database**
- Tipo: Table
- Propriedades necessárias:
  - Status (Select)
  - Cliente (Text)
  - Telefone (Phone)
  - Valor (Number)
  - Prazo (Date)
  - Farmacêutico (Person)

---

## 🧪 Testes e Validação

### 1. Teste de Recepção

#### WhatsApp
```bash
# Envie uma mensagem de teste
"Olá, gostaria de fazer um orçamento"

# Envie uma imagem de receita
[Anexe uma imagem JPG/PNG]
```

#### Email
```bash
# Envie para: farmacia@seudominio.com
# Assunto: Orçamento Receita
# Anexo: receita.pdf
```

### 2. Teste de OCR

1. **Prepare imagens de teste**
- Receita clara (boa qualidade)
- Receita com ruído
- Receita manuscrita
- PDF multipáginas

2. **Verifique extração**
```sql
SELECT 
  order_id,
  medication_count,
  extracted_text,
  budget_data
FROM receitas
ORDER BY created_at DESC
LIMIT 5;
```

### 3. Teste de Resposta

1. **Simule aprovação**
```bash
curl -X POST https://n8n.farmacia.com/webhook/farmacia-responses \
  -H "Content-Type: application/json" \
  -d '{
    "action": "approve",
    "orderId": "PED-xxxxx",
    "source": "test"
  }'
```

### 4. Teste de Carga

```bash
# Instale o Apache Bench
apt-get install apache2-utils

# Teste com 100 requests
ab -n 100 -c 10 -p test_payload.json \
   -T application/json \
   https://n8n.farmacia.com/webhook/farmacia-receitas
```

---

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. WhatsApp não conecta
```bash
# Verifique o status
curl https://api.evolution.com/instance/connectionState/farmacia-instance \
  -H "apikey: sua-api-key"

# Reinicie a instância
curl -X POST https://api.evolution.com/instance/restart/farmacia-instance \
  -H "apikey: sua-api-key"
```

#### 2. OCR falhando
```javascript
// Verifique as credenciais
// No n8n, teste manualmente:
Settings > Credentials > Test Connection

// Verifique os logs
docker logs n8n-farmacia | grep -i error
```

#### 3. Emails não chegam
```bash
# Teste IMAP
openssl s_client -connect imap.gmail.com:993
# LOGIN email@gmail.com senha
# SELECT INBOX
# LOGOUT

# Verifique pasta spam
# Adicione farmacia@dominio.com aos contatos
```

#### 4. Banco de dados lento
```sql
-- Analise queries lentas
SELECT 
  query,
  mean_exec_time,
  calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Reindexe se necessário
REINDEX DATABASE farmacia_db;
```

### Logs e Diagnóstico

1. **Ative logs detalhados**
```bash
export N8N_LOG_LEVEL=debug
n8n start
```

2. **Monitore em tempo real**
```bash
# Todos os logs
docker-compose logs -f

# Apenas n8n
docker logs -f n8n-farmacia --tail 100

# Apenas erros
docker logs n8n-farmacia 2>&1 | grep ERROR
```

3. **Verifique métricas**
```bash
# CPU e Memória
docker stats n8n-farmacia

# Espaço em disco
df -h /var/n8n/farmacia/storage
```

---

## 🛡️ Segurança

### 1. Configurações Essenciais

```bash
# Firewall
ufw allow 22/tcp
ufw allow 443/tcp
ufw allow from 10.0.0.0/8 to any port 5432
ufw enable

# Fail2ban
apt-get install fail2ban
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
systemctl enable fail2ban
```

### 2. SSL/TLS

```bash
# Certbot para HTTPS
apt-get install certbot
certbot certonly --standalone -d n8n.farmacia.com.br

# Auto-renovação
crontab -e
0 2 * * 1 certbot renew --quiet
```

### 3. Backup e Recuperação

```bash
# Backup completo
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/farmacia/$DATE"

mkdir -p $BACKUP_DIR

# Database
pg_dump -U farmacia_user farmacia_db > $BACKUP_DIR/database.sql

# n8n data
tar -czf $BACKUP_DIR/n8n-data.tar.gz /var/n8n/.n8n

# Storage files
tar -czf $BACKUP_DIR/storage.tar.gz /var/n8n/farmacia/storage

# Upload para S3
aws s3 sync $BACKUP_DIR s3://farmacia-backups/$DATE/
```

### 4. Monitoramento de Segurança

```bash
# Instale OSSEC
wget -q -O - https://updates.atomicorp.com/installers/atomic | sh
yum install ossec-hids ossec-hids-server

# Configure alertas
nano /var/ossec/etc/ossec.conf
```

---

## 📅 Manutenção

### Diária
- ✅ Verificar logs de erro
- ✅ Monitorar filas pendentes
- ✅ Conferir espaço em disco

### Semanal
- ✅ Revisar relatórios de performance
- ✅ Atualizar medicamentos e preços
- ✅ Limpar arquivos temporários

### Mensal
- ✅ Atualizar sistema e dependências
- ✅ Revisar e otimizar queries
- ✅ Testar recuperação de backup
- ✅ Auditar acessos e segurança

### Scripts de Manutenção

```bash
# Limpeza de arquivos antigos
find /var/n8n/farmacia/storage -name "*.tmp" -mtime +7 -delete

# Vacuum do PostgreSQL
psql -U farmacia_user -d farmacia_db -c "VACUUM ANALYZE;"

# Limpeza de logs
journalctl --vacuum-time=30d

# Restart semanal (domingo 3h)
0 3 * * 0 docker-compose restart
```

---

## 📞 Suporte

### Documentação Adicional
- n8n: https://docs.n8n.io
- Evolution API: https://doc.evolution-api.com
- PostgreSQL: https://www.postgresql.org/docs/14/

### Comunidade
- Slack: farmacia-dev.slack.com
- Discord: discord.gg/farmacia-automation
- Forum: forum.farmacia-automation.com

### Contato Direto
- **Email**: suporte@farmacia-automation.com
- **WhatsApp**: +55 11 99999-9999
- **Horário**: Seg-Sex 9h-18h

---

## 🎯 Próximos Passos

1. **Configure as integrações** seguindo este guia
2. **Importe os workflows** na ordem correta
3. **Execute os testes** de validação
4. **Configure o monitoramento** e alertas
5. **Treine a equipe** no uso do sistema
6. **Monitore as métricas** nos primeiros dias
7. **Ajuste conforme necessário**

**Lembre-se**: Este é um sistema em produção. Sempre teste em ambiente de desenvolvimento antes de aplicar mudanças!

---

*Última atualização: Dezembro 2024*
*Versão: 1.0.0*