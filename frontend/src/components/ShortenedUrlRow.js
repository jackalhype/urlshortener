import React from 'react'
import ReactDOM from 'react-dom'

class ShortenedUrlRow extends React.Component
{
    render() {
        return (
            <div className="shortened-url-row">
                <div className="shortened-url-row__orig-url"></div>
                <div className="shortened-url-row__result-url"></div>
                <div className="shortened-url-row__btns">
                    <button type="button" className="copy-btn">Copy</button>
                </div>
            </div>
        )
    }
}

export default ShortenedUrlRow
