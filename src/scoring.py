import pandas as pd


def minmax(series):

    if series.max() == series.min():
        return series * 0

    return (series - series.min()) / (
        series.max() - series.min()
    )


def calculate_reuse_score(df):

    df = df.copy()

    df["greywater_score"] = minmax(
        df["greywater_tons_per_hour"]
    )

    if "urban_population_pct" in df.columns:

        df["urban_score"] = minmax(
            df["urban_population_pct"]
        )

    else:
        df["urban_score"] = 0.5

    df["reuse_potential_score"] = (
        70 * df["greywater_score"]
        + 30 * df["urban_score"]
    )

    df["reuse_potential_class"] = pd.cut(
        df["reuse_potential_score"],
        bins=[0, 40, 70, 100],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    return df
