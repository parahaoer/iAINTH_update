import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "must": [
                  {
                    "bool": {
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "4662"
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "object_properties.keyword": "*Replicating Directory Changes All*"
                                }
                              },
                              {
                                "wildcard": {
                                  "object_properties.keyword": "*1131f6ad-9c07-11d1-f79f-00c04fc2dcd2*"
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must_not": [
                        {
                          "bool": {
                            "must": [
                              {
                                "match_phrase": {
                                  "SubjectDomainName": "Window Manager"
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "SubjectUserName.keyword": "NT AUTHORITY*"
                                }
                              },
                              {
                                "wildcard": {
                                  "SubjectUserName.keyword": "*$"
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  }
                ]
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
procedure = "Mimikatz DC Sync"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 14)

json_str = json.dumps(doc)
with open("dst_procedures/Mimikatz DC Sync.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Mimikatz DC Sync"\n')
	f.write('tech_code = "T1003"\n')
