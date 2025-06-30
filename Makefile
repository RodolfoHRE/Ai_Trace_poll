.PHONY: production_build production_up production_down \
        dev_build dev_up dev_down


production_build: Dockerfile docker-compose-production.yml
	sudo docker compose -p production -f docker-compose-production.yml --env-file env/production.env up --build -d

production_up: Dockerfile docker-compose-production.yml
	sudo docker compose -p production -f docker-compose-production.yml --env-file env/production.env up -d

production_down: Dockerfile docker-compose-production.yml
	sudo docker compose -p production -f docker-compose-production.yml --env-file env/production.env down






dev_build: Dockerfile docker-compose-dev.yml
	sudo docker compose -p dev -f docker-compose-dev.yml --env-file env/development.env up --build -d

dev_up: Dockerfile docker-compose-dev.yml
	sudo docker compose -p dev -f docker-compose-dev.yml --env-file env/development.env up -d

dev_down: Dockerfile docker-compose-dev.yml
	sudo docker compose -p dev -f docker-compose-dev.yml --env-file env/development.env down
