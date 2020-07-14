import * as React from "react";
import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const DrinkEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <NumberInput source="pump_number" />
            <NumberInput source="total_volume" />
            <NumberInput source="volume_left" />
        </SimpleForm>
    </Edit>
)