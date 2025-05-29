from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from search.opensearch_client import client

class ProductTagSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tags = request.query_params.getlist("tags")
        query = request.query_params.get("q", "")

        body = {
            "query": {
                "bool": {
                    "must": [
                        {"multi_match": {"query": query, "fields": ["name", "description"]}} if query else {"match_all": {}}
                    ],
                    "filter": [
                        {"terms": {"tags": tags}} if tags else {}
                    ]
                }
            }
        }

        res = client.search(index="products", body=body)
        results = [hit["_source"] for hit in res["hits"]["hits"]]
        return Response(results)
