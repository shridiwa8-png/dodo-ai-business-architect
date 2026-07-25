import streamlit as st



# =========================
# OPTIONS
# =========================


ROLES = [

    "Owner",
    "Freelancer",
    "Consultant",
    "Ecommerce Seller",
    "Service Business Owner",
    "Startup Founder",
    "Small Business Owner",
    "Other"

]


TECH_LEVELS = [

    "Beginner",
    "Intermediate",
    "Advanced"

]


BUSINESS_TYPES = [

    "Web Design Agency",
    "Software Company",
    "Marketing Agency",
    "Consulting Business",
    "Ecommerce",
    "Local Service Business",
    "SaaS",
    "Other"

]


TEAM_SIZES = [

    "Solo",
    "2-5 employees",
    "6-20 employees",
    "20+ employees"

]


BUSINESS_STAGE = [

    "Starting",
    "Growing",
    "Established",
    "Scaling"

]


GOALS = [

    "Increase Sales",
    "Automate Operations",
    "Improve Team Productivity",
    "Reduce Manual Work",
    "Build SOPs",
    "Scale Business",
    "Improve Customer Support"

]


SALES_CHANNELS = [

    "WhatsApp",
    "Email",
    "Website",
    "Social Media",
    "Marketplace",
    "Cold Outreach",
    "Other"

]


BOTTLENECKS = [

    "Getting Customers",
    "Closing Sales",
    "Follow-ups",
    "Team Management",
    "Operations",
    "Automation",
    "Customer Support",
    "Documentation",
    "Cash Flow",
    "Not Sure"

]


TOOLS = [

    "WhatsApp",
    "Google Sheets",
    "Excel",
    "Notion",
    "Slack",
    "HubSpot",
    "Trello",
    "ClickUp",
    "Zapier",
    "Make.com",
    "ChatGPT",
    "Gemini"

]



# =========================
# HERO
# =========================


def hero():

    st.markdown(
        "# 🦤 DoDo"
    )

    st.markdown(
        """
### Turn messy business problems into executable systems.

DoDo analyzes your business,
finds bottlenecks,
and builds practical operating workflows.
"""
    )




# =========================
# USER PROFILE
# =========================


def user_profile():


    st.markdown(
        "## 👤 Business Profile"
    )


    profile = {}


    profile["role"] = st.selectbox(
        "Your Role",
        ROLES
    )


    profile["business_type"] = st.selectbox(
        "Business Type",
        BUSINESS_TYPES
    )


    profile["business_stage"] = st.selectbox(
        "Business Stage",
        BUSINESS_STAGE
    )


    profile["team_size"] = st.selectbox(
        "Team Size",
        TEAM_SIZES
    )


    profile["tech_level"] = st.selectbox(
        "Tech Confidence",
        TECH_LEVELS
    )


    profile["goals"] = st.multiselect(
        "Main Business Goals",
        GOALS
    )


    profile["biggest_bottleneck"] = st.selectbox(
        "Biggest Current Bottleneck",
        BOTTLENECKS
    )


    profile["sales_channels"] = st.multiselect(
        "Current Sales Channels",
        SALES_CHANNELS
    )


    profile["tools"] = st.multiselect(
        "Current Tools",
        TOOLS
    )


    return profile




# =========================
# BUSINESS INPUT
# =========================


def user_input_box():


    st.markdown(
        "## 💬 Describe Your Business Problem"
    )


    user_input = st.text_area(

        "Problem",

        height=300,


        placeholder="""

Example:


I own a web design agency.

My team has 5 people.

We get leads from WhatsApp.

After sending quotations,
customers stop replying.

I want a sales recovery system.


OR


My employees repeat the same tasks daily.

I want to automate operations.

"""

    )


    return user_input