#!/bin/bash

# Cria o venv se não existir
if [ ! -d "venv" ]; then
  echo "❌ venv não encontrado. Criando..."
  python3 -m venv venv
fi

# Ativa o venv
source venv/bin/activate
echo "🟢 Ambiente virtual ativado"

# Atualiza pip
pip install --upgrade pip

# Instala todas as dependências
pip install -r requirements.txt

echo "✅ Todas as dependências foram instaladas!"
