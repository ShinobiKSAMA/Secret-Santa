from pandas import read_excel, DataFrame

class WorkbookHelper:
    @staticmethod
    def readExcel(file_path: str, sheet_name: str | int = 0) -> DataFrame | None:
        """
        Reads data from an Excel file and returns it as a DataFrame.

        Parameters:
        - file_path (str): The path to the Excel file.
        - sheet_name (str | int, optional): The name or index of the sheet to read. Defaults to 0.

        Returns:
        - DataFrame | None: A DataFrame containing the data if successful, None otherwise.
        """
        
        try:
            df: DataFrame = read_excel(file_path, sheet_name=sheet_name)
            return df
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

    @staticmethod
    def writeExcel(df: DataFrame, file_path: str, sheet_name: str = "Sheet1", index: bool = False) -> None:
        """
        Writes a DataFrame to an Excel file.

        Parameters:
        - df (DataFrame): The DataFrame to write to the Excel file.
        - file_path (str): The path to the Excel file to be created.
        - sheet_name (str, optional): The name of the sheet in the Excel file. Defaults to "Sheet1".
        - index (bool, optional): Whether to include row names (index) in the output. Defaults to False.

        Returns:
        - None
        """

        try:
            df.to_excel(file_path, sheet_name=sheet_name, index=index)
            print(f"Excel file '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating Excel file: {e}")