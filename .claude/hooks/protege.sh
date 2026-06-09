#!/usr/bin/env bash
# Bloqueia escrita em data/ e em arquivos da versão preservada.
payload="$(cat)"; path="$(echo "$payload" | grep -oE '"file_path"[^,]*' | head -1)"
case "$path" in
  *"/data/"*|*"entrega-12-submetida"*) echo "BLOQUEADO: caminho protegido ($path)"; exit 2;;
esac
exit 0
