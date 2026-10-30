# -*- coding: utf-8 -*-
"""
GenPark Amazon Market Analyzer FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkAmazonMarketAnalyzer

mcp = FastMCP("genpark-amazon-market-analyzer")
analyzer = GenParkAmazonMarketAnalyzer()

@mcp.tool()
def predict_buy_box_win_probability(
    seller_price: float,
    buy_box_price: float,
    is_fba: bool = True,
    feedback_rating_pct: float = 98.0,
    feedback_count: int = 500,
    lead_time_days: int = 2
) -> str:
    """
    Predicts Amazon Buy Box capture probabilities.
    """
    res = analyzer.predict_buy_box_win_probability(seller_price, buy_box_price, is_fba, feedback_rating_pct, feedback_count, lead_time_days)
    return json.dumps(res, indent=2)

@mcp.tool()
def arbitrate_fba_vs_fbm_unit_profitability(
    selling_price_usd: float,
    item_weight_lbs: float,
    cogs_usd: float,
    fbm_shipping_cost_usd: float,
    referral_fee_pct: float = 15.0
) -> str:
    """
    Calculates net profit and margins under FBA vs FBM.
    """
    res = analyzer.arbitrate_fba_vs_fbm_unit_profitability(selling_price_usd, item_weight_lbs, cogs_usd, fbm_shipping_cost_usd, referral_fee_pct)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_review_to_sales_velocity_ratio(
    reviews_past_30_days: int,
    estimated_sales_units_past_30_days: int,
    category: str = "general"
) -> str:
    """
    Audits organic review velocity vs unit sales volume.
    """
    res = analyzer.audit_review_to_sales_velocity_ratio(reviews_past_30_days, estimated_sales_units_past_30_days, category)
    return json.dumps(res, indent=2)

def main():
    print("Testing Amazon Market Analyzer:")
    print(predict_buy_box_win_probability(29.99, 29.99, True))

if __name__ == "__main__":
    main()
