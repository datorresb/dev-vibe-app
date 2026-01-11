#!/bin/bash
set -e

# Configure GitHub credentials if provided
if [ -n "${GITHUB_USER:-}" ] && [ -n "${GITHUB_TOKEN:-}" ]; then
  echo "Configuring GitHub credentials..."
  printf 'https://%s:%s@github.com\n' "$GITHUB_USER" "$GITHUB_TOKEN" >> "$HOME/.git-credentials"
  chmod 600 "$HOME/.git-credentials" || true

  echo "Configuring git credential helper (store)"
  git config --global credential.helper store
  git config --global credential.useHttpPath true
fi

npm i -g backlog.md

# Install Claude Code CLI (optional - set INSTALL_CLAUDE=true in devcontainer.json)
if [ "${INSTALL_CLAUDE:-false}" = "true" ]; then
  echo "Installing Claude Code CLI..."
  curl -fsSL https://claude.ai/install.sh | bash || echo "Claude CLI installation failed (non-blocking)"
else
  echo "Skipping Claude CLI (set INSTALL_CLAUDE=true to enable)"
fi

echo "postCreate done"