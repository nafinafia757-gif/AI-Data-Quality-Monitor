import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
import html

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Data Quality Monitor",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# BLACK & GOLD THEME
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --gold: #f6c84b;
    --gold-light: #ffe18a;
    --bg: #08090b;
    --panel: #111215;
    --border: #38332a;
    --muted: #b8b8bd;
}
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: var(--bg); color: #f5f5f5; }
.block-container { max-width: 1600px; padding: 1.5rem 2rem 2rem; }
header[data-testid="stHeader"] { background: #08090b; }
section[data-testid="stSidebar"] { background: #0c0d10; border-right: 1px solid #292929; }
.brand { color: var(--gold-light); font-size: 23px; font-weight: 800; }
.brand-sub { color: var(--muted); font-size: 12px; margin-top: 5px; }
.topbar { display:flex; align-items:center; gap:16px; padding:5px 0 22px; margin-bottom:24px; border-bottom:1px solid #292929; }
.top-title { color:var(--gold-light); font-size:27px; font-weight:800; }
.subtitle { color:var(--muted); font-size:12px; margin-top:5px; }
.welcome-title { color:var(--gold-light); font-size:28px; font-weight:800; }
.welcome-desc { color:#c6c6cb; line-height:1.8; font-size:14px; margin:8px 0 18px; }
.panel, .metric-card, .score-card { background:linear-gradient(145deg,#151619,#0d0e10); border:1px solid var(--border); border-radius:14px; padding:18px; margin-bottom:17px; }
.panel-title { color:var(--gold-light); font-size:16px; font-weight:700; padding-bottom:12px; border-bottom:1px solid #302d28; margin-bottom:12px; }
.score-card { background:radial-gradient(ellipse at right,rgba(246,200,75,.12),transparent 60%),#111113; border-color:#b99238; }
.score-ring { width:112px; height:112px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:conic-gradient(var(--gold) var(--score),#353535 0); position:relative; flex-shrink:0; }
.score-ring::before { content:""; position:absolute; width:91px; height:91px; border-radius:50%; background:#101113; }
.score-number { position:relative; font-size:22px; font-weight:800; color:white; }
.score-heading { color:var(--gold-light); font-size:21px; font-weight:800; }
.status-pill { display:inline-block; color:var(--gold-light); background:#292315; border:1px solid #6f5825; border-radius:20px; padding:5px 11px; font-size:12px; margin:8px 0; }
.metric-card { padding:15px 8px; text-align:center; min-height:130px; margin-bottom:0; }
.metric-icon { color:var(--gold); font-size:24px; }
.metric-label { color:#c7c7cb; font-size:11px; margin-top:8px; min-height:28px; }
.metric-value { color:white; font-size:23px; font-weight:800; overflow-wrap:anywhere; }
.bar-row { display:grid; grid-template-columns:125px 1fr 42px; gap:10px; align-items:center; margin:16px 0; font-size:12px; }
.bar-track { height:12px; background:#303033; border-radius:20px; overflow:hidden; }
.bar-fill { height:100%; background:linear-gradient(90deg,#c99522,#ffe18a); border-radius:20px; }
.bar-value { text-align:right; color:white; font-weight:700; }
.info-row { display:flex; justify-content:space-between; gap:12px; padding:11px 0; border-bottom:1px solid #292929; font-size:12px; }
.info-label { color:#c6c6cb; }
.info-value { color:white; text-align:right; overflow-wrap:anywhere; }
.insight { display:flex; gap:10px; color:#e7e7e9; font-size:12px; line-height:1.7; margin:13px 0; }
.check-icon { display:inline-flex; align-items:center; justify-content:center; width:21px; height:21px; min-width:21px; background:linear-gradient(135deg,#ffe18a,#c99522); color:#17120a; border-radius:50%; font-weight:800; }
div.stButton > button { background:linear-gradient(135deg,#ffe18a,#c99522); color:#17120a; border:none; border-radius:8px; font-weight:700; }
.stDownloadButton > button { background:#181715; color:#ffe18a; border:1px solid #9d7b2c; border-radius:8px; }
.stTabs [aria-selected="true"] { color:#ffe18a !important; }
div[data-testid="stDataFrame"] { border:1px solid #34302a; border-radius:10px; }
@media (max-width:900px) {
 .block-container { padding:1rem; }
 .top-title { font-size:22px; }
 .bar-row { grid-template-columns:95px 1fr 38px; gap:6px; }
}
/* Golden navigation buttons */

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 12px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: #151515;
    border: 1px solid #5c4820;
    border-radius: 12px;
    padding: 12px 15px;
    transition: all 0.25s ease;
}

/* Selected button */
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, #ffe18a, #c99522);
    border: 1px solid #ffe18a;
    box-shadow: 0 0 12px rgba(246, 200, 75, 0.25);
}

/* Selected button text */
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
    color: #17120a !important;
    font-weight: 800;
}

/* Unselected button text */
section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #f5f5f5;
    font-weight: 600;
}

/* Hover effect */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    border-color: #ffe18a;
    background: #292315;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "df" not in st.session_state:
    st.session_state.df = None
if "filename" not in st.session_state:
    st.session_state.filename = ""
if "uploaded_at" not in st.session_state:
    st.session_state.uploaded_at = ""
if "navigation" not in st.session_state:
    st.session_state.navigation = " Home"

def go_to_report():
    # Callback runs before the next rerun, so the radio key is safe to update.
    st.session_state.navigation = "▤ Data Quality Report"

# =========================================================
# DATASET HELPERS
# =========================================================
def read_dataset(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith(".csv"):
        try:
            uploaded_file.seek(0)
            return pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            return pd.read_csv(uploaded_file, encoding="latin-1")
    if name.endswith(".xlsx"):
        uploaded_file.seek(0)
        return pd.read_excel(uploaded_file, engine="openpyxl")
    if name.endswith(".xls"):
        uploaded_file.seek(0)
        return pd.read_excel(uploaded_file)
    raise ValueError("Please upload a CSV or Excel file.")

def get_report(df):
    rows, cols = df.shape
    total_cells = rows * cols
    missing_by_col = df.isna().sum()
    missing = int(missing_by_col.sum())
    completeness = 100 * (1 - missing / total_cells) if total_cells else 100.0

    duplicates = int(df.duplicated().sum())
    duplicate_score = 100 * (1 - duplicates / rows) if rows else 100.0

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    outlier_counts = {}
    outlier_row_ids = set()

    for col in numeric_cols:
        values = df[col].dropna()
        if len(values) < 4:
            outlier_counts[col] = 0
            continue
        q1, q3 = values.quantile(0.25), values.quantile(0.75)
        iqr = q3 - q1
        if pd.isna(iqr) or iqr == 0:
            outlier_counts[col] = 0
            continue
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        mask = ((df[col] < lower) | (df[col] > upper)).fillna(False)
        outlier_counts[col] = int(mask.sum())
        outlier_row_ids.update(df.index[mask].tolist())

    outlier_cells = int(sum(outlier_counts.values()))
    outlier_rows = len(outlier_row_ids)
    outlier_score = 100 * (1 - outlier_rows / rows) if rows else 100.0
    overall = 0.40 * completeness + 0.30 * duplicate_score + 0.30 * outlier_score
    overall = max(0.0, min(100.0, overall))
    status = "Good Quality" if overall >= 90 else ("Needs Attention" if overall >= 70 else "Poor Quality")

    return {
        "rows": rows, "columns": cols, "missing": missing,
        "missing_by_col": missing_by_col, "duplicates": duplicates,
        "completeness": completeness, "duplicate_score": duplicate_score,
        "outlier_score": outlier_score, "outlier_cells": outlier_cells,
        "outlier_rows": outlier_rows, "outlier_counts": outlier_counts,
        "numeric_cols": numeric_cols, "overall": overall, "status": status
    }

# =========================================================
# UI HELPERS
# =========================================================
def metric_card(icon, label, value):
    st.markdown(f"""
    <div class="metric-card">
      <div class="metric-icon">{icon}</div>
      <div class="metric-label">{html.escape(str(label))}</div>
      <div class="metric-value">{html.escape(str(value))}</div>
    </div>""", unsafe_allow_html=True)

def progress_bar(label, value):
    value = max(0.0, min(100.0, float(value)))
    st.markdown(f"""
    <div class="bar-row">
      <div>{html.escape(str(label))}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{value:.2f}%"></div></div>
      <div class="bar-value">{value:.0f}%</div>
    </div>""", unsafe_allow_html=True)

def info_row(label, value):
    st.markdown(f"""
    <div class="info-row">
      <div class="info-label">{html.escape(str(label))}</div>
      <div class="info-value">{html.escape(str(value))}</div>
    </div>""", unsafe_allow_html=True)

def insight(message):
    st.markdown(f"""
    <div class="insight"><span class="check-icon">✓</span>
      <span>{html.escape(str(message))}</span>
    </div>""", unsafe_allow_html=True)

def make_excel_report(df, report):
    output = BytesIO()
    summary = pd.DataFrame({
        "Metric": ["Rows", "Columns", "Missing Cells", "Duplicate Rows",
                   "Potential Outlier Cells", "Overall Score", "Status"],
        "Value": [report["rows"], report["columns"], report["missing"],
                  report["duplicates"], report["outlier_cells"],
                  round(report["overall"], 2), report["status"]]
    })
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dataset", index=False)
        summary.to_excel(writer, sheet_name="Quality Summary", index=False)
    return output.getvalue()

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown('<div class="brand">◆ Data Quality Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-sub">Better Data • Better Decisions</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.radio(
        "Navigation",
        [" Home", " Upload Dataset", "▤ Data Quality Report", " About"],
        key="navigation",
        label_visibility="collapsed"
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<div style="color:#ffe18a;font-size:13px;line-height:1.9">✦ Better Data<br>&nbsp;&nbsp;&nbsp; Better Decisions</div>',
        unsafe_allow_html=True
    )

# =========================================================
# TOP HEADER WITH EMBEDDED SVG IMAGE
# No separate image file required.
# =========================================================
header_svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffe18a"/>
      <stop offset="100%" stop-color="#c99522"/>
    </linearGradient>
  </defs>
  <rect x="5" y="5" width="90" height="90" rx="22" fill="#17150f" stroke="#8c6c24" stroke-width="2"/>
  <ellipse cx="45" cy="31" rx="23" ry="9" fill="url(#gold)"/>
  <path d="M22 31 V56 C22 61 32 66 45 66 S68 61 68 56 V31" fill="#b98a24" stroke="#ffe18a" stroke-width="2"/>
  <path d="M22 43 C22 48 32 53 45 53 S68 48 68 43" fill="none" stroke="#ffe18a" stroke-width="2"/>
  <path d="M22 55 C22 60 32 65 45 65 S68 60 68 55" fill="none" stroke="#ffe18a" stroke-width="2"/>
  <path d="M63 54 L76 59 L74 75 Q69 83 63 85 Q57 82 53 75 L51 59 Z" fill="url(#gold)" stroke="#fff0b5" stroke-width="1.5"/>
  <path d="M58 69 L62 73 L69 65" fill="none" stroke="#17150f" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""

import base64
svg_b64 = base64.b64encode(header_svg.encode("utf-8")).decode("ascii")
st.markdown(f"""
<div class="topbar">
  <img src="data:image/svg+xml;base64,{svg_b64}" width="78" height="78" alt="Data quality database and shield icon">
  <div>
    <div class="top-title">Data Quality Monitor</div>
    <div class="subtitle">Clean Data • Better Insights • Smarter Decisions</div>
  </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# UPLOAD AREA
# =========================================================
if st.session_state.navigation in ["🏠 Home", "☁️ Upload Dataset"]:
    st.markdown('<div class="panel-title">☁ Upload Your Dataset (CSV or Excel)</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx", "xls"],
        key="dataset_uploader",
        help="Upload CSV, XLSX, or XLS files."
    )

    if uploaded_file is not None:
        is_new = (
            st.session_state.filename != uploaded_file.name
            or st.session_state.df is None
        )
        if is_new:
            try:
                new_df = read_dataset(uploaded_file)
                if new_df.empty:
                    st.warning("The uploaded dataset is empty.")
                else:
                    st.session_state.df = new_df
                    st.session_state.filename = uploaded_file.name
                    st.session_state.uploaded_at = datetime.now().strftime("%b %d, %Y | %I:%M %p")
                    st.success("Dataset uploaded successfully.")
            except Exception as exc:
                st.error(f"Could not read the uploaded file: {exc}")

df = st.session_state.df

# =========================================================
# EMPTY / WELCOME STATE
# =========================================================
if df is None:
    st.markdown("""
    <div style="text-align:center;padding:65px 20px;background:linear-gradient(145deg,#111215,#0a0b0d);border:1px solid #302c24;border-radius:16px">
      <div style="font-size:48px;color:#ffe18a">▤</div>
      <div style="color:#ffe18a;font-size:28px;font-weight:800;margin:15px 0">Welcome to Data Quality Monitor</div>
      <div style="color:#c5c5ca;font-size:14px;line-height:1.9">
        Upload a dataset to identify missing values, duplicate records and potential outliers.<br>
        Supported formats: CSV, XLSX and XLS.
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

report = get_report(df)

# =========================================================
# HOME DASHBOARD
# =========================================================
if st.session_state.navigation == "🏠 Home":
    left, right = st.columns([2.1, 1], gap="large")

    with left:
        st.markdown('<div class="welcome-title">Welcome to Data Quality Monitor</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="welcome-desc">Monitor your dataset, identify quality issues and explore actionable data insights.</div>',
            unsafe_allow_html=True
        )

        score = report["overall"]
        st.markdown(f"""
        <div class="score-card">
          <div style="display:flex;align-items:center;gap:22px;flex-wrap:wrap">
            <div class="score-ring" style="--score:{score:.2f}%"><div class="score-number">{score:.1f}%</div></div>
            <div style="flex:1;min-width:180px">
              <div class="score-heading">Overall Data Quality</div>
              <div class="status-pill">● {report["status"]}</div>
              <div style="color:#d0d0d3;font-size:13px;line-height:1.7">
                A rule-based score calculated from completeness, duplicate rows and potential outlier rows.
              </div>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)

        cols = st.columns(5, gap="small")
        cards = [
            ("▤", "Total Rows", f'{report["rows"]:,}'),
            ("▥", "Total Columns", f'{report["columns"]:,}'),
            ("⚠", "Missing Values", f'{report["missing"]:,}'),
            ("▣", "Duplicate Rows", f'{report["duplicates"]:,}'),
            ("✦", "Outlier Cells", f'{report["outlier_cells"]:,}'),
        ]
        for col, (icon, label, value) in zip(cols, cards):
            with col:
                metric_card(icon, label, value)

        st.markdown('<div class="panel" style="margin-top:18px"><div class="panel-title">▥ Data Quality Breakdown</div>', unsafe_allow_html=True)
        progress_bar("Completeness", report["completeness"])
        progress_bar("Duplicate-free", report["duplicate_score"])
        progress_bar("Outlier-free rows", report["outlier_score"])
        st.markdown('<div style="color:#b8b8bd;font-size:11px;margin-top:12px">Semantic (AI Check): Not configured. No AI score is fabricated.</div></div>', unsafe_allow_html=True)

        st.button("View Full Report →", on_click=go_to_report, use_container_width=True)

    with right:
        st.markdown('<div class="panel"><div class="panel-title">▤ Dataset Information</div>', unsafe_allow_html=True)
        info_row("File Name", st.session_state.filename)
        info_row("Rows", f'{report["rows"]:,}')
        info_row("Columns", f'{report["columns"]:,}')
        suffix = st.session_state.filename.rsplit(".", 1)[-1].upper() if "." in st.session_state.filename else "Unknown"
        info_row("File Type", suffix)
        info_row("Uploaded On", st.session_state.uploaded_at or "This session")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="panel"><div class="panel-title">♧ Key Insights</div>', unsafe_allow_html=True)
        if report["missing"] == 0:
            insight("No missing values detected.")
        else:
            insight(f'{report["missing"]:,} missing cells detected.')
        if report["duplicates"] == 0:
            insight("No duplicate rows detected.")
        else:
            insight(f'{report["duplicates"]:,} duplicate rows detected.')
        if report["outlier_cells"] == 0:
            insight("No IQR outliers detected in numeric columns.")
        else:
            insight(f'{report["outlier_cells"]:,} potential outlier cells detected.')
        insight(f'Overall quality status: {report["status"]}.')
        st.markdown('<div style="color:#ffe18a;text-align:center;font-style:italic;line-height:1.8;padding-top:15px">“High quality data leads to better decisions.”</div></div>', unsafe_allow_html=True)

# =========================================================
# UPLOAD DATASET / PREVIEW PAGE
# =========================================================
elif st.session_state.navigation == "☁️ Upload Dataset":
    st.markdown('<div class="welcome-title">Dataset Preview</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-desc">Preview your uploaded data and inspect each column.</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(f'**File:** `{html.escape(st.session_state.filename)}`')
    st.dataframe(df.head(100), use_container_width=True, height=420)
    st.caption(f"Showing up to 100 of {len(df):,} rows.")
    st.markdown("</div>", unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Column": df.columns.astype(str),
        "Data Type": [str(x) for x in df.dtypes],
        "Missing Values": [int(x) for x in df.isna().sum()],
        "Missing (%)": [
            round(float(x / len(df) * 100), 2) if len(df) else 0
            for x in df.isna().sum()
        ],
        "Unique Values": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    st.markdown('<div class="panel-title">Column Summary</div>', unsafe_allow_html=True)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

# =========================================================
# DATA QUALITY REPORT PAGE
# =========================================================
elif st.session_state.navigation == "▤ Data Quality Report":
    st.markdown('<div class="welcome-title">Data Quality Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-desc">Detailed checks for missing values, duplicates and numerical outliers.</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Missing Values", "Duplicates", "Outliers", "Summary"])

    with tab1:
        missing_table = pd.DataFrame({
            "Column": df.columns.astype(str),
            "Missing Values": [int(x) for x in df.isna().sum()],
            "Missing (%)": [
                round(float(x / len(df) * 100), 2) if len(df) else 0
                for x in df.isna().sum()
            ],
        })
        missing_table = missing_table[missing_table["Missing Values"] > 0].sort_values("Missing Values", ascending=False)
        if missing_table.empty:
            st.success("No missing values found.")
        else:
            st.dataframe(missing_table, use_container_width=True, hide_index=True)

    with tab2:
        duplicates_df = df[df.duplicated(keep=False)]
        if duplicates_df.empty:
            st.success("No duplicate rows found.")
        else:
            st.warning(f'{report["duplicates"]:,} duplicate rows detected, excluding the first occurrence of each repeated row.')
            st.dataframe(duplicates_df.head(200), use_container_width=True, hide_index=True)

    with tab3:
        if not report["numeric_cols"]:
            st.info("No numerical columns are available for outlier detection.")
        else:
            outlier_table = pd.DataFrame({
                "Column": list(report["outlier_counts"].keys()),
                "Potential Outliers": list(report["outlier_counts"].values()),
            }).sort_values("Potential Outliers", ascending=False)
            st.dataframe(outlier_table, use_container_width=True, hide_index=True)

            selected_col = st.selectbox("Choose a numerical column", report["numeric_cols"])
            values = df[selected_col].dropna()
            if len(values) < 4:
                st.info("Not enough numeric observations to calculate IQR.")
            else:
                q1, q3 = values.quantile(0.25), values.quantile(0.75)
                iqr = q3 - q1
                if pd.isna(iqr) or iqr == 0:
                    st.info("IQR is zero; no IQR outlier range is available.")
                else:
                    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
                    st.write(f"Lower IQR boundary: **{lower:,.3f}**")
                    st.write(f"Upper IQR boundary: **{upper:,.3f}**")
                    st.write(f'Potential outliers: **{report["outlier_counts"].get(selected_col, 0):,}**')

    with tab4:
        c1, c2, c3 = st.columns(3)
        c1.metric("Overall Quality", f'{report["overall"]:.1f}%')
        c2.metric("Missing Cells", f'{report["missing"]:,}')
        c3.metric("Duplicate Rows", f'{report["duplicates"]:,}')
        st.write("**Status:**", report["status"])
        st.caption("Potential outliers are values outside the 1.5 × IQR boundaries. They are not automatically errors.")

    st.markdown("### Export Report")
    try:
        excel_bytes = make_excel_report(df, report)
        st.download_button(
            "⬇ Download Excel Quality Report",
            data=excel_bytes,
            file_name="data_quality_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
    except Exception as exc:
        st.error(f"Could not create Excel report: {exc}")
        csv_bytes = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "Download Dataset as CSV",
            data=csv_bytes,
            file_name="dataset.csv",
            mime="text/csv",
        )
    st.caption("The report preserves the original dataset; it does not automatically remove or modify records.")

# =========================================================
# ABOUT PAGE
# =========================================================
elif st.session_state.navigation == "ⓘ About":
    st.markdown('<div class="welcome-title">About Data Quality Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-desc">Clean data, better insights and smarter decisions.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
      <div class="panel-title">Project Overview</div>
      <p style="color:#dedee1;line-height:1.9">
        Data Quality Monitor is a Python-based application that helps users
        inspect datasets and identify common data quality issues before
        performing analysis or Deep learning 

      <div class="panel-title">Main Features</div>
      <p style="color:#dedee1;line-height:2">
        ✓ CSV and Excel dataset upload<br>
        ✓ Dataset preview and column summary<br>
        ✓ Missing-value detection<br>
        ✓ Duplicate-row detection<br>
        ✓ Numerical outlier detection using IQR<br>
        ✓ Overall data quality score<br>
        ✓ Downloadable Excel quality report
      </p>

      <div class="panel-title">Technologies Used</div>
      <p style="color:#dedee1;line-height:2">
        Python • Streamlit • Pandas • NumPy • OpenPyXL
      </p>

      <div class="panel-title">Scoring Method</div>
      <p style="color:#dedee1;line-height:1.9">
        Overall Score = 40% Completeness + 30% Duplicate Score +
        30% Outlier-free Row Score.
      </p>
      <p style="color:#b8b8bd;font-size:12px;line-height:1.8">
        This is a rule-based indicator, not a universal measure of dataset
        quality. Semantic AI validation is not enabled in this version.
      </p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div style="text-align:center;color:#f6c84b;font-size:11px;padding:20px 0 5px">
  Data Quality Monitor • Clean Data • Better Insights • Smarter Decisions
</div>
""", unsafe_allow_html=True)