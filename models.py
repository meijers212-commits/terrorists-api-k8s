import pandas as pd
from pydantic import BaseModel , 


class top5terorist(BaseModel):
    name: pd.DataFrame
    location: pd.DataFrame
    danger_rate: pd.DataFrame



# sorted_df = df.sort_values(by=['Age', 'Score'])

class CsvManagement():
    
    @staticmethod
    def sort_by_danger_rate_top_5(df: pd.DataFrame)-> pd.DataFrame:
        try:
            sorted_df = df.sort_values(['danger_rate'],ascending=False).groupby('danger_rate').head(5)
            return sorted_df
        except Exception as e:
            raise {"Error parsing df":e}


    @staticmethod
    def Column_filtering(df: pd.DataFrame)-> pd.DataFrame:
        try:
            top_5_sorted = [
                top5terorist(**row)
                for row in df.to_dict(orient="records")
                            ]

            dict = {
                "count":df.count(),
                    "top":top_5_sorted
                    }
        except Exception as e:
            raise {"Error creating dict from df":e}
    









