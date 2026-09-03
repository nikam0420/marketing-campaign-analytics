-- Marketing Campaign Performance Analytics
-- Creates the main table used to store campaign-level data

CREATE TABLE IF NOT EXISTS campaign_performance (
    record_id SERIAL PRIMARY KEY,
    report_date DATE NOT NULL,
    campaign_name VARCHAR(100) NOT NULL,
    channel VARCHAR(50) NOT NULL,
    device VARCHAR(50) NOT NULL,
    impressions INTEGER NOT NULL,
    clicks INTEGER NOT NULL,
    spend DECIMAL(10, 2) NOT NULL,
    conversions INTEGER NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL
);