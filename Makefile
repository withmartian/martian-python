
build:
	rm -rf dist/ build/
	python3 -m build .

upload_test:
	python3 -m twine upload --repository testpypi dist/*
	rm -rf dist

upload:
	python3 -m twine upload dist/*
	rm -rf dist