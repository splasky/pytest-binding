all:
	gcc -fprofile-arcs -ftest-coverage -o tests/add.so -shared add.c
pytest:
	pytest tests --cov=wrapper --cov-report=html
	lcov --capture --directory . --output-file coverage.info
	genhtml coverage.info --output-directory out
