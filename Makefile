.PHONY: run-backend run-frontend seed-db

run-backend:
	uvicorn backend.main:app --reload

run-frontend:
	cd frontend && npm install && npm run dev

seed-db:
	python backend/db/seed_all.py