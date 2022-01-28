rose:
	python arts/rose.py

linear:
	python arts/shape.py 2

triangle:
	python arts/shape.py 3

square:
	python arts/shape.py 4

pentagon:
	python arts/shape.py 5

hexagon:
	python arts/shape.py 6

magic:
	python arts/shape.py $(shell bash -c 'echo $$((RANDOM % 7))')

chaos:
	python arts/chaos.py