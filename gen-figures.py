import pandas as pd
import matplotlib.pyplot as plt
import AssertCount as ac


def generateAssertCountPlots():
    ac.getAssertCountForAllFiles()
    ac.writeToCSV()
    data = pd.read_csv('data/AssertCount.csv')
    groupedByModuleAssertCountData = data.groupby('Module')['Assert Count'].sum().reset_index()
    groupedByModuleAssertErrorData = data.groupby('Module')['Assert Error'].sum().reset_index()
    groupedByModuleTotalCountOfTestCasesData = data.groupby('Module').size()
    groupedByModuleTotalCountOfTestCasesData.plot(kind='barh', title='Test Files in each Module (Total - 167)')
    plt.savefig("figures/Test-Files-Count", dpi=300)
    groupedByModuleAssertCountData.sort_values(['Assert Count'], ascending=False).plot(kind='barh', y='Assert Count',
                                                                                       x='Module',
                                                                                       title='Assert Statements in '
                                                                                             'each Module (Total - '
                                                                                             '18748)')
    plt.savefig("figures/Assert-Statements-Count", dpi=300)
    groupedByModuleAssertErrorData.sort_values(['Assert Error'], ascending=False).plot(kind='barh', y='Assert Error',
                                                                                       x='Module',
                                                                                       title='Assert Errors in each '
                                                                                             'Module (Total - 91)')
    plt.savefig("figures/Assert-Errors-Count", dpi=300)


generateAssertCountPlots()
