import os
import json
import requests
import urllib3

from fastapi import HTTPException

from . import llm_router

from .models import GenerateQueryRequest, GenerateQueryResponse



def indexer_proxy(query: dict) -> dict:
    """\
    - payload must be the json DSL query for opensearch

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


def generate_query(payload: GenerateQueryRequest) -> GenerateQueryResponse:
    """\
    - user_prompt: must be prompt from user (SOC Analyst)
    """

    user_prompt = payload.user_prompt

    raw_response = llm_router.singular_message(user_prompt=user_prompt)
    # removing the first and last line markdown code block ```
    lines = raw_response.split("\n")[1:][:-1]
    response = "\n".join(lines)

    return json.loads(response)
