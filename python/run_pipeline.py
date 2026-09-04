from analyze_campaign_performance import (
    summarize_daily_performance,
    summarize_performance,
)
from extract_campaign_data import extract_campaign_data
from transform_campaign_data import transform_campaign_data


ENRICHED_OUTPUT = (
    "data/processed/marketing_campaign_enriched.csv"
)
CHANNEL_OUTPUT = (
    "data/processed/channel_performance_summary.csv"
)
DEVICE_OUTPUT = (
    "data/processed/device_performance_summary.csv"
)
DAILY_OUTPUT = (
    "data/processed/daily_performance_summary.csv"
)


def run_pipeline():
    print("Starting marketing campaign analytics pipeline...")

    campaign_data = extract_campaign_data()
    print(f"Extracted {len(campaign_data)} rows from PostgreSQL.")

    transformed_data, quality_summary = transform_campaign_data(
        campaign_data
    )
    print(f"Transformed {len(transformed_data)} rows.")

    channel_performance = summarize_performance(
        transformed_data,
        "channel",
    )

    device_performance = summarize_performance(
        transformed_data,
        "device",
    )

    daily_performance = summarize_daily_performance(
        transformed_data
    )

    transformed_data.to_csv(
        ENRICHED_OUTPUT,
        index=False,
    )

    channel_performance.to_csv(
        CHANNEL_OUTPUT,
        index=False,
    )

    device_performance.to_csv(
        DEVICE_OUTPUT,
        index=False,
    )

    daily_performance.to_csv(
        DAILY_OUTPUT,
        index=False,
    )

    print("\nData quality summary:")

    for check, result in quality_summary.items():
        print(f"{check}: {result}")

    print("\nOutput files created:")
    print(ENRICHED_OUTPUT)
    print(CHANNEL_OUTPUT)
    print(DEVICE_OUTPUT)
    print(DAILY_OUTPUT)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    try:
        run_pipeline()

    except Exception as error:
        print(f"Pipeline failed: {error}")