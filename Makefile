install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C hello.py
	pylint --disable=R,C Demo2.py
	pylint --disable=R,C Fib.py


	
