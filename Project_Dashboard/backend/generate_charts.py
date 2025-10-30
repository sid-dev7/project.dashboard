import pandas as pd
import plotly.express as px

projects = pd.read_csv('../data/sample_data.csv')
resources = pd.read_csv('../data/sample_resources.csv')

# Gantt Chart
fig_gantt = px.timeline(projects, x_start='Start', x_end='End', y='Project', color='Completion', title='Project Timelines')
fig_gantt.update_yaxes(autorange='reversed')
fig_gantt.write_html('../frontend/templates/gantt_chart.html', include_plotlyjs='cdn')

# Cost Chart
fig_cost = px.bar(projects, x='Project', y=['Used_Cost','Remaining_Cost'], title='Project Cost Overview', labels={'value':'Cost','variable':'Cost Type'})
fig_cost.write_html('../frontend/templates/cost_chart.html', include_plotlyjs='cdn')

# Resource Utilization
fig_resource = px.pie(resources, names='Resource', values='Hours_Worked', title='Resource Utilization')
fig_resource.write_html('../frontend/templates/resource_chart.html', include_plotlyjs='cdn')
