import * as React from "react";
import { AmountSelector } from "../components/amountSelector";
import { Edit, SimpleForm, TextInput, NumberInput, ArrayInput, SimpleFormIterator, ReferenceInput, SelectInput } from 'react-admin';

export const CoktailEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput source="image" />
            <ArrayInput source="drinks">
                <SimpleFormIterator>
                    <ReferenceInput label="Drinks" source="id" reference="drinks">
                        <SelectInput optionText="name" />
                    </ReferenceInput>
                    <AmountSelector source="volume"/>
                </SimpleFormIterator>
            </ArrayInput>
        </SimpleForm>
    </Edit>
);