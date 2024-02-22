PYBIN=./venv/bin
SRC=./src


$(SRC)/main: $(PYBIN)/activate
	$(PYBIN)/python3 $@.py

$(PYBIN)/activate: requirements.txt
	python3 -m venv venv
	$(PYBIN)/pip install -r requirements.txt


clean::
	rm -rf __pycache__ venv
