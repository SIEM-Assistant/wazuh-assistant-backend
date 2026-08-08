import os
import requests
import urllib3

from fastapi import HTTPException






def indexer_proxy(query: dict) -> dict:
    """\
    - payload must be the json DQL query for opensearch

    this functon is to be used for querying the indexer from other functions
    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = f"{os.environ["WAZUH_INDEXER_HOST"]}/wazuh-alerts-*/_search"

    username = os.environ["WAZUH_USERNAME"]
    password = os.environ["WAZUH_PASSWORD"]

    response = requests.post(
        url,
        auth=(username, password),
        headers = {
            "Content-Type": "application/json"
        },
        json=query,
        verify=False
    )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
        return
    
    return response.json()
