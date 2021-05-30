import React from 'react'

import UrlInputField from './UrlInputField'
import ShortenedUrlList from './ShortenedUrlList'


function ShorteningForm (props) {
    const [newUrl, setNewUrl] = React.useState('')
    
    const handleNewUrlSubmit = (newUrlData) => {        
        setNewUrl(newUrlData)
    }
    

    return (        
        <div className="app-form-wrap">            
            <UrlInputField onNewUrlSubmit={handleNewUrlSubmit}/>
            <ShortenedUrlList newUrl={newUrl} />
        </div>
    )
}

export default ShorteningForm
