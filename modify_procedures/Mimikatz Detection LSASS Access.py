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
              "match_phrase": {
                "event_id": "10"
              }
            },
            {
              "match_phrase": {
                "process_target_path": "C:\\windows\\system32\\lsass.exe"
              }
            },
            {
              "match_phrase": {
                "process_granted_access": "4112"
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
                                  "process_path.keyword": "*\\\\wmiprvse.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\taskmgr.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\procexp64.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\procexp.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\lsm.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\csrss.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\wininit.exe"
                                }
                              },
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\vmtoolsd.exe"
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
procedure = "Mimikatz Detection LSASS Access"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 15)

json_str = json.dumps(doc)
with open("dst_procedures/Mimikatz Detection LSASS Access.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Mimikatz Detection LSASS Access"\n')
	f.write('tech_code = "T1003"\n')
