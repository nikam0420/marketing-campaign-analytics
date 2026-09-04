import pandas as pd

from extract_campaign_data import extract_campaign_data


def transform_campaign_data(campaign_data):
    transformed_data = campaign_data.copy()

    transformed_data["report_date"] = pd.to_datetime(
        transformed_data["report_date"]
    )

    numeric_columns = [
        "impressions",
        "clicks",
        "spend",
        "conversions",
        "revenue",
    ]

    transformed_data[numeric_columns] = transformed_data[
        numeric_columns
    ].apply(pd.to_numeric, errors="coerce")

    duplicate_rows = transformed_data.duplicated().sum()
    missing_values = transformed_data.isna().sum().sum()

    transformed_data = transformed_data.drop_duplicates()
    transformed_data = transformed_data.dropna()

    impressions_denominator = transformed_data["impressions"].where(
        transformed_data["impressions"] != 0
    )
    clicks_denominator = transformed_data["clicks"].where(
        transformed_data["clicks"] != 0
    )
    spend_denominator = transformed_data["spend"].where(
        transformed_data["spend"] != 0
    )

    transformed_data["ctr_percentage"] = (
        transformed_data["clicks"] * 100 / impressions_denominator
    ).round(2)

    transformed_data["conversion_rate_percentage"] = (
        transformed_data["conversions"] * 100 / clicks_denominator
    ).round(2)

    transformed_data["roas"] = (
        transformed_data["revenue"] / spend_denominator
    ).round(2)

    transformed_data["profit"] = (
        transformed_data["revenue"] - transformed_data["spend"]
    ).round(2)

    quality_summary = {
        "original_rows": len(campaign_data),
        "duplicate_rows": int(duplicate_rows),
        "missing_values": int(missing_values),
        "final_rows": len(transformed_data),
    }

    return transformed_data, quality_summary


if __name__ == "__main__":
    try:
        campaign_data = extract_campaign_data()

        transformed_data, quality_summary = transform_campaign_data(
            campaign_data
        )

        output_path = "data/processed/marketing_campaign_enriched.csv"

        transformed_data.to_csv(
            output_path,
            index=False,
        )

        print("Transformation completed successfully.")
        print(f"Transformed data saved to: {output_path}")
        print("\nData quality summary:")

        for check, result in quality_summary.items():
            print(f"{check}: {result}")

        print("\nTransformed columns:")
        print(transformed_data.columns.tolist())

        print("\nFirst 5 transformed rows:")
        print(
            transformed_data[
                [
                    "report_date",
                    "campaign_name",
                    "channel",
                    "ctr_percentage",
                    "conversion_rate_percentage",
                    "roas",
                    "profit",
                ]
            ].head()
        )

    except Exception as error:
        print(f"Transformation failed: {error}")