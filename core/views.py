from django.shortcuts import render
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django.db.models import Sum
from .models import Altmetrics
import plotly.express as px


def show_totals(request):
    # Filter data by year
    altmetrics_2022 = Altmetrics.objects.filter(year=2022)
    altmetrics_2023 = Altmetrics.objects.filter(year=2023)

    # Calculate totals with dictionary comprehension (more concise)
    totals_2022 = {field: sum(getattr(obj, field) for obj in altmetrics_2022)
                   for field in ['mendeley_readers','facebook', 'x', 'blogs',
                                'news', 'reddit', 'stackoverflow', 'policies',
                                'patents', 'youtube', 'wikipedia', 'total']}
    totals_2023 = {field: sum(getattr(obj, field) for obj in altmetrics_2023)
                   for field in totals_2022.keys()}  # Reuse field names

    # Create bar chart data (using a loop for clarity)
    years = ['2022', '2023']
    # metric_names = list(totals_2022.keys())  # Extract metric names
    # metric_values_2022 = list(totals_2022.values())
    # metric_values_2023 = list(totals_2023.values())

    # Exclude 'mendeley_readers' from both names and values
    exclude_key = 'mendeley_readers'

    metric_names = [key for key in totals_2022.keys() if key != exclude_key]
    metric_values_2022 = [value for value in totals_2022.values() if value != totals_2022[exclude_key]]

    metric_values_2023 = [value for value in totals_2023.values() if value != totals_2023[exclude_key]]


    # Create traces for each metric
    traces = []
    for i, metric_name in enumerate(metric_names):
        trace = go.Bar(
            x=years,
            y=[metric_values_2022[i], metric_values_2023[i]],
            name=metric_name,
            marker=dict(color=['#0b2ca4','#2f90b9','#e89500','#b60000','#b9ddeb','#dfdfdf','#5b17e8','orange','#98c973','#3b2a3d','green'][i])
        )
        traces.append(trace)

    # Create layout
    layout = go.Layout(
        title=dict(text='Menciones Altmetrics 2022-2023', x=0.5),
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title='Año',
        yaxis= dict(title='Menciones totales', showticklabels=True),
        barmode='group',
        bargap=0.4,
        autosize=True,
        bargroupgap=0.1,
        template='plotly_dark',
        font_size=11
        
    )

    # Create figure
    fig = go.Figure(data=traces, layout=layout)

    # crear grafico solo de mendeley_readers 2022 vs 2023
    fig_mendeley = go.Figure(data=[
        go.Bar(name='2022', x=['2022'], y=[totals_2022['mendeley_readers']], marker_color='#33cc99'),
        go.Bar(name='2023', x=['2023'], y=[totals_2023['mendeley_readers']], marker_color='#ff6666')
    ])

    # Change the bar mode
    fig_mendeley.update_layout(
        barmode='group', 
        title=dict(text='Citaciones en <br>Mendeley 2022-2023', x=0.5),
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title='Año',
        yaxis=dict(title='Citaciones totales', showticklabels=True),
        autosize=True,
        hovermode='x',
        template='plotly_dark',
        bargroupgap=0.2,
        font_size=11
   
    )

    fig_x =go.Figure(data=[
        go.Bar(name='2022', x=['2022'], y=[totals_2022['x']], marker_color='#33cc99'),
        go.Bar(name='2023', x=['2023'], y=[totals_2023['x']], marker_color='#ff6666')
    ])

    # Change the bar mode
    fig_x.update_layout(
        barmode='group', 
        title=dict(text='Menciones en <br>X 2022-2023', x=0.5),
        margin=dict(l=20, r=20, t=60, b=20),
        xaxis_title='Año',
        yaxis=dict(title='Menciones totales', showticklabels=True),
        autosize=True,
        hovermode='x',
        template='plotly_dark',
        bargroupgap=0.2,
        font_size=11
    )

    fig_mendeley = fig_mendeley.to_html(full_html=False)
    fig_x = fig_x.to_html(full_html=False)

    # Render the chart as HTML for inclusion in the template
    chart_div = fig.to_html(full_html=False)  # Avoid extra headers

    context = {
        'totals_2022': totals_2022,
        'totals_2023': totals_2023,
        'chart_div': chart_div,
        'fig_mendeley': fig_mendeley,
        'fig_x': fig_x,
    }

    return render(request, 'base.html', context)

def bibliometria(request):
    return render(request, 'bibliometria.html')





