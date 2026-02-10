#!/bin/bash

if [ ! -d "venv" ]; then
  echo "❌ venv não encontrado. Crie com: python3 -m venv venv"
  return 1
fi

echo "🟢 Ambiente virtual ativado"
source venv/bin/activate
