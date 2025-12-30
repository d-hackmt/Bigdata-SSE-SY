import streamlit as st
import pandas as pd

st.set_page_config(page_title="NoSQL Demo App", layout="wide")

st.title("🧠 NoSQL Databases — Visual & Intuitive Demo App")
st.write("This app helps you SEE how different NoSQL databases store data and how we retrieve it conceptually — without coding or database setup.")

db_type = st.sidebar.radio(
    "Choose NoSQL Type to Explore",
    ["📄 Document Database (MongoDB)",
     "🔑 Key–Value Store (Redis / DynamoDB)",
     "📚 Column Store (Cassandra / HBase)",
     "🕸 Graph Database (Neo4j)"
    ]
)

# ========================= DOCUMENT DB =========================
if db_type.startswith("📄"):
    st.header("📄 Document Database (MongoDB Style)")
    st.write("""
Document DB stores data as **documents** (like JSON objects).
Each record can have different fields. No fixed columns like SQL tables.
""")

    st.subheader("👀 How Data Looks")
    st.json({
        "product_id": "P101",
        "name": "iPhone 16",
        "category": "Mobile",
        "price": 79999,
        "features": ["AI Camera", "Fast Chip"],
        "reviews": [
            {"user": "Riya", "rating": 5},
            {"user": "Amit", "rating": 4}
        ],
        "available": True
    })

    st.subheader("🎯 What This Means")
    st.markdown("""
- Looks like a Python dictionary or JSON
- Different documents may have different fields
- Great for flexible, evolving data
""")

    st.subheader("🔎 Conceptual ‘Query’ Understanding")
    st.code("""
Find all products category = 'Mobile'
Find products price > 50000
Project only name + price
Group products and find avg rating
""")

    st.subheader("🌍 Real-World Applications")
    st.success("""
Amazon Products
User Profiles (Instagram, Facebook)
Content Management Systems
E-commerce Catalogs
""")


# ========================= KEY VALUE =========================
elif db_type.startswith("🔑"):
    st.header("🔑 Key–Value Databases (Redis / DynamoDB Style)")
    st.write("""
Stores data as **key → value pairs**.
Think of it like a super fast dictionary.
""")

    st.subheader("👀 How Data Looks")
    st.code("""
"user:101"   →  "{ name: 'Riya', plan: 'Premium', status: 'Watching' }"
"session:22" →  "Active"
"views:video1" → 10592
""")

    st.subheader("🎯 Meaning")
    st.markdown("""
- KEY = unique identifier
- VALUE = any data (text, json, number)
- Extremely FAST
""")

    st.subheader("🔎 Conceptual ‘Query’ Understanding")
    st.code("""
GET user:101
SET user:101
INCREASE video views
Auto delete session after 10 mins
""")

    st.subheader("🌍 Real Examples")
    st.success("""
Netflix — user watch sessions
Gaming apps — live scores
Banking — OTP session tracking
Website caching — blazing speed
""")


# ========================= COLUMN STORE =========================
elif db_type.startswith("📚"):
    st.header("📚 Column Store (Cassandra / HBase Style)")
    st.write("""
Stores data **column-wise instead of row-wise**.
Amazing for analytics and big data queries.
""")

    st.subheader("👀 How Data Looks")
    df = pd.DataFrame({
        "user_id":[101,101,102],
        "date_time":["2025-01-10 10:20PM","2025-01-10 11:10PM","2025-01-10 09:00PM"],
        "duration(sec)":[180,60,200],
        "tower_city":["Mumbai","Pune","Delhi"]
    })
    st.table(df)

    st.subheader("🎯 Meaning")
    st.markdown("""
- Data grouped by **user**
- Fast when reading specific columns
- Optimized for time-series & analytics
""")

    st.subheader("🔎 Conceptual ‘Query’ Understanding")
    st.code("""
Get all calls of user 101
Get last 10 recent calls
Get total usage by user
""")

    st.subheader("🌍 Real Examples")
    st.success("""
Telecom call records (Jio, Airtel)
IoT sensor streams
Bank transaction analytics
Log analysis (Big Data)
""")


# ========================= GRAPH DB =========================
else:
    st.header("🕸 Graph Database (Neo4j Style)")
    st.write("""
Graph DB is built for **relationships**.
Data is stored as:
- Nodes (people, accounts, devices)
- Relationships (connected to, transferred to)
""")

    st.subheader("👀 How Data Looks Conceptually")
    st.markdown("""
**Example: Fraud Detection**
```
(User A) ---- TRANSFERRED ----> (Account X)
(Account X) ---- TRANSFERRED ----> (Account Y)
(Account Y) ---- OWNS ----> (User B)
```
""")

    st.subheader("🎯 Meaning")
    st.markdown("""
- We CARE about connections
- Perfect for exploring networks
""")

    st.subheader("🔎 Conceptual ‘Query’ Understanding")
    st.code("""
Find all friends of a user
Find money transfer chains
Detect suspicious network
""")

    st.subheader("🌍 Real Uses")
    st.success("""
Facebook / LinkedIn — social graph
Banks — fraud detection
Amazon / Netflix — recommendation engine
Knowledge graphs
""")

st.info("Move through the sidebar to explore each type. This app is meant to **build intuition** and make NoSQL concepts visual and simple.")
