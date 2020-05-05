import React from "react";

export default class Elements extends React.Component{
    constructor(props) {
        super(props)
        this.clickSubmit = this.clickSubmit.bind(this)
        // 默认Alert隐藏
        this.state = { 
           visible:  false 
        }
     }
     clickSubmit(e) {
        e.preventDefault()
        if (this.state.visible) {
             // Alert隐藏
             this.setState({ visible: false }) 
         } else {
              // Alert显示
             this.setState({ visible: true })
         }
    }
    render(){
        return(
            <div>
            <div>
	            {this.state.visible ? (
		            <p>You can see me.</p> 
                    ) : null}
                    
            </div>
                     <button type="primary" htmlType="submit" id="loginBtn" onClick={this.clickSubmit}>Login</button>
            </div>
        )
    }
}