"""
   An example of writing an AIM that uses the SimpleQueue server class and
   uses the `add_job` method.

   The `add_job` method is useful for ensuring that your model is only accessed
   one request at a time. Without it, multiple requests coming into your server
   would cause multiple passes of your model to run, consuming extra memory
   and possibly making the GPU run out of memory.

   Behind the scenes, self.add_job will run the given function inside an internal
   queue that runs one request at a time, and then return a future that when
   awaited, will wait for this request to be completed before returning to the
   external caller.
"""
import os
from pyhypercycle_aim import SimpleQueue, JSONResponseCORS, aim_uri

PORT = os.environ.get('PORT', 4000)

class QueueAim(SimpleQueue):
    manifest = {
        "name": "A aim service that uses the simple queue system.",
        "short_name": "aim_queue",
        "version": "0.1.0",
        "license": "Open",
        "terms-of-service": "https://hypercycle.ai/tos",
        "author": "Hypercycle"
    }

    def __init__(self):
       #Load your model here.
       self.z = 4

    @aim_uri(
        uri="/my_job",
        methods=["POST", "GET"],
        endpoint_manifest={
            "input_query": "",
            "input_headers": {},
            "input_body": {"x": "<Int>", "y": "<Int>"},
            "output": {"value": "<Int>"},
            "documentation": "",
            "currency": "HYPC",
            "price_per_call": {"estimated_cost": 0, "min": 0, "max": 0.1},
            "price_per_mb": {"estimated_cost": 0, "min": 0, "max": 0.1},
            "example_calls": [{
                "body": {"x": 1, "y": 2},
                "method": "POST",
                "query": "",
                "headers": "",
                "output": {"value": 17}
            }]

    })
    async def greet(self, request):
        costs = []
        costs.append({"estimated_cost": 1, "min": 1, "max": 4, 
                      "currency": "ProcessingUnits"})
        if request.headers.get("cost_only"):
            return JSONResponseCORS({"costs": costs})
        input_x = self.request.query_params.get("x", 0)
        input_y = self.request.query_params.get("y", 0)
        result = await self.add_job(self.run_job, input_x, y=input_y)

        return JSONResponseCORS({"value": result}, 
                                headers={"used": "2", "currency": "ProcessingUnits"})

    def run_job(self, x=1, y=2):
        #run your model here.
        return x*1+y*2+self.z*3


def main():
  app = GreetingAim()
  app.run(uvicorn_kwargs={"port": PORT, "host": "0.0.0.0"})

if __name__ == "__main__":
    main()
