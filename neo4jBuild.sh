#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./build.sh <tag-name>"
  exit 1
fi

TAG=$1

docker build $(grep -v '^#' .env | sed 's/^/--build-arg /') -f app/mcp/mcp-ne4j-memory/Dockerfile -t "$TAG" .
