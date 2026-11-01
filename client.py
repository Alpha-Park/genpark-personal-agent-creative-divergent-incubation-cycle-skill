# -*- coding: utf-8 -*-
"""
Personal Agent Creative Divergent Incubation Cycle Client
Zero-dependency Graham Wallas 4-stage creativity modeler, cognitive impasse fixation detector,
Default Mode Network (DMN) spreading activation calculator, and incubation scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentCreativeDivergentIncubation:
    """
    Detects prefrontal executive cognitive fixation, models subconscious associative spreading
    activation in the Default Mode Network (DMN), and schedules strategic incubation breaks.
    """

    def evaluate_incubation_necessity(
        self,
        focus_duration_continuous_minutes: float,
        impasse_friction_score: float = 7.5,
        conceptual_distance_tier: str = "high"
    ) -> Dict[str, Any]:
        """
        Evaluates whether an analytical impasse requires strategic disengagement.
        Continuous linear focus beyond 75-90 minutes narrows the semantic search space,
        causing cognitive fixation and suppressing novel lateral connections.
        """
        dur = max(5.0, min(360.0, float(focus_duration_continuous_minutes)))
        friction = max(1.0, min(10.0, float(impasse_friction_score)))
        tier = str(conceptual_distance_tier).lower()

        distance_weight = 1.4 if "high" in tier or "novel" in tier else (1.0 if "med" in tier else 0.7)

        # Cognitive Fixation Index (0 - 100)
        # Fixation escalates with duration and subjective impasse friction
        fixation_index = round(min(100.0, (dur * 0.42) + (friction * 6.5 * distance_weight)), 1)

        # Default Mode Network (DMN) associative potential if disengaged
        dmn_potential_pct = round(min(96.0, 40.0 + (friction * 4.5) + (dur * 0.15)), 1)

        if fixation_index >= 75.0:
            stage = "Stage 2: Critical Incubation Mandate (Impasse Fixation)"
            action = "IMMEDIATE DISENGAGEMENT: Prefrontal cortex is actively blocking lateral associative pathways. Cease direct problem-solving."
            dmn_benefit = "High: Subconscious combinatorial synthesis will operate unconstrained once executive suppression lifts."
        elif fixation_index >= 45.0:
            stage = "Stage 1: Late Preparation Phase (Approaching Fixation)"
            action = "PREPARE TO DISENGAGE: Log core constraints clearly on paper, then transition to an incubation block within 15 minutes."
            dmn_benefit = "Moderate: Prime semantic nodes before stepping away."
        else:
            stage = "Stage 1: Active Preparation & Focused Data Ingestion"
            action = "CONTINUE DIRECT FOCUS: Prefrontal working memory is actively digesting architecture and problem constraints."
            dmn_benefit = "Low: More raw data ingestion required before incubation is productive."

        return {
            "continuous_focus_minutes": dur,
            "impasse_subjective_friction_score": f"{friction} / 10",
            "cognitive_fixation_index": f"{fixation_index} / 100",
            "wallas_creative_stage": stage,
            "dmn_spreading_activation_potential": f"{dmn_potential_pct}%",
            "incubation_actionability": action,
            "neurocognitive_mechanic": dmn_benefit
        }

    def schedule_unconscious_incubation_window(
        self,
        work_domain: str = "software_architecture",
        available_break_minutes: float = 30.0
    ) -> Dict[str, Any]:
        """
        Prescribes optimal low-cognitive-demand incubation activities that maximize
        default mode network (DMN) mind-wandering without hijacking working memory.
        """
        mins = max(10.0, min(180.0, float(available_break_minutes)))
        domain = str(work_domain).lower()

        # Low-demand incubation modalities that activate default mode network (DMN)
        # Avoid podcasts, social media, or high-friction tasks which re-engage executive control
        modalities = [
            ("Unconstrained Walking Ambulation", "Outdoor walk in nature or low-traffic environment with ZERO audio input. Locomotion drives dopamine and loose associative flow."),
            ("Passive Hydrotherapy (Warm Shower)", "Warm water tactile stimulation relaxes sympathetic tone and induces diffuse hypnagogic alpha oscillations."),
            ("Low-Friction Mechanical Tidying", "Organizing physical desk or dishwashing; occupies minimal working memory while liberating subconscious processing."),
            ("Visual Daydreaming / Window Gazing", "Soft visual gaze out a window with unguided mental drift; allows disparate semantic clusters to intersect.")
        ]

        # Recommended incubation duration
        if mins < 20.0:
            incubation_depth = "Micro-Incubation (Quick semantic reset)"
            selected = modalities[0]
        elif mins <= 45.0:
            incubation_depth = "Optimal Standard Incubation (Full associative spreading activation)"
            selected = modalities[0]
        else:
            incubation_depth = "Deep Macro-Incubation (Overnight consolidation / Major breakthrough window)"
            selected = modalities[1]

        return {
            "available_incubation_window_minutes": mins,
            "prescribed_incubation_depth": incubation_depth,
            "primary_recommended_activity": selected[0],
            "protocol_execution_instructions": selected[1],
            "forbidden_interferences": "STRICTLY PROHIBITED: Podcasts, algorithmic feeds, text messaging, or administrative email. These consume working memory and abort DMN incubation.",
            "post_incubation_capture_rule": "Keep an analog pocket notebook ready. The moment illumination (Eureka insight) strikes, record raw thoughts immediately before executive filtering."
        }
