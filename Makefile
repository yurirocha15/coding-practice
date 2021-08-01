format:
	black .
	isort .

setup:
	pip install -r requirements.txt

test-solutions:
	env PYTHONPATH=src pytest tests -s --verbose --cov=src --cov-report=html --cov-report=term-missing --suppress-no-test-exit-code

tree:
	tree -I "$(shell cat .gitignore | tr -s '\n' '|')"