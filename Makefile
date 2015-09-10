all: tests

LOGLEVEL		:= INFO
TZ			:= UTC

export LOGLEVEL
export TZ

tests: lint unit functional integration

lint:
	@printf "\033[1;33mChecking for static errors\033[0m\n"
	@find m3u8 -name '*.py' | xargs flake8 --ignore=E501

clean:
	git clean -Xdf

start-server:
	nohup python tests/m3u8server.py &

stop-server:
	-@kill -9 $$(ps aux | grep m3u8server.py | grep -v grep | awk '{ print $$2 }')

unit:
	make start-server
	nosetests -x --with-coverage --cover-erase --cover-package=m3u8 --verbosity=2 -s --rednose tests
	-@make stop-server


documentation:
	@cd docs && make html
	$(OPEN_COMMAND) docs/build/html/index.html

ensure-dependencies:
	@python setup.py develop
	@pip install -r requirements-dev.txt

deps: ensure-dependencies

release: documentation
	@./.release
