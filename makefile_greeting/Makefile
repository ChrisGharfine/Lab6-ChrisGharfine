PYTHON ?= python
.PHONY: install test lint clean package

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	$(PYTHON) -m flake8 app.py tests setup.py

clean:
	$(PYTHON) -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in (Path('build'), Path('dist'), *Path('.').glob('*.egg-info'), *Path('.').rglob('__pycache__')) if p.is_dir()]"

package:
	$(PYTHON) -m build --no-isolation
