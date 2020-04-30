# Frontend
## Description
Currently, front-end has succeeded in implementing homepage with kepler.gl, and scenarios in the navbar can control the scenario display in the map(there are only 2 test data now for checking income scenario and  crime rate scenario, others have no test data). Tasks of next step are as follows:

    - [✅] hide kepler sidebar
    - [✅] import scenarios json file through navbar event and showing in the map
    - [ ] implement bar/ line chart for chosen area.
    - [ ] integration and test

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
