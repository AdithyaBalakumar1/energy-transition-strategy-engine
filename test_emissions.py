from src.emissions import annual_emissions

cement = annual_emissions(
    "cement",
    1_000_000
)

steel = annual_emissions(
    "steel",
    1_000_000
)

refinery = annual_emissions(
    "refinery",
    1_000_000
)

print(
    f"Cement: {cement:,.0f} tCO₂/year"
)

print(
    f"Steel: {steel:,.0f} tCO₂/year"
)

print(
    f"Refinery: {refinery:,.0f} tCO₂/year"
)