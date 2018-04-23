import React, { Component } from 'react';


export default class Tasks extends Component {

    constructor(props) {
        super(props)
    }

    render() {

        const tasks = this.props.tasks.map(task => <li key={task.id}>{task.name}</li>)

        return (
            <div>
                <h2>Hello from tasks!</h2>

                <ul>
                    {tasks}
                </ul>
            </div>
        )
    }

}