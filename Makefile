.PHONY: run_demo test clean

run_demo:
	python -m scripts.run_demo

run_gui:
	python -m scripts.run_gui

test:
	python -m unittest discover tests

clean:
	del /S /Q *.pyc
	del /S /Q __pycache__
