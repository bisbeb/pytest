import pytest
from test_setup import state


@pytest.fixture
def init_session():
  x = state.init()
  yield x
  state.cleanup()

def test_run(init_session):
  assert 2 == init_session
