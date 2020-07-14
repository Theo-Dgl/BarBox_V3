import * as React from "react";
import { List, Datagrid, TextField, ArrayField, SingleFieldList, ChipField, ImageField } from 'react-admin';

export const CoktailList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="name" />
            <ImageField source="image" />
            <ArrayField source="drinks">
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
            </ArrayField>
        </Datagrid>
    </List>
);