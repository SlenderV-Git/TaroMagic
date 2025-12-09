BACKEND_SERVICE = backend-service
DB_SERVICE = db-service

DC = docker compose
ENV_PATH = ./.env


build-backend:
	$(DC) --env-file $(ENV_PATH) build $(BACKEND_SERVICE)

up-all:
	docker compose --env-file $(ENV_PATH) up -d

up-all-echo:
	docker compose --env-file $(ENV_PATH) up

up-backend:
	docker compose --env-file $(ENV_PATH) up $(BACKEND_SERVICE) $(DB_SERVICE) 

up-db:
	docker compose --env-file $(ENV_PATH) up $(DB_SERVICE)

stop-all:
	docker stop $(BACKEND_SERVICE) $(DB_SERVICE) 

stop-db:
	docker stop $(DB_SERVICE)
