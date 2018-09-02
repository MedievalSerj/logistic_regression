package = dslr


install_dev:
	pip3.6 install --editable .

install:
	pip3.6 install .

install_user:
	pip3.6 install --user .

isort:
	isort -rc $(package)

flake:
	flake8 $(package)

test:
	coverage run -m unittest discover $(package)
	coverage report -m

uninstall:
	pip3.6 uninstall $(package) -y
	pip3.6 uninstall -r requirements.txt -y
