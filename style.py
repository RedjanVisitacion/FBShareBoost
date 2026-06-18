import streamlit as st


def apply_custom_styles():
    """Apply custom CSS styles to the application."""
    st.markdown("""
    <style>
        :root {
            --bg: #0f1115;
            --surface: #171a21;
            --surface-raised: #20242d;
            --surface-soft: #262b35;
            --border: #343a46;
            --text: #f7f9fc;
            --muted: #aeb7c5;
            --primary: #2f80ed;
            --primary-hover: #1f6fd6;
            --accent: #18a058;
            --warning: #f2a900;
            --danger: #ef4444;
            --radius: 8px;
            --shadow: 0 18px 48px rgba(0, 0, 0, 0.28);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: var(--bg);
            color: var(--text);
            font-family: Inter, "Segoe UI", Arial, sans-serif;
        }

        .block-container {
            max-width: 1220px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        [data-testid="stHeader"] {
            background: rgba(15, 17, 21, 0.92);
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        [data-testid="stSidebar"] {
            background: #12151b;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] .stButton > button {
            justify-content: flex-start;
            width: 100%;
            background: transparent;
            border: 1px solid transparent;
            color: var(--muted);
            box-shadow: none;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background: var(--surface-raised);
            border-color: var(--border);
            color: var(--text);
            transform: none;
        }

        .sidebar-header h3 {
            margin: 0 0 1rem;
            color: var(--text);
            font-size: 1rem;
            font-weight: 700;
        }

        .header-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            min-height: 86px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
            background: linear-gradient(135deg, rgba(47, 128, 237, 0.14), rgba(24, 160, 88, 0.08));
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
        }

        .logo-container {
            width: 48px;
            height: 48px;
            flex: 0 0 48px;
        }

        .logo {
            width: 48px;
            height: 48px;
            filter: drop-shadow(0 8px 18px rgba(47, 128, 237, 0.28));
        }

        .main-title {
            color: var(--text);
            font-size: 2rem;
            line-height: 1.15;
            font-weight: 800;
            margin: 0;
            letter-spacing: 0;
        }

        .section-title {
            position: relative;
            color: var(--text);
            font-size: 1.55rem;
            line-height: 1.25;
            font-weight: 750;
            margin: 0 0 0.75rem;
            padding-left: 0.9rem;
            letter-spacing: 0;
        }

        .section-title::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0.15rem;
            width: 4px;
            height: 1.8rem;
            border-radius: 99px;
            background: var(--primary);
        }

        p, li, label, .stMarkdown {
            color: var(--text);
        }

        .welcome-container,
        .login-container,
        .admin-login,
        .method-description,
        .cookie-info-card,
        .login-info-card,
        .admin-info-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
        }

        .welcome-container {
            padding: 2rem;
            margin-bottom: 1.25rem;
        }

        .welcome-panel {
            max-width: 860px;
            margin-left: auto;
            margin-right: auto;
        }

        .welcome-kicker {
            display: inline-flex;
            align-items: center;
            min-height: 28px;
            padding: 0.25rem 0.65rem;
            margin: 0 0 0.9rem;
            border-radius: 999px;
            background: rgba(47, 128, 237, 0.14);
            color: #b8d4ff;
            border: 1px solid rgba(47, 128, 237, 0.28);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0;
        }

        .welcome-title {
            color: var(--text);
            font-size: 1.75rem;
            line-height: 1.2;
            margin: 0 0 0.75rem;
            letter-spacing: 0;
        }

        .welcome-text {
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1.25rem;
        }

        .features-container {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin-top: 1.25rem;
        }

        .feature {
            min-height: 126px;
            padding: 1.1rem;
            background: var(--surface-raised);
            border: 1px solid var(--border);
            border-radius: var(--radius);
        }

        .feature h3 {
            color: var(--text);
            font-size: 1rem;
            line-height: 1.25;
            margin: 0 0 0.75rem;
            overflow-wrap: anywhere;
        }

        .feature p {
            color: var(--muted);
            line-height: 1.5;
            margin: 0;
            overflow-wrap: anywhere;
        }

        .login-container,
        .admin-login {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--primary);
        }

        .auth-hero {
            max-width: 920px;
            margin-left: auto;
            margin-right: auto;
        }

        .auth-hero + div,
        .auth-hero ~ div {
            max-width: 920px;
            margin-left: auto;
            margin-right: auto;
        }

        div[data-testid="stForm"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.35rem;
            box-shadow: var(--shadow);
        }

        div[data-testid="stForm"] h3 {
            color: var(--text);
            margin-top: 0;
            margin-bottom: 1rem;
            font-size: 1.2rem;
        }

        .admin-login,
        .admin-info-card {
            border-left-color: var(--warning);
        }

        .login-info-card,
        .admin-info-card,
        .cookie-info-card {
            padding: 1.5rem;
            height: 100%;
            border-left: 4px solid var(--primary);
            min-height: 214px;
        }

        .cookie-info-card.advanced {
            border-left-color: var(--accent);
        }

        .login-info-card h3,
        .admin-info-card h3,
        .cookie-info-card h3 {
            color: var(--text);
            font-size: 1.15rem;
            margin: 0 0 1rem;
        }

        .login-info-card li,
        .admin-info-card li,
        .cookie-info-card li {
            color: var(--muted);
            margin-bottom: 0.5rem;
        }

        .user-info,
        .admin-info,
        .cookie-info {
            background: rgba(47, 128, 237, 0.12);
            border: 1px solid rgba(47, 128, 237, 0.26);
            border-left: 4px solid var(--primary);
            border-radius: var(--radius);
            color: var(--text);
            padding: 0.85rem 1rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }

        .admin-info {
            background: rgba(242, 169, 0, 0.12);
            border-color: rgba(242, 169, 0, 0.28);
            border-left-color: var(--warning);
        }

        .cookie-getter-header,
        .share-booster-header,
        .follower-growth-header,
        .admin-dashboard-header,
        .admin-tool-header {
            margin: 0.75rem 0 1.25rem;
        }

        .cookie-getter-header p,
        .share-booster-header p,
        .follower-growth-header p,
        .admin-dashboard-header p,
        .admin-tool-header p,
        .method-description p,
        .login-container p {
            color: var(--muted);
            margin-bottom: 0;
        }

        .method-description {
            padding: 1.25rem;
            margin-bottom: 1.25rem;
            border-left: 4px solid var(--primary);
        }

        .method-description h3 {
            color: var(--text);
            margin: 0 0 0.5rem;
            font-size: 1.2rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
            border-bottom: 1px solid var(--border);
        }

        .stTabs [data-baseweb="tab"] {
            height: 44px;
            padding: 0 0.9rem;
            color: var(--muted);
            border-radius: var(--radius) var(--radius) 0 0;
        }

        .stTabs [aria-selected="true"] {
            background: var(--surface-raised);
            color: var(--text);
            border-bottom: 3px solid var(--primary);
        }

        .stTextInput input,
        .stTextArea textarea,
        .stNumberInput input,
        [data-baseweb="select"] > div {
            background: var(--surface-raised) !important;
            color: var(--text) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius) !important;
            box-shadow: none !important;
        }

        .stTextArea textarea {
            min-height: 112px;
            font-family: "Cascadia Mono", Consolas, monospace;
            font-size: 0.92rem;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus,
        .stNumberInput input:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(47, 128, 237, 0.18) !important;
        }

        .stButton > button {
            min-height: 42px;
            border-radius: var(--radius);
            border: 1px solid rgba(47, 128, 237, 0.72);
            background: var(--primary);
            color: white;
            font-weight: 700;
            box-shadow: 0 10px 24px rgba(47, 128, 237, 0.22);
            transition: background 0.16s ease, border-color 0.16s ease, transform 0.16s ease;
        }

        .stFormSubmitButton > button {
            min-height: 44px;
            background: var(--primary);
            border: 1px solid rgba(47, 128, 237, 0.72);
            color: #fff;
            font-weight: 800;
            border-radius: var(--radius);
            box-shadow: 0 10px 24px rgba(47, 128, 237, 0.22);
        }

        .stFormSubmitButton > button:hover {
            background: var(--primary-hover);
            color: #fff;
        }

        .stButton > button:hover {
            background: var(--primary-hover);
            border-color: var(--primary-hover);
            color: white;
            transform: translateY(-1px);
        }

        .stButton > button:active {
            transform: translateY(0);
        }

        div[data-testid="stAlert"] {
            border-radius: var(--radius);
            border: 1px solid var(--border);
        }

        .share-progress,
        .share-error,
        .share-complete {
            border-radius: var(--radius);
            padding: 0.9rem 1rem;
            margin: 0.75rem 0;
            font-weight: 650;
        }

        .share-progress,
        .share-complete {
            color: #dcfce7;
            background: rgba(24, 160, 88, 0.13);
            border-left: 4px solid var(--accent);
        }

        .share-error {
            color: #fee2e2;
            background: rgba(239, 68, 68, 0.13);
            border-left: 4px solid var(--danger);
        }

        .user-table-container {
            overflow-x: auto;
            margin-bottom: 1.5rem;
            border: 1px solid var(--border);
            border-radius: var(--radius);
        }

        .user-table {
            width: 100%;
            border-collapse: collapse;
            background: var(--surface);
        }

        .user-table thead {
            background: var(--surface-raised);
        }

        .user-table th,
        .user-table td {
            padding: 0.85rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }

        .user-table tr:last-child td {
            border-bottom: none;
        }

        [data-testid="stMetric"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1rem;
        }

        .footer {
            margin-top: 2rem;
            padding: 1rem 0 0;
            border-top: 1px solid var(--border);
            text-align: center;
            color: var(--muted);
            font-size: 0.9rem;
        }

        .footer p {
            color: var(--muted);
        }

        @media (max-width: 768px) {
            .block-container {
                padding: 1rem;
            }

            .header-container {
                align-items: flex-start;
                padding: 1rem;
                min-height: auto;
            }

            .main-title {
                font-size: 1.45rem;
            }

            .section-title {
                font-size: 1.3rem;
            }

            .features-container {
                grid-template-columns: 1fr;
            }

            .auth-hero,
            .auth-hero + div,
            .auth-hero ~ div {
                max-width: 100%;
            }
        }
    </style>
    """, unsafe_allow_html=True)
