"""Test configuration for GEO Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "geo-agent", "category": "Marketing"}
