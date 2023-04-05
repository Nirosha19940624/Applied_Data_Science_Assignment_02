
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# Function to read file
def filepath(filename):
    """
    Function : A function to read csv file and return list where in the csv file
    Parameter : Filename
    Returns :Returns All the list in csv file
    """

    df_file = pd.read_csv(filename)

    # create a dataframe years as columns
    df_years = df_file.drop(
        ['Indicator Name', 'Indicator Code', 'Country Code'], axis=1)
    print(df_years)

    # create a dataframe countries as columns
    df_countries = pd.DataFrame.transpose(df_years)
    print(df_countries)

    # cleane transpose dataframe
    df_countries = df_countries.dropna()

    # Create the header
    header = df_countries.iloc[0].values.tolist()
    df_countries.columns = header

    # remove the first two lines
    df_countries = df_countries.iloc[1:]

    # convert index to int
    df_countries.index = df_countries.index.astype(int)

    # sepatare forest area indicator
    df_forest = df_countries.iloc[:, 0:17]

    # Separate Population growth indicator
    df_population = df_countries.iloc[:, 17:34]

    # create a new column as average forest area of all countries
    df_forest["World Forest Area"] = df_forest.iloc[:, 2:19].mean(axis=1)

    # create a new column as average population of all countries
    df_population["World Population"] = df_population.iloc[:,
                                                           2:19].mean(axis=1)

    # create a dataframe to catogorized world population greater than 0.6%
    large_countries = df_population[(df_population["World Population"] > 0.6)]

    # create a dataframe to catogorized world population less than 0.6%
    small_countries = df_population[(df_population["World Population"] < 0.6)]

    # create a dataframe to catogorized world forest greater than 35.0%
    large_countries1 = df_forest[(df_forest["World Forest Area"] > 35.0)]

    # create a dataframe to catogorized world Forest area less than 35.0%
    small_countries1 = df_forest[(df_forest["World Forest Area"] < 35.0)]

    # make statical fuction to find count, mean, std, min,25%,50%,75% and max in made categoried countries using both indicators
    print(small_countries.describe())
    print(small_countries1.describe())

    # find another statistical properties of skiwness and kurtosis for both indicators
    print("Skew:", stats.skew(small_countries["World Population"]))
    print("Kurtosis:", stats.kurtosis(small_countries["World Population"]))

    print("Skew:", stats.skew(small_countries1["World Forest Area"]))
    print("Kurtosis:", stats.kurtosis(small_countries1["World Forest Area"]))

    # Kendall's correlation
    print(small_countries.corr(method="kendall"))
    print(small_countries1.corr(method="kendall"))

    plt.figure(figsize=(9, 6), facecolor="lightblue")

    # plot the line chart to find world population and world forest area using categorid countries
    plt.plot(small_countries["World Population"],
             label="World Population", linestyle="-", color='red')
    plt.plot(small_countries1["World Forest Area"],
             label="World Forest Area", linestyle="-", color='blue')

    # labeling
    plt.xlabel("Year", fontweight='bold')
    plt.ylabel("Percentage(%)", fontweight='bold')
    plt.title("Population Percerntage(%)",
              fontweight='bold')

    # Removing the white background left and right
    plt.xlim(2002, 2020)
    plt.legend()

    # save as a png
    plt.savefig("linplotcorr.png")
    plt.show()

    # plot the line chart
    plt.figure(figsize=(9, 6), facecolor="lightblue")

    # subplot count starts at 1
    plt.subplot(2, 2, 1)

    # plot the line chart to show avarage world forest percentage comparing single three countries
    plt.plot(df_countries.index, df_forest["World Forest Area"],
             label="World", linestyle="-", color='green')
    plt.plot(df_forest.index, df_forest["South Africa"],
             label="South Africa", linestyle="-", color='red')
    plt.plot(df_forest.index, df_forest["China"],
             label="China", linestyle="-", color='blue')
    plt.plot(df_forest.index, df_forest["Switzerland"],
             label="Switzerland", linestyle="-", color='orange')

    # set the current tick locations and labels of the x-axis
    plt.xticks([2002, 2007, 2012, 2017, 2020])

    # labeling
    plt.xlabel("Year", fontweight='bold')
    plt.ylabel("Percentage(%)", fontweight='bold')
    plt.title("Forest Percerntage(%) - World",
              fontweight='bold')

    # Removing the white background left and right
    plt.xlim(2002, 2020)
    plt.legend()

    # subplot count starts at 2
    plt.subplot(2, 2, 2)

    # plot the line chart to show avarage world population percentage comparing single three countries
    plt.plot(df_population.index, df_population["World Population"],
             label="World", linestyle="-", color='green')
    plt.plot(df_population.index, df_population["South Africa"],
             label="South Africa", linestyle="-", color='red')
    plt.plot(df_population.index, df_population["China"],
             label="China", linestyle="-", color='blue')
    plt.plot(df_population.index, df_population["Switzerland"],
             label="Switzerland", linestyle="-", color='orange')

    # set the current tick locations and labels of the x-axis
    plt.xticks([2002, 2007, 2012, 2017, 2020])

    # labeling
    plt.xlabel("Year", fontweight='bold')
    plt.ylabel("Percentage(%)", fontweight='bold')
    plt.title("Population Percerntage(%) - World",
              fontweight='bold')

    # Removing the white background left and right
    plt.xlim(2002, 2020)
    plt.legend()

    # save as a png
    plt.savefig("linplot1.png")
    plt.show()

    # create a group to create bar chart separting Germany, Ireland, Italy and Japan
    df_group2 = df_years.groupby('Country Name')[
        '2005', '2006', '2007', '2008', '2009'].mean().iloc[2:6]

    # create pivote table to store it
    group = pd.pivot_table(
        df_group2, values='2008', index='Country Name')

    # create a bar chart using above pivote table in 2008
    plt.figure(figsize=(9, 6), facecolor="lightblue")

    # plot the bar graph to show avarage forest percentage in Germany,Ireland, Italy and Japan in 2008
    plt.bar(group.index, group["2008"])

    # labeling
    plt.xlabel("Country", fontweight='bold')
    plt.ylabel("Percentage(%)", fontweight='bold')
    plt.title("Average Forest Percerntage(%) - 2008",
              fontweight='bold')

    # save as a png
    plt.savefig("barchart.png")
    plt.show()


# call the function which create to read csv file to analize above statitical properties
filepath("Dataset_Population_growth_Forest_Area.csv")
