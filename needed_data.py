import numpy as np
import pandas as pd

def wizards():    
    wizardsq1 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q10.csv')
    wizardsq2 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q20.csv')
    wizardsq3 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q30.csv')
    wizardsq4 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q40.csv')
    PTS = wizardsq1.loc[wizardsq1['PLAYER'] == 'TOTALS','PTS'].values + wizardsq2.loc[wizardsq2['PLAYER'] == 'TOTALS','PTS'].values + wizardsq3.loc[wizardsq3['PLAYER'] == 'TOTALS','PTS'].values + wizardsq4.loc[wizardsq4['PLAYER'] == 'TOTALS','PTS'].values
    return wizardsq1, wizardsq2, wizardsq3, wizardsq4, PTS

def hawks():    
    hawksq1 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q11.csv')
    hawksq2 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q21.csv')
    hawksq3 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q31.csv')
    hawksq4 = pd.read_csv('./data/july12th_games/Atlanta Hawks_vs_Washington Wizards_q41.csv')
    PTS = hawksq1.loc[hawksq1['PLAYER'] == 'TOTALS','PTS'].values + hawksq2.loc[hawksq2['PLAYER'] == 'TOTALS','PTS'].values + hawksq3.loc[hawksq3['PLAYER'] == 'TOTALS','PTS'].values + hawksq4.loc[hawksq4['PLAYER'] == 'TOTALS','PTS'].values
    return hawksq1, hawksq2, hawksq3, hawksq4, PTS

def pacers():
    pacersq1 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q10.csv')
    pacersq2 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q20.csv')
    pacersq3 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q30.csv')
    pacersq4 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q40.csv')
    PTS = pacersq1.loc[pacersq1['PLAYER'] == 'TOTALS','PTS'].values + pacersq2.loc[pacersq2['PLAYER'] == 'TOTALS','PTS'].values + pacersq3.loc[pacersq3['PLAYER'] == 'TOTALS','PTS'].values + pacersq4.loc[pacersq4['PLAYER'] == 'TOTALS','PTS'].values
    return pacersq1, pacersq2, pacersq3, pacersq4, PTS

def nets():
    netsq1 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q11.csv')
    netsq2 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q21.csv')
    netsq3 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q31.csv')
    netsq4 = pd.read_csv('./data/july12th_games/Brooklyn Nets_vs_Indiana Pacers_q41.csv')
    PTS = netsq1.loc[netsq1['PLAYER'] == 'TOTALS','PTS'].values + netsq2.loc[netsq2['PLAYER'] == 'TOTALS','PTS'].values + netsq3.loc[netsq3['PLAYER'] == 'TOTALS','PTS'].values + netsq4.loc[netsq4['PLAYER'] == 'TOTALS','PTS'].values
    return netsq1, netsq2, netsq3, netsq4, PTS

def magic():
    magicq1 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q10.csv')
    magicq2 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q20.csv')
    magicq3 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q30.csv')
    magicq4 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q40.csv')
    PTS = magicq1.loc[magicq1['PLAYER'] == 'TOTALS','PTS'].values + magicq2.loc[magicq2['PLAYER'] == 'TOTALS','PTS'].values + magicq3.loc[magicq3['PLAYER'] == 'TOTALS','PTS'].values + magicq4.loc[magicq4['PLAYER'] == 'TOTALS','PTS'].values
    return magicq1, magicq2, magicq3, magicq4, PTS

def cavaliers():
    cavaliersq1 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q11.csv')
    cavaliersq2 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q21.csv')
    cavaliersq3 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q31.csv')
    cavaliersq4 = pd.read_csv('./data/july12th_games/Cleveland Cavaliers_vs_Orlando Magic_q41.csv')
    PTS = cavaliersq1.loc[cavaliersq1['PLAYER'] == 'TOTALS','PTS'].values + cavaliersq2.loc[cavaliersq2['PLAYER'] == 'TOTALS','PTS'].values + cavaliersq3.loc[cavaliersq3['PLAYER'] == 'TOTALS','PTS'].values + cavaliersq4.loc[cavaliersq4['PLAYER'] == 'TOTALS','PTS'].values
    return cavaliersq1, cavaliersq2, cavaliersq3, cavaliersq4, PTS

def clippers():
    clippersq1 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q10.csv')
    clippersq2 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q20.csv')
    clippersq3 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q30.csv')
    clippersq4 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q40.csv')
    PTS = clippersq1.loc[clippersq1['PLAYER'] == 'TOTALS','PTS'].values + clippersq2.loc[clippersq2['PLAYER'] == 'TOTALS','PTS'].values + clippersq3.loc[clippersq3['PLAYER'] == 'TOTALS','PTS'].values + clippersq4.loc[clippersq4['PLAYER'] == 'TOTALS','PTS'].values
    return clippersq1, clippersq2, clippersq3, clippersq4, PTS

