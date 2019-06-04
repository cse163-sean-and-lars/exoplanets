# This is the same as the other python file, except it creates resized
# swarmplots in order to see the full distributions of things.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
sns.set()

planets = ['non-habitable', 'hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_mass(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    mass of their parent star.
    """
    plt.cla()
    fig, [ax1, ax2] = plt.subplots(2, figsize=(20, 10))
    # plt.subplots(figsize=(20, 8))
    d1 = data[data['P. Habitable Class'] == 'non-habitable']
    d2 = data[data['P. Habitable Class'] != 'non-habitable']
    # create a swarmplot to plot the dsitribution
    sns.swarmplot(x='P. Habitable Class', y='S. Mass (SU)',
                  size=3, data=d1, ax=ax1)
    sns.swarmplot(x='P. Habitable Class', y='S. Mass (SU)',
                  size=3, data=d2, ax=ax2)
    # configure the plot to make it legible
    # fig.set_title('Distribution of Number of Habitable' +
    #              ' Planets per Class vs Parent Star Mass')
    fig.savefig('wide_s_mass.png', bbox_inches='tight')


def s_radius(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    radius of their parent star.
    """
    plt.cla()
    # create a swarmplot to plot the distribution
    sns.swarmplot(x='P. Habitable Class', y='S. Radius (SU)',
                  order=planets, size=3, data=data)
    # configure the plot to make it legible
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Radius')
    plt.savefig('wide_s_radius.png', bbox_inches='tight')


def s_teff(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    effective temperature of their parent star.
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Teff (K)',
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Effective Temperature')
    plt.savefig('wide_s_teff.png', bbox_inches='tight')


def s_luminosity(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    luminosity of their parent star.
    """
    plt.cla()
    d = data[['P. Habitable Class', 'S. Luminosity (SU)']]
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  order=planets, size=3, data=d)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('wide_s_luminiosity.png', bbox_inches='tight')


def s_FeH(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    ratio of iron to hydrogen in their parent star.
    """
    # plot unaltered data
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  order=planets, size=3, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Iron to Hydrogen Ratio')
    plt.savefig('wide_s_FeH.png', bbox_inches='tight')

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
    plt.savefig('wide_s_FeH_no_outliers.png', bbox_inches='tight')

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
    plt.savefig('wide_s_FeH_only_habitable.png', bbox_inches='tight')


def s_age(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    age of their parent star.
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. Age (Gyrs)',
                  order=planets, data=data)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Age of Parent Star')
    plt.savefig('wide_s_age.png', bbox_inches='tight')


def s_ra(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    right ascension of their parent star.
    """
    plt.cla()
    sns.swarmplot(x='P. Habitable Class', y='S. RA (hrs)', data=data,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'Parent Star Right Ascension')
    plt.savefig('wide_s_ra.png', bbox_inches='tight')


def s_dec(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    declination of their parent star.
    """
    plt.cla()
    d = data[(data['S. DEC (deg)'] > -65) & (data['S. DEC (deg)'] < 55)]
    sns.swarmplot(x='P. Habitable Class', y='S. DEC (deg)', data=d,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'Parent Star Declination')
    plt.savefig('wide_s_dec.png', bbox_inches='tight')


def s_mag_from_planet(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    magnitude of the parent star as seen by the plaent
    """
    # Includes uninhabitable planets
    plt.cla()
    d = data[(data['S. Mag from Planet'] > -30) &
             (data['S. Mag from Planet'] < -25)]
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=d,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('wide_s_mag_from_planet_uninhabitable.png')

    # Only habitable planets
    d2 = data[data['P. Habitable Class'] != 'non-habitable']
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=d2,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('wide_s_mag_from_planet_inhabitable.png')


def s_size_from_planet(data):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    relative size of the parent star in the sky of the planet
    """
    plt.cla()
    d = data[data['S. Size from Planet (deg)'] < 3]
    sns.swarmplot(x='P. Habitable Class', y='S. Size from Planet (deg)',
                  data=d, order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Size from Planet')
    plt.savefig('wide_s_size_from_planet.png')


def main():
    # read in the confirmed exoplanet data
    data = pd.read_csv('phl_hec_all_confirmed.csv')
    # start a timer for the sake of seeing how long each plot takes
    start_time = time.time()

    s_mass(data)
    print('finished mass!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    """
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
    s_luminosity(data)
    print('finished luminosity!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_mag_from_planet(data)
    print('finished mag!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_size_from_planet(data)
    print('finished size!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    """


if __name__ == '__main__':
    main()
