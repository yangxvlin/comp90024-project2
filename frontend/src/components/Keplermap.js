import React from "react";
import keplerGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import KeplerGl from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import useSwr from "swr";


import testJson from "../testData/keplergl.json";
import covid19map from "../testData/covid19map.json";
import covid19 from "../testData/covid19.json";
import KeplerGlSchema from "kepler.gl/schemas";


const mapToLoad = KeplerGlSchema.load(covid19);
const reducers = combineReducers({
  keplerGl: keplerGlReducer.initialState({
    uiState: {readOnly: true}
 })            
});


const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function Keplermap(scenario) {
    return (
        <Provider store={store}>
          <Map scenario={scenario}/>
        </Provider>
      );
   
}


function Map(scenario) {
   
  const dispatch = useDispatch();
  const { data } = useSwr("covid", async () => {
 /*   const response = 
    await fetch(
      "https://gist.githubusercontent.com/leighhalliday/a994915d8050e90d413515e97babd3b3/raw/a3eaaadcc784168e3845a98931780bd60afb362f/covid19.json"
   );*/
 //  if(scenario === "1")
     const data = scenario.scenario.scenario;//await response.json();
   //   const data = {testJson};
   console.log(data);
     return data;
  });

/*
const data1 =  fetch('./testDate/convid19.json')
    .then((res) => res.json())
    .then((data1) => {
      console.log('data:', data1);
    });
*/
   

  React.useEffect(() => {
    if (data === "1") {
        const map1 = KeplerGlSchema.load(covid19map);
      dispatch(
        addDataToMap(map1 /*{
          datasets: {
            info: {
              label: "COVID-19",
              id: "covid19"
            },
            data
          },
          option: {
            centerMap: true,
            readOnly: false
          },
          config: {}
        }*/)
      );
    }
    else if (data === "2"){
        const map = KeplerGlSchema.load(testJson);
        dispatch(
            addDataToMap(map));
    }else{
        dispatch(
            addDataToMap(mapToLoad , {readOnly: true}/* {
              datasets: {
                info: {
                  label: "COVID-19",
                  id: "covid19"
                },
                data
              },
              option: {
                centerMap: true,
                readOnly: false
              },
              config: {}
            }*/)
          );
    }
    
  }, [dispatch, data]);

  return (
    <div>
      <KeplerGl
        id="covid"
        
        mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_API}
        width={window.innerWidth}
        height={window.innerHeight}
      />
    </div>
    
  );
}

