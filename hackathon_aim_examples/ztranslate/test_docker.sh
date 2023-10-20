#!/bin/bash
pip3 install -r requirements.txt
sudo docker prune -f
sudo docker kill $(sudo docker ps -a -q --filter="ancestor=ztrans")
sudo docker build --file "./DockerFile" --tag="ztrans" . 
sudo docker run -dp 4000:4000 ztrans
python3 test.py
