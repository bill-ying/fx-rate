.PHONY: help build test run clean push push-version push-all login

DOCKER_REPO ?= fx-rate
DOCKER_TAG ?= latest
DOCKER_IMAGE = $(DOCKER_REPO):$(DOCKER_TAG)
DOCKER_HUB_USER ?= billying
DOCKER_HUB_IMAGE = $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(DOCKER_TAG)
VERSION ?= latest

help:
	@echo "Available commands:"
	@echo ""
	@echo "Local Development:"
	@echo "  make build              - Build the Docker image locally (fx-rate:latest)"
	@echo "  make test               - Run the application in Docker with test data"
	@echo "  make run-local          - Run the application locally"
	@echo ""
	@echo "Docker Hub Publishing:"
	@echo "  make login              - Login to Docker Hub"
	@echo "  make push               - Push to Docker Hub as latest (billying/fx-rate:latest)"
	@echo "  make push-version       - Push specific version (VERSION=1.0.0)"
	@echo "  make push-all           - Push both version and latest (VERSION=1.0.0)"
	@echo ""
	@echo "Parameters:"
	@echo "  make run-cad DATE=YYYYMMDD  - Get CAD to USD rate for a specific date"
	@echo "  make run-usd DATE=YYYYMMDD  - Get USD to CAD rate for a specific date"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean              - Remove Docker images and local cache"

build:
	docker build -t $(DOCKER_IMAGE) .

test: build
	docker run $(DOCKER_IMAGE) c -d 20210331

run-cad: build
	docker run $(DOCKER_IMAGE) c -d $(DATE)

run-usd: build
	docker run $(DOCKER_IMAGE) u -d $(DATE)

run-local:
	python fx_rate.py

login:
	docker login

push: build
	docker tag $(DOCKER_IMAGE) $(DOCKER_HUB_IMAGE)
	docker push $(DOCKER_HUB_IMAGE)
	@echo "Successfully pushed $(DOCKER_HUB_IMAGE)"
	@echo "View at: https://hub.docker.com/r/$(DOCKER_HUB_USER)/$(DOCKER_REPO)"

push-version: build
	@if [ "$(VERSION)" = "latest" ]; then \
		echo "ERROR: Use 'make push' for latest tag, or specify VERSION=1.0.0"; \
		exit 1; \
	fi
	docker tag $(DOCKER_IMAGE) $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION)
	docker push $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION)
	@echo "Successfully pushed $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION)"
	@echo "View at: https://hub.docker.com/r/$(DOCKER_HUB_USER)/$(DOCKER_REPO)"

push-all: build
	@if [ "$(VERSION)" = "latest" ]; then \
		echo "ERROR: Specify VERSION=1.0.0 for push-all"; \
		exit 1; \
	fi
	docker tag $(DOCKER_IMAGE) $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION)
	docker tag $(DOCKER_IMAGE) $(DOCKER_HUB_USER)/$(DOCKER_REPO):latest
	docker push $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION)
	docker push $(DOCKER_HUB_USER)/$(DOCKER_REPO):latest
	@echo "Successfully pushed $(DOCKER_HUB_USER)/$(DOCKER_REPO):$(VERSION) and latest"
	@echo "View at: https://hub.docker.com/r/$(DOCKER_HUB_USER)/$(DOCKER_REPO)"

clean:
	docker rmi $(DOCKER_IMAGE) || true
	docker rmi $(DOCKER_HUB_IMAGE) || true
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete


