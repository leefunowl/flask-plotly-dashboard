import plotly.graph_objs as go, pandas as pd
from sqlalchemy import create_engine, select
from dash.dependencies import Input
from dash.dependencies import Output

from app.config import TestingConfig as config

engine = create_engine(config.DB_URL)
sql = 'SELECT * FROM EVAL'
eval_df = pd.read_sql(sql, engine)

departments = ['Emergency Medicine', 'Family Medicine', 'Internal Medicine', 'Neurology']

question_dict = {
    1:'How would you rate your experience with this doctor? (1-4; 1 strongly disagree, 4 strongly agree)',
    2:'Average minute per visit',
    3:'Are you excited about your next visit? (1-4; 1 strongly disagree, 4 strongly agree)',
    4:'My symptom was alleviated because of this doctor (1-4; 1 strongly disagree, 4 strongly agree)'
}

def register_callbacks(dashapp):

    @dashapp.callback(
        [
            Output('graph', 'figure'),
        ],
        [
            Input('question_num_filter', 'value'),
        ]
    )
    def update_graph(question_num_filter):

        data_column = 'A' + str(question_num_filter)

        data = []

        for year in ['2018', '2019', '2020']:
            _y = []
            for department in departments:
                _mean = eval_df.loc[
                    (eval_df['CALENDAR_YEAR'] == year)&(eval_df['DEPARTMENT'] == department),
                    data_column
                ].mean()
                _y.append(_mean)
            data.append(
                go.Bar(name = year, x = departments, y = _y),
            )
            
        return [go.Figure(
            data = data,
            layout = go.Layout(title = question_dict[question_num_filter])
        )]