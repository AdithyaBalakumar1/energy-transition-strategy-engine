from src.emissions import annual_emissions

from src.transition_models import (
    evaluate_strategy
)

from src.recommendation import (
    recommend_strategy
)

emissions = annual_emissions(
    "cement",
    1_000_000
)

strategies = [
    "business_as_usual",
    "natural_gas",
    "renewables",
    "ccs",
    "green_hydrogen"
]

results = []

for strategy in strategies:

    results.append(
        evaluate_strategy(
            emissions,
            strategy
        )
    )

recommendation = recommend_strategy(
    transition_results=results,
    budget=150_000_000,
    target_reduction=30
)

print(
    "\n===== RECOMMENDATION ====="
)

if recommendation:

    print(
        f"\nRecommended Strategy: "
        f"{recommendation['strategy']}"
    )

    print(
        f"Reduction: "
        f"{recommendation['reduction_percent']:.0f}%"
    )

    print(
        f"Cost: "
        f"${recommendation['cost']:,.0f}"
    )

else:

    print(
        "\nNo feasible strategy found."
    )
