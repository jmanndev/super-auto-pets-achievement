import pandas as pd
from pandas.core.frame import DataFrame


def main():
    df = pd.read_csv('data.csv')
    print('\nStandard:')
    standard_df = df[df['Standard'] == 'y']
    displayStats(standard_df)

    print('\nExpansion:')
    expansion_df = df[df['Expansion'] == 'y']
    displayStats(expansion_df)
    return


def displayStats(df: DataFrame):
    print('\tAchieved: {}/{}'.format(
        len(df[df['Achievement'] == 'y']),
        len(df)
    ))
    print('\tBadge: {}/{} {}'.format(
        len(df[df['Badge'] == 'y']),
        len(df[df['Achievement'] == 'y']),
        df[(df['Badge'] == 'y')].sort_values(by=['Name'])['Name'].tolist()
    ))

    for n in range(6):
        printTier(n+1, df)
    return


def printTier(tier: int, df: DataFrame):
    tier_df = df[df['Tier'] == tier]
    print('\tTier {}:'.format(
        tier
    ))
    print('\t\tMissing: {}/{} {}'.format(
        len(tier_df[tier_df['Achievement'] != 'y']),
        len(tier_df),
        tier_df[tier_df['Achievement'] != 'y']['Name'].tolist()
    ))
    print('\t\tNeed Badge: {}/{} {}'.format(
        len(tier_df[
            (tier_df['Achievement'] == 'y') &
            (tier_df['Badge'] != 'y')
        ]),
        len(tier_df[tier_df['Achievement'] == 'y']),
        tier_df[
            (tier_df['Achievement'] == 'y') & (tier_df['Badge'] != 'y')
        ]['Name'].tolist()
    ))
    return


main()
