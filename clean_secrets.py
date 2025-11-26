#!/usr/bin/env python3
"""
Script para remover secrets (API keys, tokens, credenciais) dos workflows n8n
"""

import json
import os
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent
REF_DIR = BASE_DIR / "Ref" / "2494913847"

# Padrões de secrets para remover/limpar
SENSITIVE_FIELDS = [
    'apiKey',
    'api_key',
    'accessToken',
    'access_token',
    'refreshToken',
    'refresh_token',
    'clientSecret',
    'client_secret',
    'password',
    'privateKey',
    'private_key',
    'secret',
    'token',
    'authToken',
    'auth_token',
    'accountSid',
    'account_sid',
]

def clean_credentials(obj):
    """Remove valores sensíveis de credenciais"""
    if isinstance(obj, dict):
        cleaned = {}
        for key, value in obj.items():
            if key == 'credentials':
                # Manter estrutura mas remover IDs sensíveis
                if isinstance(value, dict):
                    cleaned[key] = {}
                    for cred_name, cred_data in value.items():
                        if isinstance(cred_data, dict):
                            cleaned[key][cred_name] = {
                                'id': '[REMOVED]',
                                'name': cred_data.get('name', '[REMOVED]')
                            }
                        else:
                            cleaned[key][cred_name] = '[REMOVED]'
                else:
                    cleaned[key] = '[REMOVED]'
            elif key == 'id' and isinstance(value, str) and len(value) > 10:
                # IDs de credenciais são geralmente strings longas
                cleaned[key] = '[REMOVED]'
            elif any(sensitive in key.lower() for sensitive in SENSITIVE_FIELDS):
                # Campo sensível - limpar valor
                if isinstance(value, str):
                    cleaned[key] = '[REMOVED]'
                elif isinstance(value, dict):
                    cleaned[key] = clean_credentials(value)
                else:
                    cleaned[key] = '[REMOVED]'
            else:
                # Campo normal - processar recursivamente
                cleaned[key] = clean_credentials(value)
        return cleaned
    elif isinstance(obj, list):
        return [clean_credentials(item) for item in obj]
    else:
        return obj

def clean_workflow_file(file_path):
    """Limpa secrets de um arquivo JSON de workflow"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Limpar credenciais nos nodes
        if 'nodes' in data and isinstance(data['nodes'], list):
            for node in data['nodes']:
                if 'credentials' in node:
                    node['credentials'] = clean_credentials(node['credentials'])

                # Limpar parâmetros sensíveis
                if 'parameters' in node:
                    node['parameters'] = clean_credentials(node['parameters'])

        # Salvar arquivo limpo
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True
    except json.JSONDecodeError:
        # Arquivo JSON inválido - pular
        return False
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        return False

def main():
    print("🧹 Limpando secrets dos workflows n8n...\n")

    total_files = 0
    cleaned_files = 0
    skipped_files = 0

    for topico_dir in REF_DIR.iterdir():
        if not topico_dir.is_dir():
            continue

        for json_file in topico_dir.glob("*.json"):
            # Ignorar metadata e messages
            if json_file.name in ['metadata.json', 'messages.json']:
                continue

            total_files += 1

            if clean_workflow_file(json_file):
                cleaned_files += 1
                print(f"✓ Limpo: {json_file.relative_to(BASE_DIR)}")
            else:
                skipped_files += 1
                print(f"⊘ Pulado: {json_file.relative_to(BASE_DIR)}")

    print(f"\n📊 Resumo:")
    print(f"   Total de arquivos: {total_files}")
    print(f"   ✓ Limpos: {cleaned_files}")
    print(f"   ⊘ Pulados: {skipped_files}")
    print(f"\n✅ Secrets removidos com sucesso!")
    print(f"\n💡 Próximo passo:")
    print(f"   git add Ref/")
    print(f"   git commit --amend --no-edit")
    print(f"   git push -u origin main")

if __name__ == "__main__":
    main()
