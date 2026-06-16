from src.emissions import annual_emissions
from src.transition_models import evaluate_strategy

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

print("\n===== TRANSITION ANALYSIS =====\n")

for strategy in strategies:

    result = evaluate_strategy(
        emissions,
        strategy
    )

    print(
        f"\nStrategy: {result['strategy']}"
    )

    print(
        f"Reduction: "
        f"{result['reduction_percent']:.0f}%"
    )

    print(
        f"CO₂ Avoided: "
        f"{result['emissions_avoided']:,.0f} t/year"
    )

    print(
        f"Remaining Emissions: "
        f"{result['emissions_after']:,.0f} t/year"
    )

    print(
        f"Cost: "
        f"${result['cost']:,.0f}"
    )
