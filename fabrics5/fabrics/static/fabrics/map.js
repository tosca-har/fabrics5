getMap = function () {    
    let tfAttr = 'Maps &copy; <a href="https://www.thunderforest.com">Thunderforest</a>, Data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>';
    let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    let tfUrl = 'https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey='+ thsu;
    let mbUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token='+ mbsu;
    let mbSUrl = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=' + mbsu;




    let landscape = L.tileLayer(tfUrl, {maxZoom: 22, attribution: tfAttr});
    let streets = L.tileLayer(mbUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let satellite = L.tileLayer(mbSUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {tileSize: 512, zoomOffset: -1, attribution: 'OpenStreetMap'});
    let macrostratLayer = L.tileLayer('https://tiles.macrostrat.org/carto/{z}/{x}/{y}.png', {
        maxZoom: 22, // Adjust maxZoom as needed
        attribution: '<a href="https://macrostrat.org/">Macrostrat</a>' // Add appropriate attribution
    });
    let sites = L.featureGroup();
    let full = L.featureGroup();
    let imag = L.featureGroup();
    let volcanoes = L.featureGroup();

    var potIcon = L.icon({
        iconUrl: picon,
        iconSize: [15, 20]
    });

    var potIconB = L.icon({
        iconUrl: bicon,
        iconSize: [15, 20]
    });

    var potIconC = L.icon({
        iconUrl: ricon,
        iconSize: [15, 20]
    });

    var blackV = L.icon({iconUrl: blackv, iconSize: [17, 15]});
    var blueV = L.icon({iconUrl: bluev, iconSize: [17, 15]});
    var greenV = L.icon({iconUrl: greenv, iconSize: [17, 15]});    
    var redV = L.icon({iconUrl: redv, iconSize: [17, 15]});
    var pinkV = L.icon({iconUrl: pinkv, iconSize: [17, 15]});
    var purpleV = L.icon({iconUrl: purplev, iconSize: [17, 15]});    
    var brownV = L.icon({iconUrl: brownv, iconSize: [17, 15]});
    var orangeV = L.icon({iconUrl: orangev, iconSize: [17, 15]});
        
    let map = L.map('map', {
        center: mapcentre,
        zoom: 4,
        layers: [streets, full, imag, sites]
    });

    let baseLayers = {
        'Landscape': landscape,
        'Satellite': satellite,
        'Streets': streets,
        'OSM' : osm
        
    };

    for (var i = 0; i < siteNames.length; i += 1) {
        sitename = siteNames[i];
        sitelink = siteLinks[i];
        complex = "<a href=" +sitelink+">"+sitename+ "</a>" + siteFabrics[i];
        if (siteColour[i] == 0) {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconB, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(sites);
        } else if (siteColour[i] == 2) {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconC, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(imag);
        } else {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(full);
 
        }
    } 
    for (var i = 0; i < volcNames.length; i += 1) {
        volcname = volcNames[i];
        volclink = "https://volcano.si.edu/volcano.cfm?vn=" + volcLinks[i];
        complex = "<a href=" +volclink+">"+volcname+ "</a>: " + volcDetails[i];
        if (volcType[i] == "Basalt / Picro-Basalt") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: redV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Andesite / Basaltic Andesite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: orangeV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Dacite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: blueV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Phono-tephrite /  Tephri-phonolite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: brownV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Trachybasalt / Tephrite Basanite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: purpleV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Trachyandesite / Basaltic Trachyandesite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: pinkV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else if (volcType[i] == "Rhyolite") {
            marker = L.marker([volcLat[i],volcLng[i]],{icon: greenV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        } else{
            marker = L.marker([volcLat[i],volcLng[i]],{icon: blackV, title: complex}).bindPopup(complex).on("click", markerOnClickVolcano).addTo(volcanoes);
        }

    }

        let overlays = {}
        
        if (siteview) { 
            overlays = {
            'Has full slide': full,
            'Has image': imag,
            'No images': sites,
            'Volcanoes': volcanoes,
            'Geology': macrostratLayer
            }; 
        } else {
            overlays = {
                'Selected': full,
                'Volcanoes': volcanoes,
                'Geology': macrostratLayer
                }; 
        }
        var layerControl = L.control.layers(baseLayers, overlays).addTo(map);

   
  }

  function markerOnClick(e) {
    targetSite = this.options.title;
    targetLink = this.options.link;
    document.getElementById("targetSite").innerHTML = "Site selected: <a href=" +targetLink+">"+targetSite+ "</a>." ; 
        
}

  function markerOnClickVolcano(e) {
    targetSite = this.options.title;
    document.getElementById("targetSite").innerHTML = "Selected Volcano "+targetSite ; 
        
}

