-- Marketing Campaign Performance Analytics
-- Business analysis queries


-- 1. Overall campaign performance
SELECT
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spend), 2) AS total_spend,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(revenue) - SUM(spend), 2) AS profit,
    ROUND(
        SUM(revenue) / NULLIF(SUM(spend), 0),
        2
    ) AS overall_roas
FROM campaign_performance;


-- 2. Rank marketing channels by ROAS
SELECT
    channel,
    total_spend,
    total_revenue,
    roas,
    profit
FROM channel_performance_summary
ORDER BY roas DESC;


-- 3. Compare campaign performance
SELECT
    campaign_name,
    ROUND(SUM(spend), 2) AS total_spend,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        SUM(revenue) / NULLIF(SUM(spend), 0),
        2
    ) AS roas
FROM campaign_performance
GROUP BY campaign_name
ORDER BY roas DESC;


-- 4. Compare performance by device
SELECT
    device,
    SUM(impressions) AS total_impressions,
    SUM(clicks) AS total_clicks,
    ROUND(SUM(spend), 2) AS total_spend,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        SUM(clicks) * 100.0 / NULLIF(SUM(impressions), 0),
        2
    ) AS ctr_percentage,
    ROUND(
        SUM(revenue) / NULLIF(SUM(spend), 0),
        2
    ) AS roas
FROM campaign_performance
GROUP BY device
ORDER BY roas DESC;


-- 5. Analyze daily revenue and spend trends
SELECT
    report_date,
    ROUND(SUM(spend), 2) AS daily_spend,
    ROUND(SUM(revenue), 2) AS daily_revenue,
    ROUND(SUM(revenue) - SUM(spend), 2) AS daily_profit
FROM campaign_performance
GROUP BY report_date
ORDER BY report_date;