from extract_campaign_data import extract_campaign_data
from transform_campaign_data import transform_campaign_data


def summarize_performance(transformed_data, dimension):
    performance_summary = (
        transformed_data.groupby(
            dimension,
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

    impressions_denominator = performance_summary[
        "total_impressions"
    ].where(
        performance_summary["total_impressions"] != 0
    )

    spend_denominator = performance_summary["total_spend"].where(
        performance_summary["total_spend"] != 0
    )

    performance_summary["ctr_percentage"] = (
        performance_summary["total_clicks"]
        * 100
        / impressions_denominator
    ).round(2)

    performance_summary["roas"] = (
        performance_summary["total_revenue"]
        / spend_denominator
    ).round(2)

    performance_summary["profit"] = (
        performance_summary["total_revenue"]
        - performance_summary["total_spend"]
    ).round(2)

    performance_summary = performance_summary.sort_values(
        by="roas",
        ascending=False,
    )

    return performance_summary


if __name__ == "__main__":
    try:
        campaign_data = extract_campaign_data()

        transformed_data, quality_summary = transform_campaign_data(
            campaign_data
        )

        channel_performance = summarize_performance(
            transformed_data,
            "channel",
        )

        device_performance = summarize_performance(
            transformed_data,
            "device",
        )

        channel_output_path = (
            "data/processed/channel_performance_summary.csv"
        )
        device_output_path = (
            "data/processed/device_performance_summary.csv"
        )

        channel_performance.to_csv(
            channel_output_path,
            index=False,
        )

        device_performance.to_csv(
            device_output_path,
            index=False,
        )

        print("Campaign analysis completed successfully.")
        print(f"Channel summary saved to: {channel_output_path}")
        print(f"Device summary saved to: {device_output_path}")

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

        print("\nDevices ranked by ROAS:")
        print(
            device_performance[
                [
                    "device",
                    "total_impressions",
                    "total_clicks",
                    "total_conversions",
                    "total_revenue",
                    "ctr_percentage",
                    "roas",
                ]
            ].to_string(index=False)
        )

    except Exception as error:
        print(f"Campaign analysis failed: {error}")