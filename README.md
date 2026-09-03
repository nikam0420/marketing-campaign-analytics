# Marketing Campaign Performance Analytics

## Project Overview

This project analyzes marketing campaign performance using PostgreSQL and SQL to identify trends in advertising spend, revenue, conversions, profitability, and return on ad spend (ROAS).

The goal is to transform raw campaign data into business insights that can help marketing teams understand which campaigns, channels, and devices are performing most effectively.

## Business Questions

This analysis focuses on answering the following questions:

1. What is the overall performance of the marketing campaigns?
2. Which marketing channels generate the highest ROAS?
3. Which campaigns perform best based on spend, revenue, conversions, and ROAS?
4. How does marketing performance differ across devices?
5. How do advertising spend, revenue, and profit change over time?

## Tools & Technologies

- PostgreSQL
- SQL
- pgAdmin
- Git
- GitHub

## SQL Analysis

The SQL workflow is organized into four stages:

- `01_create_table.sql` - Creates the campaign performance table.
- `02_data_quality_checks.sql` - Performs data quality and validation checks.
- `03_create_kpi_views.sql` - Creates reusable views for marketing KPIs.
- `04_business_analysis.sql` - Performs campaign, channel, device, and daily trend analysis.

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
│   └── marketing_campaign_data.csv
├── sql/
│   ├── 01_create_table.sql
│   ├── 02_data_quality_checks.sql
│   ├── 03_create_kpi_views.sql
│   └── 04_business_analysis.sql
├── python/
├── powerbi/
├── images/
└── README.md