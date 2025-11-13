build:
	docker build -t santillanimg:latest .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
	docker stack rm quinto
