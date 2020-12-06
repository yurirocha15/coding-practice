setup:
	python -m pip install -r requirements.txt

format:
	black .
	isort .

lint:
	env PYTHONPATH=src pytest src --flake8 --mypy

test-solutions:
	env PYTHONPATH=src python run_all.py