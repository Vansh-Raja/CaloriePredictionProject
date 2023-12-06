import plotly
import plotly.graph_objs as go
import plotly.offline as opy
import sqlite3
import plotly.express as px
import json


def fetch_data(userid):
    conn = sqlite3.connect('Calorie.db')
    cursor = conn.cursor()


    # Example query: Retrieve total quantity sold for each product
    query = "SELECT exercise_name, duration, date, calories, bpm FROM exercise WHERE userid = ?"
    cursor.execute(query, (userid,))
    data = cursor.fetchall()

    uquery = "SELECT exercise_name, duration, date, calories, bpm FROM exercise WHERE userid = ?"
    cursor.execute(query, (userid,))
    data_with_bpm = cursor.fetchall()


    # Example query: Retrieve total quantity sold over time
    time_query = "SELECT date, calories FROM exercise WHERE userid = ?"
    cursor.execute(time_query, (userid,))
    time_data = cursor.fetchall()

    calories_query = "SELECT exercise_name, calories FROM exercise WHERE userid = ?"
    cursor.execute(calories_query, (userid,))
    calories_data = cursor.fetchall()

    heart_query = "SELECT bpm, calories FROM exercise WHERE userid = ?"
    cursor.execute(heart_query, (userid,))
    heart_data = cursor.fetchall()

    import pandas as pd
    df = pd.read_csv("calorie_prediction_db")
    correlation_matrix = df.corr()

    cursor.close()
    conn.close()

    return data, time_data, calories_data, heart_data, correlation_matrix, data_with_bpm


"""
def create_bar_chart(data):
    exercise, duration = zip(*data)

    trace = go.Bar(x=exercise, y=duration)
    layout = go.Layout(title='Exercise vs duration', xaxis=dict(title='Exercise'), yaxis=dict(title='Duration'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def create_line_chart(time_data):
    date, calories = zip(*time_data)

    trace = go.Scatter(x=date, y=calories, mode='lines+markers', marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Total Calories Over Time', xaxis=dict(title='Date'), yaxis=dict(title='Total Calories'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def create_pie_chart(data, title):
    exercise_names, calories = zip(*data)

    trace = go.Pie(labels=exercise_names, values=calories)
    layout = go.Layout(title=title)
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def create_heart_rate_scatter_plot(data):
    bpm, calories = zip(*data)

    trace = go.Scatter(x=bpm, y=calories, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Heart Rate vs. Calories Burned', xaxis=dict(title='Heart Rate (BPM)'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
"""


def create_bar_chart(data):
    exercise, duration, date, calories, bpm = zip(*data)

    trace = go.Bar(x=exercise, y=duration)
    layout = go.Layout(title='Exercise vs duration', xaxis=dict(
        title='Exercise'), yaxis=dict(title='Duration'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')




def create_line_chart(time_data):
    date, calories = zip(*time_data)

    trace = go.Scatter(x=date, y=calories, mode='lines+markers',
                       marker=dict(size=10), line=dict(width=2))
    layout = go.Layout(title='Total Calories Over Time', xaxis=dict(
        title='Date'), yaxis=dict(title='Total Calories'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def create_pie_chart(data, title):
    exercise_names, calories = zip(*data)

    trace = go.Pie(labels=exercise_names, values=calories)
    layout = go.Layout(title=title)
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')


def create_heart_rate_scatter_plot(data):
    bpm, calories = zip(*data)

    trace = go.Scatter(x=bpm, y=calories, mode='markers', marker=dict(size=12))
    layout = go.Layout(title='Heart Rate vs. Calories Burned', xaxis=dict(
        title='Heart Rate (BPM)'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')



def create_heatmap(correlation_matrix):
    # Customize the color scale (you can choose any color scale from Plotly)
    color_scale = 'Mint'

    fig = px.imshow(correlation_matrix, labels=dict(color="Correlation"), 
                    x=correlation_matrix.columns, y=correlation_matrix.columns,
                    color_continuous_scale=color_scale)

    fig.update_layout(title="Variable Correlation Heatmap")
    return opy.plot(fig, auto_open=False, output_type='div')

def create_exercise_vs_calories_chart(data):
    # Assuming data is a list of tuples where each tuple contains exercise_name and calories
    exercise, duration, date, calories, bpm = zip(*data)

    trace = go.Bar(x=exercise, y=calories)
    layout = go.Layout(title='Exercise vs Calories Burned', xaxis=dict(title='Exercise'), yaxis=dict(title='Calories Burned'))
    fig = go.Figure(data=[trace], layout=layout)

    return opy.plot(fig, auto_open=False, output_type='div')

def create_violin_plot(data):
    exercise, duration, date, calories, bpm= zip(*data)

    fig = px.violin(y=duration, x=bpm, box=True, points="all", 
                    labels={'y': 'Exercise Duration', 'x': 'Heart Rate (BPM)'})

    fig.update_layout(title='Exercise Duration vs. Heart Rate')
    return opy.plot(fig, auto_open=False, output_type='div')