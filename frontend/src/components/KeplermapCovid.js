import React from "react";
import keplerGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import KeplerGl from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import useSwr from "swr";

import homepage from "../testData/homepage.json";
import covid19 from "../testData/covid19.json";
import KeplerGlSchema from "kepler.gl/schemas";

import animationS1 from "../testData/animationS1.json";
import animationS5 from "../testData/animationS5.json";

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
    const data = scenario.scenario.scenario; //await response.json();
    return data;
  });


  React.useEffect(() => {
    if (data === "4") {
      const map = KeplerGlSchema.load(animationS5);
      dispatch(addDataToMap(map));
    } else if (data === "1") {
      const map1 = KeplerGlSchema.load(animationS1);
      dispatch(addDataToMap(map1));
    } else {
      const map1 = KeplerGlSchema.load(homepage);
      dispatch(addDataToMap(map1));
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
