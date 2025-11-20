import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏠 Boston Housing Data Analysis App")

uploaded_file = st.file_uploader("Upload your Boston Housing CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Show dataset
    st.subheader("🔹 First 10 Rows")
    st.write(df.head(10))

    st.subheader("🔹 Column Names")
    st.write(df.columns.tolist())

    st.subheader("🔹 Summary Statistics")
    st.write(df.describe())

    st.subheader("🔹 Shape (Rows, Columns)")
    st.write(df.shape)

    st.subheader("🔹 Missing Values")
    st.write(df.isnull().sum())

    # Filtering operations
    st.header("📌 Filtering")

    # Houses with price > 30
    if "MEDV" in df.columns:
        st.subheader("Houses with Price > 30 (MEDV > 30)")
        st.write(df[df["MEDV"] > 30])
    else:
        st.warning("MEDV column not found. Please check your CSV header.")

    # Houses with more than 6 rooms
    if "RM" in df.columns:
        st.subheader("Houses with More Than 6 Rooms (RM > 6)")
        st.write(df[df["RM"] > 6])
    else:
        st.warning("RM column not found.")

    # Low crime rate
    if "CRIM" in df.columns:
        st.subheader("Low Crime Rate (CRIM < 0.1)")
        st.write(df[df["CRIM"] < 0.1])
    else:
        st.warning("CRIM column not found.")

    # Grouping
    st.header("📌 Grouping")

    if "RM" in df.columns and "MEDV" in df.columns:
        st.subheader("Average Price by Number of Rooms")
        st.write(df.groupby("RM")["MEDV"].mean())
    else:
        st.warning("Cannot group because RM or MEDV missing.")

    # Visualization
    st.header("📊 Visualization")

    if "RM" in df.columns and "MEDV" in df.columns:
        st.subheader("Rooms vs Price Scatter Plot")

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(df["RM"], df["MEDV"])
        ax.set_xlabel("Rooms (RM)")
        ax.set_ylabel("House Price (MEDV)")
        ax.set_title("Rooms vs Price Scatter Plot")
        st.pyplot(fig)
    else:
        st.warning("Cannot show scatter plot because RM or MEDV missing.")
else:
    st.info("Please upload a CSV file to begin.")
