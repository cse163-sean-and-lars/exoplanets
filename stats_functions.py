# Creates swarmplots relating the habitability and habitable class of
# confirmed exoplanets to different attributes of the stars they revolve
# around. Also creates models for predicting the habitability and habitable
# class of different Kepler objects based on said attirubtes.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import time
sns.set()

planets = ['hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_type(data):
    """
    Plot the number of habitable exoplanets for differen star types from the
    data. In order to avoid severely cluttered axes, only broad star types are
    included, the specific types are aggregated into general type categories
    """
    # plot habitable planets
    plt.cla()
    # group the data by star letter classification
    d = data[['S. Type', 'P. Habitable']].dropna()
    types = list()
    for star_type in d['S. Type']:
        types.append(star_type[0])
    d['Type'] = types
    d = d.groupby('Type')['P. Habitable'].sum().reset_index(name='count')
    # cast groupby object to a dataframe object
    pd.DataFrame(d)
    o = list(d['Type'])
    # create a bar chart to show the data
    sns.catplot(x='Type', y='count', kind='bar', ci=None, color='b',
                data=d, order=o)
    # configure the plot to make it legible
    plt.title('Nuber of Confirmed Habitable Exoplanets per Star Type')
    plt.xlabel('Star Class')
    plt.ylabel('Number of Confirmed Exoplanets')
    plt.savefig('s_type.png', bbox_inches='tight')
    plt.close()

    # plot all planets
    plt.cla()
    d2 = data[['S. Type']].dropna()
    counts = dict()
    for star_type in d2['S. Type']:
        if star_type[0] in counts:
            counts[star_type[0]] += 1
        else:
            counts[star_type[0]] = 1
    counts_pd = pd.DataFrame(list(zip(counts.keys(), counts.values())),
                             columns=['Type', 'Counts'])
    sns.catplot(x='Type', y='Counts', kind='bar', ci=None, color='b',
                data=counts_pd, order=o)
    plt.title('Nuber of Confirmed Exoplanets per Star Type')
    plt.xlabel('Star Class')
    plt.ylabel('Number of Confirmed Exoplanets')
    plt.savefig('s_type_all.png', bbox_inches='tight')
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
              ' Planets per Class vs Parent Star Mass', fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. Mass (SU)', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
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
              ' Exoplanets per Class vs Parent Star Radius', fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. Radius (SU)', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
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
              ' with Known Habitable Exoplanets')
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
              ' Exoplanets per Class vs Parent Star Effective Temperature',
              fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. Teff (K)', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
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
              ' Planets per Class vs Parent Star Luminosity', fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. Luminosity (SU)', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
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
              ' Planets per Class vs Parent Star Iron to Hydrogen Ratio',
              fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. [Fe/H]', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
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
              ' Exoplanets per Class vs Age of Parent Star', fontsize=20)
    plt.xlabel('P. Habitable Class', fontsize=16)
    plt.ylabel('S. Age (Gyrs)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('s_age_nh.png', bbox_inches='tight')
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
    plt.savefig('s_mag_from_planet_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(10, 10))
    sns.swarmplot(x='P. Habitable Class', y='S. Mag from Planet', data=nh,
                  size=3)
    plt.title('Planet Habitability in Relation to Star Magnitude from Planet',
              fontsize=24)
    plt.xlabel('P. Habitable Class', fontsize=16)
    plt.ylabel('S. Mag from Planet', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('s_mag_from_planet_nh.png', bbox_inches='tight')
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
    plt.savefig('s_size_from_planet_h.png', bbox_inches='tight')
    plt.close()

    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(20, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. Size from Planet (deg)',
                  data=nh, size=3)
    plt.title('Planet Habitability in Relation to Star Size from Planet',
              fontsize=30)
    plt.xlabel('P. Habitable Class', fontsize=24)
    plt.ylabel('S. Size from Planet (deg)', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig('s_size_from_planet_nh.png', bbox_inches='tight')
    plt.close()


def model(data, kepler_data):
    """
    Creates models for predicting the habitability and habitable class of
    different exoplanets and Kepler objects based on characteristics of the
    stars they revolve around. Prints accuracy scores for both models in
    making predictions based on both confirmed exoplanets and Kepler objects.
    """

    filt = data.loc[:, ['S. Mass (SU)', 'S. Radius (SU)', 'S. Teff (K)',
                        'S. Luminosity (SU)', 'S. Age (Gyrs)', 'S. RA (hrs)',
                        'S. DEC (deg)', 'S. Mag from Planet',
                        'S. Size from Planet (deg)', 'P. Habitable',
                        'P. Habitable Class']]
    filt = filt.dropna()

    # Models habitability based on characteristics of confirmed exoplanets

    X = filt.loc[:, (filt.columns != 'P. Habitable Class') &
                 (filt.columns != 'P. Habitable')]
    y = filt['P. Habitable']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    print('Confirmed Exoplanet Habitability Accuracy Score:')
    print(accuracy_score(y_test, model.predict(X_test)))

    # Tests previous model on all Kepler objects

    kep_filt = kepler_data.loc[:, ['S. Mass (SU)', 'S. Radius (SU)',
                                   'S. Teff (K)', 'S. Luminosity (SU)',
                                   'S. Age (Gyrs)', 'S. RA (hrs)',
                                   'S. DEC (deg)', 'S. Mag from Planet',
                                   'S. Size from Planet (deg)',
                                   'P. Habitable', 'P. Habitable Class']]
    kep_filt = kep_filt.dropna()
    kep_filt = kep_filt[kep_filt['S. Size from Planet (deg)'] != '-']

    kepler_X = kep_filt.loc[:, (kep_filt.columns != 'P. Habitable Class') &
                            (kep_filt.columns != 'P. Habitable')]
    kepler_y = kep_filt['P. Habitable']

    print('Kepler Object Habitability Accuracy Score:')
    print(accuracy_score(kepler_y, model.predict(kepler_X)))

    # Models habitable class based on characteristics of confirmed exoplanets

    y_class = filt['P. Habitable Class']

    X_class_train, X_class_test, y_class_train, y_class_test = \
        train_test_split(X, y_class, test_size=.2)

    model_class = DecisionTreeClassifier()
    model_class.fit(X_class_train, y_class_train)

    print('Confirmed Exoplanet Habitable Class Accuracy Score:')
    print(accuracy_score(y_class_test, model_class.predict(X_class_test)))

    # Tests previous model on all Kepler objects

    kepler_y_class = kep_filt['P. Habitable Class']

    print('Kepler Object Habitable Class Accuracy Score:')
    print(accuracy_score(kepler_y_class, model_class.predict(kepler_X)))


def main():
    # read in the confirmed exoplanet data
    data = pd.read_csv('phl_hec_all_confirmed.csv')
    kepler_data = pd.read_csv('phl_hec_all_kepler.csv')

    # filter data into habitable (h) and non-habitable (nh) sets
    nh = data[data['P. Habitable Class'] == 'non-habitable']
    h = data[data['P. Habitable Class'] != 'non-habitable']

    # start a timer for the sake of seeing how long each plot takes
    # some take a long time, this is due to overlapping values in the swarmplot
    # to stop this from happening we need to make the axis larger, but kind of
    # unreasonably wider, so we crop it for the sake of legibility.
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
    s_mag_from_planet(h, nh)
    print('finished mag!   ',
          '--- %s seconds ---' % (time.time() - start_time))
    s_size_from_planet(h, nh)
    print('finished size!   ',
          '--- %s seconds ---\n' % (time.time() - start_time))

    model(data, kepler_data)


if __name__ == '__main__':
    main()
