import pandas as pd

class ExcelUpdater:
    
    def __init__(self):
        self.input_file = "CSP_Extensions_Plan.xlsx"
        self.output_file = "CSP_Extensions_Plan_New2.xlsx"

    def updateExcel(self):
        #Put the Excel file into a DataFrame
        df = pd.read_excel(self.input_file)

        df['Active'] = df['Active'].replace({'Yes': 1})

        new_columns = ['Data-Load-Operation', 'Data-Load-Status']
        new_data_string = 'Create'

        for i, header in enumerate(new_columns):
            df.insert(i, header, new_data_string if i == 0 else None)

        df = df.drop(columns=['ID','Task Mode','Outline Level','Predecessors'])
        print(df)
    
        #Save the updated DataFrame to a new Excel file
        df.to_excel(self.output_file, index=False)
        #print(f"Updated data saved to {self.output_file}")

show = ExcelUpdater()
show.updateExcel()