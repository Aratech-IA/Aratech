#!/usr/bin/env bash
docker compose --env-file ../combined-$1.env up -d
