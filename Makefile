all: install clean


install:
	pip install .

clean:
	rm -rf build mock_cmd.egg-info

sync:
	rsync -avr --partial --progress . cham@10.3.10.10:~/cluster
	ssh cham@10.3.10.10 "pip install ~/cluster"