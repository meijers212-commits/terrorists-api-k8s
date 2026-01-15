from fastapi import FastAPI, File, UploadFile ,HTTPException
import pandas as pd
from models import CsvManagement
from db import DbCommunication

app = FastAPI()



@app.post("/top-threat")
def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")
    try:
        df = pd.read_csv(file.file)
        sorted_df = CsvManagement.sort_by_danger_rate_top_5(df)
        df_dict = CsvManagement.Column_filtering(sorted_df)
        top_5_list = []
        top_5_list = df_dict["top"]
        if not top_5_list:
            raise HTTPException(status_code=400, detail="No valid data found to insert")
        DbCommunication.insert_to_db(top_5_list, "top_threats")
        # top_5_list.pop("_id")
        return {"message": "The data was entered successfully.", "data": top_5_list}
    except HTTPException:
        raise 
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)