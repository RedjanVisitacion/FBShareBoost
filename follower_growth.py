import time

import streamlit as st

from utils import (
    add_growth_campaign,
    load_follower_growth,
    remove_growth_campaign,
    update_campaign_status,
    update_growth_goal,
)


STATUSES = ["Planned", "Active", "Done", "Paused"]
CHANNELS = ["Facebook Page", "Facebook Profile", "Group Post", "Reel", "Story", "Live", "Other"]


def _progress_percent(current_followers, target_followers):
    if target_followers <= 0:
        return 0
    return min(100, int((current_followers / target_followers) * 100))


def show_follower_growth():
    """Display a safe follower growth planning dashboard."""
    data = load_follower_growth()
    current_followers = int(data.get("current_followers", 0))
    target_followers = int(data.get("target_followers", 0))
    weekly_goal = int(data.get("weekly_goal", 0))
    progress = _progress_percent(current_followers, target_followers)
    remaining = max(target_followers - current_followers, 0)

    st.markdown("""
    <div class="follower-growth-header">
        <h2 class="section-title">Follower Growth Dashboard</h2>
        <p>Plan campaigns, track follower goals, and grow with real content activity.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Current Followers", current_followers)
    with col2:
        st.metric("Target Followers", target_followers)
    with col3:
        st.metric("Remaining", remaining)
    with col4:
        st.metric("Weekly Goal", weekly_goal)

    st.progress(progress)
    st.caption(f"{progress}% of your follower target reached")

    goal_tab, campaign_tab, tracker_tab, ideas_tab = st.tabs([
        "Goals",
        "Campaign Planner",
        "Tracker",
        "Content Ideas",
    ])

    with goal_tab:
        st.markdown("""
        <div class="method-description">
            <h3>Follower Goals</h3>
            <p>Update these numbers manually as your page grows.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("follower_goal_form"):
            goal_col1, goal_col2, goal_col3 = st.columns(3)
            with goal_col1:
                new_current = st.number_input(
                    "Current Followers",
                    min_value=0,
                    value=current_followers,
                    step=1,
                )
            with goal_col2:
                new_target = st.number_input(
                    "Target Followers",
                    min_value=0,
                    value=target_followers,
                    step=10,
                )
            with goal_col3:
                new_weekly = st.number_input(
                    "Weekly Goal",
                    min_value=0,
                    value=weekly_goal,
                    step=5,
                )

            if st.form_submit_button("Save Goals", use_container_width=True):
                update_growth_goal(new_current, new_target, new_weekly)
                st.success("Follower goals updated.")
                time.sleep(0.5)
                st.rerun()

    with campaign_tab:
        st.markdown("""
        <div class="method-description">
            <h3>Campaign Planner</h3>
            <p>Create real growth activities such as posts, reels, lives, collaborations, or group campaigns.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("growth_campaign_form"):
            title = st.text_input("Campaign Title", placeholder="Example: Friday reel series")
            form_col1, form_col2 = st.columns(2)
            with form_col1:
                channel = st.selectbox("Channel", CHANNELS)
                planned_date = st.date_input("Planned Date")
            with form_col2:
                expected_followers = st.number_input(
                    "Expected New Followers",
                    min_value=0,
                    value=10,
                    step=1,
                )
                status = st.selectbox("Status", STATUSES)

            post_url = st.text_input("Post or Page URL", placeholder="https://www.facebook.com/...")
            notes = st.text_area("Campaign Notes", placeholder="Audience, hook, CTA, hashtags, or posting plan")

            if st.form_submit_button("Add Campaign", use_container_width=True):
                if not title.strip():
                    st.error("Campaign title is required.")
                else:
                    add_growth_campaign(
                        title.strip(),
                        channel,
                        post_url.strip(),
                        planned_date,
                        expected_followers,
                        status,
                        notes.strip(),
                    )
                    st.success("Campaign added.")
                    time.sleep(0.5)
                    st.rerun()

    with tracker_tab:
        campaigns = data.get("campaigns", [])
        if not campaigns:
            st.info("No campaigns yet. Add one in the Campaign Planner tab.")
        else:
            st.markdown("<div class='user-table-container'>", unsafe_allow_html=True)
            rows = [
                "<table class='user-table'><thead><tr>"
                "<th>Title</th><th>Channel</th><th>Date</th><th>Status</th><th>Expected</th>"
                "</tr></thead><tbody>"
            ]
            for campaign in campaigns:
                rows.append(
                    "<tr>"
                    f"<td>{campaign.get('title', '')}</td>"
                    f"<td>{campaign.get('channel', '')}</td>"
                    f"<td>{campaign.get('planned_date', '')}</td>"
                    f"<td>{campaign.get('status', '')}</td>"
                    f"<td>{campaign.get('expected_followers', 0)}</td>"
                    "</tr>"
                )
            rows.append("</tbody></table>")
            st.markdown("".join(rows), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            campaign_options = {
                f"{campaign.get('title', 'Untitled')} - {campaign.get('planned_date', '')}": campaign["id"]
                for campaign in campaigns
            }
            selected_label = st.selectbox("Select Campaign", list(campaign_options.keys()))
            selected_id = campaign_options[selected_label]

            action_col1, action_col2 = st.columns(2)
            with action_col1:
                new_status = st.selectbox("Update Status", STATUSES, key="growth_status_update")
                if st.button("Save Status", use_container_width=True):
                    update_campaign_status(selected_id, new_status)
                    st.success("Campaign status updated.")
                    time.sleep(0.5)
                    st.rerun()
            with action_col2:
                if st.button("Remove Campaign", use_container_width=True):
                    remove_growth_campaign(selected_id)
                    st.success("Campaign removed.")
                    time.sleep(0.5)
                    st.rerun()

    with ideas_tab:
        st.markdown("""
        <div class="method-description">
            <h3>Growth Checklist</h3>
            <p>Use these prompts to plan authentic follower growth.</p>
        </div>
        """, unsafe_allow_html=True)

        st.checkbox("Pin a clear intro or offer post on the page")
        st.checkbox("Post a short reel with a direct follow call-to-action")
        st.checkbox("Reply to comments within the first hour")
        st.checkbox("Share one behind-the-scenes or proof post")
        st.checkbox("Invite engaged commenters to follow the page")
        st.checkbox("Review which campaign brought the most profile visits")

        st.markdown("""
        <div class="cookie-info">
            <p>Best practice: track real campaigns here, then update the follower count once a day.</p>
        </div>
        """, unsafe_allow_html=True)
