def recommend_treatment_methods(row):
    greywater = row.get("greywater_tons_per_hour", 0)
    reuse_class = row.get("predicted_reuse_class", "Medium")

    recommendations = []

    if greywater > 1_000_000:
        recommendations.extend([
            "MBR",
            "SBR",
            "MBBR",
            "Tertiary Filtration",
            "UV Disinfection"
        ])

    elif greywater > 100_000:
        recommendations.extend([
            "SBR",
            "MBBR",
            "Sand Filtration",
            "Chlorination"
        ])

    else:
        recommendations.extend([
            "Constructed Wetlands",
            "Sand Filtration",
            "UV Disinfection",
            "Decentralized Greywater Reuse"
        ])

    if reuse_class in ["Low", "Moderate"]:
        recommendations.append("Policy + Dual Plumbing Upgrade")

    return ", ".join(recommendations)
