-- Find locations within 600 km of Berlin

SELECT
    city,
    country,
    ROUND(
        (
            ST_Distance(
                geometry::geography,
                (
                    SELECT geometry::geography
                    FROM locations
                    WHERE city = 'Berlin'
                )
            ) / 1000
        )::numeric,
        2
    ) AS distance_km
FROM locations
WHERE city <> 'Berlin'
  AND ST_DWithin(
        geometry::geography,
        (
            SELECT geometry::geography
            FROM locations
            WHERE city = 'Berlin'
        ),
        600000
      )
ORDER BY distance_km;