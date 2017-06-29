import React from 'react';
import ReactDOM from 'react-dom';

import { jsonServerRestClient, Admin, Resource } from 'admin-on-rest';
import { PostList } from 'radmin/components/Posts';
import authClient from 'radmin/utils/authClient'

const radminRootEl = document.getElementById('radmin');

ReactDOM.render(
    <Admin restClient={jsonServerRestClient('/api/v1')} authClient={authClient}>
        <Resource name="post-post" list={PostList}/>
    </Admin>,
    radminRootEl
)
