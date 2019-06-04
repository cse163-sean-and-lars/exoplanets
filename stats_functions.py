# we can put the code for our stats functions in here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
sns.set()

planets = ['non-habitable', 'hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_type(data):
    """
    Plot the number of habitable exoplanets for differen star types from the
    data. In order to avoid severely cluttered axes, only star types with one
    or more habitable exoplanet are included.
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
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Mass')
    plt.savefig('s_mass.png', bbox_inches='tight')


def s_radius(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Radius (SU)',
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Radius')
    plt.savefig('s_radius.png', bbox_inches='tight')


def s_mass_vs_radius(data):
    """
    """
    plt.cla()
    sns.relplot(x='S. Mass (SU)', y='S. Radius (SU)',
                hue='P. Habitable Class', data=data)
    plt.xticks(rotation=-15)
    plt.title('Star Mass vs Star Radius for Stars with Known Exoplanets')
    plt.savefig('s_mass_vs_radius_all.png', bbox_inches='tight')

    plt.cla()
    d = data[data['P. Habitable'] == 1]
    sns.relplot(x='S. Mass (SU)', y='S. Radius (SU)',
                hue='P. Habitable Class', data=d)
    plt.xticks(rotation=-15)
    plt.title('Star Mass vs Star Radius for Stars' +
              'with Known Habitable Exoplanets')
    plt.savefig('s_mass_vs_radius_habitable.png', bbox_inches='tight')


def s_teff(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Teff (K)',
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Effective Temperature')
    plt.savefig('s_teff.png', bbox_inches='tight')


def s_luminosity(data):
    """
    """
    plt.cla()
    d = data[['P. Habitable Class', 'S. Luminosity (SU)']]
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  order=planets, size=3, data=d)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('s_luminiosity.png', bbox_inches='tight')


def s_FeH(data):
    """
    """
    # plot unaltered data
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Iron to Hydrogen Ratio')
    plt.savefig('s_FeH.png', bbox_inches='tight')

    # plot with outliers removed
    plt.cla()
    d = data[['S. [Fe/H]', 'P. Habitable Class'
              ]][data['S. [Fe/H]'] > -5]
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  order=planets, size=3, data=d)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Iron to Hydrogen Ratio' +
              ' with Outlying Points Removed')
    plt.savefig('s_FeH_no_outliers.png', bbox_inches='tight')

    # plot with only habitable planets
    plt.cla()
    d = data[['S. [Fe/H]', 'P. Habitable Class'
              ]][data['P. Habitable'] == 1]
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  order=planets, size=3, data=d)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Habitable Class vs Parent Star' +
              ' Iron to Hydrogen Ratio')
    plt.savefig('s_FeH_only_habitable.png', bbox_inches='tight')


def s_age(data):
    """
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Age (Gyrs)',
                  order=planets, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Age of Parent Star')
    plt.savefig('s_age.png', bbox_inches='tight')


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

    # Includes uninhabitable planets
    plt.cla()
    d = data[(data['S. Mag from Planet'] > -30) &
             (data['S. Mag from Planet'] < -25)]
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=d,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('s_mag_from_planet_uninhabitable.png')

    # Only habitable planets
    d2 = data[data['P. Habitable Class'] != 'non-habitable']
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=d2,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('s_mag_from_planet_inhabitable.png')


def s_size_from_planet(data):
    """
    """
    plt.cla()
    d = data[data['S. Size from Planet (deg)'] < 3]
    sns.swarmplot(x='P. Habitable Class', y='S. Size from Planet (deg)',
                  data=d, order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Size from Planet')
    plt.savefig('s_size_from_planet.png')


def main():
    data = pd.read_csv('phl_hec_all_confirmed.csv')
    start_time = time.time()
    """
    s_type(data)
    print('finished type!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_mass(data)
    print('finished mass!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_teff(data)
    print('finished teff!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_FeH(data)
    print('finished [Fe/H]!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_age(data)
    print('finished age!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_ra(data)
    print('finished ra!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_dec(data)
    print('finished dec!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_radius(data)
    print('finished radius!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    """
    s_luminosity(data)
    print('finished luminosity!   ',
          '--- %s seconds ---' % (time.time() - start_time))


if __name__ == '__main__':
    main()
