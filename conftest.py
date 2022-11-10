import pytest
import random
import main as m


@pytest.fixture(scope="module")
def random_labels():
    response = m.get_labels()
    random_labels = ",".join(random.sample(response.json()["data"]["labels"], k=3))
    return random_labels
