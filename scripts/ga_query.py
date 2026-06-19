"""
Consulta la Google Analytics Data API usando el token guardado por ga_auth.py.
Uso: python3 -m scripts.ga_query [dias_atras]
"""

import json
import os
import sys

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2.credentials import Credentials

import config

TOKEN_PATH = os.path.join(os.path.dirname(__file__), "ga_token.json")


def get_client():
    with open(TOKEN_PATH) as f:
        info = json.load(f)
    creds = Credentials.from_authorized_user_info(info)
    return BetaAnalyticsDataClient(credentials=creds)


def run_report(days=7):
    client = get_client()
    request = RunReportRequest(
        property=f"properties/{config.GA_PROPERTY_ID}",
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="today")],
        dimensions=[Dimension(name="date"), Dimension(name="pagePath")],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="activeUsers"),
            Metric(name="sessions"),
        ],
        order_bys=[{"dimension": {"dimension_name": "date"}}],
        limit=200,
    )
    response = client.run_report(request)

    rows = []
    for row in response.rows:
        date, page = row.dimension_values[0].value, row.dimension_values[1].value
        views, users, sessions = (v.value for v in row.metric_values)
        rows.append({"date": date, "page": page, "views": int(views), "users": int(users), "sessions": int(sessions)})
    return rows


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    data = run_report(days)
    for r in data:
        print(r)
    print(f"\nTotal filas: {len(data)}")
