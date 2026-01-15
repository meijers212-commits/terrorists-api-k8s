from fastapi import FastAPI, File, UploadFile
import pandas as pd
from models import CsvManagement
 
app = FastAPI()


@app.post("/top-threat")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    sorted_df = CsvManagement.sort_by_danger_rate_top_5(df)
    df_dict = CsvManagement.Column_filtering(sorted_df)
    return df_dict



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)