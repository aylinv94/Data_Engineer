from fastapi import FastAPI
import pandas as pd

app = FastAPI(title= 'ETL con docker y FastApi',
            description= 'Extract, Transform, Load of the platforms Amazon, Disney, Hulu y Netflix', 
            version= '1.0.1')

@app.get('/')
async def init():
    return {'Hello:World'}

@app.on_event('startup')
def startup():
    global df_integral
    df_integral= pd.read_csv('./Datasets/df_integral.csv', encoding='utf-8')

@app.get('/get_keyword_count')
async def get_keyword_count (platforma:str, keyword:str):
    platform = platforma[0].lower()
    keyword = keyword.lower()
    df = df_integral[ df_integral['id'].str.contains(platform)]
    mask= df['title'].str.contains(keyword)
    counter = len(df[mask])
    return {'Plataforma': platforma,'Cantidad': counter}

@app.get('/get_score_count')
async def get_score_count(platforma:str, score:int, year:int):
    platform = platforma[0].lower()
    df_id = df_integral[ df_integral['id'].str.contains(platform)]
    df_movie = df_id[df_id['type']== 'movie']
    df = df_movie[df_movie['release_year'] == year]
    mask = df['score'] > score
    counter = len(df[mask])
    
    return {'Plataforma': platforma,'Cantidad': counter}

@app.get('/get_second_score')
async def get_second_score(platforma:str):
    platform = platforma[0].lower()
    df_id = df_integral[ df_integral['id'].str.contains(platform)]
    mask = df_id.sort_values(['score','title'],ascending=[False,True])
    title = mask['title'].iloc[1]
    score = mask['score'].iloc[1]
    return {'Titulo':title, 'Puntuacion':int(score)}

@app.get('/get_longest')
async def get_longest(platforma:str, duration_type:str, year:int):
    platform = platforma[0].lower()
    duration_type = duration_type.lower()
    df_id = df_integral[ df_integral['id'].str.contains(platform)]
    df = df_id[df_id['release_year'] == year]
    df_type = df[df['duration_type']== duration_type].sort_values('duration_int',ascending=False)
    title = df_type['title'].iloc[0]
    duration = df_type['duration_int'].iloc[0]
    return {'Titulo':title, 'Duracion':int(duration),'Tipo de Duracion':duration_type}

@app.get('/get_rating_count')
async def get_rating_count(rating:str):
    rating= rating.lower()
    df = df_integral[df_integral['rating'] == rating]
    return {'Clasificacion':rating, 'Cantidad':len(df)}