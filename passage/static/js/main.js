
var PassageMain = React.createClass({

    getInitialState: function() {
        return { data: [] };
    },

    componentDidMount: function() {
        this.sendMessage({
            endpoint: this.props.starting,
        })
    },

    sendMessage: function(m) {
        console.log("send", m);
        $.ajax({
            type: 'POST',
            url: '/call', 
            contentType: 'application/json',
            data: JSON.stringify(m),
            dataType: 'json',
            success: this.handleMessage,
        });
    },

    handleMessage: function(m) {
        console.log("recv", m);
        this.setState({ data: this.state.data.concat(m) });
    },

    renderLine: function(line) {
        if (line.lineType == "input") {
            // TODO: include the passage main in here as well, or at least
            // a handler for incoming requests after the ajax call
            return (
                <PassageInput
                    text={line.data.text}
                    endpoint={line.data.endpoint}
                    sender={this.sendMessage}
                />
            );
        }
        else if (line.lineType == "output") {
            return (
                <PassageOutput
                    text={line.data.text}
                />
            );
        } else {
            return (
                <h1>Invalid lineType {line.lineType}</h1>
            );
        }
    },

    render: function() {
        var lineContent = this.state.data.map(this.renderLine);
        return (
            <div className="passage-content">
                {lineContent}
            </div>
        );
    }

});

var PassageInput = React.createClass({

    getInitialState: function() {
        return { inputValue: "" };
    },

    handleSubmit: function() {
        var node = React.findDOMNode(this.refs.inputValue);
        var value = node.value.trim();
        this.props.sender({
            endpoint: this.props.endpoint,
            text: value
        });
        node.value = "";
        return false;
    },

    render: function() {
        return (
            <div className="passage-input">
                <form onSubmit={this.handleSubmit}>
                    <p>{this.props.text}</p>
                    <input type="text" placeholder={this.props.text} ref="inputValue" />
                    <input type="submit" value="Submit" />
                </form>
            </div>
        );
    }

});

var PassageOutput = React.createClass({

    render: function() {
        return (
            <div className="passage-output">
                <p>{this.props.text}</p>
            </div>
        );
    }

});