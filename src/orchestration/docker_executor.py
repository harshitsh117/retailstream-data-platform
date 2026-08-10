import docker
from docker.errors import NotFound


class DockerExecutor:

    def __init__(self, container_name="retailstream-spark"):

        self.client = docker.from_env()

        try:
            self.container = self.client.containers.get(container_name)
        except NotFound:
            raise RuntimeError(
                f"Container '{container_name}' is not running."
            )

    def run(self, command: str):

        print(f"\nExecuting inside {self.container.name}")
        print(f"Command: {command}\n")

        exit_code, output = self.container.exec_run(command)

        print(output.decode())

        if exit_code != 0:
            raise RuntimeError(output.decode())

    def run_script(self, script_name: str):
        """
        Execute a Python script inside the Spark container.
        """
        self.run(f"python3 {script_name}")