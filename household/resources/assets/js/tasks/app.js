import React from 'react';
import ReactDOM from 'react-dom';

const $ = require('jquery');


const App = () => {
    return (
        <h1>Hello World!</h1>
    )
}

$(document).ready(function() {
    ReactDOM.render(<App />, document.getElementById('reactApp'))
})


module.hot.accept();

