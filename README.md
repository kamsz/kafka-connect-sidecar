# Kafka Connect Sidecar

Purpose of this container is to constantly watch and create/update connector definitions from a directory. Super useful with Kubernetes ConfigMaps.

## Configuration

This container will look for *.json files in /connectors directory. Then it'll either create or update connectors every 60 seconds.
