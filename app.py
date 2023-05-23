import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv("data\data.csv", encoding="ISO-8859-1", sep=";")
df.insert(2, "RealGoals", round(df['90s'] * df['Goals']))
df.insert(3, 'RealShots', round(df['90s'] * df['Shots']))

df_GoalsbyComps = df.groupby('Comp', as_index=False).sum()
df_GoalsbyCompsTemp = df_GoalsbyComps[['Comp', 'RealGoals']]

courses = list(df_GoalsbyCompsTemp['Comp'])
values = list(df_GoalsbyCompsTemp['RealGoals'])

fig = plt.figure(figsize=(10, 5))
plt.bar(courses, values, color='blue', width=0.4)
plt.xlabel("Ligen")
plt.ylabel("Anzahl der Tore")
plt.title("Gesamtzahl der Tore für jede Liga")
st.pyplot(fig)

df_GoalsbySquads = df.groupby(['Comp', 'Squad'], as_index=False).sum()
df_GoalsbySquadTemp = df_GoalsbySquads[['Comp', 'Squad', 'RealGoals', 'RealShots']]

def ShowGraph(league):
    if league == 'Bundesliga':
        df_GoalsbySquadsBL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == league]
        goalsBL = list(df_GoalsbySquadsBL['RealGoals'])
        shotsBL = list(df_GoalsbySquadsBL['RealShots'])
        squadsBL = list(df_GoalsbySquadsBL['Squad'])
    
        plt.figure(figsize=(12, 8))
        plt.scatter(goalsBL, shotsBL, s=50, alpha=0.5)
        plt.axhline(y=500, color='red')
        plt.axvline(x=60, color='red')
        plt.xlabel("Tore")
        plt.ylabel("Schüsse")
        plt.title(f"{league} - Schuss-/Torverhältnis")
        for i in range(len(squadsBL)):
            if goalsBL[i] >= 60:
                plt.annotate(squadsBL[i], (goalsBL[i], shotsBL[i]), ha='left')
        st.pyplot()
    elif league == 'La Liga':
        df_GoalsbySquadsLL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == league]
        goalsLL = list(df_GoalsbySquadsLL['RealGoals'])
        shotsLL = list(df_GoalsbySquadsLL['RealShots'])
        squadsLL = list(df_GoalsbySquadsLL['Squad'])

        plt.figure(figsize=(12, 8))
        plt.scatter(goalsLL, shotsLL, s=50, alpha=0.5)
        plt.axhline(y=500, color='red')
        plt.axvline(x=55, color='red')
        plt.xlabel("Tore")
        plt.ylabel("Schüsse")
        plt.title(f"{league} - Schuss-/Torverhältnis")
        for i in range(len(squadsLL)):
            if goalsLL[i] >= 55:
                plt.annotate(squadsLL[i], (goalsLL[i], shotsLL[i]), ha='left')
        st.pyplot()
    elif league == 'Serie A':
        df_GoalsbySquadsSA = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == league]
        goalsSA = list(df_GoalsbySquadsSA['RealGoals'])
        shotsSA = list(df_GoalsbySquadsSA['RealShots'])
        squadsSA = list(df_GoalsbySquadsSA['Squad'])

        plt.figure(figsize=(12, 8))
        plt.scatter(goalsSA, shotsSA, s=50, alpha=0.5)
        plt.axhline(y=500, color='red')
        plt.axvline(x=55, color='red')
        plt.xlabel("Tore")
        plt.ylabel("Schüsse")
        plt.title(f"{league} - Schuss-/Torverhältnis")
        for i in range(len(squadsSA)):
            if goalsSA[i] >= 55:
                plt.annotate(squadsSA[i], (goalsSA[i], shotsSA[i]), ha='left')
        st.pyplot()
    elif league == 'Ligue 1':
        df_GoalsbySquadsL1 = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == league]
        goalsL1 = list(df_GoalsbySquadsL1['RealGoals'])
        shotsL1 = list(df_GoalsbySquadsL1['RealShots'])
        squadsL1 = list(df_GoalsbySquadsL1['Squad'])

        plt.figure(figsize=(12, 8))
        plt.scatter(goalsL1, shotsL1, s=50, alpha=0.5)
        plt.axhline(y=463, color='red')
        plt.axvline(x=60, color='red')
        plt.xlabel("Tore")
        plt.ylabel("Schüsse")
        plt.title(f"{league} - Schuss-/Torverhältnis")
        for i in range(len(squadsL1)):
            if goalsL1[i] >= 60:
                plt.annotate(squadsL1[i], (goalsL1[i], shotsL1[i]), ha='left')
        st.pyplot()
    elif league == 'Premier League':
        df_GoalsbySquadsPL = df_GoalsbySquadTemp[df_GoalsbySquadTemp['Comp'] == league]
        goalsPL = list(df_GoalsbySquadsPL['RealGoals'])
        shotsPL = list(df_GoalsbySquadsPL['RealShots'])
        squadsPL = list(df_GoalsbySquadsPL['Squad'])

        plt.figure(figsize=(12, 8))
        plt.scatter(goalsPL, shotsPL, s=50, alpha=0.5)
        plt.axhline(y=550, color='red')
        plt.axvline(x=60, color='red')
        plt.xlabel("Tore")
        plt.ylabel("Schüsse")
        plt.title(f"{league} - Schuss-/Torverhältnis")
        for i in range(len(squadsPL)):
            if goalsPL[i] >= 60:
                plt.annotate(squadsPL[i], (goalsPL[i], shotsPL[i]), ha='left')
        st.pyplot()

league_dropdown = st.sidebar.selectbox("League:", options=courses, index=0)
ShowGraph(league_dropdown)
