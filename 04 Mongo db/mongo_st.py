import streamlit as st
import pymongo
import pandas as pd
import plotly.express as px
import certifi

# --- CONNECTION ---
@st.cache_resource
def get_db():
    client = pymongo.MongoClient(st.secrets["mongo"]["uri"], tlsCAFile=certifi.where())
    return client["musixdb"]

db = get_db()

st.title("🎵 MusixDB Management Dashboard 2026")

# --- SIDEBAR: GLOBAL METRICS ---
with st.sidebar:
    st.header("Database Overview")
    st.metric("Total Tracks", db.tracks.count_documents({}))
    st.metric("Active Artists", db.artists.count_documents({"is_active": True}))

# --- TABS FOR OPERATIONS ---
tab1, tab2, tab3 = st.tabs(["📊 Analytics", "📝 CRUD Operations", "🔍 Search"])

# --- TAB 1: VISUALIZATIONS ---
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        # BPM vs Energy Scatter
        df_tracks = pd.DataFrame(list(db.tracks.find()))
        fig1 = px.scatter(df_tracks, x="bpm", y="energy", color="genre", 
                          size="bpm", hover_name="title", title="Track Energy vs Speed")
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        # Festival Capacity Bar
        df_fests = pd.DataFrame(list(db.festivals.find()))
        fig2 = px.bar(df_fests, x="name", y="capacity", color="genre_focus",
                      title="2026 Festival Scale (Capacity)")
        st.plotly_chart(fig2, use_container_width=True)

# --- TAB 2: CRUD (ARTIST EXAMPLE) ---
with tab2:
    st.subheader("Manage Artists")
    
    # CREATE
    with st.expander("➕ Add New Artist"):
        with st.form("new_artist"):
            name = st.text_input("Name")
            genre = st.selectbox("Genre", ["Rap", "Techno", "Psytrance"])
            pop = st.slider("Popularity", 0, 100, 50)
            if st.form_submit_button("Save"):
                db.artists.insert_one({"name": name, "genre": genre, "popularity": pop, "is_active": True})
                st.success(f"Added {name}")
                st.rerun()

    # READ / UPDATE / DELETE
    artists = list(db.artists.find())
    for a in artists:
        colA, colB, colC = st.columns([3, 1, 1])
        colA.write(f"**{a['name']}** ({a['genre']})")
        
        # UPDATE POPULARITY
        new_pop = colB.number_input("Pop", value=a['popularity'], key=f"pop_{a['_id']}")
        if colB.button("Update", key=f"upd_{a['_id']}"):
            db.artists.update_one({"_id": a["_id"]}, {"$set": {"popularity": new_pop}})
            st.rerun()
            
        # DELETE
        if colC.button("🗑️", key=f"del_{a['_id']}"):
            db.artists.delete_one({"_id": a["_id"]})
            st.rerun()

# --- TAB 3: SEARCH ---
with tab3:
    search = st.text_input("Find tracks by artist or title...")
    if search:
        results = db.tracks.find({"$or": [
            {"title": {"$regex": search, "$options": "i"}},
            {"artist": {"$regex": search, "$options": "i"}}
        ]})
        st.table(pd.DataFrame(list(results)).drop(columns=['_id']))
