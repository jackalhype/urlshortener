import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'
import reactDom from 'react-dom'
import ShortenedUrlRow from './ShortenedUrlRow'

class UrlInputField extends React.Component
{
    constructor(props) {
        super(props)
        this.state = {
            inputUrl: ''
        }        
    }

    handleSubmit = () => {
        const url =  this.state.inputUrl.trim()
        if (!url.length) {
            return 
        }        
        axios.post(process.env.REACT_APP_API_URL + 'user_url', {
            user_url: url
        }).then(resp => {            
            this.props.onNewUrlSubmit(resp.data.data)
        }).catch((err) => {
            console.log(JSON.stringify(err.response?.data?.errors))
            alert(JSON.stringify(err.response?.data?.errors))
        })
    }

    updateInputUrl(ev){
        this.setState({
            inputUrl: ev.target.value
        })
    }

    render() {
        return (
            <div className="url-input-field-wrap">
                <input type="text" 
                    className="url-input-field" 
                    autoComplete="off" 
                    autoCorrect="off" 
                    placeholder="Enter link here"
                    value={this.state.inputUrl}
                    onChange={ev => this.updateInputUrl(ev)}
                    />
                <input type="button" 
                    onClick={this.handleSubmit}
                    className="url-input-submit-btn" 
                    value="Shorten URL" 
                />
            </div>
        )
    }

}

export default UrlInputField
