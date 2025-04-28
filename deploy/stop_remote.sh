#!/usr/bin/env bash

# To start the docker compose
docker compose -p aratech-vitrine --env-file ../combined-$1.env -f docker-compose-$1.yaml down
