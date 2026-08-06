from src.orchestration.docker_executor import DockerExecutor

executor = DockerExecutor()

executor.run_script("run_spark_bronze.py")