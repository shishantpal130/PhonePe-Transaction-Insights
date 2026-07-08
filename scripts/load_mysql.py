import mysql.connector
import pandas as pd
import os


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="phonepe"
)


cursor = conn.cursor()


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


tables = {

"transaction.csv":"aggregated_transaction",

"user.csv":"aggregated_user",

"insurance.csv":"aggregated_insurance",

"map_transaction.csv":"map_transaction",

"map_user.csv":"map_user",

"map_insurance.csv":"map_insurance",

"top_transaction.csv":"top_transaction",

"top_user.csv":"top_user",

"top_insurance.csv":"top_insurance"

}



for file, table in tables.items():

    print("Loading:", file)


    path=os.path.join(
        BASE_DIR,
        "data",
        file
    )


    df=pd.read_csv(path)


    df=df.where(
        pd.notnull(df),
        None
    )


    columns=",".join(df.columns)


    placeholders=",".join(
        ["%s"]*len(df.columns)
    )


    query=f"""

    INSERT INTO {table}
    ({columns})

    VALUES
    ({placeholders})

    """


    cursor.executemany(
        query,
        df.values.tolist()
    )


    conn.commit()


    print(
        table,
        "completed"
    )


print("ALL DATA LOADED ✅")


cursor.close()
conn.close()