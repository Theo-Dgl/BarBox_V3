import * as React from "react";
import DataProvider from "./DataProvider";
import { Admin, Resource, EditGuesser, ListGuesser } from 'react-admin';
import { DrinkList } from "./resources/DrinksList";
import { DrinkEdit } from "./resources/DrinksEdit";
import { DrinkCreate } from "./resources/DrinksCreate";
import DrinkIcon from '@material-ui/icons/LocalDrink';
import CoktailIcon from '@material-ui/icons/LocalBar';
import { CoktailList } from "./resources/CoktailList";

const App = () => (
    <Admin dataProvider={DataProvider('')}>
        <Resource name="drinks" list={DrinkList} edit={DrinkEdit} create={DrinkCreate} icon={DrinkIcon}/>
        <Resource name="coktails" list={CoktailList} edit={EditGuesser} create={DrinkCreate} icon={CoktailIcon}/>
    </Admin>
);

export default App;