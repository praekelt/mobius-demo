import React from 'react';
import { List, Datagrid, TextField, ChipField, ReferenceManyField, SingleFieldList } from 'admin-on-rest';

export const PostList = (props) => (
    <List {...props}>
        <Datagrid>
            <TextField source="title" />
            <TextField source="description" />
            <ReferenceManyField label="Content" reference="jmbo-modelbase/" target="content">
                <SingleFieldList>
                    <ChipField source="post.title" />
                </SingleFieldList>
            </ReferenceManyField>
        </Datagrid>
    </List>
);