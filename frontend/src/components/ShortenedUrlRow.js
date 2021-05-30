import React from 'react'
import ReactDOM from 'react-dom'

function ShortenedUrlRow (props) {
    const cp2Clipboard = (txt) => {
        let textField = document.createElement('textarea')
        textField.innerText = txt
        document.body.appendChild(textField)
        textField.select()
        document.execCommand('copy')
        textField.remove()
    }

    return (
        <li className="shortened-url-row">
            <div className="shortened-url-row__orig-url">{props.user_url}</div>
            <div className="shortened-url-row__result-url">
                <a target="_blank" href={props.short_url_http}>{props.short_url_no_schema}</a>
            </div>
            <div className="shortened-url-row__btns">
                <button type="button" className="copy-btn" onClick={() => {cp2Clipboard(props.short_url_http)}}>Copy</button>
            </div>
        </li>
    )    
}

export default ShortenedUrlRow
