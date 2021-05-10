import React from 'react'
import axios from 'axios'

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
            console.log(resp)
        }).catch(err => {
            console.log(err)
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
