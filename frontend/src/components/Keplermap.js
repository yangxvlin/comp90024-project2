import React from "react";
import keplerGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import KeplerGl from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import useSwr from "swr";

import covid19map from "../testData/covid19map.json";
import covid19 from "../testData/covid19.json";
import KeplerGlSchema from "kepler.gl/schemas";

import animationS1 from "../testData/animationS1.json";
import animationS5 from "../testData/animationS5.json";

const mapToLoad = KeplerGlSchema.load(covid19);
const reducers = combineReducers({
  keplerGl: keplerGlReducer.initialState({
    uiState: { readOnly: true }
  })
});

const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function Keplermap(scenario) {
  console.log(scenario);
  return (
    <Provider store={store}>
      <Map scenario={scenario} />
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
    
    const data = scenario.scenario.scenario; //await response.json();
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
    if (data === "3") {
      const map1 = KeplerGlSchema.load(covid19map);
      dispatch(
        addDataToMap(
          map1 /*{
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
        }*/
        )
      );
    } else if (data === "5") {
      const map = KeplerGlSchema.load(animationS5);
      dispatch(addDataToMap(map));
    } else if (data === "1") {
      const map1 = KeplerGlSchema.load(animationS1);
      dispatch(addDataToMap(map1));
    /*  fetch("http://172.26.132.122:5001/scenario1?lga=Greater%20Adelaide,Greater%20Melbourne,Greater%20Brisbane,Greater%20Sydney&weekday=1,2,3&daytime_start=0&daytime_end=24&age_group=0,1,2,17"
      ).then(res => res.json()).then(data => {console.log(data);
        const map = KeplerGlSchema.load(data);
        dispatch(addDataToMap(map));
      })*/
      /*
      .then(res => {if (res.ok) {
        console.log('ok');
      } else {
        console.log('error');
      };console.log(res.json())}, err=>{
        console.log(err)
    }).then(data => {
        console.log(data);
      },err=>{
        console.log(err)
    });*/
     }else {
      dispatch(
        addDataToMap(
          mapToLoad,
          {
            readOnly: true
          } /* {
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
            }*/
        )
      );
    }
  }, [dispatch, data]);

  return (
    <div>
      <KeplerGl
        id="covid"
        mapboxApiAccessToken="pk.eyJ1Ijoib2xpdmlhMTMxNCIsImEiOiJjazljMnkweGYwMHN2M29vN2h5N3Y0Z2p3In0.ii0pWAJQE5VJWg_X-84MSw" //process.env.REACT_APP_MAPBOX_API}
        width={window.innerWidth}
        height={window.innerHeight}
      />
    </div>
  );
}
