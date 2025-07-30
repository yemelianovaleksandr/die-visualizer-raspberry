install:
	sudo apt update
	sudo apt install -y python3-pip ffmpeg
	pip3 install -r requirements.txt

run:
	python3 app/app.py

docker-build:
	sudo docker build -t dieapp .

docker-run:
	sudo docker run -d -p 5000:5000 --name dieapp dieapp

docker-stop:
	sudo docker stop dieapp || true
	sudo docker rm dieapp || true
