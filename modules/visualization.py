import plotly.express as px

def plot_time_spent(df):
    fig = px.line(
        df,
        x="date",
        y="time_spent_min",
        title="Daily Time Investment in Learning",
        markers=True
    )
    return fig

def plot_domain_distribution(df):
    fig = px.pie(
        df,
        names="domain",
        title="Learning Domain Distribution"
    )
    return fig

