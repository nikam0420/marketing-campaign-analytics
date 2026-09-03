-- Marketing Campaign Performance Analytics
-- Data quality and import validation checks

-- 1. Verify row count, ID range and reporting period
SELECT
    COUNT(*) AS total_rows,
    MIN(record_id) AS first_record_id,
    MAX(record_id) AS last_record_id,
    MIN(report_date) AS first_date,
    MAX(report_date) AS last_date
FROM campaign_performance;


-- 2. Check whether important columns contain missing values
SELECT
    COUNT(*) AS total_rows,
    COUNT(report_date) AS valid_dates,
    COUNT(campaign_name) AS valid_campaigns,
    COUNT(channel) AS valid_channels,
    COUNT(device) AS valid_devices,
    COUNT(impressions) AS valid_impressions,
    COUNT(clicks) AS valid_clicks,
    COUNT(spend) AS valid_spend,
    COUNT(conversions) AS valid_conversions,
    COUNT(revenue) AS valid_revenue
FROM campaign_performance;


-- 3. Identify negative or logically impossible values
SELECT *
FROM campaign_performance
WHERE impressions < 0
   OR clicks < 0
   OR spend < 0
   OR conversions < 0
   OR revenue < 0
   OR clicks > impressions
   OR conversions > clicks;


-- 4. Confirm record coverage across marketing channels
SELECT
    channel,
    COUNT(*) AS number_of_records
FROM campaign_performance
GROUP BY channel
ORDER BY channel;