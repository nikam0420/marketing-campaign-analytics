import pandas as pd
from sqlalchemy import text

from db_connection import get_engine


query = """
SELECT
    record_id,
    report_date,
    campaign_name,
    channel,
    device,
    impressions,
    clicks,
    spend,
    conversions,
    revenue
FROM campaign_performance
ORDER BY report_date, record_id;
"""

engine = get_engine()

try:
    with engine.connect() as connection:
        campaign_data = pd.read_sql(
            text(query),
            connection,
        )

    print("Campaign data extracted successfully.")
    print(f"Rows: {campaign_data.shape[0]}")
    print(f"Columns: {campaign_data.shape[1]}")
    print("\nFirst 5 rows:")
    print(campaign_data.head())

except Exception as error:
    print(f"Data extraction failed: {error}")

finally:
    engine.dispose()