def nuggets():
    nuggetsq1 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q11.csv')
    nuggetsq2 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q21.csv')
    nuggetsq3 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q31.csv')
    nuggetsq4 = pd.read_csv('./data/july12th_games/Denver Nuggets_vs_LA Clippers_q41.csv')
    PTS = nuggetsq1.loc[nuggetsq1['PLAYER'] == 'TOTALS','PTS'].values + nuggetsq2.loc[nuggetsq2['PLAYER'] == 'TOTALS','PTS'].values + nuggetsq3.loc[nuggetsq3['PLAYER'] == 'TOTALS','PTS'].values + nuggetsq4.loc[nuggetsq4['PLAYER'] == 'TOTALS','PTS'].values
    return nuggetsq1, nuggetsq2, nuggetsq3, nuggetsq4, PTS

def lakers():
    lakersq1 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q10.csv')
    lakersq2 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q20.csv')
    lakersq3 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q30.csv')
    lakersq4 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q40.csv')
    PTS = lakersq1.loc[lakersq1['PLAYER'] == 'TOTALS','PTS'].values + lakersq2.loc[lakersq2['PLAYER'] == 'TOTALS','PTS'].values + lakersq3.loc[lakersq3['PLAYER'] == 'TOTALS','PTS'].values + lakersq4.loc[lakersq4['PLAYER'] == 'TOTALS','PTS'].values
    return lakersq1, lakersq2, lakersq3, lakersq4, PTS

def rockets():
    rocketsq1 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q11.csv')
    rocketsq2 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q21.csv')
    rocketsq3 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q31.csv')
    rocketsq4 = pd.read_csv('./data/july12th_games/Houston Rockets_vs_Los Angeles Lakers_q41.csv')
    PTS = rocketsq1.loc[rocketsq1['PLAYER'] == 'TOTALS','PTS'].values + rocketsq2.loc[rocketsq2['PLAYER'] == 'TOTALS','PTS'].values + rocketsq3.loc[rocketsq3['PLAYER'] == 'TOTALS','PTS'].values + rocketsq4.loc[rocketsq4['PLAYER'] == 'TOTALS','PTS'].values
    return rocketsq1, rocketsq2, rocketsq3, rocketsq4, PTS

def timberwolves():
    timberwolvesq1 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q10.csv')
    timberwolvesq2 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q20.csv')
    timberwolvesq3 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q30.csv')
    timberwolvesq4 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q40.csv')
    PTS = timberwolvesq1.loc[timberwolvesq1['PLAYER'] == 'TOTALS','PTS'].values + timberwolvesq2.loc[timberwolvesq2['PLAYER'] == 'TOTALS','PTS'].values + timberwolvesq3.loc[timberwolvesq3['PLAYER'] == 'TOTALS','PTS'].values + timberwolvesq4.loc[timberwolvesq4['PLAYER'] == 'TOTALS','PTS'].values
    return timberwolvesq1, timberwolvesq2, timberwolvesq3, timberwolvesq4, PTS

def pelicans():
    pelicansq1 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q11.csv')
    pelicansq2 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q21.csv')
    pelicansq3 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q31.csv')
    pelicansq4 = pd.read_csv('./data/july12th_games/New Orleans Pelicans_vs_Minnesota Timberwolves_q41.csv')
    PTS = pelicansq1.loc[pelicansq1['PLAYER'] == 'TOTALS','PTS'].values + pelicansq2.loc[pelicansq2['PLAYER'] == 'TOTALS','PTS'].values + pelicansq3.loc[pelicansq3['PLAYER'] == 'TOTALS','PTS'].values + pelicansq4.loc[pelicansq4['PLAYER'] == 'TOTALS','PTS'].values
    return pelicansq1, pelicansq2, pelicansq3, pelicansq4, PTS

def grizzlies():
    grizzliesq1 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q10.csv')
    grizzliesq2 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q20.csv')
    grizzliesq3 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q30.csv')
    grizzliesq4 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q40.csv')
    PTS = grizzliesq1.loc[grizzliesq1['PLAYER'] == 'TOTALS','PTS'].values + grizzliesq2.loc[grizzliesq2['PLAYER'] == 'TOTALS','PTS'].values + grizzliesq3.loc[grizzliesq3['PLAYER'] == 'TOTALS','PTS'].values + grizzliesq4.loc[grizzliesq4['PLAYER'] == 'TOTALS','PTS'].values
    return grizzliesq1, grizzliesq2, grizzliesq3, grizzliesq4, PTS

def kings():
    kingsq1 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q11.csv')
    kingsq2 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q21.csv')
    kingsq3 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q31.csv')
    kingsq4 = pd.read_csv('./data/july12th_games/Sacramento Kings_vs_Memphis Grizzlies_q41.csv')
    PTS = kingsq1.loc[kingsq1['PLAYER'] == 'TOTALS','PTS'].values + kingsq2.loc[kingsq2['PLAYER'] == 'TOTALS','PTS'].values + kingsq3.loc[kingsq3['PLAYER'] == 'TOTALS','PTS'].values + kingsq4.loc[kingsq4['PLAYER'] == 'TOTALS','PTS'].values
    return kingsq1, kingsq2, kingsq3, kingsq4, PTS
