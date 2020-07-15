function get(url) {
    const proxyurl = "https://cors-anywhere.herokuapp.com/";

    return fetch(proxyurl + url)
        .then(response => {
            return response.json()
        }).then(json => {
            // return drinks
            return json.data
        })
        .catch(error => {
            throw(error)
        });
}

function postRequest(url) {
    const proxyurl = "https://cors-anywhere.herokuapp.com/";

    return fetch(proxyurl + url, {
            method: 'POST',
            mode: 'no-cors'
        })
        .then(response => {
            return response
        }).then(json => {
            return json
        })
        .catch(error => {
            throw(error)
        });
}

function getDrinks() {
    return get('https://d0590bb2b4c1.ngrok.io/drinks');
}

function getCoktails() {
    return get('https://d0590bb2b4c1.ngrok.io/coktails');
}

function getCoktail(id) {
    return get('https://d0590bb2b4c1.ngrok.io/coktails/' + id);
}

function postServeCoktail(id) {
    return postRequest('https://d0590bb2b4c1.ngrok.io/coktails/' + id + '/serve');
}