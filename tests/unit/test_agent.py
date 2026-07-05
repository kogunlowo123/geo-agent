"""GEO Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_audit_ai_visibility():
    """Test Audit brand visibility in AI search results and chatbot responses."""
    tools = AgentTools()
    result = await tools.audit_ai_visibility(brand_name="test", queries="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_for_llm():
    """Test Optimize content structure for LLM citation and extraction."""
    tools = AgentTools()
    result = await tools.optimize_for_llm(content="test", target_queries="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_ai_mentions():
    """Test Track brand mentions in AI-generated content."""
    tools = AgentTools()
    result = await tools.track_ai_mentions(brand_name="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_structured_data():
    """Test Generate structured data markup for AI crawlers."""
    tools = AgentTools()
    result = await tools.generate_structured_data(page_url="test", content_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.geo_agent_agent import GeoAgentAgent
    agent = GeoAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
