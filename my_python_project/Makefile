PYTHON ?= python
PYB ?= pyb
.DEFAULT_GOAL := all
.PHONY: clean install_deps test build all

clean:
	$(PYB) clean

install_deps:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYB) run_unit_tests

build:
	$(PYB) publish

all:
	$(MAKE) install_deps
	$(MAKE) clean
	$(MAKE) test
	$(MAKE) build
