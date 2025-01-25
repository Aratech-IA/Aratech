#!/usr/bin/env bash
docker compose --env-file vitrine-$1.env up -d
