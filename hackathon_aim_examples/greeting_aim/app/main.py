import os
from pyhypercycle_aim import SimpleQueue, JSONResponseCORS, aim_uri

PORT = os.environ.get('PORT', 4000)

class GreetingAim(SimpleQueue):
    manifest = {
        "name": "A aim greeting service",
        "short_name": "aim_greeting",
        "version": "0.1.0",
        "license": "Open",
        "terms-of-service": "https://hypercycle.ai/tos",
        "author": "Hypercycle"
    }
    def __init__(self):
       pass

    @aim_uri(
        uri="/greet",
        methods=["POST", "GET"],
        endpoint_manifest={
            "input_query": "",
            "input_headers": {},
            "input_body": {"inputs": "<Text>"},
            "output": "<JSON>",
            "documentation": "",
            "currency": "HYPC",
            "price_per_call": {"estimated_cost": 0, "min": 0, "max": 0.1},
            "price_per_mb": {"estimated_cost": 0, "min": 0, "max": 0.1},
            "example_calls": [{
                "body": "",
                "method": "POST",
                "query": "",
                "headers": "",
                "output": {"text": "Hello World!"}
            }]

    })
    async def greet(self, request):
        costs = []
        costs.append({"estimated_cost": 1, "min": 1, "max": 1, 
                      "currency": "ProcessingUnits"})
        if request.headers.get("cost_only"):
            return JSONResponseCORS({"costs": costs})
        result = "Hello World!"
        return JSONResponseCORS({"text": result}, 
                                headers={"used": "1", "currency": "ProcessingUnits"})


def main():
  app = GreetingAim()
  app.run(uvicorn_kwargs={"port": PORT, "host": "0.0.0.0"})

if __name__ == "__main__":
    main()
