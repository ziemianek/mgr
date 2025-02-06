run-tasks-svc:
	uvicorn services.tasks.app.main:app --host 0.0.0.0 --port 5050 --reload

all:
	run-tasks-svc
