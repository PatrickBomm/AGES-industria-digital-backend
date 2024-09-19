#!/bin/bash

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

feat_pattern="^feat/[0-9]+/.+"
fix_pattern="^fix/[0-9]+/.+"
chore_pattern="^chore/[0-9]+/.+"

if [[ $BRANCH_NAME =~ $feature_pattern ]]; then
    echo "Branch name '$BRANCH_NAME' is valid (feature)."
elif [[ $BRANCH_NAME =~ $fix_pattern ]]; then
    echo "Branch name '$BRANCH_NAME' is valid (fix)."
elif [[ $BRANCH_NAME =~ $chore_pattern ]]; then
    echo "Branch name '$BRANCH_NAME' is valid (chore)."
else
    echo "Branch name '$BRANCH_NAME' is invalid. Please follow the naming conventions:"
    echo "feature/id-task/nome-da-feature"
    echo "fix/id-task/nome-do-fix"
    echo "chore/id-task/objetivo-da-atualização"
    exit 1
fi
