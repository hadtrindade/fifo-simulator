compile-ui:
	pyside2-uic ui_fifo_simulator/fifo_simulator.ui -o fifo_simulator/ui_fifo_simulator.py

start-app:
	python fifo_simulator/app.py

black:
	black -l 79 fifo_simulator