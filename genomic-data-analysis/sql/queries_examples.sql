
-- SQL query examples for the genomic SQLite database (genomics.db)

-- 1) Count samples per condition
SELECT condition, COUNT(*) as n_samples
FROM metadata
GROUP BY condition;

-- 2) Average expression of gene_0 by condition
SELECT m.condition, AVG(e.gene_0) as avg_gene_0
FROM expression e
JOIN metadata m USING(sample_id)
GROUP BY m.condition;

-- 3) Top 10 variants by average allele count
SELECT variant_id, AVG(allele_count) as mean_ac
FROM variants
GROUP BY variant_id
ORDER BY mean_ac DESC
LIMIT 10;

-- 4) Per-sample number of variants with at least one alt allele
SELECT sample_id, SUM(CASE WHEN allele_count>0 THEN 1 ELSE 0 END) as n_variants
FROM variants
GROUP BY sample_id
ORDER BY n_variants DESC
LIMIT 20;

-- 5) Join expression and variants: average expression of gene_1 for samples with variant var0 present (allele_count>0)
SELECT AVG(e.gene_1) as avg_gene1_in_var0_samples
FROM expression e
JOIN variants v USING(sample_id)
WHERE v.variant_id = 'var0' AND v.allele_count > 0;
