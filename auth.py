import streamlit as st
import json
import os
import time
import uuid
import hashlib
from utils import load_users, add_user, update_last_login, verify_user

def show_login_page():
    """Display the user login page."""
    st.markdown("""
    <div class="login-container auth-hero">
        <p class="welcome-kicker">User Account</p>
        <h2 class="section-title">Login or Create Account</h2>
        <p>Access your dashboard, follower growth tracker, cookie tools, and share tools.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for login and signup
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
    
    with login_tab:
        col1, col2 = st.columns([3, 2])
        
        with col1:
            with st.form("user_login_form"):
                st.markdown("### Welcome back")
                username = st.text_input("Username", key="login_username", placeholder="Enter your username")
                password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
                submit_button = st.form_submit_button("Login", use_container_width=True)

            if submit_button:
                username = username.strip()
                if not username or not password:
                    st.error("Username and password cannot be empty")
                else:
                    # Verify user credentials
                    result = verify_user(username, password)
                    
                    if result["success"]:
                        # Update last login time
                        update_last_login(username)
                        
                        # Set session state
                        st.session_state.authenticated = True
                        st.session_state.current_user = username
                        st.session_state.page = "main"
                        
                        st.success("Login successful!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(result["message"])
        
        with col2:
            st.markdown("""
            <div class="login-info-card">
                <h3>What happens after login?</h3>
                <ul>
                    <li>Your local app session opens</li>
                    <li>You can use dashboard tools</li>
                    <li>You can track follower growth plans</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with signup_tab:
        col1, col2 = st.columns([3, 2])
        
        with col1:
            with st.form("user_signup_form"):
                st.markdown("### Create your account")
                new_username = st.text_input("Choose Username", key="signup_username", placeholder="Example: redjan")
                new_password = st.text_input("Choose Password", type="password", key="signup_password", placeholder="Create a password")
                confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", placeholder="Repeat your password")
                signup_button = st.form_submit_button("Create Account", use_container_width=True)

            if signup_button:
                new_username = new_username.strip()
                if not new_username or not new_password or not confirm_password:
                    st.error("All fields are required")
                elif len(new_password) < 6:
                    st.error("Password must be at least 6 characters")
                elif new_password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    # Check if username already exists
                    users_data = load_users()
                    user_exists = False
                    
                    for user in users_data["users"]:
                        if user["username"] == new_username:
                            user_exists = True
                            break
                    
                    if user_exists:
                        st.error(f"Username '{new_username}' is already taken")
                    else:
                        # Hash the password and create new user
                        password_hash = hashlib.sha256(new_password.encode()).hexdigest()
                        
                        # Create the user account
                        users_data["users"].append({
                            "username": new_username,
                            "password": password_hash,
                            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                            "last_login": time.strftime("%Y-%m-%d %H:%M:%S")
                        })
                        
                        # Save the updated user data
                        with open("data/users.json", "w") as f:
                            json.dump(users_data, f, indent=4)
                        
                        # Set session state
                        st.session_state.authenticated = True
                        st.session_state.current_user = new_username
                        st.session_state.page = "main"
                        
                        st.success("Account created and logged in successfully!")
                        time.sleep(1)
                        st.rerun()
        
        with col2:
            st.markdown("""
            <div class="login-info-card">
                <h3>Account setup</h3>
                <ul>
                    <li>Stored locally in this project</li>
                    <li>Password is saved as a hash</li>
                    <li>Account opens right after signup</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Add a back button
    if st.button("Back to Home", key="back_btn"):
        st.session_state.page = "main"
        st.rerun()
