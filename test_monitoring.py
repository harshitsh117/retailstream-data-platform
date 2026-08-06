from src.monitoring.models import PipelineExecution


def main():

    execution = PipelineExecution(
        pipeline_name="Bronze",
        layer="bronze",
    )

    print(execution)


if __name__ == "__main__":
    main()