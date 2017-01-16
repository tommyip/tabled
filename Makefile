.PHONY: init clean tests docs

all: clean init tests docs

init:
	rm venv -rf && \
	virtualenv venv && \
	. venv/bin/activate && \
	$(MAKE) update-dep

update-dep:
	pip install -r requirements.txt

tests:
	$(MAKE) update-dep
	pip install -e .
	py.test
	mypy tabled/*.py tests/*.py

docs:
	cd docs && $(MAKE) html

clean:
	find . -name '*.pyc' -exec rm -f {} +
	rm __pycache__ -rf
	rm tabled.egg-info -rf