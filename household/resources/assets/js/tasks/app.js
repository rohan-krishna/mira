const $ = require('jquery');
const axios = require('axios');


import React from 'react';
import ReactDOM from 'react-dom';

import Tasks from './components/tasks';


class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            tasks: []
        }
    }

    componentDidMount() {
        axios.get('api/tasks/')
                .then(res => this.setState({ tasks: res.data }))
                .catch(err => console.log(err))
    }

    render() {
        return(
            <div>
                <Tasks tasks={this.state.tasks} />
            </div>
        )
    }
}

$(document).ready(function() {
    ReactDOM.render(<App />, document.getElementById('reactApp'))
})


module.hot.accept();

