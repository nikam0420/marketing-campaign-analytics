from extract_campaign_data import extract_campaign_data
from transform_campaign_data import transform_campaign_data


def analyze_channel_performance(transformed_data):
    channel_performance = (
        transformed_data.groupby(
            "channel",
            as_index=False,
        )
        .agg(
            total_impressions=("impressions", "sum"),
            total_clicks=("clicks", "sum"),
            total_spend=("spend", "sum"),
            total_conversions=("conversions", "sum"),
            total_revenue=("revenue", "sum"),
        )
    )

    channel_performance["ctr_percentage"] = (
        channel_performance["total_clicks"]
        * 100
        / channel_performance["total_impressions"]
    ).round(2)

    channel_performance["roas"] = (
        channel_performance["total_revenue"]
        / channel_performance["total_spend"]
    ).round(2)

    channel_performance["profit"] = (
        channel_performance["total_revenue"]
        - channel_performance["total_spend"]
    ).round(2)

    channel_performance = channel_performance.sort_values(
        by="roas",
        ascending=False,
    )

    return channel_performance


if __name__ == "__main__":
    try:
        campaign_data = extract_campaign_data()

        transformed_data, quality_summary = transform_campaign_data(
            campaign_data
        )

        channel_performance = analyze_channel_performance(
            transformed_data
        )

        output_path = "data/processed/channel_performance_summary.csv"

        channel_performance.to_csv(
            output_path,
            index=False,
        )

        print("Channel analysis completed successfully.")
        print(f"Channel summary saved to: {output_path}")
        print("\nChannels ranked by ROAS:")

        print(
            channel_performance[
                [
                    "channel",
                    "total_spend",
                    "total_revenue",
                    "roas",
                    "profit",
                ]
            ].to_string(index=False)
        )

    except Exception as error:
        print(f"Channel analysis failed: {error}")