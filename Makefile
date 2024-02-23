SRC=./src
PYBIN=$(SRC)/venv/bin


$(PYBIN)/activate: requirements.txt
	python3 -m venv $(SRC)/venv
	$(PYBIN)/pip install -r requirements.txt


clean::
	rm -rf __pycache__ $(SRC)/__pycache__ $(SRC)venv
