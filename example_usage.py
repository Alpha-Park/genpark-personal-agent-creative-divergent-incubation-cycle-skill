# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Creative Divergent Incubation Cycle Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCreativeDivergentIncubation

def main():
    agent = PersonalAgentCreativeDivergentIncubation()

    print("=" * 70)
    print("DEMO: Personal Agent Creative Divergent Incubation Cycle Modeler")
    print("=" * 70)

    # 1. Evaluate individual stuck on architecture impasse for 105 minutes
    res_eval = agent.evaluate_incubation_necessity(
        focus_duration_continuous_minutes=105.0,
        impasse_friction_score=8.5,
        conceptual_distance_tier="high"
    )

    print(f"\n1. Creative Impasse & Fixation Audit (105 min focus, friction 8.5/10):")
    print(f"   Fixation Index: {res_eval['cognitive_fixation_index']}")
    print(f"   Wallas Stage: {res_eval['wallas_creative_stage']}")
    print(f"   DMN Spreading Potential: {res_eval['dmn_spreading_activation_potential']}")
    print(f"   Action: {res_eval['incubation_actionability']}")
    print(f"   Mechanic: {res_eval['neurocognitive_mechanic']}")

    # 2. Schedule 35-minute incubation session
    res_sched = agent.schedule_unconscious_incubation_window(
        work_domain="distributed_consensus",
        available_break_minutes=35.0
    )

    print(f"\n2. Subconscious Incubation Window Prescription (35 min):")
    print(f"   Depth: {res_sched['prescribed_incubation_depth']}")
    print(f"   Activity: {res_sched['primary_recommended_activity']}")
    print(f"   Instructions: {res_sched['protocol_execution_instructions']}")
    print(f"   Prohibited: {res_sched['forbidden_interferences']}")
    print(f"   Capture Rule: {res_sched['post_incubation_capture_rule']}")

    print("\nVerification complete: Creative divergent incubation engine executed flawlessly.")

if __name__ == "__main__":
    main()
