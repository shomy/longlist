#使い方
# サーバー起動　uvicorn main:app --reload

from unittest import result
from fastapi import FastAPI
import pandas as pd
import ast

df=pd.read_csv("./vector_make_df.csv")
# df['recommend'] = [ast.literal_eval(d) for d in df['recommend']]


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    taisyo_df=df[df["提出者名"]==q]
    corp=taisyo_df["recommend"].values[0]
    corp_list=corp.strip("[]").split(" ")

    output_corp=[]
    
    for i in corp_list:
        try:
            num=int(i)
            output_corp.append(num)
        except:
            pass
    print(type(output_corp))
        
    info_list=[]
    sales_list=[]
    profitrate_list=[]
    for id_num in output_corp:
        print(id_num)
        recommend_df=df[df.index==id_num]
        i1=recommend_df["提出者名"].values[0]
        s1=int(recommend_df["売上高5"].values[0])
        p1=float(recommend_df["経常利益率5"].values[0])
        info_list.append(i1)
        sales_list.append(s1)
        profitrate_list.append(p1)


    result = {
        "item_id": item_id,
         "q": q, 
         "企業1":{
         "企業名1":info_list[0],
         "売上高1":sales_list[0],
         "利益率1":profitrate_list[0]
         },

        "企業2":{
         "企業名2":info_list[1],
         "売上高2":sales_list[1],
         "利益率2":profitrate_list[1]
         },
        "企業3":{
         "企業名3":info_list[2],
         "売上高3":sales_list[2],
         "利益率3":profitrate_list[2]
         },
        "企業4":{
         "企業名4":info_list[3],
         "売上高4":sales_list[3],
         "利益率4":profitrate_list[3]
         }
         ,
        "企業5":{
         "企業名5":info_list[4],
         "売上高5":sales_list[4],
         "利益率5":profitrate_list[4]
         }

    }
    return result

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
 
#     taisyo_df=df[df["提出者名"]==q]

#     corp=taisyo_df["recommend"].values[0]

#     rec_corp=[]
#     for i in corp:
#         rec_df=df[df.index==i]
#         rec_corp.append(rec_df["提出者名"].values[0])

#     return {"item_id": item_id, "q": q, "企業名":rec_corp}
