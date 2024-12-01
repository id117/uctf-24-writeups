all: upload

prep:
	mkdir task
	cp encrypt.py Makefile task

flag: prep
	echo "UCTF{$(shell cat /dev/urandom | head -c 64 | md5sum -b | head -c 32)}" > flag.txt

encrypt: flag
	cat flag.txt | python3 encrypt.py -o task/flag.txt.encrypted

task: encrypt

decrypt: task
	cp solve/decrypt.py ./
	cp task/flag.txt.encrypted ./encrypted.py
	python3 decrypt.py

test-decrypt: decrypt
	echo "decrypted: $(shell cat decrypted.txt)"

test: test-decrypt

upload: test
	python3 build_json.py
	mkdir ../../upload/aes
	cat task.json > ../../upload/aes/ctfd.json
	mkdir ../../upload/aes/files
	cp task/* ../../upload/aes/files

clean:
	rm -rf task flag.txt flag.txt.encrypted decrypt.py decrypted.txt task.json __pycache__ ctfd.json ../../upload/aes