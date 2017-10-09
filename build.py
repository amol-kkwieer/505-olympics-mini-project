import pandas as pd

# Create a function load_data to read CSV file and convert CSV data to dataframe.
# Skip first row
def load_data():
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

    # Rename column containing 01, 02 and 03 to Gold, Silver and Bronze
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
        if col[:2] == '02':
            df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
        if col[:2] == '03':
            df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
        if col[:1] == '№':
            df.rename(columns={col: '#' + col[1:]}, inplace=True)

    # Split country name and country code and add country name as data frame index
    names_ids = df.index.str.split('\s\(')  # split the index by '('

    df.index = names_ids.str[0]  # the [0] element is the country name (new index)
    # Remove extra unnecessary characters from country name.
    df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)
    # Drop the column Totals
    df = df.drop('Totals')
    # Return dataframe.
    return df

# Create a function first_country.
def first_country(df):
    return df.iloc[0]
    # Return results for first country.




# Create a function gold_medal to get name of country who won most gold medals.
def gold_medal(df):
    return df['Gold'].argmax()


# Create a function biggest_difference_in_gold_medal to get name of country
# who has biggest difference between their summer and winter gold medal counts?
def biggest_difference_in_gold_medal(df):
    return (df['Gold'] - df['Gold.1']).argmax()

# Write a function to update the dataframe to include a new column called "Points" for Games
# which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points,
#  and bronze medals for 1 point. The function should return only the column (a Series object)
#  which you created.
def get_points(df):
    df['Points'] = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2']
    return df['Points']

# def k_means():

df = load_data()
print(first_country(df)["# Summer"])
print(gold_medal(df))
print(biggest_difference_in_gold_medal(df))
print(get_points(df))
