def estimate_greywater(df, water_col, greywater_fraction=0.65):

    df = df.copy()

    df["estimated_greywater_m3_year"] = (
        df[water_col] * greywater_fraction
    )

    df["greywater_tons_per_hour"] = (
        df["estimated_greywater_m3_year"] / 365 / 24
    )

    return df
