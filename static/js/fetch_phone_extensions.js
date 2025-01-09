document.addEventListener("DOMContentLoaded", function() {
    const phoneExtensionSelect = document.getElementById('phone_extension');

    try {
        fetch('https://restcountries.com/v3.1/all')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                try {
                    data.forEach(country => {
                        if (country.idd && country.idd.root && country.idd.suffixes) {
                            country.idd.suffixes.forEach(suffix => {
                                const option = document.createElement('option');
                                option.value = `${country.idd.root}${suffix}`;
                                option.textContent = `${country.idd.root}${suffix} (${country.name.common})`;
                                phoneExtensionSelect.appendChild(option);
                            });
                        }
                    });
                } catch (innerError) {
                    console.error('Error processing country data:', innerError);
                }
            })
            .catch(error => console.error('Error fetching phone extensions:', error));
    } catch (outerError) {
        console.error('Error initializing phone extensions fetching:', outerError);
    }
});
