NETBOX_VER?=v3.2.0

NAME=netbox_gateways

COMPOSE_FILE=./nb_development/docker-compose.yml
VERFILE=./netbox_cisco_support/version.py


pull:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} pull

debug:
	@echo "Starting Netbox .. "
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} up

start:
	@echo "Starting Netbox in detached mode.. "
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} up -d

stop:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} down

destroy:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} down -v

nbshell:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py nbshell

logs:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} logs -f

shell:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox /bin/bash

adduser:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py createsuperuser

collectstatic:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic

migrations:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} up -d postgresql
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox \
	/opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py makemigrations --name ${NAME}
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} down

pbuild:
	python3 -m pip install --upgrade build
	python3 -m build

pypipub:
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

relpatch:
	$(eval GSTATUS := $(shell git status --porcelain))
ifneq ($(GSTATUS),)
	$(error Git status is not clean. $(GSTATUS))
endif
	git checkout develop
	git remote update
	git pull origin develop
	$(eval CURVER := $(shell cat $(VERFILE) | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'))
	$(eval NEWVER := $(shell pysemver bump patch $(CURVER)))
	$(eval RDATE := $(shell date '+%Y-%m-%d'))
	git checkout -b release-$(NEWVER) origin/develop
	echo '__version__ = "$(NEWVER)"' > $(VERFILE)
	git commit -am 'bump ver'
	git push origin release-$(NEWVER)
	git checkout develop


test:
	docker-compose -f ${COMPOSE_FILE} -p ${NAME} exec netbox python manage.py test ${NAME}
