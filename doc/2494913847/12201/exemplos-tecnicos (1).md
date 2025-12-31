
# Exemplos Técnicos – Agentes e Pipelines IA

Este documento acompanha o pacote de automações e agentes enviados no arquivo `modelos-json.zip`.

---

## 1. agente-atendimento-estilo.json
**Descrição:** Agente com respostas personalizadas no estilo Ferran Tort. Aplica coaching direto, sem listas e com estilo provocativo.
**Ideal para:** Automação de atendimento via WhatsApp ou Telegram.

---

## 2. agente-rag-interativo.json
**Descrição:** RAG com controle estruturado de upload, eliminação e formatação segura de mensagens para Telegram.
**Ideal para:** Atendimento baseado em documentos com regras de formatação.

---

## 3. agente-rag-delete.json
**Descrição:** Pipeline que remove arquivos tanto do Supabase quanto do Google Drive com base no ID do documento.
**Ideal para:** Manutenção de base vetorial RAG.

---

## 4. pipeline-rag-avancado.json
**Descrição:** Pipeline completo que extrai texto de PDF e Excel, resume, e insere no Supabase com tratamento de arquivos e chunks.
**Ideal para:** Processamento automático de grandes volumes de documentos.

---

## 5. agente-rag-semantico.json
**Descrição:** Pipeline RAG com chunking semântico, identificação de hierarquias de seções e mapeamento por índice no texto.
**Ideal para:** Documentação técnica, legal, livros ou regulamentos.

---

## 6. chatbot-multicanal-ftd.json
**Descrição:** Pipeline educacional com fluxo multicanal, embeddings com Pinecone e orientação de aprendizado contínuo.
**Ideal para:** Chatbots educativos com base em conhecimento estruturado.

---

## 7. rag-multimidia-imagens.json
**Descrição:** OCR de arquivos com imagens, gráficos ou tabelas usando Mistral AI + descrição visual + indexação multimodal.
**Ideal para:** PDFs com conteúdo visual complexo.

---

## 8. pipeline-rag-dinamico.json
**Descrição:** Watcher dinâmico que detecta novos arquivos no Google Drive e atualiza automaticamente a base Supabase com embeddings.
**Ideal para:** Atualização contínua de repositórios de conhecimento.

---

## 9. enxame-de-agentes.json
**Descrição:** Agente orquestrador multimodal que recebe entrada por voz ou texto e direciona para subagentes como e-mail, calendário, etc.
**Ideal para:** Atendimento completo via Telegram com entrada multimodal.

---
