function searchCountry() {
    const inputElement = document.getElementById('country-input');
    const countryInfoElement = document.getElementById('country-info');

    const countryName = inputElement.value.trim();

    if (countryName === '') {
        countryInfoElement.innerHTML = '<p>Please enter a country name.</p>';
        return;
    }

    fetch(`https://restcountries.com/v3.1/name/${countryName}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 404) {
                countryInfoElement.innerHTML = '<p>Country not found. Please check the spelling and try again.</p>';
                return;
            }

            const country = data[0];

            const htmlContent = `
                <h2>${country.name.common}</h2>
                <p>Capital: ${country.capital}</p>
                <p>Population: ${country.population}</p>
                <p>Region: ${country.region}</p>
                <p>Subregion: ${country.subregion}</p>
            `;

            countryInfoElement.innerHTML = htmlContent;
        })
        .catch(error => {
            console.error('Error fetching country information:', error);
            countryInfoElement.innerHTML = '<p>Error loading data. Please try again later.</p>';
        });
}
