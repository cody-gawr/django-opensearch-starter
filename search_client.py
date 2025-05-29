from opensearchpy import OpenSearch
es = OpenSearch(hosts=[{'host':'opensearch','port':9200}])
