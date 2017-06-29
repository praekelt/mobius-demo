import React from 'react';
import ReactDOM from 'react-dom';

import { Admin, Resource, fetchUtils } from 'admin-on-rest';
import { PostList } from 'radmin/components/Posts';
import authClient from 'radmin/utils/authClient'
import drfRestClient from 'radmin/utils/drfRestClient'

const radminRootEl = document.getElementById('radmin');

const httpClient = (url, options = {}) => {
    if (!options.headers) {
        options.headers = new Headers({ Accept: 'application/json' });
    }
    const token = localStorage.getItem('token');
    options.headers.set('Authorization', `JWT ${token}`);
    options['content-type'] = 'application/json';
    return fetchUtils.fetchJson(url, options);
}

ReactDOM.render(
    <Admin restClient={drfRestClient('/api/v1', httpClient)} authClient={authClient}>
        <Resource name="post-post" list={PostList}/>
    </Admin>,
    radminRootEl
)
