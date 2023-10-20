import http.client
from PIL import Image
import base64
import io
import json

def main():
    img = Image.open("ja_example.jpg")
    image_byte_array = io.BytesIO()
    img.save(image_byte_array, format='PNG')
    image_data = image_byte_array.getvalue()

    image_data = base64.b64encode(image_data)
    data_body = json.dumps({"image": image_data.decode("utf-8")})

    conn = http.client.HTTPConnection("localhost", 4000)#running in docker
    conn.request("POST", "/translate?target_lang=EN&output=png", data_body)
    r1 = conn.getresponse()
    data = r1.read()
    print(data)
    data = json.loads(data)
    data_bytes = base64.b64decode(data['result']['image'])
    bytes_output = io.BytesIO()
    bytes_output.write(data_bytes)
    img_out = Image.open(bytes_output)
    img_out.save("output.png")
    print("translated image written to \"output.png\"")

if __name__=='__main__':
    main()
