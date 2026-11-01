# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Creative Divergent Incubation Cycle Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCreativeDivergentIncubation

mcp = FastMCP("PersonalAgentCreativeDivergentIncubation")
client = PersonalAgentCreativeDivergentIncubation()

@mcp.tool()
def evaluate_incubation_necessity(
    focus_duration_continuous_minutes: float,
    impasse_friction_score: float = 7.5,
    conceptual_distance_tier: str = "high"
) -> str:
    """Evaluates cognitive impasse fixation index and DMN associative spreading activation potential."""
    import json
    return json.dumps(client.evaluate_incubation_necessity(
        focus_duration_continuous_minutes, impasse_friction_score, conceptual_distance_tier
    ), indent=2)

@mcp.tool()
def schedule_unconscious_incubation_window(
    work_domain: str = "software_architecture",
    available_break_minutes: float = 30.0
) -> str:
    """Prescribes optimal low-demand Default Mode Network incubation activities and capture rules."""
    import json
    return json.dumps(client.schedule_unconscious_incubation_window(
        work_domain, available_break_minutes
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
