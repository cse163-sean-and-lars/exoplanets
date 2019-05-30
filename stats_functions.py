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
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)', data=d)
    plt.savefig('luminiosity.png')


def s_FeH(data):
    """
    """
    plt.cla()


def s_age(data):
    """
    """
    plt.cla()


def s_appar_mag(data):
    """
    """
    plt.cla()


def s_ra(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. RA (hrs)', data=data,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'Parent Star Right Ascension')
    plt.savefig('s_ra.png', bbox_inches='tight')


def s_dec(data):
    """
    """
    plt.cla()
    d = data[(data['S. DEC (deg)'] > -65) & (data['S. DEC (deg)'] < 55)]
    sns.swarmplot(x='P. Habitable Class', y='S. DEC (deg)', data=d,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'Parent Star Declination')
    plt.savefig('s_dec.png', bbox_inches='tight')


def s_mag_from_planet(data):
    """
    """
    plt.cla()


def s_size_from_planet(data):
    """
    """
    plt.cla()


def main():
    """
    """
    data = pd.read_csv('phl_hec_all_confirmed.csv')
    # s_luminosity(data)
    s_type(data)
    s_mass(data)


if __name__ == '__main__':
    main()
