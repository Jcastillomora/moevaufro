from django.shortcuts import render
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django.db.models import Sum
from .models import Altmetrics, RespuestasForm
import plotly.express as px
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import plot_likert
import numpy as np
from collections import Counter



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

        
# def respuestas_forms(request):
#     respuestas = RespuestasForm.objects.all()

#     # Diccionario para mapear los números a etiquetas deseadas
#     etiquetas_respuesta = {
#         1: 'Totalmente en desacuerdo',
#         2: 'En desacuerdo',
#         3: 'Neutro',
#         4: 'De acuerdo',
#         5: 'Totalmente de acuerdo'
#     }

#     conteo_respuestas = {columna: Counter() for columna in range(1, 16)}

#     for respuesta in respuestas:
#         for columna in range(1, 16):
#             conteo_respuestas[columna][getattr(respuesta, f'r{columna}')] += 1

#     figs = []  # Lista para almacenar los gráficos individuales

#     for columna, conteo in conteo_respuestas.items():
#         etiquetas_x = [etiquetas_respuesta[numero] for numero in conteo.keys()]
#         fig = go.Figure()
#         fig.add_trace(go.Bar(
#             x=etiquetas_x,
#             y=list(conteo.values()),
#             name=f'Pregunta {columna}',
#             orientation='v',
#             marker_line=dict(width=1, color="#333"),
#             marker_color='#33cc99'
#         ))
#         fig.update_layout(
#             title=f"Pregunta {columna}",
#             xaxis_title="Respuesta",
#             yaxis_title="Cantidad",
#             barmode="group",
#             template='plotly_dark',
#             font_family='Roboto, sans-serif'
#         )
#         figs.append(fig.to_html(full_html=False))

#     context = {
#         'figs': figs  # Pasar los gráficos individuales al contexto
#     }

#     return render(request, 'respuestas_forms.html', context)


# funcion para filtrar por la columna 'facultad' los valores totales por factultad del modelo RespuestasForm

def respuestas_facultad(request):
    r_medicina  = RespuestasForm.objects.filter(facultad='Medicina')
    r_ingenieria = RespuestasForm.objects.filter(facultad='Ingeniería y Ciencias')
    r_humanidades = RespuestasForm.objects.filter(facultad='Educación, Ciencias Sociales y Hdes.')
    r_odonto = RespuestasForm.objects.filter(facultad='Odontología')
    r_juridicas = RespuestasForm.objects.filter(facultad='Ciencias Jurídicas y Empresariales')
    r_nucleo = RespuestasForm.objects.filter(facultad='Núcleo')

def respuestas_forms(request):
    respuestas = RespuestasForm.objects.all()

    # Diccionario para mapear los números a etiquetas deseadas
    etiquetas_respuesta = {
        1: 'Totalmente en desacuerdo',
        2: 'En desacuerdo',
        3: 'Neutro',
        4: 'De acuerdo',
        5: 'Totalmente de acuerdo'
    }

    # Lista de títulos personalizados para cada gráfico
    titulos = [
        '"Utilizo software libre y de código abierto en mis proyectos de investigación"',
        '"Participo activamente en comunidades de desarrollo de software abierto"',
        '"Mi universidad ha desarrollado y compartido varios proyectos de software libre y de código abierto"',
        '"Considero que los procesos de revisión por pares en mi universidad son transparentes y accesibles"',
        '"La mayoría de mis trabajos son revisados en plataformas de revisión abiertas y accesibles"',
        '"Participo regularmente como revisor en procesos de evaluación abierta"',
        '"Utilizo métricas alternativas para complementar la evaluación tradicional de mi investigación"',
        '"Las métricas alternativas son consideradas en los informes institucionales de mi universidad"',
        '"Las métricas alternativas tienen una influencia significativa en decisiones de financiamiento y reconocimientos académicos en mi universidad"',
        '"Publico mis investigaciones en abierto y las deposito en algún Repositorio"',
        '"Genero y comparto conjuntos de datos abiertos como parte de mi labor investigativa"',
        '"En la mayoría de mis proyectos de investigación, hago públicos mis datos para que puedan ser accesibles para otros investigadores"',
        '"Utilizo y reutilizo conjuntos de datos abiertos de otros investigadores en mi trabajo académico"',
        '"Comparto recursos educativos de manera abierta para contribuir al acceso gratuito a la educación"',
        '"Utilizo, comparto y descargo regularmente recursos educativos abiertos en mi labor académica"'
    ]

    conteo_respuestas = {columna: Counter() for columna in range(1, 16)}

    for respuesta in respuestas:
        for columna in range(1, 16):
            conteo_respuestas[columna][getattr(respuesta, f'r{columna}')] += 1

    figs = []  # Lista para almacenar los gráficos individuales

    for columna, conteo in conteo_respuestas.items():
        etiquetas_x = [etiquetas_respuesta[numero] for numero in conteo.keys()]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=etiquetas_x,
            y=list(conteo.values()),
            name=f'Pregunta {columna}',
            orientation='v',
            marker_line=dict(width=1, color="#333"),
            marker_color='#33cc99'
        ))
        fig.update_layout(
            title=f'Ítem {columna}',  # Usar el título correspondiente de la lista
            xaxis_title="Respuesta",
            yaxis_title="Cantidad",
            barmode="group",
            template='plotly_dark',
            font_family='Roboto, sans-serif'
        )
        figs.append({
            'columna': columna,  # Agregar el número de la columna para identificarla en el template
            'title': titulos[columna - 1],
            'fig': fig.to_html(full_html=False)
        })

    context = {
        'figs': figs  # Pasar los gráficos individuales al contexto con sus títulos
    }

    return render(request, 'respuestas_forms.html', context)


