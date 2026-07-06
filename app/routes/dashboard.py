from pathlib import Path

import pandas as pd
import plotly.express as px
from flask import Blueprint, render_template, send_from_directory

dashboard_bp = Blueprint("dashboard", __name__)
@dashboard_bp.route("/favicon.ico")
def favicon():
    static_images = Path(__file__).resolve().parents[1] / "static" / "images"
    return send_from_directory(static_images, "favicon.ico")

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "output"


def load_forecasts():
    forecast_file = OUTPUT_DIR / "baseline_risk_forecasts.csv"

    if not forecast_file.exists():
        return pd.DataFrame()

    return pd.read_csv(forecast_file)


def load_threat_correlations():
    correlation_file = OUTPUT_DIR / "threat_priority_correlations.csv"

    if not correlation_file.exists():
        return pd.DataFrame()

    return pd.read_csv(correlation_file)


@dashboard_bp.route("/")
def dashboard():
    forecasts = load_forecasts()
    threats = load_threat_correlations()

    if forecasts.empty:
        return render_template(
            "dashboard.html",
            dashboard_ready=False,
            message=(
                "No forecast data is available yet. Run the validated Lighthouse "
                "telemetry pipeline and baseline risk model first."
            ),
        )

    tier_counts = (
        forecasts["predicted_risk_tier"]
        .value_counts()
        .reindex(["Critical", "High", "Medium", "Low"], fill_value=0)
        .reset_index()
    )
    tier_counts.columns = ["risk_tier", "asset_count"]

    risk_chart = px.bar(
        tier_counts,
        x="risk_tier",
        y="asset_count",
        title="Predicted Enterprise Risk Distribution",
        labels={
            "risk_tier": "Predicted Risk Tier",
            "asset_count": "Assets",
        },
    )

    high_risk_assets = forecasts[
        forecasts["predicted_risk_tier"].isin(["Critical", "High"])
    ].sort_values(
        by="high_risk_probability",
        ascending=False,
    ).head(10)

    anomaly_count = int((forecasts["anomaly_flag"] == "Yes").sum())
    review_count = int(
        (forecasts["analyst_review_required"] == "Yes").sum()
    )

    critical_count = int(
        (forecasts["predicted_risk_tier"] == "Critical").sum()
    )
    high_count = int(
        (forecasts["predicted_risk_tier"] == "High").sum()
    )

    threat_chart_html = None

    if not threats.empty:
        threat_counts = (
            threats["threat_priority_tier"]
            .value_counts()
            .reindex(["Critical", "High", "Medium", "Low"], fill_value=0)
            .reset_index()
        )
        threat_counts.columns = ["priority_tier", "asset_count"]

        threat_chart = px.bar(
            threat_counts,
            x="priority_tier",
            y="asset_count",
            title="Threat-Priority Correlation Distribution",
            labels={
                "priority_tier": "Threat Priority",
                "asset_count": "Assets",
            },
        )

        threat_chart_html = threat_chart.to_html(
            full_html=False,
            include_plotlyjs=False,
        )

    return render_template(
        "dashboard.html",
        dashboard_ready=True,
        risk_chart_html=risk_chart.to_html(
            full_html=False,
            include_plotlyjs="cdn",
        ),
        threat_chart_html=threat_chart_html,
        critical_count=critical_count,
        high_count=high_count,
        anomaly_count=anomaly_count,
        review_count=review_count,
        high_risk_assets=high_risk_assets.to_dict(orient="records"),
    )
