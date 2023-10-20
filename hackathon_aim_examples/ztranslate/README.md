# ZTranslate screenshot translator
This is an example aim that translates screenshot images with the ZTranslate.net api.

# Running the example
To use, run:

`pip install -r requirements.txt`

`python3 serve.py`

Now `http://localhost:4000/translate` is ready to read incoming requests.

# Running the test:

You can test the server yourself by running:

`python3 test.py`

Which will take the japanese screenshot located at `ja_example.jpg` and translate it into english and write it to `output.png`

# Running the server in realtime:

The AIM is compatible with some external programs. For instance, with RetroArch, you can run this example during realtime gameplay by specifiying the AI service URL as `http://localhost:4000/translate`. Specify a hotkey for the AI service, and you can use the translator in realtime.


# Building the docker image

A DockerFile is also included in the folder so the service can be built into a docker image. You can build it yourself and run the image like so:

`sudo docker build --file "./DockerFile" --tag="ztrans" . `
`sudo docker run -dp 4000:4000 ztrans`


