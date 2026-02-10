#!/bin/bash

if [ ! -d "venv" ]; then
  echo "❌ venv não encontrado. Rode: ./scripts/install_deps.sh"
  return 1
fi

echo "🟢 Ambiente virtual ativado"
source venv/bin/activate
