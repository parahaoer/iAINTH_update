from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "11"
              }
            },
            {
              "wildcard": {
                "file_name.keyword": "*lsass*"
              }
            },
            {
              "wildcard": {
                "file_name.keyword": "*dmp"
              }
            }
          ]
        }
      }
    }
  }
}





res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "LSASS Memory Dump File Creation"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 9)

