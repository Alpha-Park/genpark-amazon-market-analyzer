# -*- coding: utf-8 -*-
"""
GenPark Amazon Market Analyzer Client
Zero-dependency Amazon Buy Box win probability logistic modeler, FBA vs FBM unit cost profitability calculator,
and review-to-sales velocity anomaly ratio auditor.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkAmazonMarketAnalyzer:
    """
    Predicts Amazon Buy Box capture probabilities, computes multi-tier FBA vs FBM profit margins,
    and audits organic review conversion anomalies.
    """

    def predict_buy_box_win_probability(
        self,
        seller_price: float,
        buy_box_price: float,
        is_fba: bool = True,
        feedback_rating_pct: float = 98.0,
        feedback_count: int = 500,
        lead_time_days: int = 2
    ) -> Dict[str, Any]:
        """
        Predicts Buy Box win probability using calibrated multi-factor logistic regression:
        z = beta_0 - 15*(Price_delta/BB_price) + 2.5*(is_fba) + 0.05*(rating - 90) - 0.3*lead_time
        """
        if seller_price <= 0 or buy_box_price <= 0:
            raise ValueError("Prices must be positive.")

        price_delta = seller_price - buy_box_price
        pct_price_delta = price_delta / buy_box_price

        # Logistic logit
        fba_bonus = 2.2 if is_fba else -1.5
        rating_score = (feedback_rating_pct - 90.0) * 0.15
        shipping_penalty = min(5, lead_time_days) * 0.35

        z = 0.5 - 18.0 * pct_price_delta + fba_bonus + rating_score - shipping_penalty

        win_prob = 1.0 / (1.0 + math.exp(-max(-8.0, min(8.0, z))))
        win_prob_pct = round(win_prob * 100.0, 1)

        # Recommendation to win Buy Box
        if win_prob_pct >= 70.0:
            advice = "DOMINANT_BUY_BOX: Maintain current price and fulfill inventory."
        elif win_prob_pct >= 40.0:
            # Drop price by 1-2% to seize ownership
            rec_price = round(buy_box_price * 0.99, 2)
            advice = f"COMPETITIVE: Drop price to ${rec_price:.2f} or switch to FBA Prime to secure Buy Box."
        else:
            rec_price = round(buy_box_price * 0.97, 2)
            advice = f"UNCOMPETITIVE: Match or beat Buy Box price at ${rec_price:.2f}."

        return {
            "seller_price": seller_price,
            "buy_box_price": buy_box_price,
            "price_delta_pct": round(pct_price_delta * 100.0, 2),
            "is_fba": is_fba,
            "buy_box_win_probability_pct": win_prob_pct,
            "competitive_status": advice
        }

    def arbitrate_fba_vs_fbm_unit_profitability(
        self,
        selling_price_usd: float,
        item_weight_lbs: float,
        cogs_usd: float,
        fbm_shipping_cost_usd: float,
        referral_fee_pct: float = 15.0
    ) -> Dict[str, Any]:
        """
        Calculates net profit and margins under Fulfillment by Amazon (FBA) vs Merchant Fulfilled (FBM).
        """
        if selling_price_usd <= 0 or cogs_usd <= 0:
            raise ValueError("Selling price and COGS must be positive.")

        referral_fee = selling_price_usd * (referral_fee_pct / 100.0)

        # Standard Amazon FBA Fee schedule approximation (standard size tiers)
        base_fba_pick_pack = 3.22 if item_weight_lbs <= 1.0 else (4.15 + (item_weight_lbs - 1.0) * 0.40)
        monthly_storage_per_unit = 0.45
        total_fba_fees = round(referral_fee + base_fba_pick_pack + monthly_storage_per_unit, 2)

        # FBM Fees: referral fee + actual merchant shipping cost + packaging
        fbm_packaging_cost = 0.75
        total_fbm_fees = round(referral_fee + fbm_shipping_cost_usd + fbm_packaging_cost, 2)

        fba_net_profit = round(selling_price_usd - cogs_usd - total_fba_fees, 2)
        fbm_net_profit = round(selling_price_usd - cogs_usd - total_fbm_fees, 2)

        fba_margin_pct = round(100.0 * fba_net_profit / selling_price_usd, 2)
        fbm_margin_pct = round(100.0 * fbm_net_profit / selling_price_usd, 2)

        recommendation = "CHOOSE_FBA (Higher conversion & Prime eligibility offset fees)" if fba_net_profit >= fbm_net_profit - 1.5 else "CHOOSE_FBM (Merchant fulfillment yields significantly higher profit)"

        return {
            "selling_price_usd": selling_price_usd,
            "cogs_usd": cogs_usd,
            "referral_fee_usd": round(referral_fee, 2),
            "fba_option": {
                "fba_fees_usd": total_fba_fees,
                "net_profit_usd": fba_net_profit,
                "net_margin_pct": fba_margin_pct
            },
            "fbm_option": {
                "fbm_fees_usd": total_fbm_fees,
                "net_profit_usd": fbm_net_profit,
                "net_margin_pct": fbm_margin_pct
            },
            "profit_difference_usd": round(fba_net_profit - fbm_net_profit, 2),
            "recommendation": recommendation
        }

    def audit_review_to_sales_velocity_ratio(
        self,
        reviews_past_30_days: int,
        estimated_sales_units_past_30_days: int,
        category: str = "general"
    ) -> Dict[str, Any]:
        """
        Audits organic review velocity vs unit sales volume (Amazon organic review rate benchmark is 1.0% to 3.0%).
        """
        if estimated_sales_units_past_30_days <= 0:
            return {"review_rate_pct": 0.0, "status": "NO_SALES_VOLUME"}

        review_rate = (reviews_past_30_days / float(estimated_sales_units_past_30_days)) * 100.0
        review_rate_pct = round(review_rate, 2)

        if review_rate_pct > 7.0:
            risk = "HIGH_MANIPULATION_RISK: Review rate abnormally high (>7%). Amazon algorithm may trigger listing review or suppression."
            verdict = "ANOMALY_SPIKE"
        elif review_rate_pct < 0.3:
            risk = "REVIEW_DEFICIT: Review rate below 0.3%. Implement Amazon Request a Review automated sequence."
            verdict = "UNDERPERFORMING"
        else:
            risk = "ORGANIC_HEALTHY: Review rate within natural benchmark bounds (1% - 5%)."
            verdict = "HEALTHY"

        return {
            "reviews_past_30_days": reviews_past_30_days,
            "sales_units_past_30_days": estimated_sales_units_past_30_days,
            "review_conversion_rate_pct": review_rate_pct,
            "benchmark_range_pct": "1.0% - 3.5%",
            "audit_verdict": verdict,
            "compliance_risk_assessment": risk
        }
