from dagster import execute_pipeline
from docs_snippets.overview.object_managers.root_input_manager import my_pipeline


def test_execute_pipeline():
    execute_pipeline(my_pipeline)
