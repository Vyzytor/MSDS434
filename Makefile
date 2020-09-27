install:
	pip install --upgrade pip &&\
<<<<<<< HEAD
        pip install -r requirements.txt
lint:
	pylint --disable=R,C hello.py
	pylint --disable=R,C Demo2.py
	pylint --disable=R,C Fib.py
=======
	pip install -r requirements.txt
lint:
	pylint --disable=R,C hello.py
	pylint --disable=R,C Demo2.py
	pylint --disable=R,C Fib.py
>>>>>>> 54bd5655d6221c0a101587f91ed0b28983a9e9d5
