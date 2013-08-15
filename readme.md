Python Celery Proof of Concept App
=

Overview
-

This is a proof of concept to assess the feasibility of running Celery as a task manager for encoding jobs.

Problems
-

-	1.) Feasibility / ease of management for workers running on different hosts and running multiple processes
-	2.) Worker load management. Ease of starting / stopping workers and spinning up/down servers
-	3.) Ease of running multiple hubs for celery computing. ie: what happens when we one server can't handle all of the tasks associated with managing the workers and tasks


Commands
-


-	start up a worker

		`celery worker --app=src -l info`

