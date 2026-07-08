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
    "insurance",
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


    state_path=os.path.join(
        path,
        state
    )


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
                os.path.join(year_path,file),
                "r"
            ) as f:

                data=json.load(f)



            for item in data["data"]["districts"]:


                records.append({

                    "state":state,

                    "year":int(year),

                    "quarter":int(
                        file.replace(".json","")
                    ),

                    "district":
                    item["entityName"],

                    "count":
                    item["metric"]["count"],

                    "amount":
                    item["metric"]["amount"]

                })



df=pd.DataFrame(records)


df.to_csv(
os.path.join(
BASE_DIR,
"data",
"top_insurance.csv"
),
index=False
)


print("TOP INSURANCE DONE ✅")
print(df.shape)
print(df.head())