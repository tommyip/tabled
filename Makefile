.PHONY: init clean test docs

all: clean init test docs

init:
	rm venv -rf && \
	virtualenv venv && \
	. venv/bin/activate && \
	$(MAKE) update-dep

update-dep:
	pip install -r requirements.txt
	pip install -r ./requirements/tests.txt
	pip install -r ./requirements/docs.txt

test:
	pip install -e .
	py.test
	mypy tabled/*.py tests/*.py --follow-imports=silent --ignore-missing-imports
	flake8 tabled tests

docs:
	cd docs && $(MAKE) html

clean:
	find . -name '*.pyc' -exec rm -f {} +
	rm __pycache__ -rf
	rm tabled.egg-info -rf
