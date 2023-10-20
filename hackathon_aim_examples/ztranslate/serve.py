import tornado
from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop

import os
import asyncio
import json

PORT = os.environ.get('PORT', 4000)
API_KEY = os.environ.get('API_KEY', "")

MANIFEST = {
    "name": "Ztranslate.net wrapper",
    "short_name": "ztranslate",
    "version": "0.1",
    "endpoints": [{
        "uri": "/translate",
        "price_per_call": {"min": 0.003, "max": 0.006, "esimated_cost": 0.005, "currency": "USD"},
        "price_per_input_mb": {"min": 0, "max": 0, "estimated_cost": 0, "currency": "USD"},
        "price_per_input_char": {"min": 0, "max": 0, "estimated_cost": 0, "currency": "USD"},
        "input_methods": ["POST"],
        "input_query": "?target_lang={LangCode}&source_lang={LangCode}&mode={Fast}&output={png,wav}",
        "input_body": {"image": "<Image:Base64>"},
        "input_headers": {},
        "output": {"image": "<Image:Base64>"},
        "documentation": "Takes as input a json object with \"image\" field as a base64 image and returns back the image with translation text boxes written over.",
        "example_calls": [
            {"method": "POST",
             "query": "?target_lang=En&source_lang=Ja&output=png,wav",
             "headers": {},
             "body": {"image": "ahdg0n32...="},
             "output": {"image": "ahdg07d...="}
            }
        ]
    }],
    "documentation_url": "https://ztranslate.net/docs/service",
    "license": "Open",
    "terms_of_service": "https://example.com/tos",
    "author": "Barry Rowe"
}


class ManifestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(MANIFEST))

class TranslationHandler(tornado.web.RequestHandler):
    async def post(self):
        try:
            if self.request.headers.get("cost_only"):
                #return self.write(json.dumps({"costs": [{"min": 0.003, "max": 0.003, "estimated_cost": 0.003, "currency": "USD"}]}))
                return self.write(json.dumps({"costs": []}))

            http_client = AsyncHTTPClient()
        
            query = self.request.query
            if "api_key" in query.lower():
                self.set_status(400)
                return self.write("Invalid uri")
            query+="&API_KEY="+API_KEY
            url = "https://ztranslate.net/service?"+query
            response = await http_client.fetch(url, method="POST", body=self.request.body)
            self.write(response.body)
            output_costs = [{"currency": "USD", "used": 3000}]
            self.set_header("costs", json.dumps(output_costs))
        except:
            import traceback
            self.write(traceback.format_exc())

def make_app():
    return tornado.web.Application([
        (r"/manifest.json", ManifestHandler),
        (r"/translate", TranslationHandler),
    ])

def shutdown():
    print("Stopping server...")
    tornado.ioloop.IOLoop.current().stop()

async def main():
    print("RUNNING: PORT", PORT)
    app = make_app()
    server = app.listen(PORT, address='0.0.0.0')
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down...")
        server.stop()
        tornado.ioloop.IOLoop.current().add_callback_from_signal(shutdown)


if __name__ == "__main__":
    asyncio.run(main())
