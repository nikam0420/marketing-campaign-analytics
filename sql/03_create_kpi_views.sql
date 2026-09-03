-- Marketing Campaign Performance Analytics
-- Creates reusable KPI views for analysis and Power BI


-- 1. Record-level KPI view
CREATE OR REPLACE VIEW campaign_performance_kpis AS
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
    revenue,

    ROUND(clicks * 100.0 / NULLIF(impressions, 0), 2)
        AS ctr_percentage,

    ROUND(spend / NULLIF(clicks, 0), 2)
        AS cpc,

    ROUND(spend * 1000.0 / NULLIF(impressions, 0), 2)
        AS cpm,

    ROUND(conversions * 100.0 / NULLIF(clicks, 0), 2)
        AS conversion_rate_percentage,

    ROUND(revenue / NULLIF(spend, 0), 2)
        AS roas,

    ROUND(revenue - spend, 2)
        AS profit

FROM campaign_performance;


-- 2. Channel-level performance summary
CREATE OR REPLACE VIEW channel_performance_summary AS
SELECT
    channel,
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
        SUM(spend) / NULLIF(SUM(clicks), 0),
        2
    ) AS cpc,

    ROUND(
        SUM(spend) * 1000.0 / NULLIF(SUM(impressions), 0),
        2
    ) AS cpm,

    ROUND(
        SUM(conversions) * 100.0 / NULLIF(SUM(clicks), 0),
        2
    ) AS conversion_rate_percentage,

    ROUND(
        SUM(revenue) / NULLIF(SUM(spend), 0),
        2
    ) AS roas,

    ROUND(SUM(revenue) - SUM(spend), 2) AS profit

FROM campaign_performance
GROUP BY channel;