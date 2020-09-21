import pandas as p
from matplotlib import pyplot as plt
from src.DB.Models.DTO.department import Department
import numpy as np

# graph methods
# plot graph methods
from src.DB.Models.DTO.nurse_statistics import NurseStatistics


def create_plot_graph(month, births):
    plt.plot(month, births)
    #   plt.savefig('plot.png')
    plt.show()


# create bar graph - number of births
def create_bar_graph(month, births):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    plt.title('Number of births per month')
    ax.bar(month, births)
    # plt.savefig('bar.png')
    plt.show()


def create_multiple_bar_graph(hospital_statistics, nurse_statistics):
    bar_width = 0.25

    # Set position of bar on X axis
    r1 = np.arange(len(hospital_statistics))
    r2 = [x + bar_width for x in r1]

    # Make the plot
    plt.bar(r1, hospital_statistics, color='#7f6d5f', width=bar_width, edgecolor='white', label='var1')
    plt.bar(r2, nurse_statistics, color='#557f2d', width=bar_width, edgecolor='white', label='var2')

    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(hospital_statistics))],
               ['תודיל סמ', 'םיירסיק', 'םוקאו', '3 הגרד םיכתח', 'יפא', 'לרודיפא'])

    # save file
    # plt.savefig('multiple_bar.png')

    # Create legend & Show graphic
    plt.legend()
    plt.show()


def create_pie_graph(labels, sizes, number_of_birth):
    colors = ['gold', 'lightcoral']
    explode = (0.1, 0)  # explode 1st slice
    plt.title('Vacuum percentage from vaginal ' + number_of_birth + ' births')

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    # plt.savefig('pie.png')
    plt.show()


def count_birth_by_month(date):
    return Department("").count_hospital_living_birth(date)


# data
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

# hospital and nurse statistics
hs = Department("")
ns = NurseStatistics("179801")

# vacuum data for vaginal birth in the first birth
vacuum = Department("").count_hospital_prognoza_first_birth("Vacuum", "19", 1)
not_vacuum_not_cs = Department("").count_hospital_prognoza_first_birth("Section", "19", 1) + Department(
    "").count_hospital_prognoza_first_birth("Vaccum", "19", 1)
not_vacuum = Department("").count_hospital_prognoza_first_birth("", "19", 1) - not_vacuum_not_cs
# vacuum data for vaginal births gt than first birth
vacuum_gt_first = Department("").count_hospital_prognoza_first_birth("Vacuum", "19", 2)
not_vacuum_not_cs = Department("").count_hospital_prognoza_first_birth("Section", "19", 2) + Department(
    "").count_hospital_prognoza_first_birth("Vacuum", "19", 2)
not_vacuum_gt_first = Department("").count_hospital_prognoza_first_birth("", "19", 2) - not_vacuum_not_cs

labels = 'Vacuum', 'Not Vacuum'
sizes = [vacuum, not_vacuum]
sizes_gt_than_first = [vacuum_gt_first, not_vacuum_gt_first]

# plot graphs
create_pie_graph(labels, sizes, "first")
create_pie_graph(labels, sizes_gt_than_first, "second")
create_bar_graph(month, births)
h_births = hs.number_of_births
n_births = ns.number_of_births
per = 100
create_multiple_bar_graph([hs.number_of_births,(hs.cs/h_births)*per,(hs.vaccum/h_births)*per,(hs.third_degree_tear/h_births)*per,(hs.epi/h_births)*per, (hs.epidoral/h_births)*per], [ns.number_of_births,(ns.cs/n_births)*per, (ns.vaccum/n_births)*per, (ns.third_degree_tear/n_births)*per, (ns.epi/n_births)*per, (ns.epidoral/n_births)*per])  # comparing nurse and hospital statistics for irena