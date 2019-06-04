# we can put the code for our stats functions in here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
sns.set()

planets = ['hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_type(data):
    """
    Plot the number of habitable exoplanets for differen star types from the
    data. In order to avoid severely cluttered axes, only star types with one
    or more habitable exoplanet are included.
    """
    plt.cla()
    # filter the data to remove uninhabitable planets, and then groupby
    # parent star type, summing the counts of habitable exoplanets per type
    d = data[data['P. Habitable'] != 0
             ].groupby('S. Type')['P. Habitable'
                                  ].sum().reset_index(name='count')
    # cast groupby object to a dataframe object
    pd.DataFrame(d)
    # create a bar chart to show the data
    sns.catplot(x='S. Type', y='count', kind='bar', ci=None, color='b', data=d)
    # configure the plot to make it legible
    plt.xticks(rotation=-80)
    plt.title('Nuber of Confirmed Habitable Exoplanets per Star Type')
    plt.savefig('s_type.png', bbox_inches='tight')
    plt.close()


def s_mass(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    mass of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    # create a swarmplot to plot the dsitribution
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Mass (SU)',
                  order=planets, size=3, data=h)
    # configure the plot to make it legible
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Mass')
    plt.savefig('s_mass_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    # create a swarmplot to plot the dsitribution
    plt.subplots(figsize=(20, 8))
    sns.swarmplot(x='P. Habitable Class', y='S. Mass (SU)',
                  size=3, data=nh)
    # configure the plot to make it legible
    plt.title('Distribution of Number of Non-Habitable' +
              ' Planets per Class vs Parent Star Mass')
    plt.savefig('s_mass_nh.png', bbox_inches='tight')
    plt.close()


def s_radius(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    radius of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    # create a swarmplot to plot the distribution
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Radius (SU)',
                  order=planets, size=3, data=h)
    # configure the plot to make it legible
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Radius')
    plt.savefig('s_radius_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    # create a swarmplot to plot the distribution
    plt.subplots(figsize=(20, 8))
    sns.swarmplot(x='P. Habitable Class', y='S. Radius (SU)',
                  size=3, data=nh)
    # configure the plot to make it legible
    plt.title('Distribution of Number of Non-Habitable' +
              ' Exoplanets per Class vs Parent Star Radius')
    plt.savefig('s_radius_nh.png', bbox_inches='tight')
    plt.close()


def s_mass_vs_radius(data, h):
    """
    Plot star mass vs star radius for the parent stars of confirmed exoplanets,
    and color code by exoplanet type. Because of how many planets are shown, a
    second plot is also made that includes only potentially habitable planets
    """
    # plot with both habitable and non-habitable planets
    plt.cla()
    # create a scatter plot to compare each parent star's mass to its radius
    plt.subplots(figsize=(20, 20))
    sns.relplot(x='S. Mass (SU)', y='S. Radius (SU)',
                hue='P. Habitable Class', data=data)
    # configure the plot to make it legible
    plt.title('Star Mass vs Star Radius for Stars with Known Exoplanets')
    plt.savefig('s_mass_vs_radius_all.png', bbox_inches='tight')
    plt.close()

    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.relplot(x='S. Mass (SU)', y='S. Radius (SU)',
                hue='P. Habitable Class', data=h)
    # configure the plot to make it legible
    plt.title('Star Mass vs Star Radius for Stars' +
              'with Known Habitable Exoplanets')
    plt.savefig('s_mass_vs_radius_h.png', bbox_inches='tight')
    plt.close()


def s_teff(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    effective temperature of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Teff (K)',
                  order=planets, size=3, data=h)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Parent Star Effective Temperature')
    plt.savefig('s_teff_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. Teff (K)',
                  size=3, data=nh)
    plt.title('Distribution of Number of Non-Habitable' +
              ' Exoplanets per Class vs Parent Star Effective Temperature')
    plt.savefig('s_teff_nh.png', bbox_inches='tight')
    plt.close()


def s_luminosity(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    luminosity of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  order=planets, size=3, data=h)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('s_luminiosity_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  size=3, data=nh)
    plt.title('Distribution of Number of Non-Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('s_luminiosity_nh.png', bbox_inches='tight')
    plt.close()


def s_FeH(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    ratio of iron to hydrogen in their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  order=planets, size=3, data=h)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Planets per Habitable Class vs Parent Star' +
              ' Iron to Hydrogen Ratio')
    plt.savefig('s_FeH_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. [Fe/H]',
                  size=3, data=nh)
    plt.title('Distribution of Number of Non-Habitable' +
              ' Planets per Class vs Parent Star Iron to Hydrogen Ratio')
    plt.savefig('s_FeH_nh.png', bbox_inches='tight')
    plt.close()


def s_age(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    age of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Age (Gyrs)',
                  order=planets, size=3, data=h)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable' +
              ' Exoplanets per Class vs Age of Parent Star')
    plt.savefig('s_age_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(10, 10))
    sns.swarmplot(x='P. Habitable Class', y='S. Age (Gyrs)',
                  size=3, data=nh)
    plt.title('Distribution of Number of Non-Habitable' +
              ' Exoplanets per Class vs Age of Parent Star')
    plt.savefig('s_age_nh.png', bbox_inches='tight')
    plt.close()


def s_ra(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    right ascension of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. RA (hrs)', data=h,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'vs Parent Star Right Ascension')
    plt.savefig('s_ra_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. RA (hrs)', data=nh,
                  size=3)
    plt.title('Distribution of Number of Non-Habitable Planets per Class' +
              'vs Parent Star Right Ascension')
    plt.savefig('s_ra_nh.png', bbox_inches='tight')
    plt.close()


def s_dec(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    declination of their parent star.
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. DEC (deg)', data=h,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Distribution of Number of Habitable Planets per Class' +
              'vs Parent Star Declination')
    plt.savefig('s_dec_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(15, 15))
    sns.swarmplot(x='P. Habitable Class', y='S. DEC (deg)', data=nh,
                  size=3)
    plt.title('Distribution of Number of Non-Habitable Planets per Class' +
              'vs Parent Star Declination')
    plt.savefig('s_dec_nh.png', bbox_inches='tight')
    plt.close()


def s_mag_from_planet(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    magnitude of the parent star as seen by the plaent
    """
    # plot with only habitable planets
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=h,
                  order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('s_mag_from_planet_h.png')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(10, 10))
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=nh,
                  size=3)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet')
    plt.savefig('s_mag_from_planet_nh.png')
    plt.close()


def s_size_from_planet(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    relative size of the parent star in the sky of the planet
    """
    # plot with only habitable planets
    plt.cla()
    plt.subplots(figsize=(5, 5))
    sns.swarmplot(x='P. Habitable Class', y='S. Size from Planet (deg)',
                  data=h, order=planets, size=3)
    plt.xticks(rotation=-15)
    plt.title('Planet Habitability in Relation to Star Size from Planet')
    plt.savefig('s_size_from_planet_h.png')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. Size from Planet (deg)',
                  data=nh, size=3)
    plt.title('Planet Habitability in Relation to Star Size from Planet')
    plt.savefig('s_size_from_planet_nh.png')
    plt.close()


def main():
    # read in the confirmed exoplanet data
    data = pd.read_csv('phl_hec_all_confirmed.csv')

    # filter data into habitable (h) and non-habitable (nh) sets
    nh = data[data['P. Habitable Class'] == 'non-habitable']
    h = data[data['P. Habitable Class'] != 'non-habitable']

    # start a timer for the sake of seeing how long each plot takes
    start_time = time.time()

    # plot each relationship
    s_type(data)
    print('finished type!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_mass(h, nh)
    print('finished mass!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_radius(h, nh)
    print('finished radius!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_mass_vs_radius(data, h)
    print('finished mass vs radius!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_teff(h, nh)
    print('finished teff!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_luminosity(h, nh)
    print('finished luminosity!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_FeH(h, nh)
    print('finished [Fe/H]!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_age(h, nh)
    print('finished age!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_ra(h, nh)
    print('finished ra!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_dec(h, nh)
    print('finished dec!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_mag_from_planet(h, nh)
    print('finished mag!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_size_from_planet(h, nh)
    print('finished size!   ',
          '--- %s seconds ---' % (time.time() - start_time))


if __name__ == '__main__':
    main()
