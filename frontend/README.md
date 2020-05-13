# Frontend
## Description

Frontend can display animation with kepler.gl by choosing scenario, and can set parameters to fetch related data from backend, then display related diagrams. Currently, data of scenario1 has been tested succesfully.

## How to run
1. ```cd frontend```
2. ```yarn```
3. ```npm start```
    Local:            http://localhost:3000
  On Your Network:  http://192.168.0.2:3000

## Repository Structure
```
| /frontend
      - basic website file
  /src 
      - main front end code files
    /App.js
      - application js file.
    /index.js
      - index
    /components
      - components file
      / Navibar.js
        - navigation bar
      / Keplermap.js
        - kepler map
      / Sidepanel.js
        - side panel for showing diagrams.
    /testData
        - data files for testing.
       /covid19.json 
         - test file
       /covid19.csv 
         - test file
       / covid19map.js
        - test file with animition for income scenario.
       / keplergl.json
        - test file with animition for crime rate scenario.
    /assets
        - dependencies for visualisation daigrams.
  /package.json
      - front end scripts
```
<<<<<<< HEAD
=======

>>>>>>> 6b7857ee667a300cb238be51448509755c521b09
