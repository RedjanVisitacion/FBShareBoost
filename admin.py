import streamlit as st
import json
import time
from utils import load_users, save_users, remove_user
import cookie_getter
import follower_growth
import share_booster

def show_admin_login():
    """Display the admin login page."""
    st.markdown("""
    <div class="login-container admin-login auth-hero">
        <p class="welcome-kicker">Administrator</p>
        <h2 class="section-title">Admin Login</h2>
        <p>Enter administrator credentials to manage users, stats, and tools.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        with st.form("admin_login_form"):
            st.markdown("### Admin access")
            username = st.text_input("Admin Username", key="admin_username", placeholder="Enter admin username")
            password = st.text_input("Admin Password", type="password", key="admin_password", placeholder="Enter admin password")
            submit_button = st.form_submit_button("Login as Admin", use_container_width=True)
        
        if submit_button:
            username = username.strip()
            if username == "rpsv_codes" and password == "Redjan09":
                st.session_state.admin_authenticated = True
                st.session_state.page = "admin"
                st.success("Admin login successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid admin credentials")
    
    with col2:
        st.markdown("""
        <div class="login-info-card admin-info-card">
            <h3>Admin panel includes</h3>
            <ul>
                <li>User management</li>
                <li>System statistics</li>
                <li>Follower growth tracker</li>
                <li>Tool access from one panel</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Add a back button
    if st.button("Back to Home", key="admin_back_btn"):
        st.session_state.page = "main"
        st.rerun()

def show_admin_dashboard():
    """Display the admin dashboard."""
    # Admin tabs
    admin_tab, tools_tab, growth_tab, cookie_tab, share_tab = st.tabs(["User Management", "System Stats", "Follower Growth", "Cookie Getter", "Share Booster"])
    
    with admin_tab:
        st.markdown("""
        <div class="admin-dashboard-header">
            <h2 class="section-title">User Management</h2>
            <p>Manage users registered in the system</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Load user data
        user_data = load_users()
        
        if not user_data["users"]:
            st.info("No users registered in the system")
        else:
            # User removal implementation
            user_to_remove = st.selectbox("Select a user to remove:", 
                                        [user["username"] for user in user_data["users"]])
            
            if st.button("Remove Selected User", key="remove_user_btn", use_container_width=True):
                if remove_user(user_to_remove):
                    st.success(f"User '{user_to_remove}' successfully removed")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(f"Failed to remove user '{user_to_remove}'")
            
            # Display user table
            st.markdown("<div class='user-table-container'>", unsafe_allow_html=True)
            
            user_table = "<table class='user-table'><thead><tr><th>Username</th><th>Created At</th><th>Last Login</th></tr></thead><tbody>"
            
            for user in user_data["users"]:
                username = user.get("username", "N/A")
                created_at = user.get("created_at", "N/A")
                last_login = user.get("last_login", "N/A")
                
                user_table += f"<tr><td>{username}</td><td>{created_at}</td><td>{last_login}</td></tr>"
            
            user_table += "</tbody></table>"
            st.markdown(user_table, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    with tools_tab:
        st.markdown("""
        <div class="admin-dashboard-header">
            <h2 class="section-title">System Statistics</h2>
            <p>Monitor system performance and usage</p>
        </div>
        """, unsafe_allow_html=True)
        
        # System Statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Users", len(user_data["users"]))
        with col2:
            st.metric("Active Today", sum(1 for user in user_data["users"] if "last_login" in user and user["last_login"].startswith(time.strftime("%Y-%m-%d"))))
        with col3:
            st.metric("New Users (Today)", sum(1 for user in user_data["users"] if "created_at" in user and user["created_at"].startswith(time.strftime("%Y-%m-%d"))))
        
        # Add any additional admin tools or settings here
        st.markdown("### System Settings")
        st.write("Future settings will appear here")

    with growth_tab:
        st.markdown("""
        <div class="admin-tool-header">
            <h2 class="section-title">Follower Growth Tool</h2>
            <p>Plan real follower growth campaigns and track progress</p>
        </div>
        """, unsafe_allow_html=True)

        follower_growth.show_follower_growth()
    
    with cookie_tab:
        st.markdown("""
        <div class="admin-tool-header">
            <h2 class="section-title">Cookie Getter Tool</h2>
            <p>Access the cookie getter tool directly from admin panel</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show the cookie getter interface
        cookie_getter.show_cookie_getter()
    
    with share_tab:
        st.markdown("""
        <div class="admin-tool-header">
            <h2 class="section-title">Share Booster Tool</h2>
            <p>Access the share booster tool directly from admin panel</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show the share booster interface
        share_booster.show_share_booster()
