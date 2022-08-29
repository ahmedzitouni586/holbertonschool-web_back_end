-- SQL script that lists all bands with Glam rock as their main style,
-- Column names must be: band_name and lifespan (in years),
-- You should use attributes formed and split for computing the lifespan,

SELECT band_name, IFNULL(split, YEAR(CURDATE())) - formed as lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';
