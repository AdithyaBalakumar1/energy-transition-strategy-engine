def recommend_strategy(
    transition_results,
    budget,
    target_reduction
):
    """
    Recommend the best transition pathway.

    Parameters
    ----------
    transition_results : list
        List of strategy dictionaries

    budget : float
        Maximum allowable cost ($)

    target_reduction : float
        Minimum emission reduction (%)

    Returns
    -------
    dict
    """

    feasible = []

    for strategy in transition_results:

        if (
            strategy["cost"] <= budget
            and strategy["reduction_percent"]
            >= target_reduction
        ):

            feasible.append(strategy)

    if not feasible:

        return None

    return min(
        feasible,
        key=lambda x: x["cost"]
    )
