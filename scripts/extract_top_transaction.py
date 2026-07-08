import os
import json
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


path=os.path.join(
    BASE_DIR,
    "pulse",
    "data",
    "top",
    "transaction",
    "country",
    "india",
    "state"
)


print("Reading from:")
print(path)


records=[]


for state in os.listdir(path):

    if state.startswith("."):
        continue


    state_path=os.path.join(path,state)


    if not os.path.isdir(state_path):
        continue


    for year in os.listdir(state_path):

        if year.startswith("."):
            continue


        year_path=os.path.join(
            state_path,
            year
        )


        if not os.path.isdir(year_path):
            continue


        for file in os.listdir(year_path):

            if not file.endswith(".json"):
                continue


            with open(
                os.path.join(year_path,file)
            ) as f:

                data=json.load(f)


            districts=data["data"]["districts"]

            pincodes=data["data"]["pincodes"]


            for d in districts:

                records.append({

                "state":state,

                "year":int(year),

                "quarter":int(
                    file.replace(".json","")
                ),

                "level":"district",

                "name":d["entityName"],

                "count":
                d["metric"]["count"],

                "amount":
                d["metric"]["amount"]

                })


            for p in pincodes:

                records.append({

                "state":state,

                "year":int(year),

                "quarter":int(
                    file.replace(".json","")
                ),

                "level":"pincode",

                "name":
                p["entityName"],

                "count":
                p["metric"]["count"],

                "amount":
                p["metric"]["amount"]

                })



df=pd.DataFrame(records)


df.to_csv(
os.path.join(
BASE_DIR,
"data",
"top_transaction.csv"
),
index=False
)


print("TOP TRANSACTION DONE ✅")
print(df.shape)
print(df.head())