import pandas as pd
import matplotlib.pyplot as plt
import AssertCount as ac
import AssertLocAndCountInProduction as acp
import plotly.express as px


def generateAssertCountPlots():
    ac.getAssertCountForAllFiles()
    ac.writeToCSV()
    data = pd.read_csv('data/AssertCount.csv')
    numberOfTestFiles = len(data)
    numberOfAssertStatements = data['Assert Count'].sum()
    numberOfAssertErrors = data['Assert Error'].sum()
    groupedByModuleAssertCountData = data.groupby('Module')['Assert Count'].sum().reset_index()
    groupedByModuleAssertErrorData = data.groupby('Module')['Assert Error'].sum().reset_index()
    groupedByModuleTotalCountOfTestCasesData = data.groupby('Module').size()
    groupedByModuleTotalCountOfTestCasesData.plot(kind='barh', title='Test Files in each Module (Total - ' + str(
        numberOfTestFiles) + ')')
    plt.savefig("figures/Test-Files-Count", dpi=300)
    plt.close()
    groupedByModuleAssertCountData.sort_values(['Assert Count'], ascending=False).plot(kind='barh', y='Assert Count',
                                                                                       x='Module',
                                                                                       title='Assert Statements in '
                                                                                             'each Module (Total - '
                                                                                             + str(
                                                                                           numberOfAssertStatements) + ')')
    plt.savefig("figures/Assert-Statements-Count", dpi=300)
    plt.close()
    groupedByModuleAssertErrorData.sort_values(['Assert Error'], ascending=False).plot(kind='barh', y='Assert Error',
                                                                                       x='Module',
                                                                                       title='Assert Errors in each '
                                                                                             'Module (Total - ' + str(
                                                                                           numberOfAssertErrors) + ')')
    plt.savefig("figures/Assert-Errors-Count", dpi=300)
    plt.close()
    return numberOfAssertStatements


def generateAssertCountInProductionPlots():
    res = acp.getAssertLocAndCountForAllFiles()
    acp.writeToCSV()
    data = pd.read_csv('data/AssertLocAndCountInProduction.csv')
    numberOfAssertStatementsInProd = data['Assert Count'].sum()
    sorted_d = dict(sorted(res.items(), key=lambda x: x[1][0], reverse=True))
    first3pairs = {k: sorted_d[k] for k in list(sorted_d)[:3]}
    labels = list()
    values = list()
    for key, value in first3pairs.items():
        labels.append(key[key.rfind("/") + 1:])
        values.append(value[0])
    plt.bar(labels, values, label="Total Asserts - " + str(numberOfAssertStatementsInProd))
    plt.title("Assert Count of Top 3 Files In Producation Files")
    plt.legend()
    plt.savefig("figures/Top3AssertCounts-Production", dpi=300)
    plt.close()
    return numberOfAssertStatementsInProd


def compareAsserts():
    values = [numberOfAssertStatements, numberOfAssertStatementsInProd]
    labels = ["Production","TestFiles"]
    wp = {'linewidth': 0.5, 'edgecolor': "Black"}
    explode = (0.1, 0.3)
    plt.pie(values, labels=labels, wedgeprops=wp, explode = explode)
    plt.title("Comparision of Assert Counts in Test and Production Files")
    plt.savefig("figures/ComapreAsserts", dpi=300)
    plt.close()


def generatePlotsPyDriller():
    data1 = pd.read_csv('data/PyDrillerCommitMessages.csv')
    dataframe = pd.DataFrame(data1)
    count = list(dataframe.iloc[:, 0])
    num_of_occurences = list(dataframe.iloc[:, 1])
    plt.bar(count, num_of_occurences, color='b')
    plt.title("Commit Message Trends")
    plt.xlabel("code")
    plt.ylabel("Number of commits")
    plt.savefig('figures/PyDrillerCommits')
    plt.close()

def generatePlotsAuthorNames():
    data = pd.read_csv('data/PyDrillerAuthors.csv')
    dataframe = pd.DataFrame(data)
    dataframe = dataframe.sort_values('count', ascending=False)
    name = list(dataframe.iloc[:6, 0])
    count = list(dataframe.iloc[:6, 1])
    plt.bar(name, count, color='b')
    plt.xticks(name, name, rotation=20)
    plt.title("Top Contributors")
    plt.xlabel("Names")
    plt.ylabel("Number of Commits")
    plt.tight_layout()
    plt.savefig('figures/PyDrillerAuthors')
    plt.close()

if __name__ == "__main__":
    numberOfAssertStatements = generateAssertCountInProductionPlots()
    numberOfAssertStatementsInProd = generateAssertCountPlots()
    compareAsserts()
    generatePlotsPyDriller()
    generatePlotsAuthorNames()
