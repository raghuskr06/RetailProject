# this file is created to do the setup part for fixtures and also tear down, and code will automatically
# know that fixtures are defined here.

import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    "creates a spark session"
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    # after yield and before stoping the session, all the unit tests will run
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    "gives the expected results"
    results_schema = "state string,count int"
    return spark.read \
        .format("csv") \
        .schema(results_schema) \
        .load("data/test_result/state_aggregate.csv")