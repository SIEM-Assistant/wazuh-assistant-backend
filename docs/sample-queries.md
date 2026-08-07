# Sample Queries for the Indexer

## 2 most recent rule 550 alerts

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
