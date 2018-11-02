build:
	docker build --rm -t decora .

run:
	docker run -p 8888:8888 -it decora 
shell:
	docker run -p 8888:8888 -it decora /bin/sh