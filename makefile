# --------------------------------------------------------------------
# Red Hat Home Code Assignment
# Greg Kopels
# gregkopels@gmail.com
# Makefile for creating a Alpine docker image
# --------------------------------------------------------------------

# PROJECT_NAME defaults to name of the current directory.
# should not to be changed if you follow GitOps operating procedures.
PROJECT_NAME = $(notdir $(PWD))

# all our targets are phony (no files to check).
.PHONY: docker

docker:
	#$(MAKE) install DESTDIR=docker/dist
	#cp Dockerfile docker
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
