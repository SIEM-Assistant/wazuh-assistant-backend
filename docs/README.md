# Documentation of Wazuh Assistant Backend

## Requirements

1. HTTP access to Wazuh Indexer (usually at `:9200`)
2. Wazuh account username and password that has read access to indexer

## Development

1. Python 3.12
2. `pip install -r requirements.txt` (in a virtual env)
3. `pip install fastapi[standard]` (for the fastapi cli)
4. `set -a`
5. `source .env` (in repo root, after copying `sample.env` to `.env` and modifying the values)
6. `fastapi dev app/main.py` (from repo root)

## Production

1. Docker
2. Image `shobanchiddarth/wazuh-assistant-backend:latest`
3. Deploy with required environment variables

