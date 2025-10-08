build:
	docker-compose up --build -d

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down --volumes --remove-orphans

logs:
	docker-compose logs -f

prune-volumes:
	docker volume prune -f

test:
	 docker-compose exec web poetry run python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=90 --log-level ERROR
