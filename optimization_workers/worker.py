# worker.py
from celery import Celery
import subprocess

app = Celery("tasks", broker="redis://redis:6379/0")


@app.task
def run_gurobi(task_data):
    # Spawn a Gurobi container and run the optimization
    # This is a simplified example; you'll need to adjust it based on your specific requirements
    # TODO fix nonsense
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            "/path/to/your/gurobi/license:/opt/gurobi/gurobi.lic:ro",
            "gurobi/compute",
            "your_gurobi_command_here",
        ]
    )
    # Process the task_data and return the result
    return "Task completed"
