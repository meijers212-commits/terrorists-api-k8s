import pandas as pd
from pydantic import BaseModel 


class top5terorist(BaseModel):
    name: str
    location: str
    danger_rate: float

# sorted_df = df.sort_values(by=['Age', 'Score'])

class CsvManagement():

    @staticmethod
    def sort_by_danger_rate_top_5(df: pd.DataFrame) -> pd.DataFrame:
        try:
            return df.sort_values(
                by="danger_rate",
                ascending=False
            ).head(5)
        except Exception as e:
            raise RuntimeError("Error parsing df") from e



    @staticmethod
    def Column_filtering(df: pd.DataFrame) -> dict:
        try:
            top_5_sorte = [{ 
                "name": row["name"], 
                "location": row["location"], 
                "danger_rate": row["danger_rate"] 
                }
                for row in df.to_dict()
                ]

            dict = {
                "count": len(df),
                "top": top_5_sorte
            }

            return dict
        except Exception as e:
            raise RuntimeError("Error creating dict from df") 

