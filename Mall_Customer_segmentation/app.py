# ============================================================
# MALL CUSTOMER SEGMENTATION
# STREAMLIT USER INTERFACE
# ============================================================

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_samples
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mall Customer Segmentation",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    /* KPI cards */
    .metric-card {
        background: white;
        padding: 22px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        min-height: 140px;
    }

    .metric-title {
        font-size: 14px;
        color: #6b7280;
        font-weight: 600;
    }

    .metric-value {
        font-size: 32px;
        font-weight: 800;
        color: #2563eb;
        margin-top: 10px;
    }

    .metric-description {
        font-size: 12px;
        color: #9ca3af;
        margin-top: 5px;
    }

    /* Section title */
    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #0B132B;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Insight cards */
    .insight-card {
        background: white;
        border-left: 5px solid #2563eb;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }

    .insight-title {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
    }

    .insight-text {
        color: #4b5563;
        margin-top: 8px;
        line-height: 1.6;
    }

    /* Info box */
    .info-box {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        padding: 18px;
        border-radius: 12px;
        color: #1e3a8a;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        margin-top: 50px;
        color: #6b7280;
        border-top: 1px solid #e5e7eb;
    }

    .tech-list {
        margin-top: 10px;
    }
    
    .tech-item {
        color: #0F172A;
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 10px 15px;
        margin: 7px 0;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
    }
    
    .tech-item:hover {
        background-color: #EFF6FF;
        border-color: #2563EB;
        color: #2563EB;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    try:
        df = pd.read_csv("dataset/Mall_Customers.csv")

    except FileNotFoundError:

        online_path = (
            "https://raw.githubusercontent.com/"
            "plotly/datasets/master/mall_customers_2019.csv"
        )

        df = pd.read_csv(online_path)

    return df


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h1 style="text-align:center;">🛍️</h1>
    <h2 style="text-align:center;">Mall Analytics</h2>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 EDA & Analytics",
        "🎯 Customer Segmentation",
        "👥 Cluster Profiles",
        "🔎 Customer Explorer",
        "📈 Model Evaluation",
        "💡 Business Insights",
        "📚 About Project"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project**

    Mall Customer Segmentation

    **Algorithm**

    K-Means Clustering

    **Features**

    Annual Income + Spending Score
    """
)


# ============================================================
# RUN K-MEANS
# ============================================================

features = [
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

X = df[features].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ============================================================
# FIND K USING SILHOUETTE
# ============================================================

@st.cache_data
def calculate_k_metrics(X_scaled):

    wcss = []
    silhouette_scores = []

    k_values = range(2, 11)

    for k in k_values:

        model = KMeans(
            n_clusters=k,
            init="k-means++",
            random_state=42,
            n_init=10
        )

        labels = model.fit_predict(X_scaled)

        wcss.append(model.inertia_)

        silhouette_scores.append(
            silhouette_score(X_scaled, labels)
        )

    return list(k_values), wcss, silhouette_scores


k_values, wcss, silhouette_scores = calculate_k_metrics(X_scaled)


# ============================================================
# DEFAULT K = 5
# ============================================================

optimal_k = 5

kmeans = KMeans(
    n_clusters=optimal_k,
    init="k-means++",
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)

df["Cluster"] = labels


# ============================================================
# CLUSTER CENTERS
# ============================================================

centers_original = scaler.inverse_transform(
    kmeans.cluster_centers_
)

cluster_centers = pd.DataFrame(
    centers_original,
    columns=features
)

cluster_centers.index = [
    f"Cluster {i}" for i in range(optimal_k)
]


# ============================================================
# METRICS
# ============================================================

sil_score = silhouette_score(
    X_scaled,
    labels
)

calinski_score = calinski_harabasz_score(
    X_scaled,
    labels
)

davies_score = davies_bouldin_score(
    X_scaled,
    labels
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">🛍️ Mall Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Discover customer groups using K-Means clustering
        and transform customer data into actionable business insights.
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">TOTAL CUSTOMERS</div>
                <div class="metric-value">{len(df)}</div>
                <div class="metric-description">
                    Customers analyzed
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">CLUSTERS</div>
                <div class="metric-value">{optimal_k}</div>
                <div class="metric-description">
                    Customer segments
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">SILHOUETTE</div>
                <div class="metric-value">{sil_score:.2f}</div>
                <div class="metric-description">
                    Cluster quality
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        avg_income = df["Annual Income (k$)"].mean()

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">AVG INCOME</div>
                <div class="metric-value">${avg_income:.1f}k</div>
                <div class="metric-description">
                    Annual income
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        avg_spending = df["Spending Score (1-100)"].mean()

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">AVG SPENDING</div>
                <div class="metric-value">{avg_spending:.1f}</div>
                <div class="metric-description">
                    Spending score
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="section-title">Customer Segmentation Overview</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # CLUSTER SCATTER PLOT
    # --------------------------------------------------------

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        palette="viridis",
        s=100,
        alpha=0.8,
        ax=ax
    )

    ax.scatter(
        centers_original[:, 0],
        centers_original[:, 1],
        marker="X",
        s=300,
        color="red",
        edgecolor="black",
        linewidth=2,
        label="Centroids"
    )

    ax.set_title(
        "Mall Customer Segments",
        fontsize=18,
        fontweight="bold"
    )

    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score (1-100)")

    ax.grid(alpha=0.2)

    st.pyplot(fig)

    plt.close()


    # --------------------------------------------------------
    # TWO COLUMN SUMMARY
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="section-title">📊 Cluster Distribution</div>',
            unsafe_allow_html=True
        )

        counts = df["Cluster"].value_counts().sort_index()

        fig, ax = plt.subplots(figsize=(7, 4))

        bars = ax.bar(
            counts.index.astype(str),
            counts.values
        )

        ax.set_xlabel("Cluster")
        ax.set_ylabel("Number of Customers")
        ax.set_title("Customers per Cluster")

        for bar, value in zip(bars, counts.values):

            ax.text(
                bar.get_x() + bar.get_width()/2,
                value + 2,
                str(value),
                ha="center",
                fontweight="bold"
            )

        st.pyplot(fig)

        plt.close()


    with col2:

        st.markdown(
            '<div class="section-title">💡 Key Finding</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="info-box">

            The K-Means algorithm divided the mall's
            <b>{len(df)} customers</b> into
            <b>{optimal_k} distinct customer segments</b>.

            <br><br>

            The Silhouette Score is
            <b>{sil_score:.3f}</b>, indicating the
            quality of the clustering structure.

            <br><br>

            The segmentation is based on:

            <br>• Annual Income
            <br>• Spending Score

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# EDA PAGE
# ============================================================

elif page == "📊 EDA & Analytics":

    st.markdown(
        '<div class="main-title">📊 Exploratory Data Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Understand the customer dataset before clustering.</div>',
        unsafe_allow_html=True
    )


    # Dataset overview

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1] - 1
    )

    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )


    st.markdown(
        '<div class="section-title">Dataset Preview</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        df.drop(columns=["Cluster"]),
        use_container_width=True
    )


    # --------------------------------------------------------
    # DISTRIBUTIONS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Feature Distributions</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)


    with col1:

        fig, ax = plt.subplots()

        sns.histplot(
            df["Age"],
            bins=20,
            kde=True,
            ax=ax
        )

        ax.set_title("Age Distribution")

        st.pyplot(fig)

        plt.close()


    with col2:

        fig, ax = plt.subplots()

        sns.histplot(
            df["Annual Income (k$)"],
            bins=20,
            kde=True,
            ax=ax
        )

        ax.set_title("Annual Income Distribution")

        st.pyplot(fig)

        plt.close()


    with col3:

        fig, ax = plt.subplots()

        sns.histplot(
            df["Spending Score (1-100)"],
            bins=20,
            kde=True,
            ax=ax
        )

        ax.set_title("Spending Score Distribution")

        st.pyplot(fig)

        plt.close()


    # --------------------------------------------------------
    # RELATIONSHIPS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Feature Relationships</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    with col1:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.scatterplot(
            data=df,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            hue="Gender",
            s=80,
            ax=ax
        )

        ax.set_title(
            "Income vs Spending Score"
        )

        st.pyplot(fig)

        plt.close()


    with col2:

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.scatterplot(
            data=df,
            x="Age",
            y="Spending Score (1-100)",
            hue="Gender",
            s=80,
            ax=ax
        )

        ax.set_title(
            "Age vs Spending Score"
        )

        st.pyplot(fig)

        plt.close()


# ============================================================
# CUSTOMER SEGMENTATION
# ============================================================

elif page == "🎯 Customer Segmentation":

    st.markdown(
        '<div class="main-title">🎯 Customer Segmentation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Visualize the customer groups identified by K-Means.</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # SELECT AXES
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    x_axis = col1.selectbox(
        "Select X-axis",
        [
            "Annual Income (k$)",
            "Age",
            "Spending Score (1-100)"
        ]
    )

    y_axis = col2.selectbox(
        "Select Y-axis",
        [
            "Spending Score (1-100)",
            "Annual Income (k$)",
            "Age"
        ]
    )


    # --------------------------------------------------------
    # PLOT
    # --------------------------------------------------------

    fig, ax = plt.subplots(figsize=(11, 7))

    sns.scatterplot(
        data=df,
        x=x_axis,
        y=y_axis,
        hue="Cluster",
        palette="viridis",
        s=100,
        alpha=0.8,
        ax=ax
    )

    ax.set_title(
        "Interactive Customer Segmentation",
        fontsize=18,
        fontweight="bold"
    )

    ax.grid(alpha=0.2)

    st.pyplot(fig)

    plt.close()


    # --------------------------------------------------------
    # CLUSTER COUNTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Cluster Distribution</div>',
        unsafe_allow_html=True
    )

    counts = df["Cluster"].value_counts().sort_index()

    distribution = pd.DataFrame({
        "Cluster": counts.index,
        "Customers": counts.values,
        "Percentage": (
            counts.values / len(df) * 100
        ).round(1)
    })

    st.dataframe(
        distribution,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CLUSTER PROFILES
# ============================================================

elif page == "👥 Cluster Profiles":

    st.markdown(
        '<div class="main-title">👥 Cluster Profiles</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Understand the characteristics of each customer segment.</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PROFILE TABLE
    # --------------------------------------------------------

    profile = df.groupby("Cluster")[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ].mean().round(2)

    profile["Customers"] = (
        df["Cluster"]
        .value_counts()
        .sort_index()
    )

    profile["Percentage"] = (
        profile["Customers"] /
        len(df) * 100
    ).round(1)

    st.dataframe(
        profile,
        use_container_width=True
    )


    # --------------------------------------------------------
    # CLUSTER SELECTOR
    # --------------------------------------------------------

    selected_cluster = st.selectbox(
        "Select a Cluster",
        range(optimal_k)
    )

    cluster_data = df[
        df["Cluster"] == selected_cluster
    ]


    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        len(cluster_data)
    )

    col2.metric(
        "Average Age",
        f"{cluster_data['Age'].mean():.1f}"
    )

    col3.metric(
        "Average Income",
        f"${cluster_data['Annual Income (k$)'].mean():.1f}k"
    )

    col4.metric(
        "Spending Score",
        f"{cluster_data['Spending Score (1-100)'].mean():.1f}"
    )


    # --------------------------------------------------------
    # PROFILE VISUALIZATION
    # --------------------------------------------------------

    fig, ax = plt.subplots(figsize=(9, 5))

    values = [
        cluster_data["Age"].mean(),
        cluster_data["Annual Income (k$)"].mean(),
        cluster_data["Spending Score (1-100)"].mean()
    ]

    labels_profile = [
        "Age",
        "Income",
        "Spending"
    ]

    ax.bar(
        labels_profile,
        values
    )

    ax.set_title(
        f"Profile of Cluster {selected_cluster}",
        fontsize=17,
        fontweight="bold"
    )

    st.pyplot(fig)

    plt.close()


    st.markdown(
        '<div class="section-title">Customers in this Cluster</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        cluster_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CUSTOMER EXPLORER
# ============================================================

elif page == "🔎 Customer Explorer":

    st.markdown(
        '<div class="main-title">🔎 Customer Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Explore individual customers and their assigned segment.</div>',
        unsafe_allow_html=True
    )


    customer_id_column = None

    if "CustomerID" in df.columns:
        customer_id_column = "CustomerID"


    if customer_id_column:

        customer_id = st.selectbox(
            "Select Customer ID",
            df[customer_id_column].tolist()
        )

        customer = df[
            df[customer_id_column] == customer_id
        ].iloc[0]

        cluster = int(customer["Cluster"])


        st.markdown(
            '<div class="section-title">Customer Information</div>',
            unsafe_allow_html=True
        )


        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Customer ID",
            customer_id
        )

        col2.metric(
            "Age",
            customer["Age"]
        )

        col3.metric(
            "Income",
            f"${customer['Annual Income (k$)']}k"
        )

        col4.metric(
            "Spending Score",
            customer["Spending Score (1-100)"]
        )


        st.success(
            f"This customer belongs to **Cluster {cluster}**."
        )


        st.dataframe(
            pd.DataFrame([customer]),
            use_container_width=True
        )


# ============================================================
# MODEL EVALUATION
# ============================================================

elif page == "📈 Model Evaluation":

    st.markdown(
        '<div class="main-title">📈 Clustering Evaluation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Evaluate the quality of the K-Means clustering.</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Silhouette Score",
        f"{sil_score:.4f}"
    )

    col2.metric(
        "Calinski-Harabasz",
        f"{calinski_score:.2f}"
    )

    col3.metric(
        "Davies-Bouldin",
        f"{davies_score:.4f}"
    )


    # --------------------------------------------------------
    # EXPLANATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Metric Interpretation</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="insight-card">

        <div class="insight-title">
        Silhouette Score
        </div>

        <div class="insight-text">
        Score: <b>{sil_score:.4f}</b><br><br>

        Higher values indicate that customers are well
        separated between clusters.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="insight-card">

        <div class="insight-title">
        Calinski-Harabasz Index
        </div>

        <div class="insight-text">

        Score: <b>{calinski_score:.2f}</b><br><br>

        Higher values indicate better-defined and
        well-separated clusters.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="insight-card">

        <div class="insight-title">
        Davies-Bouldin Index
        </div>

        <div class="insight-text">

        Score: <b>{davies_score:.4f}</b><br><br>

        Lower values indicate better separation
        between clusters.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ELBOW METHOD
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Elbow Method</div>',
        unsafe_allow_html=True
    )


    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        k_values,
        wcss,
        marker="o",
        linewidth=2
    )

    ax.axvline(
        optimal_k,
        linestyle="--",
        linewidth=2,
        label=f"Selected k = {optimal_k}"
    )

    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("WCSS")
    ax.set_title("Elbow Method")

    ax.legend()

    st.pyplot(fig)

    plt.close()


    # --------------------------------------------------------
    # SILHOUETTE SCORES
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Silhouette Score by K</div>',
        unsafe_allow_html=True
    )


    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(
        k_values,
        silhouette_scores,
        marker="o",
        linewidth=2
    )

    ax.axvline(
        optimal_k,
        linestyle="--",
        linewidth=2,
        label=f"Selected k = {optimal_k}"
    )

    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Silhouette Analysis")

    ax.legend()

    st.pyplot(fig)

    plt.close()


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

elif page == "💡 Business Insights":

    st.markdown(
        '<div class="main-title">💡 Business Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Turn customer segmentation into marketing strategies.</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # GENERATE INSIGHTS
    # --------------------------------------------------------

    for i in range(optimal_k):

        cluster_data = df[
            df["Cluster"] == i
        ]

        income = cluster_data[
            "Annual Income (k$)"
        ].mean()

        spending = cluster_data[
            "Spending Score (1-100)"
        ].mean()

        age = cluster_data[
            "Age"
        ].mean()


        # Determine segment

        if income > 70 and spending > 60:

            title = "💎 High Value Customers"

            strategy = """
            These customers have relatively high income
            and high spending behavior.

            Recommended strategy:
            VIP programs, premium products,
            exclusive offers and loyalty rewards.
            """


        elif income > 70 and spending <= 60:

            title = "💰 Targetable Wealthy Customers"

            strategy = """
            These customers have high income but
            comparatively lower spending.

            Recommended strategy:
            Personalized promotions, premium product
            recommendations and targeted campaigns.
            """


        elif income <= 70 and spending > 60:

            title = "🛍️ Aspirational Shoppers"

            strategy = """
            These customers show strong spending behavior
            despite moderate income.

            Recommended strategy:
            Discounts, bundles, installment options
            and attractive promotions.
            """


        elif income <= 40 and spending <= 40:

            title = "💵 Frugal Customers"

            strategy = """
            These customers have relatively low income
            and low spending behavior.

            Recommended strategy:
            Affordable products, essential items,
            discounts and budget-friendly offers.
            """


        else:

            title = "👥 Moderate Customers"

            strategy = """
            These customers have moderate income
            and spending behavior.

            Recommended strategy:
            Cross-selling, up-selling and
            personalized engagement campaigns.
            """


        st.markdown(
            f"""
            <div class="insight-card">

            <div class="insight-title">
            Cluster {i}: {title}
            </div>

            <div class="insight-text">

            <b>Average Age:</b> {age:.1f} years<br>

            <b>Average Income:</b> ${income:.1f}k<br>

            <b>Average Spending Score:</b> {spending:.1f}/100

            <br><br>

            <b>Recommended Strategy:</b><br>

            {strategy}

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "📚 About Project":

    st.markdown(
        '<div class="main-title">📚 About the Project</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Mall Customer Segmentation using K-Means Clustering</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="info-box">

        <h3>🎯 Project Objective</h3>

        The objective of this project is to divide mall customers
        into meaningful groups based on their characteristics,
        particularly Annual Income and Spending Score.

        The project uses <b>K-Means Clustering</b>, an
        unsupervised machine learning algorithm.

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="section-title">🔄 Machine Learning Workflow</div>',
        unsafe_allow_html=True
    )


    steps = [
        ("1", "Dataset Loading", "Load and inspect customer data."),
        ("2", "EDA", "Explore distributions and feature relationships."),
        ("3", "Preprocessing", "Select and standardize clustering features."),
        ("4", "Optimal K", "Use Elbow Method and Silhouette Score."),
        ("5", "K-Means", "Train the clustering model."),
        ("6", "Visualization", "Visualize customer segments."),
        ("7", "Evaluation", "Evaluate cluster quality."),
        ("8", "Business Insights", "Convert clusters into marketing strategies.")
    ]


    for number, title, description in steps:

        st.markdown(
            f"""
            <div class="insight-card">

            <div class="insight-title">
            {number}. {title}
            </div>

            <div class="insight-text">
            {description}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '<div class="section-title">🧠 Technologies Used</div>',
        unsafe_allow_html=True
    )


    st.markdown(
    """
    <div class="tech-list">
        <div class="tech-item">🐍 Python</div>
        <div class="tech-item">🐼 Pandas</div>
        <div class="tech-item">🔢 NumPy</div>
        <div class="tech-item">🤖 Scikit-learn</div>
        <div class="tech-item">📊 Matplotlib</div>
        <div class="tech-item">📈 Seaborn</div>
        <div class="tech-item">🌐 Streamlit</div>
        <div class="tech-item">🎯 K-Means Clustering</div>
    </div>
    """,
    unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🛍️ <b>Mall Customer Segmentation Dashboard</b>

    <br>

    Built using Python, Scikit-learn & Streamlit

    <br>

    K-Means Clustering | Customer Analytics

    </div>
    """,
    unsafe_allow_html=True
)