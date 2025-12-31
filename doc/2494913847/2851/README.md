# Workflow de Geração de Músicas

## Descrição
Este é um workflow do n8n que automatiza a criação de músicas usando a API da PiAPI e as envia para uma pasta específica no Google Drive. O workflow é ideal para quem precisa de trilhas sonoras originais para Reels, vídeos ou outros conteúdos digitais.

## Funcionalidades

- Geração automática de música baseada em um prompt de estilo
- Monitoramento do status de processamento da música
- Download automático do áudio gerado
- Upload para uma pasta específica no Google Drive
- Lógica de repetição para verificar o status até a conclusão

## Requisitos

1. **Conta no n8n** (pode ser auto-hospedado ou n8n.cloud)
2. **Credenciais da PiAPI**
   - Crie uma conta em [PiAPI](https://piapi.ai/)
   - Obtenha sua chave de API
3. **Acesso ao Google Drive**
   - Configure as credenciais do Google Drive no n8n
   - Tenha o ID da pasta de destino no Google Drive

## Como Usar

1. **Importe o workflow** para o seu n8n
2. **Configure as credenciais**:
   - Adicione suas credenciais da PiAPI
   - Configure o acesso ao Google Drive
   - Atualize o ID da pasta de destino no Google Drive

3. **Personalize o prompt de estilo** (opcional):
   - O prompt padrão já está configurado para criar uma música suave e etérea
   - Você pode modificar o campo `style_prompt` para alterar o estilo da música

4. **Execute o workflow**:
   - Você pode executar manualmente (usando o nó de trigger manual)
   - Ou agendar execuções regulares (usando o Schedule Trigger)

## Estrutura do Workflow

1. **Gerar Música**
   - Envia uma requisição para a API da PiAPI com o prompt de estilo
   
2. **Busca Música Gerada**
   - Verifica o status da tarefa de geração de áudio
   
3. **Lógica de Verificação**
   - Se a música estiver pronta, faz o download
   - Se ainda estiver processando, aguarda 20 segundos e tenta novamente
   
4. **Download da Música**
   - Baixa o arquivo de áudio gerado
   
5. **Upload para o Google Drive**
   - Envia o arquivo para a pasta configurada

## Configuração das Credenciais

### PiAPI
1. Acesse https://piapi.ai/
2. Crie uma conta e obtenha sua chave de API
3. No n8n, adicione as credenciais HTTP Header Auth

### Google Drive
1. No n8n, adicione as credenciais do Google Drive OAuth2
2. Siga o fluxo de autenticação do Google
3. Copie o ID da pasta de destino no Google Drive

## Personalização

### Alterar o Estilo da Música
Para modificar o estilo da música gerada, edite o campo `style_prompt` no nó "Gerar Música".

### Agendamento
Para executar o workflow automaticamente em horários específicos, configure o nó "Schedule Trigger" de acordo com suas necessidades.

## Solução de Problemas

- **Erro de autenticação**: Verifique se as credenciais da PiAPI e do Google Drive estão corretas
- **Tempo de processamento**: Dependendo da carga da API, a geração da música pode levar alguns minutos
- **Limites da API**: Verifique os limites de uso da sua conta na PiAPI

## Segurança

- Nunca compartilhe suas chaves de API
- Mantenha suas credenciais em variáveis de ambiente ou no gerenciador de credenciais do n8n
- Revise as permissões concedidas ao aplicativo do Google Drive

## Suporte

Para suporte ou dúvidas, abra uma issue no repositório ou consulte a documentação do n8n.
