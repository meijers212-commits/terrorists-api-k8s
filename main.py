from fastapi import FastAPI, File, UploadFile
import pandas as pd

 
app = FastAPI()


@app.post("/top-threat")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    return {"filename": file.filename}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)