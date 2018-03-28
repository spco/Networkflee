# Networkflee
This project is an inspiration of the Hackday at the Collaborations Workshop 2018 organised by SSI.

## Overview
FLEE, an agent-based simulation tool, developed by Groen (2016) at Brunel University London. It uses data from the [Armed Conflict Location & Event Data Project](http://data2.unhcr.org/en/situations) (ACLED) to model the migration of refugees within a conflict zone and data from the [United Nations High Commission for Refugees](http://data2.unhcr.org/en/situations) (UNHCR) to identify locations of camps. 

After obtaining conflict locations and neighbouring camps, prediction of refugee movements requires network maps. As we have several locations, identifying connection routes, distances, constructing and visualising these links becomes time consuming. Hence, manually constructed network maps are proven to be inefficient at this moment. 

Automated network map construction - Networkflee - allows to detect route connections and distances between locations, as well as constuct visual representation. It requires a dataset (e.g. locations.csv) with location names and GPS coordinates in csv format, which is also used for simulation purposes at the later stage. 

Acquired data from ACLED and UNHCR, publicly available sources, provide an input for running an agent-based simulation. It uses FLEE code for predicting refugee movements and produces output numbers of the population for cities and camps over the simulation period. An introductory paper on simulating refugee movements is written by [Groen (2016)](http://www.sciencedirect.com/science/article/pii/S1877050916308766) with a description of parameters, assumptions and application to crisis situation of Mali. FLEE simulation model has also been applied to Burundi, Central African Republic and South Sudan, which is written by [Suleimenova et al. (2017)](https://goo.gl/t16LA1) published in Scientific Reports. 
