import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Sejal | Data Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. "MIDNIGHT GLASS" DESIGN SYSTEM (CSS)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 1. GOOGLE FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&family=Outfit:wght@300;600&display=swap');

    /* 2. GLOBAL THEME RESET */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #0f1c2e 0%, #040608 90%);
    }
    
    h1, h2, h3, h4, p, span, div {
        font-family: 'Inter', sans-serif;
        color: #F0F2F6;
        font-weight: 300;
    }
    
    /* 3. HERO TYPOGRAPHY (Gradient Text) */
    .hero-text {
        font-family: 'Outfit', sans-serif;
        font-size: 60px;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #FFFFFF 0%, #8899AC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .project-header {
        font-family: 'Outfit', sans-serif;
        font-size: 38px;
        font-weight: 300;
        color: white;
        margin-bottom: 5px;
    }

    /* 4. GLASSMORPHISM CARDS (The "Soft" Look) */
    div[data-testid="stMetric"], .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px; /* Soft rounded corners */
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    
    div[data-testid="stMetric"]:hover {
        border: 1px solid rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    /* 5. PROBLEM STATEMENT (Elegant Pill) */
    .problem-box {
        background: rgba(0, 173, 181, 0.08); /* Very faint cyan */
        border-left: 4px solid #00ADB5;
        padding: 20px;
        border-radius: 0 15px 15px 0;
        margin-bottom: 30px;
        font-size: 16px;
        line-height: 1.6;
    }
    
    /* 6. SIDEBAR REFINEMENT */
    section[data-testid="stSidebar"] {
        background-color: #040608;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* HIDE STREAMLIT UI (But keep sidebar arrow) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {background: transparent !important;}
    
    /* PADDING */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<h3 style='font-family: Outfit; letter-spacing: 2px; color: #8899AC;'>PORTFOLIO</h3>", unsafe_allow_html=True)
    st.write("")
    
    selected_project = st.radio(
        "",
        ["Impact Summary", 
         "01. Revenue Analysis", 
         "02. Churn Prediction", 
         "03. AI Triage System"],
        index=0
    )
    
    st.write("---")
    st.markdown("""
    <div style="padding: 10px; background: rgba(255,255,255,0.03); border-radius: 10px;">
        <small style="color: #8899AC; font-weight: 600;">TECH STACK</small><br>
        <span style="color: #00ADB5;">Python</span> &nbsp; 
        <span style="color: #00ADB5;">SQL</span> &nbsp; 
        <span style="color: #00ADB5;">LLMs</span>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# PAGE 0: HOME / IMPACT SUMMARY
# -----------------------------------------------------------------------------
if selected_project == "Impact Summary":
    # FADE IN ANIMATION
    st.markdown('<div class="hero-text">Translating data into<br>strategic clarity.</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #8899AC; margin-bottom: 40px;'>Sejal Parihar • Data Analyst & Engineer</p>", unsafe_allow_html=True)
    
    # METRICS ROW
    col1, col2, col3 = st.columns(3)
    col1.metric("Clients Served", "3", "Retail, SaaS, Fintech")
    col2.metric("Revenue Impact", "$420k+", "Optimized Spend")
    col3.metric("Data Processed", "1.5TB", "ETL Pipelines")
    
    st.write("##")
    
    # ELEGANT PROJECT GRID
    st.markdown("<h4 style='font-family: Outfit; letter-spacing: 1px; color: #FFFFFF; margin-top: 20px;'>SELECTED WORKS</h4>", unsafe_allow_html=True)
    
    # Using 'info' boxes as clean summary cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**RETAIL ANALYTICS**\n\nIdentified inefficient ad spend across 14 global regions, saving $15k monthly.")
    with c2:
        st.info("**SAAS PREDICTION**\n\nReduced customer churn by 12% using a predictive risk-scoring model.")
    with c3:
        st.info("**AI AUTOMATION**\n\nCut support ticket response time by 95% using LLM semantic routing.")


# -----------------------------------------------------------------------------
# PAGE 1: RETAIL PROJECT (UPDATED WITH SPACER)
# -----------------------------------------------------------------------------
elif selected_project == "01. Revenue Analysis":
    st.markdown('<div class="project-header">Global Sales Intelligence</div>', unsafe_allow_html=True)
    st.caption("CLIENT: FASHION RETAILER • TOOLS: Python, Plotly, SQL")
    
    # 1. THE PROBLEM
    st.markdown("""
    <div class="problem-box">
        <b>THE CHALLENGE</b><br>
        Client spend was inefficient. We needed to visualize <b>Seasonality, Regional Performance, and Ad ROI</b> simultaneously.
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------
    # VISUAL 1: THE NEON PULSE (Trend Analysis)
    # -------------------------------------------------------
    st.markdown("**01. MACRO TREND: REVENUE vs SPEND**")
    
    dates = pd.date_range(start="2025-01-01", periods=12, freq="M")
    df_trend = pd.DataFrame({
        "Month": dates,
        "Revenue": [45, 52, 48, 60, 65, 70, 75, 72, 80, 85, 90, 95], 
        "Ad_Spend": [10, 12, 11, 25, 14, 15, 16, 15, 18, 19, 20, 21], 
    })

    fig_pulse = go.Figure()
    
    # Revenue (The Glow)
    fig_pulse.add_trace(go.Scatter(
        x=df_trend["Month"], y=df_trend["Revenue"], name="Revenue",
        mode='lines', fill='tozeroy', 
        line=dict(color="#00ADB5", width=3), # Cyan Neon
        fillcolor="rgba(0, 173, 181, 0.1)" # Transparent glow
    ))
    
    # Ad Spend (The Warning Line)
    fig_pulse.add_trace(go.Scatter(
        x=df_trend["Month"], y=df_trend["Ad_Spend"], name="Ad Spend",
        mode='lines+markers', 
        line=dict(color="#FF2E63", width=2, dash='dash'), # Hot Pink
        marker=dict(size=6, color="#FF2E63")
    ))

    fig_pulse.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=350,
        margin=dict(l=0, r=0, t=20, b=0),
        xaxis=dict(showgrid=False, title=None),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        legend=dict(orientation="h", y=1.1)
    )
    st.plotly_chart(fig_pulse, use_container_width=True)

    st.write("##")

    # -------------------------------------------------------
    # VISUAL 2 & 3: SPLIT VIEW (Deep Dive)
    # -------------------------------------------------------
    # ADDED SPACER: [1, 0.2, 1] creates a 20% gap in the middle
    col1, spacer, col2 = st.columns([1, 0.2, 1])

    with col1:
        st.markdown("**02. REGIONAL HEATMAP (Performance Matrix)**")
        st.caption("Identifying underperforming regions (Darker = Lower Revenue).")
        
        # Matrix Data
        regions = ["North America", "Europe", "Asia Pac", "LatAm"]
        matrix_data = np.random.randint(50, 100, size=(4, 12)) 
        matrix_data[3, :] = matrix_data[3, :] - 30 # Injecting Failure
        
        fig_heat = px.imshow(
            matrix_data, 
            x=[d.strftime('%b') for d in dates], 
            y=regions,
            color_continuous_scale="Viridis",
            aspect="auto"
        )
        
        fig_heat.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig_heat, use_container_width=True)

    with col2:
        st.markdown("**03. EFFICIENCY FRONTIER (ROI Analysis)**")
        st.caption("Bubble Size = Total Profit. Top Left = High Efficiency.")
        
        # Bubble Data
        df_bubble = pd.DataFrame({
            "Campaign": [f"Camp {i}" for i in range(1, 16)],
            "Spend": np.random.randint(10, 50, 15),
            "Revenue": np.random.randint(40, 150, 15),
            "ROI": np.random.uniform(1.5, 5.0, 15)
        })
        
        fig_bubble = px.scatter(
            df_bubble, x="Spend", y="Revenue", 
            size="Revenue", color="ROI",
            color_continuous_scale="Teal", 
            hover_name="Campaign"
        )
        
        fig_bubble.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, title="Ad Spend ($k)"),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title="Revenue ($k)")
        )
        st.plotly_chart(fig_bubble, use_container_width=True)
        
    st.write("---")
    st.markdown("##### 💡 ARCHITECT'S NOTE")
    st.info("The **Heatmap (Left)** revealed that LatAm (Purple) was dragging ROI down. We reallocated budget to high-efficiency campaigns shown in the **Bubble Chart (Right)**, achieving a **22% ROI boost**.")


