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

# Install Backlog.md CLI (optional)
if [ "${INSTALL_BACKLOG_MD:-false}" = "true" ]; then
  echo "Installing Backlog.md CLI..."
  npm i -g backlog.md
else
  echo "Skipping Backlog.md CLI (set INSTALL_BACKLOG_MD=true to enable)"
fi

# Install Claude Code CLI (optional)
if [ "${INSTALL_CLAUDE:-false}" = "true" ]; then
  echo "Installing Claude Code CLI..."
  curl -fsSL https://claude.ai/install.sh | bash || echo "Claude CLI installation failed (non-blocking)"
else
  echo "Skipping Claude CLI (set INSTALL_CLAUDE=true to enable)"
fi

echo "postCreate done"