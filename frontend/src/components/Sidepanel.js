import React, { useState } from 'react';
import SlidingPanel from 'react-sliding-side-panel';
import '../assets/sidepanel.css';
 
export default function Sidepanel(a){
	console.log(a);
  const [openPanel, setOpenPanel] = useState(false);
  return (

	  <SlidingPanel
        type={'right'}
        isOpen={openPanel}
        backdropClicked={() => setOpenPanel(false)}
        size={30}
        panelClassName="additional-class"
      >
        <div className="panel-container">
          <div>My Panel Content</div>
          <button type="button" className="close-button" onClick={() => setOpenPanel(false)}>
            close
          </button>
        </div>
      </SlidingPanel>
    
  );
};
 