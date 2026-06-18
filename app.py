import streamlit as st
import json
import os
import time
from datetime import datetime

# Import custom modules
import utils
import auth
import admin
import cookie_getter
import follower_growth
import share_booster
import style

# Page configuration
st.set_page_config(
    page_title="FB Share Booster Pro",
    page_icon="F",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styling
style.apply_custom_styles()

# Create data directory if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Create users file if it doesn't exist
if not os.path.exists("data/users.json"):
    with open("data/users.json", "w") as f:
        json.dump({"users": []}, f)

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "page" not in st.session_state:
    st.session_state.page = "main"

# Display logo and header
st.markdown("""
<div class="header-container">
    <div class="logo-container">
        <svg class="logo" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="logo-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#7B68EE" />
                    <stop offset="100%" stop-color="#4B0082" />
                </linearGradient>
            </defs>
            <path d="M100,20 L180,90 L140,160 L60,160 L20,90 Z" fill="url(#logo-gradient)" />
            <text x="100" y="110" font-family="Arial" font-size="36" font-weight="bold" fill="white" text-anchor="middle">FB</text>
        </svg>
    </div>
    <h1 class="main-title">FB Share Booster Pro</h1>
</div>
""", unsafe_allow_html=True)

# Sidebar with navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h3>Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.authenticated:
        st.markdown(f"<div class='user-info'>Logged in as: {st.session_state.current_user}</div>", unsafe_allow_html=True)
        if st.button("Main Dashboard", key="nav_main"):
            st.session_state.page = "main"
        if st.button("Cookie Getter", key="nav_cookie"):
            st.session_state.page = "cookie_getter"
        if st.button("Follower Growth", key="nav_follower_growth"):
            st.session_state.page = "follower_growth"
        if st.button("Logout", key="nav_logout"):
            st.session_state.authenticated = False
            st.session_state.admin_authenticated = False
            st.session_state.current_user = None
            st.session_state.page = "main"
            st.rerun()
    elif st.session_state.admin_authenticated:
        st.markdown("<div class='admin-info'>Logged in as Admin</div>", unsafe_allow_html=True)
        if st.button("Admin Dashboard", key="nav_admin"):
            st.session_state.page = "admin"
        if st.button("Logout", key="nav_admin_logout"):
            st.session_state.authenticated = False
            st.session_state.admin_authenticated = False
            st.session_state.current_user = None
            st.session_state.page = "main"
            st.rerun()
    else:
        if st.button("Login", key="nav_login"):
            st.session_state.page = "login"
        if st.button("Admin Login", key="nav_admin_login"):
            st.session_state.page = "admin_login"

# Main content area
main_container = st.container()

with main_container:
    # Handle different pages
    if st.session_state.page == "login":
        auth.show_login_page()
    
    elif st.session_state.page == "admin_login":
        admin.show_admin_login()
    
    elif st.session_state.page == "admin" and st.session_state.admin_authenticated:
        admin.show_admin_dashboard()
    
    elif st.session_state.page == "cookie_getter" and st.session_state.authenticated:
        cookie_getter.show_cookie_getter()

    elif st.session_state.page == "follower_growth" and st.session_state.authenticated:
        follower_growth.show_follower_growth()
    
    elif st.session_state.authenticated:
        # Main dashboard with share booster
        share_booster.show_share_booster()
    
    else:
        # Welcome page with login options
        cols = st.columns([1, 4, 1])
        with cols[1]:
            st.markdown("""
            <div class="welcome-container welcome-panel">
                <p class="welcome-kicker">Account Access</p>
                <h2 class="welcome-title">Welcome to FB Share Booster Pro</h2>
                <p class="welcome-text">
                    Sign in to open your tools, or use admin access to manage users and growth tracking.
                </p>
                <div class="features-container">
                    <div class="feature">
                        <h3>User Login</h3>
                        <p>Open the share, cookie, and follower growth tools.</p>
                    </div>
                    <div class="feature">
                        <h3>Create Account</h3>
                        <p>Register a local account and start immediately.</p>
                    </div>
                    <div class="feature">
                        <h3>Admin Panel</h3>
                        <p>Manage users, stats, and campaign planning.</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Login", key="main_login_btn", use_container_width=True):
                    st.session_state.page = "login"
                    st.rerun()
            with col2:
                if st.button("Admin Login", key="main_admin_btn", use_container_width=True):
                    st.session_state.page = "admin_login"
                    st.rerun()

# Footer
st.markdown("""
<footer class="footer">
    <p>Copyright 2023 FB Share Booster Pro. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
