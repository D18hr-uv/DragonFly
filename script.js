function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 28.644, lng: 77.216 },
        zoom: 13,
    });

    const input = document.getElementById("pac-input");
    const options = {
        fields: ["formatted_address", "geometry", "name"],
        strictBounds: false,
    };

    const autocomplete = new google.maps.places.Autocomplete(input, options);
    autocomplete.bindTo("bounds", map);

    const infowindow = new google.maps.InfoWindow();
    const infowindowContent = document.getElementById("infowindow-content");
    infowindow.setContent(infowindowContent);

    const marker = new google.maps.Marker({
        map: map,
        anchorPoint: new google.maps.Point(0, -29),
    });

    autocomplete.addListener("place_changed", () => {
        infowindow.close();
        marker.setVisible(false);

        const place = autocomplete.getPlace();

        if (!place.geometry || !place.geometry.location) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }
        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        infowindowContent.querySelector("#place-name").textContent = place.name;
        infowindowContent.querySelector("#place-address").textContent = place.formatted_address;
        infowindow.open(map, marker);

        updateAtmosphericData(place.geometry.location.lat(), place.geometry.location.lng());
    });

    const currentLocationButton = document.getElementById("current-location");
    currentLocationButton.addEventListener("click", () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };

                map.setCenter(userLocation);
                map.setZoom(17);

                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "Your Location",
                });

                updateAtmosphericData(userLocation.lat, userLocation.lng);
            });
        } else {
            alert("Geolocation is not supported by your browser.");
        }
    });
}

function updateAtmosphericData(lat, lng) {
    const fakeData = {
        pm25: "35 µg/m³",
        temperature: "22°C",
        humidity: "60%",
    };

    document.getElementById("pm25-level").innerText = fakeData.pm25;
    document.getElementById("temperature").innerText = fakeData.temperature;
    document.getElementById("humidity").innerText = fakeData.humidity;
}

window.initMap = initMap;
