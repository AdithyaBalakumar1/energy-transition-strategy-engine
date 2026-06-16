from src.emissions import annual_emissions

from src.transition_models import (
    evaluate_strategy
)

from src.economics import (
    abatement_cost
)

emissions = annual_emissions(
    "cement",
    1_000_000
)

strategies = [
    "natural_gas",
    "renewables",
    "ccs",
    "green_hydrogen"
]

print(
    "\n===== ECONOMIC ANALYSIS ====="
)

for strategy in strategies:

    result = evaluate_strategy(
        emissions,
        strategy
    )

    cost = abatement_cost(
        result["cost"],
        result["emissions_avoided"]
    )

    print(
        f"\n{strategy.upper()}"
    )

    print(
        f"Cost per tCO₂ avoided: "
        f"${cost:,.2f}"
    )
