import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="PhonePe Transaction Insights",
    page_icon="📱",
    layout="wide"
)


# Database connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="phonepe"
)


def get_data(query):
    return pd.read_sql(query, conn)



# Title

st.title("📱 PhonePe Transaction Insights Dashboard")

st.markdown(
"""
This dashboard analyzes PhonePe transactions, users and insurance trends
using PhonePe Pulse data.
"""
)


# Sidebar

section = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Overview",
        "Transactions",
        "Users",
        "Insurance"
    ]
)



# ---------------- OVERVIEW ----------------


if section=="Overview":


    st.header("📊 Overall Performance")


    transaction = get_data(
    """
    SELECT * FROM aggregated_transaction
    """
    )


    users = get_data(
    """
    SELECT * FROM aggregated_user
    """
    )


    insurance = get_data(
    """
    SELECT * FROM aggregated_insurance
    """
    )


    c1,c2,c3,c4 = st.columns(4)


    c1.metric(
        "Total Transactions",
        f"{transaction.transaction_count.sum():,.0f}"
    )


    c2.metric(
        "Transaction Value",
        f"₹ {transaction.transaction_amount.sum()/1e9:.2f} B"
    )


    c3.metric(
        "Registered Users",
        f"{users.registered_users.max():,.0f}"
    )


    c4.metric(
        "Insurance Value",
        f"₹ {insurance.transaction_amount.sum()/1e6:.2f} M"
    )


    yearly = transaction.groupby(
        "year"
    )["transaction_amount"].sum().reset_index()


    fig = px.line(
        yearly,
        x="year",
        y="transaction_amount",
        markers=True,
        title="Transaction Growth"
    )


    st.plotly_chart(fig,use_container_width=True)



# ---------------- TRANSACTION ----------------


elif section=="Transactions":


    st.header("💳 Transaction Analysis")


    df=get_data(
    """
    SELECT *
    FROM aggregated_transaction
    """
    )


    year=st.selectbox(
        "Select Year",
        sorted(df.year.unique())
    )


    filtered=df[
        df.year==year
    ]


    state=filtered.groupby(
        "state"
    )["transaction_amount"].sum().reset_index()


    fig=px.bar(
        state.sort_values(
            "transaction_amount",
            ascending=False
        ).head(10),

        x="state",

        y="transaction_amount",

        title=f"Top States - {year}"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    types=filtered.groupby(
        "transaction_type"
    )["transaction_count"].sum().reset_index()


    fig2=px.pie(
        types,
        names="transaction_type",
        values="transaction_count",
        title="Transaction Types"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



# ---------------- USERS ----------------


elif section=="Users":


    st.header("👥 User Analytics")


    df=get_data(
    """
    SELECT *
    FROM aggregated_user
    """
    )


    yearly=df.groupby(
        "year"
    )["registered_users"].sum().reset_index()



    fig=px.area(
        yearly,
        x="year",
        y="registered_users",
        title="User Growth"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    states=df.groupby(
        "state"
    )["registered_users"].max().reset_index()


    fig2=px.bar(
        states.sort_values(
            "registered_users",
            ascending=False
        ).head(10),

        x="state",

        y="registered_users",

        title="Top User States"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



# ---------------- INSURANCE ----------------


elif section=="Insurance":


    st.header("🛡️ Insurance Analysis")


    df=get_data(
    """
    SELECT *
    FROM aggregated_insurance
    """
    )


    states=df.groupby(
        "state"
    )["transaction_amount"].sum().reset_index()



    fig=px.bar(
        states.sort_values(
            "transaction_amount",
            ascending=False
        ).head(10),

        x="state",

        y="transaction_amount",

        title="Top Insurance States"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )