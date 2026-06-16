# src/transition_models.py

TRANSITION_STRATEGIES = {
    "business_as_usual": {
        "reduction": 0.00,
        "cost": 0
    },

    "natural_gas": {
        "reduction": 0.25,
        "cost": 80_000_000
    },

    "renewables": {
        "reduction": 0.35,
        "cost": 120_000_000
    },

    "ccs": {
        "reduction": 0.90,
        "cost": 250_000_000
    },

    "green_hydrogen": {
        "reduction": 0.75,
        "cost": 300_000_000
    }
}


def evaluate_strategy(
    emissions,
    strategy
):
    """
    Evaluate an energy transition strategy.

    Parameters
    ----------
    emissions : float
        Annual CO₂ emissions (t/year)

    strategy : str
        Selected transition pathway

    Returns
    -------
    dict
    """

    strategy = strategy.lower()

    if strategy not in TRANSITION_STRATEGIES:
        raise ValueError(
            f"Unknown strategy: {strategy}"
        )

    reduction = (
        TRANSITION_STRATEGIES[strategy]
        ["reduction"]
    )

    cost = (
        TRANSITION_STRATEGIES[strategy]
        ["cost"]
    )

    emissions_after = (
        emissions
        * (1 - reduction)
    )

    emissions_avoided = (
        emissions
        - emissions_after
    )

    return {
        "strategy": strategy,
        "reduction_percent":
            reduction * 100,

        "emissions_after":
            emissions_after,

        "emissions_avoided":
            emissions_avoided,

        "cost":
            cost
    }
