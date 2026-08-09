# API Docs of Wazuh Assistant Backend

Currently just a proxy to indexer.

## Endpoints


### 1. POST `/indexer-proxy`

In the payload, provide a Opensearch JSON query. Receive JSON output.

Sample Payload:
```json
{
  "size": 2,
  "_source": [
    "@timestamp",
    "agent.name",
    "agent.ip",
    "agent.id",
    "rule.id",
    "rule.level",
    "rule.description",
    "decoder.name",
    "syscheck.path",
    "syscheck.event",
    "syscheck.changed_attributes",
    "syscheck.md5_before",
    "syscheck.md5_after",
    "syscheck.sha256_before",
    "syscheck.sha256_after",
    "full_log"
  ],
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "rule.id": "550"
          }
        }
      ]
    }
  },
  "sort": [
    {
      "@timestamp": {
        "order": "desc"
      }
    }
  ]
}
```

Sample Response:
```json
{
  "took": 20,
  "timed_out": false,
  "_shards": {
    "total": 21,
    "successful": 21,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 33,
      "relation": "eq"
    },
    "max_score": null,
    "hits": [
      {
        "_index": "wazuh-alerts-4.x-2026.07.28",
        "_id": "K5NYp58BrfQXAxwk2pnL",
        "_score": null,
        "_source": {
          "syscheck": {
            "path": "c:\\users\\administrator\\desktop\\monitorme\\myfile.txt",
            "changed_attributes": [
              "size",
              "mtime",
              "md5",
              "sha1",
              "sha256"
            ],
            "md5_before": "5a317b0aafec378d1ffdfbab6256eaf5",
            "sha256_before": "72d279c8734b9af8ef1fdc0d67d8418b6c9ac9fe80ba88ac221e4d989d255ec5",
            "event": "modified",
            "md5_after": "67008425a20d911aa1ea171fcd9610e6",
            "sha256_after": "db449a3fb0b5640cc07d1f2d4f36ff96506734ef1ccb8d11b60dd48a61d7baac"
          },
          "agent": {
            "ip": "10.0.0.101",
            "name": "windows-user",
            "id": "002"
          },
          "@timestamp": "2026-07-28T06:10:43.888Z",
          "rule": {
            "level": 7,
            "description": "Integrity checksum changed.",
            "id": "550"
          },
          "decoder": {
            "name": "syscheck_integrity_changed"
          },
          "full_log": "File 'c:\\users\\administrator\\desktop\\monitorme\\myfile.txt' modified\nMode: realtime\nChanged attributes: size,mtime,md5,sha1,sha256\nSize changed from '36' to '19'\nOld modification time was: '1785218967', now it is '1785219043'\nOld md5sum was: '5a317b0aafec378d1ffdfbab6256eaf5'\nNew md5sum is : '67008425a20d911aa1ea171fcd9610e6'\nOld sha1sum was: '048f15b2cd4ff6c1660c78e3da5e2265b16f8545'\nNew sha1sum is : '7d9fde112572352d3837a920d3fc5a5cbbf846eb'\nOld sha256sum was: '72d279c8734b9af8ef1fdc0d67d8418b6c9ac9fe80ba88ac221e4d989d255ec5'\nNew sha256sum is : 'db449a3fb0b5640cc07d1f2d4f36ff96506734ef1ccb8d11b60dd48a61d7baac'\n"
        },
        "sort": [
          1785219043888
        ]
      },
      {
        "_index": "wazuh-alerts-4.x-2026.07.28",
        "_id": "70Pbp58Bci4RObf1Ovq6",
        "_score": null,
        "_source": {
          "syscheck": {
            "path": "c:\\users\\administrator\\desktop\\monitorme\\myfile.txt",
            "changed_attributes": [
              "size",
              "mtime",
              "md5",
              "sha1",
              "sha256"
            ],
            "md5_before": "5a317b0aafec378d1ffdfbab6256eaf5",
            "sha256_before": "72d279c8734b9af8ef1fdc0d67d8418b6c9ac9fe80ba88ac221e4d989d255ec5",
            "event": "modified",
            "md5_after": "67008425a20d911aa1ea171fcd9610e6",
            "sha256_after": "db449a3fb0b5640cc07d1f2d4f36ff96506734ef1ccb8d11b60dd48a61d7baac"
          },
          "agent": {
            "ip": "10.0.0.101",
            "name": "windows-user",
            "id": "002"
          },
          "@timestamp": "2026-07-28T06:10:43.888Z",
          "rule": {
            "level": 7,
            "description": "Integrity checksum changed.",
            "id": "550"
          },
          "decoder": {
            "name": "syscheck_integrity_changed"
          },
          "full_log": "File 'c:\\users\\administrator\\desktop\\monitorme\\myfile.txt' modified\nMode: realtime\nChanged attributes: size,mtime,md5,sha1,sha256\nSize changed from '36' to '19'\nOld modification time was: '1785218967', now it is '1785219043'\nOld md5sum was: '5a317b0aafec378d1ffdfbab6256eaf5'\nNew md5sum is : '67008425a20d911aa1ea171fcd9610e6'\nOld sha1sum was: '048f15b2cd4ff6c1660c78e3da5e2265b16f8545'\nNew sha1sum is : '7d9fde112572352d3837a920d3fc5a5cbbf846eb'\nOld sha256sum was: '72d279c8734b9af8ef1fdc0d67d8418b6c9ac9fe80ba88ac221e4d989d255ec5'\nNew sha256sum is : 'db449a3fb0b5640cc07d1f2d4f36ff96506734ef1ccb8d11b60dd48a61d7baac'\n"
        },
        "sort": [
          1785219043888
        ]
      }
    ]
  }
}
```


### 2. POST `/generate-query`

In the payload, provide prompt from user (SOC Analyst).

Sample Payload:
```json
{
  "user_prompt": "Write a query to filter top 2 most recent rule 550 alerts"
}
```

The response will have a json object with 2 keys.

- `message` will contain a message to be shown to the user, in text.
- `query` will contain the query the user initially asked, as JSON object.

Sample Response:
```json
{
  "message": "Okay, I will generate the OpenSearch DSL query for your request.",
  "query": {
    "size": 2,
    "_source": [
      "@timestamp",
      "agent.name",
      "agent.ip",
      "agent.id",
      "rule.id",
      "rule.level",
      "rule.description",
      "decoder.name",
      "full_log"
    ],
    "query": {
      "bool": {
        "filter": [
          {
            "term": {
              "rule.id": "550"
            }
          }
        ]
      }
    },
    "sort": [
      {
        "@timestamp": {
          "order": "desc"
        }
      }
    ]
  }
}
```

In the frontend, show the `message` part to the user and put the value of the `query` part in another code editor box that the user can edit and execute.

When user executes, call the `/indexer-proxy` endpoint again.
