# genomic_analysis.R
# Requires R packages: DBI, RSQLite, tidyverse, ggplot2
library(DBI)
library(RSQLite)
library(tidyverse)

db <- dbConnect(RSQLite::SQLite(), "sql/genomics.db")

# Load metadata and simple EDA
meta <- dbGetQuery(db, "SELECT * FROM metadata")
head(meta)

# Distribution of conditions
meta %>% count(condition) %>% print()

# Load expression for a few genes (to keep memory small)
expr <- dbGetQuery(db, "SELECT sample_id, gene_0, gene_1, gene_2, gene_3, gene_4 FROM expression")
expr <- as_tibble(expr) %>% left_join(meta, by="sample_id")

# Boxplot gene_0 by condition
p1 <- ggplot(expr, aes(x=condition, y=gene_0)) +
  geom_boxplot() + theme_minimal() + ggtitle("gene_0 expression by condition")
ggsave("results/gene0_by_condition.png", p1, width=6, height=4, dpi=150)

# PCA on top genes
expr_matrix <- dbGetQuery(db, "SELECT * FROM expression")
expr_matrix <- expr_matrix %>% select(starts_with("gene_")) %>% as.matrix()
rownames(expr_matrix) <- dbGetQuery(db, "SELECT sample_id FROM expression")$sample_id
# simple log transform
expr_log <- log1p(expr_matrix)
pca <- prcomp(expr_log, center=TRUE, scale.=TRUE)
pca_df <- as_tibble(pca$x[,1:3]) %>% mutate(sample_id = rownames(pca$x)) %>% left_join(meta, by="sample_id")

p2 <- ggplot(pca_df, aes(x=PC1, y=PC2, color=condition)) + geom_point(alpha=0.7) + theme_minimal() + ggtitle("PCA of expression (PC1 vs PC2)")
ggsave("results/pca_pc1_pc2.png", p2, width=6, height=5, dpi=150)

# Variant summary: top variants by mean allele count
top_vars <- dbGetQuery(db, "SELECT variant_id, AVG(allele_count) as mean_ac FROM variants GROUP BY variant_id ORDER BY mean_ac DESC LIMIT 10")
write_csv(top_vars, "results/top_variants.csv")

# Per-sample variant burden
sample_burden <- dbGetQuery(db, "SELECT sample_id, SUM(CASE WHEN allele_count>0 THEN 1 ELSE 0 END) as n_variants FROM variants GROUP BY sample_id")
sample_burden <- as_tibble(sample_burden) %>% left_join(meta, by="sample_id")
p3 <- ggplot(sample_burden, aes(x=n_variants)) + geom_histogram(bins=30) + theme_minimal() + ggtitle("Per-sample variant burden")
ggsave("results/variant_burden_hist.png", p3, width=6, height=4, dpi=150)

dbDisconnect(db)
