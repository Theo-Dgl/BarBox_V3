import * as React from "react";
import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const CoktailEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <ArrayInput source="drinks">
                <SimpleFormIterator>
                    <TextInput source="id" />
                    <NumberInput source="volume" />
                </SimpleFormIterator>
            </ArrayInput>
            <TextInput source="id" />
            <TextInput source="image" />
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
);