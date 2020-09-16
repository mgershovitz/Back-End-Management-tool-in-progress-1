import pandas as p
from matplotlib import pyplot as plt

from src.DB.Models.DTO.department import Department


# graph methods
def create_plot_graph(month, births):
    plt.plot(month, births)
 #   plt.savefig('plot.png')
    plt.show()


# create bar graph - number of births
def create_bar_graph(month, births):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    plt.title('Number of births per month')
    ax.bar(month, births)
    plt.savefig('bar.png')
    plt.show()


def create_pie_graph(labels, sizes, number_of_birth):
    colors = ['gold', 'lightcoral']
    explode = (0.1, 0)  # explode 1st slice
    plt.title('Vacuum percentage from vaginal ' + number_of_birth +' births')

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('pie.png')
    plt.show()


def count_birth_by_month(date):
    return Department("").count_hospital_living_birth(date)


# data for graphs
# number of births data
jun = count_birth_by_month('01/18')
feb = count_birth_by_month('02/18')
mar = count_birth_by_month('03/18')
apr = count_birth_by_month('04/18')
may = count_birth_by_month('05/18')
jun = count_birth_by_month('06/18')
jul = count_birth_by_month('07/18')
aug = count_birth_by_month('08/18')
sep = count_birth_by_month('09/18')
oct = count_birth_by_month('10/18')
nov = count_birth_by_month('11/18')
dec = count_birth_by_month('12/18')

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
births = [jun, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

# vacuum data for vaginal birth in the first birth
vacuum = Department("").count_hospital_prognoza_first_birth("Vacuum", "19", 1)
not_vacuum_not_cs = Department("").count_hospital_prognoza_first_birth("Section", "19", 1) + Department("").count_hospital_prognoza_first_birth("Vaccum", "19",1)
not_vacuum = Department("").count_hospital_prognoza_first_birth("", "19", 1) - not_vacuum_not_cs

labels = 'Vacuum', 'Not Vacuum'
sizes = [vacuum, not_vacuum]

# create graphs
create_pie_graph(labels, sizes, "first")
create_bar_graph(month, births)