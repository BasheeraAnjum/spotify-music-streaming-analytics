-- Watermark Control Table
-- This table stores the last processed timestamp for incremental loading.

CREATE TABLE watermark_control (
    table_name VARCHAR(100),
    watermark_column VARCHAR(100),
    last_watermark_value DATETIME,
    updated_at DATETIME
);

INSERT INTO watermark_control
(table_name, watermark_column, last_watermark_value, updated_at)
VALUES
('spotify_tracks', 'last_updated', '2026-05-01 00:00:00', GETDATE());

-- Example incremental extraction query
SELECT *
FROM spotify_tracks
WHERE last_updated > (
    SELECT last_watermark_value
    FROM watermark_control
    WHERE table_name = 'spotify_tracks'
);