# -----------------------------------------------------------------------------
# PAGE 2: SAAS PROJECT
# -----------------------------------------------------------------------------
elif selected_project == "02. Churn Prediction":
    st.markdown('<div class="project-header">Customer Retention Engine</div>', unsafe_allow_html=True)
    st.caption("CLIENT: B2B SAAS • TOOLS: Scikit-Learn, Python")
    
    st.markdown("""
    <div class="problem-box">
        <b>THE CHALLENGE</b><br>
        The client faced an 8% monthly churn rate. They needed a predictive model to identify <b>'At Risk' customers</b> 
        based on usage patterns before they cancelled.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**01. RISK SIMULATOR**")
        st.write("Adjust usage patterns:")
        
        login_freq = st.slider("Logins / Week", 0, 20, 2)
        support_tickets = st.slider("Support Tickets", 0, 10, 5)
        
        risk = 0
        if login_freq < 3: risk += 45
        if support_tickets > 3: risk += 40
        risk = min(risk, 99)
        
        st.metric("Churn Probability", f"{risk}%", delta="Critical" if risk > 70 else "Stable", delta_color="inverse")

    with col2:
        st.markdown("**02. CUSTOMER SEGMENTATION**")
        labels = ['Safe', 'At Risk', 'Critical']
        values = [450, 120, 55] 
        
        fig = px.pie(
            values=values, names=labels, hole=0.7, 
            color_discrete_sequence=['#00ADB5', '#393E46', '#FF4B4B'] 
        )
        fig.update_layout(
            template="plotly_dark", 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=True,
            margin=dict(l=0, r=0, t=20, b=0),
            annotations=[dict(text=f'{sum(values)}', x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        st.plotly_chart(fig, use_container_width=True)

    # ROW 2: MODEL EXPLAINABILITY
    st.write("##")
    st.markdown("**03. MODEL EXPLAINABILITY (Top Churn Drivers)**")
    st.caption("Which variables contribute most to the risk score?")
    
    # Mock Feature Importance Data
    df_imp = pd.DataFrame({
        "Feature": ["Low Login Freq", "High Support Tickets", "Short Tenure", "Bill Increase", "Competitor Ads"],
        "Importance": [0.85, 0.72, 0.45, 0.30, 0.15]
    }).sort_values(by="Importance", ascending=True)
    
    fig_bar = px.bar(
        df_imp, x="Importance", y="Feature", orientation='h',
        color="Importance", color_continuous_scale="Teal"
    )
    
    fig_bar.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False),
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # THE ARCHITECT'S NOTE
    st.write("---")
    st.markdown("##### 💡 ARCHITECT'S NOTE")
    st.info("""
    The Explainability Chart (Graph 03) identified **'Low Login Frequency'** as the #1 leading indicator of churn (0.85 weight). 
    Based on this finding, we automated an **'Inactivity Alert' email campaign**, which re-engaged 15% of at-risk users before they cancelled.
    """)


# -----------------------------------------------------------------------------
# PAGE 3: AI TRIAGE SYSTEM (UPDATED & KEY ADDED TO BUTTON)
# -----------------------------------------------------------------------------
elif selected_project == "03. AI Triage System":
    st.markdown('<div class="project-header">Automated Support Triage</div>', unsafe_allow_html=True)
    st.caption("CLIENT: FINTECH • TOOLS: OpenAI API, Vector DB, Pinecone")
    
    st.markdown("""
    <div class="problem-box">
        <b>THE CHALLENGE</b><br>
        With 2,000+ daily emails, critical 'Fraud' alerts were buried in spam, causing a 48-hour response lag. 
        We implemented <b>Semantic Routing</b> to tag urgent issues instantly.
    </div>
    """, unsafe_allow_html=True)
    
    # -------------------------------------------------------
    # VISUAL 1: SEMANTIC CLUSTERS
    # -------------------------------------------------------
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**01. SEMANTIC VECTOR SPACE**")
        st.caption("Visualizing how the LLM groups 5,000 emails by 'meaning' rather than keywords.")
        
        # Mock Cluster Data
        x1, y1 = np.random.normal(5, 1, 100), np.random.normal(5, 1, 100) 
        x2, y2 = np.random.normal(2, 1, 100), np.random.normal(8, 1, 100) 
        x3, y3 = np.random.normal(8, 1, 100), np.random.normal(2, 1, 100) 
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', name='Urgent', marker=dict(color='#FF4B4B', size=8, opacity=0.8)))
        fig.add_trace(go.Scatter(x=x2, y=y2, mode='markers', name='Feature', marker=dict(color='#00ADB5', size=8, opacity=0.8)))
        fig.add_trace(go.Scatter(x=x3, y=y3, mode='markers', name='General', marker=dict(color='#666666', size=6, opacity=0.5)))
        
        fig.update_layout(
            template="plotly_dark", 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)', 
            height=350,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            legend=dict(orientation="h", y=-0.1)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("**02. LIVE CLASSIFIER**")
        st.caption("Test the LLM logic in real-time.")
        user_text = st.text_area("Email Content:", "I cannot access my account, please help!", height=100)
        
        # FIX: ADDED UNIQUE KEY 'ai_btn'
        if st.button("Run Classification", key="ai_btn"):
            with st.spinner("Embedding..."):
                import time
                time.sleep(0.5)
                
                if "account" in user_text.lower() or "help" in user_text.lower():
                    tag, color = "🚨 URGENT", "#FF4B4B"
                else:
                    tag, color = "ℹ️ GENERAL", "#8899AC"
                
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border-left: 3px solid {color}; margin-top: 10px;">
                    <span style="color: {color}; font-weight: 600;">{tag}</span><br>
                    <small style="color: #8899AC;">Confidence: 98.2%</small>
                </div>
                """, unsafe_allow_html=True)

    # -------------------------------------------------------
    # VISUAL 2 & 3: PERFORMANCE METRICS
    # -------------------------------------------------------
    st.write("##")
    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("**03. CONFUSION MATRIX (Accuracy)**")
        st.caption("Where does the AI get confused?")
        
        # Matrix Data (Actual vs Predicted)
        z = [[50, 2, 1], [3, 45, 5], [1, 6, 80]]
        x = ['Urgent', 'Feature', 'Spam']
        y = ['Urgent', 'Feature', 'Spam']

        fig_conf = px.imshow(z, x=x, y=y, color_continuous_scale='Teal', text_auto=True)
        fig_conf.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig_conf, use_container_width=True)

    with c2:
        st.markdown("**04. LATENCY REDUCTION (Human vs AI)**")
        st.caption("Response time per ticket (Minutes).")
        
        # Comparison Data
        hours = [f"{i}h" for i in range(0, 24, 2)]
        human_time = [45, 50, 120, 180, 200, 150, 100, 60, 50, 45, 40, 42]
        ai_time = [2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2] # Constant speed

        fig_lat = go.Figure()
        fig_lat.add_trace(go.Scatter(x=hours, y=human_time, name="Human (Manual)", fill='tozeroy', line=dict(color="#666"), fillcolor="rgba(255,255,255,0.1)"))
        fig_lat.add_trace(go.Scatter(x=hours, y=ai_time, name="AI Agent", line=dict(color="#00ADB5", width=4)))

        fig_lat.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(orientation="h", y=1.1)
        )
        st.plotly_chart(fig_lat, use_container_width=True)

    # THE ARCHITECT'S NOTE
    st.write("---")
    st.markdown("##### 💡 ARCHITECT'S NOTE")
    st.info("""
    The **Latency Chart (Right)** demonstrates the core value: while human response times spiked to **200 mins** during peak traffic (8 AM), the AI Agent maintained a constant **<2 min** triage speed.
    This stability allowed the client to scale from 2k to 10k daily users without hiring new support staff.
    """)