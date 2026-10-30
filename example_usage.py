# -*- coding: utf-8 -*-
import json
from client import GenParkAmazonMarketAnalyzer

analyzer = GenParkAmazonMarketAnalyzer()

# 1. Amazon Buy Box Win Probability
bb = analyzer.predict_buy_box_win_probability(
    seller_price=29.50,
    buy_box_price=29.99,
    is_fba=True,
    feedback_rating_pct=99.0
)
print(f"Buy Box Prediction: WinProb={bb['buy_box_win_probability_pct']}% (Delta: {bb['price_delta_pct']}%)")
print(f"  Advice: {bb['competitive_status']}")

# 2. FBA vs FBM Unit Profitability Arbitration
fba_fbm = analyzer.arbitrate_fba_vs_fbm_unit_profitability(
    selling_price_usd=39.99,
    item_weight_lbs=1.5,
    cogs_usd=9.00,
    fbm_shipping_cost_usd=6.50
)
print()
print(f"Fulfillment Arbitration: FBA Profit=${fba_fbm['fba_option']['net_profit_usd']} ({fba_fbm['fba_option']['net_margin_pct']}%) vs FBM Profit=${fba_fbm['fbm_option']['net_profit_usd']} ({fba_fbm['fbm_option']['net_margin_pct']}%)")
print(f"  Verdict: {fba_fbm['recommendation']}")

# 3. Review-to-Sales Velocity Anomaly Audit
audit = analyzer.audit_review_to_sales_velocity_ratio(
    reviews_past_30_days=45,
    estimated_sales_units_past_30_days=500
)
print()
print(f"Review Velocity Audit: Review Rate={audit['review_conversion_rate_pct']}% | Verdict={audit['audit_verdict']}")
print(f"  Risk Note: {audit['compliance_risk_assessment']}")
