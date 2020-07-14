import * as React from "react";
import { List, Datagrid, TextField, ArrayField, ChipField, ReferenceField, ImageField } from 'react-admin';

export const CoktailList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <ImageField source="image" />
            <TextField source="name" />
            <ArrayField source="drinks">
                <Datagrid>
                    <ReferenceField label="Drinks" source="id" reference="drinks">
                        <ChipField source="name" />
                    </ReferenceField>
                    <TextField source="volume"/>
                </Datagrid>
            </ArrayField>
        </Datagrid>
    </List>
);