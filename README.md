# genpark-amazon-market-analyzer

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![MCP Dependency](https://img.shields.io/badge/MCP-mcp%20SDK-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Amazon Market Analyzer is a Amazon seller performance and listing optimization engine implementing logistic Buy Box win probability modeling, multi-tier FBA vs FBM unit cost and margin arbitration, and organic review-to-sales velocity anomaly fraud detection.

```mermaid
flowchart TD
    A[Seller Price, FBA Status & Rating] --> B[Buy Box Logistic Model]
    B --> C[Win Probability & Price Recommendation]
    D[Selling Price, Item Weight & COGS] --> E[FBA vs FBM Fee Engine]
    E --> F[Net Margin Comparison & Fulfillment Choice]
    G[30-Day Reviews & Sales Units] --> H[Review Velocity Rate Auditor]
    H --> I[Organic Compliance Risk Assessment]
```

## Features
- **Buy Box Win Predictor**: Models capture likelihood based on relative price delta, Prime fulfillment, and merchant feedback score.
- **FBA vs FBM Profit Arbitrage**: Evaluates Amazon pick-and-pack fee schedules against merchant shipping costs to maximize unit profit.
- **Review Velocity Fraud Auditor**: Benchmarks review conversion rates against organic e-commerce averages to prevent listing suppression.

## MCP Runtime Requirements

Use Python 3.10+ for the MCP server. The core `client.py` has no external dependencies; MCP transport requires `mcp>=1.0.0,<2`. From this checkout, install it into the Python environment used by your MCP client:

```bash
python -m pip install -r requirements.txt
```

Use the same Python interpreter to launch `mcp_server.py`. In desktop client configuration, set `command` to that interpreter's absolute path.

## Quickstart

```python
from client import GenParkAmazonMarketAnalyzer

analyzer = GenParkAmazonMarketAnalyzer()
res = analyzer.predict_buy_box_win_probability(29.99, 29.99, is_fba=True)
print("Buy Box Win Probability:", res["buy_box_win_probability_pct"], "%")
```

## Local MCP Server

After installing the MCP requirements, launch the local STDIO server:

```bash
python mcp_server.py
```

Point your MCP client at the absolute path to `mcp_server.py` using the same Python interpreter. This repository does not provide a hosted MCP endpoint.

## License
MIT
