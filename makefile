DOCKER_TAG := $('tester')
PROJECT_NAME = $(notdir $(PWD))
.PHONY: docker

docker:
	#$(MAKE) install DESTDIR=docker/dist
	cp Dockerfile docker
	docker build -t tester .

prune:
	# clean all that is not actively used
	docker system prune -af

rebuild:
	# force a rebuild by passing --no-cache
	docker-compose build --no-cache

test:
	# here it is useful to add your own customised tests
	docker run -it --rm -v `pwd`:`pwd` -w `pwd` tester pytest test1.py
