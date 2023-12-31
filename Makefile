SHELL := bash

.PHONY: lint test test-all dist bump test-release release clean-dist clean

VENV_EXE=python3 -m virtualenv
VENV=.venv
VENV_ACTIVATE=. $(VENV)/bin/activate
BUMPTYPE=patch

$(VENV):
	$(VENV_EXE) $(VENV)
	$(VENV_ACTIVATE); pip install -e .[test]

lint: $(VENV)
	$(VENV_ACTIVATE); ruff .

test: $(VENV)
	$(VENV_ACTIVATE); python tests/test.py

test-all: $(VENV)
	$(VENV_ACTIVATE); tox

dist: clean-dist $(VENV)
	$(VENV_ACTIVATE); python -m build
	ls -ls dist
	tar tzf dist/*.tar.gz
	$(VENV_ACTIVATE); twine check dist/*

bump: $(VENV)
	$(VENV_ACTIVATE); bump2version $(BUMPTYPE)
	git show -q
	@echo
	@echo "SUCCESS: Version was bumped and committed"

clean-dist:
	rm -rf dist
	rm -rf *.egg-info

clean: clean-dist
	rm -rf $(VENV) .tox
