import * as React from "react";
import { Create, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const DrinkCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <NumberInput source="pump_number" />
            <NumberInput source="total_volume" />
            <NumberInput source="volume_left" />
        </SimpleForm>
    </Create>
)