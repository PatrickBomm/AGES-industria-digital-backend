#!/bin/bash

# Get the commit message
COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Define the Conventional Commit pattern
commit_regex="^(feat|fix|docs|style|refactor|test|chore)(\([a-zA-Z0-9-]+\))?: [A-Z].{0,72}$"

error_msg="Commit message does not follow Conventional Commits guidelines:
Type(scope): Description (max 75 chars)
Examples:
  feat(1234): Adiciona a funcionalidade de busca por nome de usuário
  fix(5678): Corrige o erro de carregamento na página inicial
"

# Check if the commit message matches the pattern
if ! [[ "$COMMIT_MSG" =~ $commit_regex ]]; then
  echo "$error_msg"
  exit 1
fi
