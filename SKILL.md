---
description: E-Commerce Market Analyzer. Automates data cleaning, trend analysis, and genre performance reporting for sales datasets.
license: MIT
metadata:
  last_deployed: "2026-04-25"
  version: "1.0.0"
  source: "https://github.com/anikaahluwalia/amazon-best-sellers-analysis"
---

# Amazon Market Analyzer

This skill enables AI agents to process large-scale e-commerce datasets to extract actionable market insights. It specializes in cleaning raw sales data and identifying multi-year trends in pricing and popularity.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Instructions
1. **Data Normalization:** Automatically clean duplicates, standardize column names (e.g., 'User Rating' to 'Rating'), and handle missing values.
2. **Trend Analysis:** Segment sales data by category (e.g., Fiction vs. Non-Fiction) and calculate average pricing and ratings over time.
3. **Entity Ranking:** Identify top-performing entities (authors, brands, or products) based on frequency and customer feedback.
4. **Insight Generation:** Produce a structured summary of market shifts, highlighting the most profitable or highest-rated niches.

## Examples
- "Analyze this CSV of Amazon best sellers and tell me which genre has had the highest average rating over the last 10 years."
- "Identify the top 5 authors by book count from this dataset and compare their average book prices."
