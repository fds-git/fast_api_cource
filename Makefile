up:
	docker compose up -d 

down:
	docker compose down -v

build:
	docker compose build

clear:
	find ./log -type f -delete