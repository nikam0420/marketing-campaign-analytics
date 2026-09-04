# Marketing Campaign Performance Analytics

## Project Overview

This project analyzes marketing campaign performance using PostgreSQL, SQL, and Python

The goal is to transform raw campaign data into business insights that can help marketing teams understand which campaigns, channels, and devices are performing most effectively.

## Business Questions

This analysis focuses on answering the following questions:

1. What is the overall performance of the marketing campaigns?
2. Which marketing channels generate the highest ROAS?
3. Which campaigns perform best based on spend, revenue, conversions, and ROAS?
4. How does marketing performance differ across devices?
5. How do advertising spend, revenue, and profit change over time?

## Tools & Technologies

- Python
- pandas
- SQLAlchemy

## SQL Analysis

The SQL workflow is organized into four stages:

- `01_create_table.sql` - Creates the campaign performance table.
- `02_data_quality_checks.sql` - Performs data quality and validation checks.
- `03_create_kpi_views.sql` - Creates reusable views for marketing KPIs.
- `04_business_analysis.sql` - Performs campaign, channel, device, and daily trend analysis.

## Python ETL Pipeline

The Python workflow connects to PostgreSQL, extracts campaign data into a pandas DataFrame, validates data quality, calculates additional KPIs, and saves an analysis-ready CSV.

- `db_connection.py` - Creates a reusable and secure PostgreSQL connection.
- `extract_campaign_data.py` - Extracts 180 campaign records from PostgreSQL.
- `transform_campaign_data.py` - Checks data quality, calculates CTR, conversion rate, ROAS, and profit, and saves the transformed output.
- `marketing_campaign_enriched.csv` - Contains the processed data with calculated KPI columns.
- `analyze_campaign_performance.py` - Aggregates channel performance, ranks channels by ROAS, and validates the SQL findings.
- `channel_performance_summary.csv` - Contains the channel-level summary prepared for reporting and Power BI.

The dataset passed the Python quality checks with 0 duplicate rows, 0 missing values, and all 180 rows retained.

## Key Metrics

The analysis includes:

- Impressions
- Clicks
- Click-Through Rate (CTR)
- Advertising Spend
- Conversions
- Revenue
- Profit
- Return on Ad Spend (ROAS)

## Key Insights

- Email was the most efficient marketing channel, achieving a ROAS of 22.65.
- Mobile generated the highest overall volume in impressions, clicks, conversions, and revenue.
- Tablet achieved the highest device-level CTR and ROAS.
- Campaign performance was analyzed over time using daily spend, revenue, and profit trends.

## Project Structure
```text
marketing-campaign-analytics/
├── data/
│   ├── marketing_campaign_data.csv
│   └── processed/
│       └── marketing_campaign_enriched.csv
├── sql/
│   ├── 01_create_table.sql
│   ├── 02_data_quality_checks.sql
│   ├── 03_create_kpi_views.sql
│   └── 04_business_analysis.sql
├── python/
│   ├── db_connection.py
│   ├── extract_campaign_data.py
│   ├── transform_campaign_data.py
│   └── analyze_campaign_performance.py
├── powerbi/
├── images/
├── .gitignore
├── requirements.txt
└── README.md
│   └── processed/
│       ├── marketing_campaign_enriched.csv
│       └── channel_performance_summary.csv
```
## Future Development

- Build an interactive Power BI dashboard using the processed campaign dataset.
- Add dbt models for reusable analytics transformations and testing.
- Orchestrate the ETL workflow with Apache Airflow.
- Extend the pipeline to AWS for cloud-based storage and processing.