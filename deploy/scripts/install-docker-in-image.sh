#!/usr/bin/env bash
set -euo pipefail

apt-get update
apt-get install -y --no-install-recommends git ca-certificates docker.io
rm -rf /var/lib/apt/lists/*

if getent group docker >/dev/null 2>&1; then
  usermod -aG docker jenkins || true
fi
