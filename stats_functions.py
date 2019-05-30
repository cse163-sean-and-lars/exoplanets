# we can put the code for our stats functions in here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

planets = ['non-habitable', 'hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_type(data):
    """
    """
    plt.cla()
    d = data[data['P. Habitable'] != 0
             ].groupby('S. Type')['P. Habitable'
                                  ].sum().reset_index(name='count')
    pd.DataFrame(d)
    sns.catplot(x='S. Type', y='count', kind='bar', ci=None, color='b', data=d)
    plt.xticks(rotation=-80)
    plt.title('Nuber of Confirmed Habitable Exoplanets per Star Type')
    plt.savefig('s_type.png', bbox_inches='tight')


def s_mass(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Mass (SU)',
                  order=planets, data=data)
    plt.xticks(rotation=-20)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Mass')
    plt.savefig('s_mass.png', bbox_inches='tight')


def s_radius(data):
    """
    """
    plt.cla()


def s_teff(data):
    """
    """
    plt.cla()


def s_luminosity(data):
    """
    """
    plt.cla()
    d = data[['P. Habitable Class', 'S. Luminosity (SU)']]
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  order=planets, size=1, data=d)
    plt.xticks(rotation=-20)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('luminiosity.png')


def s_FeH(data):
    """
    """
    plt.cla()


def s_age(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Age (Gyrs)',
                  order=planets, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Age of Parent Star')
    plt.savefig('s_age.png')


def main():
    """
    """
    data = pd.read_csv('phl_hec_all_confirmed.csv')
    s_type(data)
    s_mass(data)
    s_luminosity(data)


if __name__ == '__main__':
    main()
