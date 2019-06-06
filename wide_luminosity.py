# we can put the code for our stats functions in here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
sns.set()

planets = ['hypopsychroplanet', 'psychroplanet', 'mesoplanet',
           'thermoplanet']


def s_luminosity(h, nh):
    """
    Plot the distribution of confirmed exoplanets by exoplanet class vs the
    luminosity of their parent star.
    """
    # plot with only non-habitable planets
    plt.cla()
    plt.subplots(figsize=(75, 20))
    sns.swarmplot(x='P. Habitable Class', y='S. Luminosity (SU)',
                  size=1, data=nh)
    plt.title('Distribution of Number of Non-Habitable' +
              ' Planets per Class vs Parent Star Luminosity')
    plt.savefig('wide_s_luminiosity_nh.png', bbox_inches='tight')
    plt.close()


def main():
    # read in the confirmed exoplanet data
    data = pd.read_csv('phl_hec_all_confirmed.csv')

    # filter data into habitable (h) and non-habitable (nh) sets
    nh = data[data['P. Habitable Class'] == 'non-habitable']
    h = data[data['P. Habitable Class'] != 'non-habitable']

    start_time = time.time()

    s_luminosity(h, nh)
    print('finished luminosity!   ',
          '--- %s seconds ---' % (time.time() - start_time))


if __name__ == '__main__':
    main()
