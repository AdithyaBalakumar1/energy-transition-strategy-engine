def abatement_cost(
    transition_cost,
    emissions_avoided
):
    """
    Calculate cost per tonne of CO₂ avoided.

    Parameters
    ----------
    transition_cost : float
        Implementation cost ($)

    emissions_avoided : float
        CO₂ emissions avoided (t/year)

    Returns
    -------
    float
        Abatement cost ($/tCO₂)
    """

    if emissions_avoided == 0:
        return float("inf")

    return (
        transition_cost
        / emissions_avoided
    )
