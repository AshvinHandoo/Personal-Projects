# Genomic Data Analysis (in-progress)

Status: in progress

## Tech stack
SQLite, SQL, R, tidyverse, ggplot2, RSQLite

## Project summary
This project demonstrates basic genomic data analysis on synthetic data.
It includes:
- A SQLite database with expression, variant, and metadata tables
- Example SQL queries
- R scripts and an RMarkdown report that perform EDA, PCA, and plots using ggplot2

## Run locally
1. Install R packages (in R):
```r
install.packages(c("DBI","RSQLite","tidyverse","ggplot2"))
```
2. Open the R script or the RMarkdown file in RStudio and run.
3. Or run the R script from the command line:
```bash
Rscript R/genomic_analysis.R
```

## Files
- `data/` CSVs with synthetic data
- `sql/genomics.db` SQLite database
- `sql/queries_examples.sql` sample SQL queries
- `R/genomic_analysis.R` analysis script
- `R/genomic_analysis.Rmd` RMarkdown report
- `results/` output images and CSVs created by the R script

## Notes
Replace the synthetic data with real data and update analysis accordingly.
