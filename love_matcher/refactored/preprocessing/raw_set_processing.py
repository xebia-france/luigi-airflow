class RawSetProcessing:
    """
    This class aims to load and clean the dataset.
    """

    def __init__(self, features):
        self.features = features

    # Select variables to process and include in the model
    @staticmethod
    def subset_features(features, df):
        sel_vars_df = df[features]
        return sel_vars_df

    @staticmethod
    # Remove ids with missing values
    def remove_ids_with_missing_values(df):
        sel_vars_filled_df = df.dropna()
        return sel_vars_filled_df

    @staticmethod
    def drop_duplicated_values(df):
        df = df.drop_duplicates()
        return df

    # Combine processing stages
    def combiner_pipeline(self, dataframe):
        raw_dataset = dataframe
        subset_df = self.subset_features(self.features,raw_dataset)
        subset_no_dup_df = self.drop_duplicated_values(subset_df)
        subset_filled_df = self.remove_ids_with_missing_values(subset_no_dup_df)
        return subset_filled_df
