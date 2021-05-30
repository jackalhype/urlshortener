import React from 'react'
import ShortenedUrlRow from './ShortenedUrlRow'

const initList = []

function ShortenedUrlList(props) {    
    const [list, setList] = React.useState(initList)
    const [keys, setKeys] = React.useState([])    
    if (props.newUrl) {        
        if (!keys[props.newUrl.user_url]) {
            list.push(props.newUrl)
            keys[props.newUrl.user_url] = 1
        }
    } 

    return (
        <div>            
            <ul className="shortened-urls-list">
                {list.map(item => (
                    <ShortenedUrlRow
                        key={item.user_url}
                        user_url={item.user_url}
                        short_url_http={item.short_url_http}
                        short_url_no_schema={item.short_url_no_schema}
                    />
                ))}
            </ul>
        </div>
    )
}

export default ShortenedUrlList
