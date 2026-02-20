DOCKER ?= docker

.PHONY: up down logs ps password rebuild

up:
	$(DOCKER) compose up -d --build

down:
	$(DOCKER) compose down

logs:
	$(DOCKER) compose logs -f jenkins

ps:
	$(DOCKER) compose ps

password:
	$(DOCKER) compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

rebuild:
	$(DOCKER) compose build --no-cache
