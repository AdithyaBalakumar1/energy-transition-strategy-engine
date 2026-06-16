# src/emissions.py

EMISSION_FACTORS = {
    "cement": 0.85,
    "steel": 1.90,
    "refinery": 0.40
}


def annual_emissions(industry, production):
    """
    Calculate annual CO₂ emissions.

    Parameters
    ----------
    industry : str
        Industry type:
        - cement
        - steel
        - refinery

    production : float
        Annual production in tonnes.

    Returns
    -------
    float
        Annual CO₂ emissions (tonnes/year).
    """

    industry = industry.lower()

    if industry not in EMISSION_FACTORS:
        raise ValueError(
            f"Unsupported industry: {industry}"
        )

    return (
        production
        * EMISSION_FACTORS[industry]
    )