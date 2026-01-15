import pandas as pd
from pydantic import BaseModel 


class top5terorist(BaseModel):
    name: str
    location: str
    danger_rate: int



class CsvManagement():

    @staticmethod
    def sort_by_danger_rate_top_5(df: pd.DataFrame):
        try:
            return df.sort_values(
                by="danger_rate",
                ascending=False
            ).head(5)
        except Exception as e:
            raise RuntimeError(f"Error parsing df:{e}") 



    @staticmethod
    def Column_filtering(df: pd.DataFrame):
        
        try:
            top_5_sorted = [
                top5terorist(
                    name=str(row["name"]),
                    location=str(row["location"]),
                    danger_rate=int(row["danger_rate"])
                    ).model_dump()
                for row in df.to_dict(orient="records")
            ]
    
            result_dict = {
                "count": len(df),
                "top": top_5_sorted
            }
            return result_dict
        except Exception as e:
            raise RuntimeError(f"Error creating dict from df:{e}") 
















    



