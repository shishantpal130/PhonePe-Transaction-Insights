import os
import json
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


path = os.path.join(
    BASE_DIR,
    "pulse",
    "data",
    "aggregated",
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


            file_path=os.path.join(
                year_path,
                file
            )


            with open(file_path,"r") as f:

                data=json.load(f)


            for item in data["data"]["transactionData"]:

                records.append({

                    "state":state,

                    "year":int(year),

                    "quarter":int(
                        file.replace(".json","")
                    ),

                    "insurance_type":
                    item["name"],

                    "transaction_count":
                    item["paymentInstruments"][0]["count"],

                    "transaction_amount":
                    item["paymentInstruments"][0]["amount"]

                })


df=pd.DataFrame(records)


output=os.path.join(
    BASE_DIR,
    "data",
    "insurance.csv"
)


df.to_csv(
    output,
    index=False
)


print("INSURANCE EXTRACTION DONE ✅")
print("Rows:",df.shape[0])
print(df.head())