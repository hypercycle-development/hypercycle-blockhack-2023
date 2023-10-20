import http.client
from PIL import Image
import base64
import io
import json


class ZTranslateTester:
    @classmethod
    def test_translate_image(cls):
      try:
        img = Image.open("ja_example.jpg")
        image_byte_array = io.BytesIO()
        img.save(image_byte_array, format='PNG')
        image_data = image_byte_array.getvalue()

        image_data = base64.b64encode(image_data)
        data_body = json.dumps({"image": image_data.decode("utf-8")})

        conn = http.client.HTTPConnection("localhost", 4000)
        conn.request("POST", "/translate?target_lang=EN&output=png", data_body)
        r1 = conn.getresponse()
        data = r1.read()
        data = json.loads(data)
        data_bytes = base64.b64decode(data['image'])
        bytes_output = io.BytesIO()
        bytes_output.write(data_bytes)
        img_out = Image.open(bytes_output)
        #img_out.save("output.png")
        return {"status": "success", "output": "Passed translation image test."}
      except:
        import traceback
        return {"status": "error", "output": traceback.format_exc()}

    @classmethod
    def test_translate_sound(cls):
      try:
        img = Image.open("ja_example.jpg")
        image_byte_array = io.BytesIO()
        img.save(image_byte_array, format='PNG')
        image_data = image_byte_array.getvalue()

        image_data = base64.b64encode(image_data)
        data_body = json.dumps({"image": image_data.decode("utf-8")})

        conn = http.client.HTTPConnection("localhost", 4000)
        conn.request("POST", "/translate?target_lang=EN&output=wav", data_body)
        r1 = conn.getresponse()
        data = r1.read()
        data = json.loads(data)
        
        data_bytes = base64.b64decode(data['sound'])
        bytes_output = io.BytesIO()
        bytes_output.write(data_bytes)
        #img_out = Image.open(bytes_output)
        #img_out.save("output.png")
        return {"status": "success", "output": "Passed translation sound test."}
      except:
        import traceback
        return {"status": "error", "output": traceback.format_exc()}


def test():
    #run all tests here
    tests = []
    tests.append(ZTranslateTester.test_translate_image())
    tests.append(ZTranslateTester.test_translate_sound())

    error = False
    for result in tests:
        if result['status'] == "error":
            error = True
    if error:
        print(tests)
        return {"status": "error", "output": "Failed tests."}
    return {"status": "success", "output": "Tests passed."}


def main():
    print(json.dumps(test()))


if __name__=='__main__':
    main()


